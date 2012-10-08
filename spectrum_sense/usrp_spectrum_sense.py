#!/usr/bin/python
#!/usr/bin/env python
#
#To do: visualize ranked spectrum results (pyplot)

from gnuradio import gr, eng_notation, window, digital
from gnuradio import audio
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from optparse import OptionParser
from matplotlib import pyplot
from xml.dom.minidom import parseString
import sys
import math
import struct
import threading
import numpy
import time
import urllib2
#import antigravity

try:
    import scipy
    from scipy import stats
except ImportError:
    print "Error: Program requires scipy."
    sys.exit(1)

try:
    import pylab
except ImportError:
    print "Error: Program requires Matplotlib."
    sys.exit(1)


sys.stderr.write("Warning: this may have issues on some machines+Python version combinations to seg fault due to the callback in bin_statitics.\n\n")

class ThreadClass(threading.Thread):
    def run(self):
        return

class tune(gr.feval_dd):
    """
    This class allows C++ code to callback into python.
    """
    def __init__(self, tb):
        gr.feval_dd.__init__(self)
        self.tb = tb

    def eval(self, ignore):
        """
        This method is called from gr.bin_statistics_f when it wants
        to change the center frequency.  This method tunes the front
        end to the new center frequency, and returns the new frequency
        as its result.
        """

        try:
            # We use this try block so that if something goes wrong
            # from here down, at least we'll have a prayer of knowing
            # what went wrong.  Without this, you get a very
            # mysterious:
            #
            #   terminate called after throwing an instance of
            #   'Swig::DirectorMethodException' Aborted
            #
            # message on stderr.  Not exactly helpful ;)

            new_freq = self.tb.set_next_freq()
            return new_freq

        except Exception, e:
            print "tune: Exception: ", e


class parse_msg(object):
    def __init__(self, msg):
        self.center_freq = msg.arg1()
        self.vlen = int(msg.arg2())
        assert(msg.length() == self.vlen * gr.sizeof_float)

        # FIXME consider using NumPy array
        t = msg.to_string()
        self.raw_data = t
        self.data = struct.unpack('%df' % (self.vlen,), t)


class my_top_block(gr.top_block):
    def online_skewness(data, alpha):
	n = 0
	mean = 0
	M2 = 0
	M3 = 0
	d_M3 = 0

	for n in xrange(len(data)):
	    delta = data[n] - mean
	    delta_n = delta / (n+1)
	    term1 = delta * delta_n * (n)
	    mean = mean + delta_n
	    M3 = term1 * delta_n * (n - 1) -3 * delta_n * M2
	    M2 = M2 + term1
	    d_M3 = (0.001)*M3 + (1-0.001)*d_M3;
	return d_M3

    def snr_est_simple(signal):
	y1 = scipy.mean(abs(signal))
	y2 = scipy.real(scipy.mean(signal**2))
	y3 = (y1*y1 - y2)
	snr_rat = y1*y1/y3
	return 10.0*scipy.log10(snr_rat), snr_rat

    def snr_est_skew(signal):
	y1 = scipy.mean(abs(signal))
	y2 = scipy.mean(scipy.real(signal**2))
	y3 = (y1*y1 - y2)
	y4 = online_skewness(abs(signal.real), 0.001)
	skw = y4*y4 / (y2*y2*y2);
	snr_rat = y1*y1 / (y3 + skw*y1*y1)
	return 10.0*scipy.log10(snr_rat), snr_rat
 
    def snr_est_m2m4(signal):
	M2 = scipy.mean(abs(signal)**2)
	M4 = scipy.mean(abs(signal)**4)
	snr_rat = 2*scipy.sqrt(2*M2*M2 - M4) / (M2 - scipy.sqrt(2*M2*M2 - M4))
	return 10.0*scipy.log10(snr_rat), snr_rat

    def snr_est_svr(signal):
	N = len(signal)
	ssum = 0
	msum = 0
	for i in xrange(1, N):
	    ssum += (abs(signal[i])**2)*(abs(signal[i-1])**2)
	    msum += (abs(signal[i])**4)
	savg = (1.0/(float(N)-1.0))*ssum
	mavg = (1.0/(float(N)-1.0))*msum
	beta = savg / (mavg - savg)
	snr_rat = 2*((beta -1) + scipy.sqrt(beta*(beta-1)))
	return 10.0*scipy.log10(snr_rat), snr_rat

    def weighted_incremental_variance(dataWeightPairs):
	sumweight = 0
	mean = 0
	M2 = 0
	for x, weight in dataWeightPairs:
	    temp = weight + sumweight
	    delta = x - mean
	    R = delta * weight / temp
	    mean = mean + R
	    M2 = M2 + sumweight * delta * R
	    sumweight = temp
	variance_n = M2/sumweight
	variance = variance_n * len(dataWeightPairs)/(len(dataWeightPairs) -1)
	return variance

    def online_kurtosis(data):
	n = 0
	mean = 0
	M2 = 0
	M3 = 0
	M4 = 0

	for x in data:
	    n1 = n
	    n = n + 1
	    delta = x - mean
	    delta_n = delta / n
	    delta_n2 = delta_n * delta_n
	    term1 = delta * delta_n * delta_n
	    mean = mean + delta_n
	    M4 = M4 + term1 * delta_n2 * (n*n - 3*n +3) + 6 * delta_n2 * M2 -4 * delta_n * M3
	    M3 = M3 + term1 * delta_n * (n - 2) -3 * delta_n * M2
	    M2 = M2 + term1
	
	kurtosis = (n*M4) / (M2*M2) -3
	return kurtosis

    gr_estimators = {"simple": digital.SNR_EST_SIMPLE,
		     "skew": digital.SNR_EST_SKEW,
		     "m2m4": digital.SNR_EST_M2M4,
		     "svr": digital.SNR_EST_SVR}
    py_estimators = {"simple": snr_est_simple,
		     "skew": snr_est_m2m4,
		     "m2m4": snr_est_m2m4,
		     "svr": snr_est_svr}


    def __init__(self):
        gr.top_block.__init__(self)
#Note that eng_float is a float in engineering notation (ie 4e5)
        usage = "usage: %prog [options] min_freq max_freq"
        parser = OptionParser(option_class=eng_option, usage=usage)
        parser.add_option("-a", "--args", type="string", default="",
                          help="UHD device device address args [default=%default]")
        parser.add_option("", "--spec", type="string", default=None,
	                  help="Subdevice of UHD device where appropriate")
        parser.add_option("-A", "--antenna", type="string", default=None,
                          help="select Rx Antenna where appropriate")
        parser.add_option("-s", "--samp-rate", type="eng_float", default=1e6,
                          help="set sample rate [default=%default]")
        parser.add_option("-g", "--gain", type="eng_float", default=None,
                          help="set gain in dB (default is midpoint)")
        parser.add_option("", "--tune-delay", type="eng_float",
                          default=1e-3, metavar="SECS",
                          help="time to delay (in seconds) after changing frequency [default=%default]")
        parser.add_option("", "--dwell-delay", type="eng_float",
                          default=10e-3, metavar="SECS",
                          help="time to dwell (in seconds) at a given frequncy [default=%default]")
        parser.add_option("-F", "--fft-size", type="int", default=256,
                          help="specify number of FFT bins [default=%default]")
        parser.add_option("", "--real-time", action="store_true", default=False,
                          help="Attempt to enable real-time scheduling")
	parser.add_option("", "--rank", action="store_true", default=False,
			  help="Rank spectra by quality and choose best")
	parser.add_option("", "--overlap", type="eng_float", default=0.75,
			  help="Percentage of chunk that is unique [default=%default]")
	parser.add_option("-N", "--nsamples", type="int", default=10000,
			  help="Set the number of samples to process [default=%default]")
	parser.add_option("", "--snr-min", type="float", default=-5,
			  help="Minimum SNR [default=%default]")
	parser.add_option("", "--snr-max", type="float", default=20,
			  help="Maximum SNR [default=%default]")
	parser.add_option("", "--snr-step", type="float", default=0.5,
			  help="SNR step amount [default=%default]")
	parser.add_option("-t", "--type", type="choice",
			  choices=my_top_block.gr_estimators.keys(), default="simple",
			  help="Estimator type {0} [default=%default]".format(
				my_top_block.gr_estimators.keys()))
        (options, args) = parser.parse_args()
        if len(args) != 2:
           parser.print_help()
           sys.exit(1)

        self.min_freq = eng_notation.str_to_num(args[0])
        self.max_freq = eng_notation.str_to_num(args[1])


        if self.min_freq > self.max_freq:
            #swap them
            self.min_freq, self.max_freq = self.max_freq, self.min_freq

	self.fft_size = options.fft_size

        if not options.real_time:
            realtime = False
        else:
            # Attempt to enable realtime scheduling
            r = gr.enable_realtime_scheduling()
            if r == gr.RT_OK:
                realtime = True
            else:
                realtime = False
                print "Note: failed to enable realtime scheduling"

        # build graph
        self.u = uhd.usrp_source(device_addr=options.args,
                                 stream_args=uhd.stream_args('fc32'))

        # Set the subdevice spec
        if(options.spec):
            self.u.set_subdev_spec(options.spec, 0)

        # Set the antenna
        if(options.antenna):
            self.u.set_antenna(options.antenna, 0)

        usrp_rate = options.samp_rate
        self.u.set_samp_rate(usrp_rate)
        dev_rate = self.u.get_samp_rate()

	s2v = gr.stream_to_vector(gr.sizeof_gr_complex, self.fft_size)

        mywindow = window.blackmanharris(self.fft_size)
        fft = gr.fft_vcc(self.fft_size, True, mywindow)
        power = 0
        for tap in mywindow:
            power += tap*tap

        c2mag = gr.complex_to_mag_squared(self.fft_size)

        # FIXME the log10 primitive is dog slow
        log = gr.nlog10_ff(10, self.fft_size,
                           -20*math.log10(self.fft_size)-10*math.log10(power/self.fft_size))

        # Set the freq_step to 75% of the actual data throughput.
        # This allows us to discard the bins on both ends of the spectrum.

        self.freq_step = options.overlap * usrp_rate
        self.min_center_freq = self.min_freq + self.freq_step/2
        nsteps = math.ceil((self.max_freq - self.min_freq) / self.freq_step)
        self.max_center_freq = self.min_center_freq + (nsteps * self.freq_step)

        self.next_freq = self.min_center_freq

        tune_delay  = max(0, int(round(options.tune_delay * usrp_rate / self.fft_size)))  # in fft_frames
        dwell_delay = max(1, int(round(options.dwell_delay * usrp_rate / self.fft_size))) # in fft_frames

        self.msgq = gr.msg_queue(16)
        self._tune_callback = tune(self)        # hang on to this to keep it from being GC'd
        stats = gr.bin_statistics_f(self.fft_size, self.msgq,
                                    self._tune_callback, tune_delay,
                                    dwell_delay)

        # FIXME leave out the log10 until we speed it up
	#self.connect(self.u, s2v, fft, c2mag, log, stats)
	self.connect(self.u, s2v, fft, c2mag, stats)

        if options.gain is None:
            # if no gain was specified, use the mid-point in dB
            g = self.u.get_gain_range()
            options.gain = float(g.start()+g.stop())/2.0

        self.set_gain(options.gain)
	print "gain =", options.gain

    def set_next_freq(self):
        target_freq = self.next_freq
        self.next_freq = self.next_freq + self.freq_step
        if self.next_freq >= self.max_center_freq:
            self.next_freq = self.min_center_freq

        if not self.set_freq(target_freq):
            print "Failed to set frequency to", target_freq
            sys.exit(1)

        return target_freq


    def set_freq(self, target_freq):
        """
        Set the center frequency we're interested in.

        @param target_freq: frequency in Hz
        @rypte: bool
        """
        r = self.u.set_center_freq(target_freq)
        if r:
            return True

        return False

    def set_gain(self, gain):
        self.u.set_gain(gain)

    

def main_loop(tb):

    def qsortr(list): #Use quick sort to rank the list of best channels
	return [] if list==[] else qsortr([x for x in list[1:] if x < list[0]]) + [list[0]] + qsortr([x for x in list[1:] if x >= list[0]])
    done = 0
    global chunk_score 
    chunk_score = []
##### Weight Constants #####
    avg_weight = 1
    dev_weight = 1
    savg_weight = 1
    tavg_weight = 1
############################
    while(done != 1): #This loop happens once for each chunk
        # Get the next message sent from the C++ code (blocking call).
        # It contains the center frequency and the mag squared of the fft
        m = parse_msg(tb.msgq.delete_head())
	
#FIXME Look for rank option and sort best frequencies. Look for other characteristics besides just raw power. 
	best_dB = []
	best = m.data[0]
	for i in numpy.arange(0, len(m.data), 1):
		best_dB.append(20*math.log(((m.data[i]**0.5)/1024), 10))
		if m.data[i] <= best:
			best = m.data[i]

#	best = qsortr(m.data)
	best = 20*math.log(((best**0.5)/1024), 10) #transform m.data to power	
	print "Lowest power of this chunk is", best,	
	print "dB at", m.center_freq,
	print "Hz" 	
#	print tb.min_freq		
	avg = numpy.mean(m.data)
	dev = numpy.std(m.data)
	streak_lengths = []
	trimmed_best = []
	streak = 0
	for j in numpy.arange(0,len(m.data),1):
		if best_dB[j] <= best + 10:
			trimmed_best.append(best_dB[i])
			streak = streak + 1
		else:
			streak_lengths.append(streak)
			streak = 0
	streakAvg = numpy.mean(streak_lengths)
	TrimmedAvg = numpy.mean(trimmed_best)
	print "Streak Average of this chunk: ",
	print streakAvg
	print "Trimmed Average of this chunk: ",
	print TrimmedAvg
	chunk_score.append(((avg/avg_weight)**2 + (dev/dev_weight)**2 + (streakAvg/savg_weight)**2 + (TrimmedAvg/tavg_weight)**2)**0.5)
#FIXME hack in the transmitter demo so that once the right frequency is picked, we can actually start
#to transmit on it.

#tab in everything one more time so I can get another block in that's not in the while loop	
#FIXME plot spectrum showing where quality bandwidth is
#	min = 500000000
#	max = 550000000
#	x = numpy.arange(min, max, 288);
#	y = numpy.sin(x)
#	pyplot.plot(x, y)
#	pyplot.show()
       

        # m.data are the mag_squared of the fft output (they are in the
        # standard order.  I.e., bin 0 == DC.)
        # Probably want to do the equivalent of "fftshift" on them
        # m.raw_data is a string that contains the binary floats.
        # You could write this as binary to a file.
	if m.center_freq >= (tb.max_freq - 1625000):
	    done = 1
	    print qsortr(chunk_score) 


if __name__ == '__main__': #If we're running this script as the main program, do this stuff:
    t = ThreadClass()
    t.start()

    tb = my_top_block()
    try:
        tb.start()
        main_loop(tb)

    except KeyboardInterrupt:
        pass

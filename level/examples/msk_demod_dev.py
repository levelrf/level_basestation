#!/usr/bin/env python

from gnuradio import digital
from gnuradio import blks2
from gnuradio import gr
from gnuradio import uhd
from gnuradio.gr import firdes
from gnuradio.level import msk
from math import pi
import time, re

class msk_demod_dev(gr.top_block):

	def __init__(self):
		gr.top_block.__init__(self, "MSK Demod Demo")

		# Variables
		self.samp_rate = samp_rate = 125e3
		self.f_center = f_center = 868e6
		self.bandwidth = bandwidth = 100e3
		self.decimation = decimation = 2

		# Blocks
		self.uhd_usrp_source_0 = uhd.usrp_source(
			device_addr="",
			stream_args=uhd.stream_args(
				cpu_format="fc32",
				channels=range(1),
			),
		)
		self.uhd_usrp_source_0.set_samp_rate(samp_rate)
		self.uhd_usrp_source_0.set_center_freq(f_center, 0)
		self.uhd_usrp_source_0.set_gain(0, 0)
		self.uhd_usrp_source_0.set_bandwidth(bandwidth, 0)

		#self.throttle = gr.throttle(gr.sizeof_gr_complex, 26.25e3)
		self.decimate = blks2.rational_resampler_ccc(1, 1)
		self.msk_demod = msk.msk_demod_cb()
		self.sink = gr.vector_sink_b(1)
		self.file_sink = gr.file_sink(gr.sizeof_char, 'fsk_dump.log')

		# Connections
		self.connect(self.uhd_usrp_source_0, self.msk_demod, self.sink)
		self.connect(self.msk_demod, self.file_sink)

def all_indices(value, qlist):
    indices = []
    idx = -1
    while True:
        try:
            idx = qlist.index(value, idx+1)
            indices.append(idx)
        except ValueError:
            break
    return indices

if __name__ == '__main__':
	gr.enable_realtime_scheduling()
	tb = msk_demod_dev()
	tb.start()
	time.sleep(1)
	tb.stop()
	sink_data = list(tb.sink.data())
	sink_str = ''.join(map(str,sink_data))
	#ones = len([x for x in sink_data if x is 1])
	preamble = '10'*4*4
	sync = '1101001110010001'
	#print float(ones) / len(sink_data)
	print len(sink_data)
	print "preamble:", [m.start() for m in re.finditer(preamble, sink_str)]
	print "sync:", [n.start() for n in re.finditer(sync, sink_str)]

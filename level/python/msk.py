from gnuradio import gr
from gnuradio import digital
from gnuradio.gr import firdes
from gnuradio import filter
from math import pi
import numpy

# spent a lot of time here...
# if having trouble demodulating compute the average of noise RX msk_demod in floats
# it should be as close to 0 as possible (.000X is preferable), gaussian filter and
# clock recovery help, also use offset to test
# if that fails dump sliced output to file and look for the packet, you should see something
# in the sublime text overhead view

# note interpolating filter on modulater, decimating on demodulator

class msk_demod_cf(gr.hier_block2):
    def __init__(self, bt = 0.3, samples_per_symbol = 2, ti_adj=False, magic_num=0):
        """
        Hierarchical block for MSK demodulation.
    
        The input is the complex modulated signal at baseband
        and the output is a stream of floats.
        """
        # Initialize base class
        gr.hier_block2.__init__(self, "msk_demod",
                gr.io_signature(1, 1, gr.sizeof_gr_complex),
                gr.io_signature(1, 1, gr.sizeof_float))

        self.sps = 2
        self.bt = 0.35
        self.mu = 0.5
        self.gain_mu = 0.175
        self.freq_error = 0.0
        self.omega_relative_limit = 0.005

        self.omega = self.sps * (1 + self.freq_error)
        self.gain_omega = .25 * self.gain_mu * self.gain_mu        # critically damped

        # Demodulate FM
        sensitivity = (pi / 2) / self.sps
        self.fmdemod = gr.quadrature_demod_cf(1.0 / sensitivity)
        self.invert = gr.multiply_const_vff((-1, ))

        # TODO: this is hardcoded, how to figure out this value?
        self.offset = gr.add_const_vff((-1.2, ))
        self.offset2 = gr.add_const_vff((magic_num, ))

        self.nfilts = nfilts = 32
        self.sps = sps = 2
        self.rrc_taps = rrc_taps = filter.firdes.root_raised_cosine(nfilts, nfilts, 1.0/float(sps), 0.35, 11*sps*nfilts)
        
        self.pfb = digital.pfb_clock_sync_ccf(sps, 2*3.14/100.0, (rrc_taps), nfilts, nfilts/2, 1.5, 1)

        # the clock recovery block tracks the symbol clock and resamples as needed.
        # the output of the block is a stream of soft symbols (float)
        self.clock_recovery = digital.clock_recovery_mm_ff(self.omega, self.gain_omega,
                                                               self.mu, self.gain_mu,
                                                               self.omega_relative_limit)

        ntaps = 4 * samples_per_symbol              # up to 3 bits in filter at once
        sensitivity = (pi / 2) / samples_per_symbol # phase change per bit = pi / 2

        # Form Gaussian filter
        # Generate Gaussian response (Needs to be convolved with window below).
        self.gaussian_taps = gr.firdes.gaussian(1, samples_per_symbol, bt, ntaps)

        self.sqwave = (1,) * samples_per_symbol       # rectangular window
        self.taps = numpy.convolve(numpy.array(self.gaussian_taps),numpy.array(self.sqwave))
        self.gaussian_filter = filter.fir_filter_ccc(samples_per_symbol, self.taps)


        self.slicer = digital.binary_slicer_fb()

        if ti_adj:
            self.connect(self, self.fmdemod, self.invert, self.clock_recovery, self.offset, self)
        else:
            self.connect(self, self.gaussian_filter, self.fmdemod, self.clock_recovery, self.offset2, self)

class msk_mod_bc(gr.hier_block2):
    def __init__(self, bt = 0.3, samples_per_symbol = 2, ti_adj=False):
        gr.hier_block2.__init__(self, "msk_demod",
                gr.io_signature(1, 1, gr.sizeof_char),
                gr.io_signature(1, 1, gr.sizeof_gr_complex))

        self.sps = 2
        self.bt = 0.35
        self.mu = 0.5
        self.gain_mu = 0.175
        self.freq_error = 0.0
        self.omega_relative_limit = 0.005

        self.omega = self.sps * (1 + self.freq_error)
        self.gain_omega = .25 * self.gain_mu * self.gain_mu        # critically damped

        ntaps = 4 * samples_per_symbol              # up to 3 bits in filter at once
        sensitivity = (pi / 2) / samples_per_symbol # phase change per bit = pi / 2

        # Turn it into NRZ data.
        self.unpack = gr.packed_to_unpacked_bb(1, gr.GR_MSB_FIRST)
        self.nrz = digital.chunks_to_symbols_bf([-1, 1], 1) # note could also invert bits here

        # Form Gaussian filter
        # Generate Gaussian response (Needs to be convolved with window below).
        self.gaussian_taps = gr.firdes.gaussian(1, samples_per_symbol, bt, ntaps)

        self.sqwave = (1,) * samples_per_symbol       # rectangular window
        self.taps = numpy.convolve(numpy.array(self.gaussian_taps),numpy.array(self.sqwave))
        self.gaussian_filter = filter.interp_fir_filter_fff(samples_per_symbol, self.taps)

        # the clock recovery block tracks the symbol clock and resamples as needed.
        # the output of the block is a stream of soft symbols (float)
        self.clock_recovery = digital.clock_recovery_mm_ff(self.omega, self.gain_omega,
                                                               self.mu, self.gain_mu,
                                                               self.omega_relative_limit)

        # FM modulation
        self.fmmod = gr.frequency_modulator_fc(sensitivity)

        # TODO: this is hardcoded, how to figure out this value?
        self.offset = gr.add_const_vff((-.5, ))

        # CC430 RF core is inverted with respect to USRP for some reason
        self.invert = gr.multiply_const_vff((-1, ))

        # Connect & Initialize base class
        if ti_adj:
            self.connect(self, self.unpack, self.nrz, self.invert, self.offset, self.gaussian_filter, self.fmmod, self)
        else:
            self.connect(self, self.unpack, self.nrz, self.gaussian_filter, self.fmmod, self)
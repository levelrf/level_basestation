#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: MPSK Demod Demo
# Generated: Thu Aug 30 18:36:39 2012
##################################################

from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.gr import firdes
from optparse import OptionParser

class mpsk_demod(gr.top_block):

	def __init__(self):
		gr.top_block.__init__(self, "MPSK Demod Demo")

		##################################################
		# Variables
		##################################################
		self.samp_rate = samp_rate = 250e3
		self.f_center = f_center = 868e6

		##################################################
		# Blocks
		##################################################
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
		self.uhd_usrp_source_0.set_bandwidth(25e3, 0)
		self.low_pass_filter_1 = gr.fir_filter_fff(1, firdes.low_pass(
			1, samp_rate, 100e3, 4000, firdes.WIN_HAMMING, 6.76))
		self.low_pass_filter_0 = gr.fir_filter_ccf(1, firdes.low_pass(
			1, samp_rate, 125e3, 4000, firdes.WIN_HAMMING, 6.76))
		self.gr_vector_sink_x_0 = gr.vector_sink_b(1)
		self.gr_quadrature_demod_cf_0 = gr.quadrature_demod_cf(.3)
		self.gr_multiply_const_vxx_0 = gr.multiply_const_vff((-1, ))
		self.digital_clock_recovery_mm_xx_0 = digital.clock_recovery_mm_ff(4, .04, .5, .4, .0323)
		self.digital_binary_slicer_fb_0 = digital.binary_slicer_fb()

		##################################################
		# Connections
		##################################################
		self.connect((self.uhd_usrp_source_0, 0), (self.low_pass_filter_0, 0))
		self.connect((self.low_pass_filter_0, 0), (self.gr_quadrature_demod_cf_0, 0))
		self.connect((self.gr_quadrature_demod_cf_0, 0), (self.low_pass_filter_1, 0))
		self.connect((self.low_pass_filter_1, 0), (self.digital_clock_recovery_mm_xx_0, 0))
		self.connect((self.digital_binary_slicer_fb_0, 0), (self.gr_vector_sink_x_0, 0))
		self.connect((self.gr_multiply_const_vxx_0, 0), (self.digital_binary_slicer_fb_0, 0))
		self.connect((self.digital_clock_recovery_mm_xx_0, 0), (self.gr_multiply_const_vxx_0, 0))

	def get_samp_rate(self):
		return self.samp_rate

	def set_samp_rate(self, samp_rate):
		self.samp_rate = samp_rate
		self.uhd_usrp_source_0.set_samp_rate(self.samp_rate)
		self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, 125e3, 4000, firdes.WIN_HAMMING, 6.76))
		self.low_pass_filter_1.set_taps(firdes.low_pass(1, self.samp_rate, 100e3, 4000, firdes.WIN_HAMMING, 6.76))

	def get_f_center(self):
		return self.f_center

	def set_f_center(self, f_center):
		self.f_center = f_center
		self.uhd_usrp_source_0.set_center_freq(self.f_center, 0)

if __name__ == '__main__':
	parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
	(options, args) = parser.parse_args()
	if gr.enable_realtime_scheduling() != gr.RT_OK:
		print "Error: failed to enable realtime scheduling."
	tb = mpsk_demod()
	tb.start()
	raw_input('Press Enter to quit: ')
	tb.stop()


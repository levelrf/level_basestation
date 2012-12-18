#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Cheetara Tx
# Generated: Mon Dec 17 21:02:50 2012
##################################################

from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.gr import firdes
from optparse import OptionParser

class cheetara_tx(gr.top_block):

	def __init__(self):
		gr.top_block.__init__(self, "Cheetara Tx")

		##################################################
		# Variables
		##################################################
		self.samp_rate = samp_rate = 32000

		##################################################
		# Blocks
		##################################################
		self.uhd_usrp_sink_0 = uhd.usrp_sink(
			device_addr="serial=E8R10Z2B1",
			stream_args=uhd.stream_args(
				cpu_format="fc32",
				channels=range(1),
			),
		)
		self.uhd_usrp_sink_0.set_samp_rate(samp_rate)
		self.uhd_usrp_sink_0.set_center_freq(500e6, 0)
		self.uhd_usrp_sink_0.set_gain(5, 0)
		self.uhd_usrp_sink_0.set_bandwidth(100e3, 0)
		self.gr_sig_source_x_0 = gr.sig_source_c(samp_rate, gr.GR_COS_WAVE, 1000, 1, 0)

		##################################################
		# Connections
		##################################################
		self.connect((self.gr_sig_source_x_0, 0), (self.uhd_usrp_sink_0, 0))

# QT sink close method reimplementation

	def get_samp_rate(self):
		return self.samp_rate

	def set_samp_rate(self, samp_rate):
		self.samp_rate = samp_rate
		self.gr_sig_source_x_0.set_sampling_freq(self.samp_rate)
		self.uhd_usrp_sink_0.set_samp_rate(self.samp_rate)

if __name__ == '__main__':
	parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
	(options, args) = parser.parse_args()
	tb = cheetara_tx()
	tb.start()
	raw_input('Press Enter to quit: ')
	tb.stop()


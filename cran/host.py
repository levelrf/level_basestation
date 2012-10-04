#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Host
# Generated: Tue Sep 18 20:18:51 2012
##################################################

from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.gr import firdes
from optparse import OptionParser
import gnuradio.extras as gr_extras

class host(gr.top_block):

	def __init__(self):
		gr.top_block.__init__(self, "Host")

		##################################################
		# Variables
		##################################################
		self.samp_rate = samp_rate = 125e3

		##################################################
		# Blocks
		##################################################
		self.uhd_usrp_sink_0 = uhd.usrp_sink(
			device_addr="",
			stream_args=uhd.stream_args(
				cpu_format="fc32",
				channels=range(1),
			),
		)
		self.uhd_usrp_sink_0.set_samp_rate(samp_rate)
		self.uhd_usrp_sink_0.set_center_freq(868E6, 0)
		self.uhd_usrp_sink_0.set_gain(5, 0)
		self.uhd_usrp_sink_0.set_bandwidth(200e3, 0)
		self.extras_socket_to_blob_0 = gr_extras.socket_to_blob("TCP", "127.0.0.1", "5000", 0)
		self.extras_blob_to_stream_0 = gr_extras.blob_to_stream(8)

		##################################################
		# Connections
		##################################################
		self.connect((self.extras_blob_to_stream_0, 0), (self.uhd_usrp_sink_0, 0))
		self.connect((self.extras_socket_to_blob_0, 0), (self.extras_blob_to_stream_0, 0))

	def get_samp_rate(self):
		return self.samp_rate

	def set_samp_rate(self, samp_rate):
		self.samp_rate = samp_rate
		self.uhd_usrp_sink_0.set_samp_rate(self.samp_rate)

if __name__ == '__main__':
	parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
	(options, args) = parser.parse_args()
	tb = host()
	tb.start()
	raw_input('Press Enter to quit: ')
	tb.stop()


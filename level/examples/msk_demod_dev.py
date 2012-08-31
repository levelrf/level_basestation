#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: MPSK Demod Demo
# Generated: Thu Aug 30 16:03:43 2012
##################################################

from gnuradio import digital
from gnuradio import gr
from gnuradio import uhd
from gnuradio.gr import firdes
from math import pi

class msk_demod_dev(gr.top_block):

	def __init__(self):
		gr.top_block.__init__(self, "FSK Demod Demo")

		##################################################
		# Variables
		##################################################
		self.samp_rate = samp_rate = 128e3
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

		self.msk_demod = digital.gmsk.gmsk_demod()
		self.sink = gr.vector_sink_b(1)

		##################################################
		# Connections
		##################################################
		self.connect(self.uhd_usrp_source_0, self.msk_demod, self.sink)

if __name__ == '__main__':
	gr.enable_realtime_scheduling()
	tb = msk_demod_dev()
	tb.start()
	raw_input('Press Enter to quit: ')
	tb.stop()
	sink_data = tb.sink.data()
	ones = len([x for x in sink_data if x is 1])
	print float(ones) / len(sink_data)
	#print sink_data[-1000:]


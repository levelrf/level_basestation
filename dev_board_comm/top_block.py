#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Top Block
# Generated: Fri Nov  2 14:42:28 2012
##################################################

from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.gr import firdes
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import wx

class top_block(grc_wxgui.top_block_gui):

	def __init__(self):
		grc_wxgui.top_block_gui.__init__(self, title="Top Block")
		_icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
		self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

		##################################################
		# Variables
		##################################################
		self.samp_rate = samp_rate = 125000

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
		self.uhd_usrp_sink_0.set_center_freq(868000000, 0)
		self.uhd_usrp_sink_0.set_gain(5, 0)
		self.uhd_usrp_sink_0.set_bandwidth(500000, 0)
		self.gr_file_source_0 = gr.file_source(gr.sizeof_char*1, "/home/hunter/packet9.bin", True)
		self.digital_gmsk_mod_0 = digital.gmsk_mod(
			samples_per_symbol=2,
			bt=0.3,
			verbose=False,
			log=False,
		)

		##################################################
		# Connections
		##################################################
		self.connect((self.gr_file_source_0, 0), (self.digital_gmsk_mod_0, 0))
		self.connect((self.digital_gmsk_mod_0, 0), (self.uhd_usrp_sink_0, 0))

	def get_samp_rate(self):
		return self.samp_rate

	def set_samp_rate(self, samp_rate):
		self.samp_rate = samp_rate
		self.uhd_usrp_sink_0.set_samp_rate(self.samp_rate)

if __name__ == '__main__':
	parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
	(options, args) = parser.parse_args()
	tb = top_block()
	tb.Run(True)


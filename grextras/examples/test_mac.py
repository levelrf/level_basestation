#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Test Mac
# Generated: Wed Oct  3 22:20:21 2012
##################################################

from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.gr import firdes
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import gnuradio.extras as gr_extras
import wx

class test_mac(grc_wxgui.top_block_gui):

	def __init__(self):
		grc_wxgui.top_block_gui.__init__(self, title="Test Mac")
		_icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
		self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

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
		self.uhd_usrp_sink_0.set_center_freq(868e6, 0)
		self.uhd_usrp_sink_0.set_gain(10, 0)
		self.uhd_usrp_sink_0.set_bandwidth(200e3, 0)
		self.extras_socket_to_blob_0 = gr_extras.socket_to_blob("TCP", "127.0.0.1", "8000", 0)
		self.digital_gmsk_mod_0 = digital.gmsk_mod(
			samples_per_symbol=2,
			bt=0.35,
			verbose=False,
			log=False,
		)

		##################################################
		# Connections
		##################################################
		self.connect((self.extras_socket_to_blob_0, 0), (self.digital_gmsk_mod_0, 0))
		self.connect((self.digital_gmsk_mod_0, 0), (self.uhd_usrp_sink_0, 0))

	def get_samp_rate(self):
		return self.samp_rate

	def set_samp_rate(self, samp_rate):
		self.samp_rate = samp_rate
		self.uhd_usrp_sink_0.set_samp_rate(self.samp_rate)

if __name__ == '__main__':
	parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
	(options, args) = parser.parse_args()
	tb = test_mac()
	tb.Run(True)


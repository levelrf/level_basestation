#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Dual Mac Loop Back
# Generated: Wed Oct  3 15:57:53 2012
##################################################

from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.gr import firdes
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import gnuradio.extras as gr_extras
import wx

class dual_mac_loop_back(grc_wxgui.top_block_gui):

	def __init__(self, rx_freq=915e6, rx_gain=15, tx_freq=915e6, tx_gain=15, rate=1e6, args="", ampl=0.7, samp_per_sym=4, no_arq_port="12345", radio_addr=85, arq_port="12346", arq_timeout=0.1):
		grc_wxgui.top_block_gui.__init__(self, title="Dual Mac Loop Back")
		_icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
		self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

		##################################################
		# Parameters
		##################################################
		self.rx_freq = rx_freq
		self.rx_gain = rx_gain
		self.tx_freq = tx_freq
		self.tx_gain = tx_gain
		self.rate = rate
		self.args = args
		self.ampl = ampl
		self.samp_per_sym = samp_per_sym
		self.no_arq_port = no_arq_port
		self.radio_addr = radio_addr
		self.arq_port = arq_port
		self.arq_timeout = arq_timeout

		##################################################
		# Variables
		##################################################
		self.samp_rate = samp_rate = rate

		##################################################
		# Blocks
		##################################################
		self.virtual_channel_formatter_0 = gr_extras.virtual_channel_formatter(86,1)
		self.simple_mac_0_0 = gr_extras.simple_mac(85,arq_timeout,10)
		self.simple_mac_0 = gr_extras.simple_mac(86,arq_timeout,10)
		self.msg_to_stdout_0 = gr_extras.msg_to_stdout()
		self.heart_beat_0_1 = gr_extras.heart_beat(0.001,"W","")
		self.heart_beat_0_0 = gr_extras.heart_beat(2,"W","this is a test beacon")

		##################################################
		# Connections
		##################################################
		self.connect((self.virtual_channel_formatter_0, 0), (self.simple_mac_0_0, 1))
		self.connect((self.simple_mac_0, 0), (self.simple_mac_0_0, 0))
		self.connect((self.heart_beat_0_1, 0), (self.simple_mac_0, 2))
		self.connect((self.heart_beat_0_0, 0), (self.virtual_channel_formatter_0, 0))
		self.connect((self.simple_mac_0, 1), (self.msg_to_stdout_0, 0))
		self.connect((self.simple_mac_0_0, 0), (self.simple_mac_0, 0))

	def get_rx_freq(self):
		return self.rx_freq

	def set_rx_freq(self, rx_freq):
		self.rx_freq = rx_freq

	def get_rx_gain(self):
		return self.rx_gain

	def set_rx_gain(self, rx_gain):
		self.rx_gain = rx_gain

	def get_tx_freq(self):
		return self.tx_freq

	def set_tx_freq(self, tx_freq):
		self.tx_freq = tx_freq

	def get_tx_gain(self):
		return self.tx_gain

	def set_tx_gain(self, tx_gain):
		self.tx_gain = tx_gain

	def get_rate(self):
		return self.rate

	def set_rate(self, rate):
		self.rate = rate
		self.set_samp_rate(self.rate)

	def get_args(self):
		return self.args

	def set_args(self, args):
		self.args = args

	def get_ampl(self):
		return self.ampl

	def set_ampl(self, ampl):
		self.ampl = ampl

	def get_samp_per_sym(self):
		return self.samp_per_sym

	def set_samp_per_sym(self, samp_per_sym):
		self.samp_per_sym = samp_per_sym

	def get_no_arq_port(self):
		return self.no_arq_port

	def set_no_arq_port(self, no_arq_port):
		self.no_arq_port = no_arq_port

	def get_radio_addr(self):
		return self.radio_addr

	def set_radio_addr(self, radio_addr):
		self.radio_addr = radio_addr

	def get_arq_port(self):
		return self.arq_port

	def set_arq_port(self, arq_port):
		self.arq_port = arq_port

	def get_arq_timeout(self):
		return self.arq_timeout

	def set_arq_timeout(self, arq_timeout):
		self.arq_timeout = arq_timeout

	def get_samp_rate(self):
		return self.samp_rate

	def set_samp_rate(self, samp_rate):
		self.samp_rate = samp_rate

if __name__ == '__main__':
	parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
	parser.add_option("", "--rx-freq", dest="rx_freq", type="eng_float", default=eng_notation.num_to_str(915e6),
		help="Set rx_freq [default=%default]")
	parser.add_option("", "--rx-gain", dest="rx_gain", type="eng_float", default=eng_notation.num_to_str(15),
		help="Set rx_gain [default=%default]")
	parser.add_option("", "--tx-freq", dest="tx_freq", type="eng_float", default=eng_notation.num_to_str(915e6),
		help="Set tx_freq [default=%default]")
	parser.add_option("", "--tx-gain", dest="tx_gain", type="eng_float", default=eng_notation.num_to_str(15),
		help="Set tx_gain [default=%default]")
	parser.add_option("", "--rate", dest="rate", type="eng_float", default=eng_notation.num_to_str(1e6),
		help="Set S [default=%default]")
	parser.add_option("", "--args", dest="args", type="string", default="",
		help="Set args [default=%default]")
	parser.add_option("", "--ampl", dest="ampl", type="eng_float", default=eng_notation.num_to_str(0.7),
		help="Set a [default=%default]")
	parser.add_option("", "--samp-per-sym", dest="samp_per_sym", type="intx", default=4,
		help="Set sps [default=%default]")
	parser.add_option("", "--no-arq-port", dest="no_arq_port", type="string", default="12345",
		help="Set no_arq_port [default=%default]")
	parser.add_option("", "--radio-addr", dest="radio_addr", type="intx", default=85,
		help="Set radio_addr [default=%default]")
	parser.add_option("", "--arq-port", dest="arq_port", type="string", default="12346",
		help="Set arq_port [default=%default]")
	parser.add_option("", "--arq-timeout", dest="arq_timeout", type="eng_float", default=eng_notation.num_to_str(0.1),
		help="Set arq_timeout [default=%default]")
	(options, args) = parser.parse_args()
	tb = dual_mac_loop_back(rx_freq=options.rx_freq, rx_gain=options.rx_gain, tx_freq=options.tx_freq, tx_gain=options.tx_gain, rate=options.rate, args=options.args, ampl=options.ampl, samp_per_sym=options.samp_per_sym, no_arq_port=options.no_arq_port, radio_addr=options.radio_addr, arq_port=options.arq_port, arq_timeout=options.arq_timeout)
	tb.Run(True)


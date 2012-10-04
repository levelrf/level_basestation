#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Client
# Generated: Tue Sep 18 20:43:37 2012
##################################################

from PyQt4 import Qt
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.gr import firdes
from optparse import OptionParser
import gnuradio.extras as gr_extras
import sys

class client(gr.top_block, Qt.QWidget):

	def __init__(self):
		gr.top_block.__init__(self, "Client")
		Qt.QWidget.__init__(self)
		self.setWindowTitle("Client")
		self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
		self.top_scroll_layout = Qt.QVBoxLayout()
		self.setLayout(self.top_scroll_layout)
		self.top_scroll = Qt.QScrollArea()
		self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
		self.top_scroll_layout.addWidget(self.top_scroll)
		self.top_scroll.setWidgetResizable(True)
		self.top_widget = Qt.QWidget()
		self.top_scroll.setWidget(self.top_widget)
		self.top_layout = Qt.QVBoxLayout(self.top_widget)
		self.top_grid_layout = Qt.QGridLayout()
		self.top_layout.addLayout(self.top_grid_layout)


		##################################################
		# Variables
		##################################################
		self.samp_rate = samp_rate = 125e3

		##################################################
		# Blocks
		##################################################
		self.uhd_usrp_source_0 = uhd.usrp_source(
			device_addr="",
			stream_args=uhd.stream_args(
				cpu_format="fc32",
				args="serial=E8R10Z2B1",
				channels=range(1),
			),
		)
		self.uhd_usrp_source_0.set_samp_rate(samp_rate)
		self.uhd_usrp_source_0.set_center_freq(868e6, 0)
		self.uhd_usrp_source_0.set_gain(5, 0)
		self.uhd_usrp_source_0.set_bandwidth(200e3, 0)
		self.extras_stream_to_blob_0 = gr_extras.stream_to_blob(8, 0)
		self.extras_blob_to_socket_0 = gr_extras.blob_to_socket("TCP", "127.0.0.1", "5000")

		##################################################
		# Connections
		##################################################
		self.connect((self.uhd_usrp_source_0, 0), (self.extras_stream_to_blob_0, 0))
		self.connect((self.extras_stream_to_blob_0, 0), (self.extras_blob_to_socket_0, 0))

	def get_samp_rate(self):
		return self.samp_rate

	def set_samp_rate(self, samp_rate):
		self.samp_rate = samp_rate
		self.uhd_usrp_source_0.set_samp_rate(self.samp_rate)

if __name__ == '__main__':
	parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
	(options, args) = parser.parse_args()
	qapp = Qt.QApplication(sys.argv)
	tb = client()
	tb.start()
	tb.show()
	qapp.exec_()
	tb.stop()


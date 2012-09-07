#!/usr/bin/python
#!/usr/bin/env python

from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import uhd
from gnuradio import window
from gnuradio import digital
from gnuradio import blks2
from gnuradio.eng_option import eng_option
from grc_gnuradio import wxgui as grc_wxgui
from gnuradio.wxgui import fftsink2
from gnuradio.gr import firdes
from optparse import OptionParser
from gnuradio import level
from math import pi

class fsk_rx(gr.top_block):
    def __init__(self):
        gr.top_block.__init__(self, "CC1101 Burst Detector")

        def rx_callback():
            print "Callback Fired"

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 125e3
        self.f_center = f_center = 868e6
        self.sps = sps = 2
        self.sensitivity = sensitivity = (pi / 2) / sps
        self.alpha = alpha = 0.0512/sps
        self.gain = gain = 0

        ##################################################
        # Blocks
        ##################################################
        self.uhd_src = uhd.usrp_source(
            device_addr="",
            stream_args=uhd.stream_args(
                cpu_format="fc32",
                channels=range(1),
            ),
        )
        self.uhd_src.set_subdev_spec("A:0", 0)
        self.uhd_src.set_samp_rate(samp_rate)
        self.uhd_src.set_center_freq(f_center, 0)
        self.uhd_src.set_gain(0, 0)
        self.uhd_src.set_antenna("TX/RX", 0)
        self.uhd_src.set_bandwidth(25e3, 0)

        self.uhd_src.set_samp_rate(self.samp_rate)
        self.uhd_src.set_center_freq(self.f_center, 0)
        self.uhd_src.set_gain(self.gain, 0)

        self.decimate = blks2.rational_resampler_ccc(1, 8)

        self.packet_receiver = level.cc1k_demod_pkts(callback=rx_callback())

        #self.filesink = gr.file_sink(gr.sizeof_gr_complex, 'rx_test.dat')

        ##################################################
        # Connections
        ##################################################
        self.connect(self.uhd_src, self.packet_receiver)
        #self.connect(self.packet_receiver, self.filesink)

if __name__ == '__main__':
    rx = fsk_rx()
    r = gr.enable_realtime_scheduling()
    rx.start()
    raw_input('Press Enter to quit: ')
    rx.stop()

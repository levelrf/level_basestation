#!/usr/bin/python

from gnuradio import gr
from gnuradio import uhd
from gnuradio import digital
from gnuradio import blks2
from gnuradio.gr import firdes
from gnuradio import level
from math import pi

class const_tx(gr.top_block):
    def __init__(self):
        gr.top_block.__init__(self, "CC1101 Burst Detector")

        def rx_callback():
            print "Callback Fired"

        # Variables
        self.samp_rate = samp_rate = 125e3
        self.f_center = f_center = 520e6
        self.bandwidth = bandwidth = 200e3
        self.gain = gain = 5

        # Blocks
        self.uhd_sink = uhd.usrp_sink(
            device_addr="serial=E4R11Y0B1", #cheetara
            stream_args=uhd.stream_args(
                cpu_format="fc32",
                channels=range(1),
            ),
        )

        self.uhd_sink.set_samp_rate(samp_rate)
        self.uhd_sink.set_center_freq(f_center, 0)
        self.uhd_sink.set_gain(gain, 0)
        self.uhd_sink.set_antenna("TX/RX", 0)
        self.uhd_sink.set_bandwidth(bandwidth, 0)

        self.uhd_sink.set_samp_rate(self.samp_rate)
        self.uhd_sink.set_center_freq(self.f_center, 0)
        self.uhd_sink.set_gain(self.gain, 0)

        self.src = gr.sig_source_f(samp_rate, gr.GR_COS_WAVE, 1000, 1, 0)
        self.f_to_b = gr.float_to_char()
        self.msk = level.msk_mod_bc()

        # Connections
        self.connect(self.src, self.f_to_b, self.msk, self.uhd_sink)
        #self.connect(self.uhd_sink, self.packet_receiver)

if __name__ == '__main__':
    tx = const_tx()
    r = gr.enable_realtime_scheduling()
    tx.start()
    raw_input('Press Enter to quit: ')
    tx.stop()

#!/usr/bin/python

from gnuradio import gr
from gnuradio import uhd
from gnuradio import digital
from gnuradio import blks2
from gnuradio.gr import firdes
from gnuradio import level
from math import pi
import os

class msk_rx(gr.top_block):
    def __init__(self):
        gr.top_block.__init__(self, "CC1101 Burst Detector")

        def rx_callback():
            print "Callback Fired"

        # Variables
        self.samp_rate = samp_rate = 250e3
        self.f_center = f_center = 510e6
        self.bandwidth = bandwidth = 125e3
        self.gain = gain = 15
        self.sps = sps = 2

        # Blocks
        self.uhd_src = uhd.usrp_source(
            device_addr="serial=E8R10Z2B1", #cheetara
            stream_args=uhd.stream_args(
                cpu_format="fc32",
                channels=range(1),
            ),
        )

        self.uhd_src.set_samp_rate(samp_rate)
        self.uhd_src.set_center_freq(f_center, 0)
        self.uhd_src.set_gain(gain, 0)
        self.uhd_src.set_antenna("TX/RX", 0)
        self.uhd_src.set_bandwidth(bandwidth, 0)

        self.uhd_src.set_samp_rate(self.samp_rate)
        self.uhd_src.set_center_freq(self.f_center, 0)
        self.uhd_src.set_gain(self.gain, 0)

        # change magic_num until abs(ratio) as close to 0 (when sending all A's) 
        # as possible (.000X or closer)
        # need to solve clock synchronization
        self.msk_demod = level.msk_demod_cf(ti_adj=False, magic_num=.022)

        self.agc = gr.agc2_cc()
        #self.clock_sync = digital.pfb_clock_sync_ccf(sps=2,)
        self.costas_loop = digital.costas_loop_cc(2*3.14/100.0, 4)

        self.packet_receiver = level.cc1k_demod_pkts(callback=rx_callback())

        self.vec_sink = gr.vector_sink_f(1)
        self.slicer = digital.binary_slicer_fb()
        self.bin_sink = gr.vector_sink_b(1)

        # Connections
        self.connect(self.uhd_src, self.agc, self.msk_demod, self.slicer, self.bin_sink)
        self.connect(self.msk_demod, self.vec_sink)
        self.connect(self.uhd_src, self.packet_receiver)

if __name__ == '__main__':
    rx = msk_rx()
    r = gr.enable_realtime_scheduling()
    #print 'Blocked waiting for GDB attach (pid = %d)' % (os.getpid(),)
    #raw_input ('Press Enter to continue: ')
    rx.start()
    raw_input('Press Enter to quit: ')
    rx.stop()
    sink_data = list(rx.vec_sink.data())
    print sum(sink_data) / float(len(sink_data))
    bin_data = list(rx.bin_sink.data())
    f = open("rx.dat", "w")
    for index, bit in enumerate(bin_data):
        f.write(str(bit))
        if index % 16 == 0:
            f.write('\n')
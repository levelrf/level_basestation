#!/usr/bin/python

from gnuradio import gr
from gnuradio import uhd
from gnuradio import digital
from gnuradio import blks2
from gnuradio.gr import firdes
import gnuradio.gr.gr_threading as _threading
from gnuradio import level
from gnuradio import extras
from math import pi
from gruel import pmt
from threading import Thread
import time

tx = None

class test_transmit(gr.top_block):
    def __init__(self):
        gr.top_block.__init__(self, "CC1101 Transmitter")

        # Variables
        self.samp_rate = samp_rate = 125e3
        self.f_center = f_center = 868e6
        self.bandwidth = bandwidth = 200e3
        self.gain = gain = 5

        self.msgq = msgq = gr.msg_queue()

        # Blocks
        self.uhd_sink = uhd.usrp_sink(
            device_addr="",
            stream_args=uhd.stream_args(
                cpu_format="fc32",
                channels=range(1),
            ),
        )
        self.uhd_sink.set_samp_rate(samp_rate)
        self.uhd_sink.set_center_freq(f_center, 0)
        self.uhd_sink.set_gain(gain, 0)
        self.uhd_sink.set_bandwidth(bandwidth, 0)

        self.msg_src = gr.message_source(1, msgq)

        self.msk = digital.gmsk_mod(
            samples_per_symbol=2,
            bt=0.3
        )

        #self.b_to_s = extras.blob_to_stream(1)
        #self.blob = extras.pmt_make_blob(8)

        #self.extras_socket_to_blob = extras.socket_to_blob("TCP", "127.0.0.1", "12345", 0)
        #self.extras_blob_to_stream = extras.blob_to_stream(1)

        #msgs = ("this", "test", "should", "pass")
        tb = gr.top_block()

        # Connections
        self.connect(self.msg_src, self.msk, self.uhd_sink)

    def send_pkt(self, payload='', eof=False):
        if eof:
            msg = gr.message(1)
        else:
            msg = gr.message_from_string(payload)
        self.msgq.insert_tail(msg)

    def main_loop(self):
        while True:
            self.send_pkt("a")
            time.sleep(1)
            print self.msgq.count()

class worker(Thread):
    def run(self):
        for x in xrange(5):
            tx.send_pkt("a")
            print tx.msgq.count()
            time.sleep(1)
        tx.send_pkt(eof=True)
        time.sleep(5)
        tx.send_pkt("a")
        tx.send_pkt(eof=True)
        time.sleep(5)

if __name__ == '__main__':
    global tx
    tx = test_transmit()
    #r = gr.enable_realtime_scheduling()
    tx.start()
    worker().start()
    #tx.main_loop()

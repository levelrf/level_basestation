#! /usr/bin/python

# simple demo that transmits the top hacker news post over our network

from gnuradio import gr
from gnuradio import uhd
from gnuradio import digital
from gnuradio import blks2
from gnuradio.gr import firdes
import gnuradio.gr.gr_threading as _threading
from gnuradio.wxgui import fftsink2
from grc_gnuradio import wxgui as grc_wxgui
from gnuradio import level
from math import pi
from gruel import pmt
import urllib2, time, json, operator, binascii, sys
import crcmod

crc16_func = crcmod.mkCrcFun(0x18005, initCrc=0xFFFF, rev=False)

class test_transmit(gr.top_block):
    def __init__(self):
        gr.top_block.__init__(self, "CC430 Transmitter")

        ################################
        # TX Connections
        ################################

        self.sent_pkts = 0

        # 5555 5555 2c6e fd00 0071 da0b e2
        self.test_packet =  chr(0x55)*4                          # preamble
        self.test_packet += chr(0x2c) + chr(0x6e)                # sync
        self.test_packet += chr(0xfc)                            # length
        self.test_packet += chr(0x00) + chr(0x00) + chr(0x00)    # payload
        self.test_packet += chr(0xc3) + chr(0xdb)                # CRC16 (currently incorrect?)

        # Variables
        self.samp_rate = samp_rate = 125e3
        self.f_center = f_center = 520e6
        self.bandwidth = bandwidth = 200e3
        self.gain = gain = 5

        self.msgq = msgq = gr.msg_queue()

        # Blocks
        self.uhd_sink = uhd.usrp_sink(
            device_addr="serial=E4R11Y0B1", #panthro
            stream_args=uhd.stream_args(
                args="",
                cpu_format="fc32",
                channels=range(1),
                antenna="TX/RX"
            ),
        )
        self.uhd_sink.set_samp_rate(samp_rate)
        self.uhd_sink.set_center_freq(f_center, 0)
        self.uhd_sink.set_gain(gain, 0)
        self.uhd_sink.set_bandwidth(bandwidth, 0)

        self.msg_src = gr.message_source(1, msgq)

        self.msk = level.msk_mod_bc(
            samples_per_symbol=2,
            bt=0.3,
            ti_adj=False
        )
        
        self.connect(self.msg_src, self.msk, self.uhd_sink)

    def send_pkt(self, payload):
        msg = gr.message_from_string(str(payload))
        self.msgq.insert_tail(msg)

    def get_top_hn(self):
        try:
            f_page = urllib2.urlopen("http://api.ihackernews.com/page").read()
            fj = json.loads(f_page)
            title = fj['items'][0]['title'][:50]
            score = fj['items'][0]['points']
        except urllib2.HTTPError:
            print "HN returned server error: 0"
            title = "HN API DOWN"
            score = 0
        except:
            print "network error"
            title = "could not connect"
            score = 0
        return str(title) + " : " + str(score)

    def form_packet(self, payload):
        length = len(payload)
        crc = crc16_func(chr(length) + payload)
        
        #packet =  chr(0x00)                             # guard
        packet = chr(0xAA)*4                           # preamble
        packet += chr(0xD3) + chr(0x91)                 # sync
        packet += chr(length)                           # length
        packet += payload
        packet += chr(crc >> 8) + chr(crc & 0xFF)       # crc
        packet += chr(0xFF) + chr(0x00)                 # guard
        return packet

    def main_loop(self, max_pkts):
        payload = self.get_top_hn()
        while self.sent_pkts < max_pkts:
            if not self.sent_pkts % 100:
                payload = self.get_top_hn()
            packet = self.form_packet(payload)
            self.send_pkt(packet)
            self.sent_pkts += 1
            try:
                print payload, self.sent_pkts
                time.sleep(.1)
                pass
            except KeyboardInterrupt:
                print "\n\nSent Packets:", self.sent_pkts, "\n"
                break

class test_receive(gr.top_block):
    
    def __init__(self):
        gr.top_block.__init__(self, "CC1101 Burst Detector")

        def rx_callback():
            print "Callback Fired"

        # Variables
        self.samp_rate = samp_rate = 125e3
        self.f_center = f_center = 520e6
        self.bandwidth = bandwidth = 100e3
        self.gain = gain = 5

        # Blocks
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
        self.uhd_src.set_gain(gain, 0)
        self.uhd_src.set_antenna("RX2", 0)
        self.uhd_src.set_bandwidth(bandwidth, 0)

        self.uhd_src.set_samp_rate(self.samp_rate)
        self.uhd_src.set_center_freq(self.f_center, 0)
        self.uhd_src.set_gain(self.gain, 0)

        self.packet_receiver = level.cc1k_demod_pkts(callback=rx_callback())

        # Connections
        self.connect(self.uhd_src, self.packet_receiver)

if __name__ == '__main__':
    tx = test_transmit()
    #rx = test_receive()
    #rx.start()
    #r = gr.enable_realtime_scheduling()
    tx.start()
    tx.main_loop(float("inf"))
    #tx.Run(True)

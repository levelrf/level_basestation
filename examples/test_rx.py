#!/usr/bin/python
#!/usr/bin/env python

from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import uhd
from gnuradio import window
from gnuradio import digital
from gnuradio.eng_option import eng_option
from grc_gnuradio import wxgui as grc_wxgui
from gnuradio.wxgui import fftsink2
from gnuradio.gr import firdes
from optparse import OptionParser
from gnuradio import level
import wx

class fsk_rx(grc_wxgui.top_block_gui):
    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="CC1101 Burst Detector")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        def rx_callback():
            print "Callback Fired"

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 500e3
        self.f_center = f_center = 434e6
        self.bandwidth = bandwidth = 1e6
        self.gain = gain = 0

        ##################################################
        # Blocks
        ##################################################

        self.wxgui_fftsink2 = fftsink2.fft_sink_c(
            self.GetWin(),
            baseband_freq=0,
            y_per_div=10,
            y_divs=10,
            ref_level=0,
            ref_scale=2.0,
            sample_rate=samp_rate,
            fft_size=1024,
            fft_rate=15,
            average=False,
            avg_alpha=None,
            title="FFT Plot",
            peak_hold=False,
        )
        self.Add(self.wxgui_fftsink2.win)

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
        self.uhd_src.set_bandwidth(bandwidth, 0)

        self.uhd_src.set_samp_rate(self.samp_rate)
        self.uhd_src.set_center_freq(self.f_center, 0)
        self.uhd_src.set_gain(self.gain, 0)

        self.data_rate = 2.4e3
        self.samples_per_symbol = 8
        self.usrp_decim = int (64e6 / self.samples_per_symbol / self.data_rate)
        self.fs = self.data_rate * self.samples_per_symbol
        payload_size = 128             # bytes

        taps = firdes.low_pass_2(1, 1, 0.4, 0.1, 60)

        self.packet_receiver = level.cc1k_demod_pkts(callback=rx_callback(),
                                                    sps=self.samples_per_symbol,
                                                    symbol_rate=self.data_rate,
                                                    p_size=payload_size)

        #self.filesink = gr.file_sink(gr.sizeof_gr_complex, 'rx_test.dat')

        ##################################################
        # Connections
        ##################################################
        self.connect(self.uhd_src, self.wxgui_fftsink2)
        self.connect(self.uhd_src, self.packet_receiver)
        #self.connect(self.packet_receiver, self.filesink)

def main():
    rx = fsk_rx()
    r = gr.enable_realtime_scheduling()
    if r != gr.RT_OK:
        print "Warning: failed to enable realtime scheduling"
    rx.Run(True)

    rx.start()
    rx.wait()

if __name__ == '__main__':
    main()

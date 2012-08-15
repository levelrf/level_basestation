class ti_demod_pkts(gr.hier_block):
    """
    demodulator that is a GNU Radio sink.

    The input is complex baseband.  When packets are demodulated, they are passed to the
    app via the callback.
    """

    def __init__(self, fg, access_code=None, callback=None, threshold=-1, *args, **kwargs):
        """
	    Hierarchical block for binary FSK demodulation.

	    The input is the complex modulated signal at baseband.
        Demodulated packets are sent to the handler.
        """

        self._rcvd_pktq = gr.msg_queue()          # holds packets from the PHY
        self.ti_demod = cc1100.demod(fg, *args, **kwargs)
        self._packet_sink = ucla.sos_packet_sink(map(ord, access_code), self._rcvd_pktq, threshold)
        
        fg.connect(self.cc1k_demod, self._packet_sink)
        #filesink = gr.file_sink (gr.sizeof_char, "/tmp/rx.log")
        #fg.connect(self.cc1k_demod,filesink)
        
        self.digital_gmsk_demod = digital.gmsk_demod(
            samples_per_symbol=2,
            gain_mu=0.175,
            mu=0.5,
            omega_relative_limit=0.005,
            freq_error=0.0,
            verbose=False,
            log=False
        )

        gr.hier_block.__init__(self, fg, self.cc1k_demod, None)
        self._watcher = _queue_watcher_thread(self._rcvd_pktq, callback)

    def carrier_sensed(self):
        return self._packet_sink.carrier_sensed()


class _queue_watcher_thread(_threading.Thread):
    def __init__(self, rcvd_pktq, callback):
        _threading.Thread.__init__(self)
        self.setDaemon(1)
        self.rcvd_pktq = rcvd_pktq
        self.callback = callback
        self.keep_running = True
        self.start()
        
    def run(self):
        while self.keep_running:
            print "waiting for packet"
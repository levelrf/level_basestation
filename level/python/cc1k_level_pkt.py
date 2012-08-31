from math import pi

from gnuradio import gr
from level_swig import *
from fsk import fsk_demod
import gnuradio.gr.gr_threading as _threading
import struct

class cc1k_demod_pkts(gr.hier_block2):
    """
    cc1101 demodulator that is a GNU Radio sink.

    The input is complex baseband.  When packets are demodulated, they are passed to the
    app via the callback.
    """

    def __init__(self, preamble=None, callback=None):
        """
    	Hierarchical block for binary FSK demodulation.

    	The input is the complex modulated signal at baseband.
            Demodulated packets are sent to the handler.

            @param preamble: 32-bit preamble
            @type preamble: string
            @param callback:  function of two args: ok, payload
            @type callback: ok: bool; payload: string

            See cc1101_demod for remaining parameters.
    	"""

        gr.hier_block2.__init__(self, "demod_pkts",
            gr.io_signature(1, 1, gr.sizeof_gr_complex), # Input signature
            gr.io_signature(0, 0, 0))                    # Output signature

        if preamble is None:
            preamble = chr(0b10101010) + chr(0b10101010) + chr(0b10101010) + chr(0b10101010)
        self._preamble = preamble

        self._rcvd_pktq = gr.msg_queue()          # holds packets from the PHY
        self.demod = fsk_demod()
        self._packet_sink = packet_sink(map(ord, preamble), self._rcvd_pktq)
        
        self.connect(self, self.demod, self._packet_sink)
        #filesink = gr.file_sink(gr.sizeof_gr_complex, "/tmp/rx.log")
        #fg.connect(self.demod, filesink)
      
        self._watcher = _queue_watcher_thread(self._rcvd_pktq, callback)

    def carrier_sensed(self):
        """
        Return True if we detect carrier.
        """
        return self._packet_sink.carrier_sensed()


class _queue_watcher_thread(_threading.Thread):
    def __init__(self, rcvd_pktq, callback):
        _threading.Thread.__init__(self)
        self.setDaemon(1)
        self.rcvd_pktq = rcvd_pktq
        self.callback = callback
        self.keep_running = True
        self.start()

    def stop(self):
        self.keep_running = False
        
    def run(self):
        while self.keep_running:
            print "cc1k_level_pkt: waiting for packet"
            msg = self.rcvd_pktq.delete_head()
            payload = msg.to_string()
            
            print "received packet "
            print payload
            #am_group = ord(payload[0])
            #module_src = ord(payload[1])
            #module_dst = ord(payload[2])
            #dst_addr = ord(payload[4])*256 + ord(payload[3])
            #src_addr = ord(payload[6])*256 + ord(payload[5])
            #msg_type = ord(payload[7])
            #msg_len = ord(payload[8])
            #msg_payload = payload[9:9+msg_len]
            #crc = ord(payload[-2]) + ord(payload[-1])*256

            #crcClass = crc8.crc8()
            #crcCheck = crcClass.crc(payload[1:9+msg_len])

            #print " bare msg: " + str(map(hex, map(ord, payload)))
            #print " am group: " + str(am_group)
            #print "  src_addr: "+str(src_addr)+" dst_addr: "+str(dst_addr)
            #print "  src_module: " + str(module_src) + " dst_module: " + str(module_dst)
            #print "  msg type: " + str(msg_type) + " msg len: " +str(msg_len)
            #print "  msg: " + str(map(hex, map(ord, msg_payload)))
            #print "  crc: " + str(crc)
            #print "  crc_check: " + str(crcCheck)
            #print
            #ok = (crc == crcCheck)
            if self.callback:
                pass
                #self.callback(ok, am_group, src_addr, dst_addr, module_src, module_dst, msg_type, msg_payload, crc)

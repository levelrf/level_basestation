from gnuradio import gr
from math import pi

class cc1101_demod(gr.hier_block):
    def __init__(self, fg, sps = 8, symbol_rate = 38400, p_size = 13):
        """
        Hierarchical block for FSK demodulation.
    
        The input is the complex modulated signal at baseband
        and the output is a stream of bytes.
        
        @param fg: flow graph
        @type fg: flow graph
        @param sps: samples per symbol
        @type sps: integer
        @param symbol_rate: symbols per second
        @type symbol_rate: float
        @param p_size: packet size
        @type p_size: integer
        """
        
        # Demodulate FM
        sensitivity = (pi / 2) / sps
        self.fmdemod = gr.quadrature_demod_cf(1 / sensitivity)

        # Low pass the output of fmdemod to allow us to remove
        # the DC offset resulting from frequency offset

        alpha = 0.0512/sps
        self.freq_offset = gr.single_pole_iir_filter_ff(alpha)
        self.sub = gr.sub_ff()
        
        fg.connect(self.fmdemod, (self.sub, 0))
        fg.connect(self.fmdemod, self.freq_offset, (self.sub, 1))
        
        # recover the clock
        omega = sps
        gain_mu=0.03
        mu=0.5
        omega_relative_limit=0.0002
        freq_error=0.0
        
        gain_omega = .25*gain_mu*gain_mu        # critically damped
        self.clock_recovery = gr.clock_recovery_mm_ff(omega, gain_omega, mu, gain_mu,
                                                      omega_relative_limit)
        
        # Connect
        fg.connect(self.sub, self.clock_recovery)
        
        #filesink = gr.file_sink(gr.sizeof_float, 'rx_fsk_test.dat')
        #fg.connect(self.clock_recovery, filesink)
        
        # Initialize base class
        gr.hier_block.__init__(self, fg, self.fmdemod, self.clock_recovery)

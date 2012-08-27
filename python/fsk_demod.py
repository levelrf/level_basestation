from gnuradio import gr
from gnuradio import digital
from math import pi

class fsk_demod(gr.hier_block2):
    def __init__(self, sps = 8, symbol_rate = 38400, p_size = 13):
        """
        Hierarchical block for FSK demodulation.
    
        The input is the complex modulated signal at baseband
        and the output is a stream of bytes.
        """
        # Initialize base class
        gr.hier_block2.__init__(self, "fsk_demod",
                gr.io_signature(1, 1, gr.sizeof_gr_complex), # Input signature
                gr.io_signature(1, 1, gr.sizeof_float)) # Output signature
        
        # Demodulate FM
        sensitivity = (pi / 2) / sps
        self.fmdemod = gr.quadrature_demod_cf(1 / sensitivity)

        # Low pass the output of fmdemod to allow us to remove
        # the DC offset resulting from frequency offset

        alpha = 0.0512/sps
        self.freq_offset = gr.single_pole_iir_filter_ff(alpha)
        self.sub = gr.sub_ff()
        
        self.connect(self, self.fmdemod)
        self.connect(self.fmdemod, (self.sub, 0))
        self.connect(self.fmdemod, self.freq_offset, (self.sub, 1))
        
        # recover the clock
        omega = sps
        gain_mu=0.03
        mu=0.5
        omega_relative_limit=0.0002
        freq_error=0.0
        
        gain_omega = .25*gain_mu*gain_mu        # critically damped
        self.clock_recovery = digital.clock_recovery_mm_ff(omega, gain_omega, mu, gain_mu,
                                                      omega_relative_limit)
        
        # Connect
        self.connect(self.sub, self.clock_recovery, self)
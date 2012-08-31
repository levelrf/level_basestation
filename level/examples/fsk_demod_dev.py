#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: MPSK Demod Demo
# Generated: Thu Aug 30 16:03:43 2012
##################################################

from gnuradio import digital
from gnuradio import gr
from gnuradio import uhd
from gnuradio.gr import firdes
from math import pi

class simple_fsk_demod(gr.top_block):

	def __init__(self):
		gr.top_block.__init__(self, "FSK Demod Demo")

		##################################################
		# Variables
		##################################################
		self.samp_rate = samp_rate = 128e3
		self.f_center = f_center = 868e6
		self.sps = sps = 2
		self.sensitivity = sensitivity = (pi / 2) / sps
		self.alpha = alpha = 0.0512/sps

		##################################################
		# Blocks
		##################################################
		self.uhd_usrp_source_0 = uhd.usrp_source(
			device_addr="",
			stream_args=uhd.stream_args(
				cpu_format="fc32",
				channels=range(1),
			),
		)
		self.uhd_usrp_source_0.set_samp_rate(samp_rate)
		self.uhd_usrp_source_0.set_center_freq(f_center, 0)
		self.uhd_usrp_source_0.set_gain(0, 0)
		self.uhd_usrp_source_0.set_bandwidth(25e3, 0)

		self.fm_demod = gr.quadrature_demod_cf(1 / sensitivity)
		self.freq_offset = gr.single_pole_iir_filter_ff(alpha)
		self.sub = gr.sub_ff()
		self.invert = gr.multiply_const_vff(-1)

		# recover the clock
		omega = sps
		gain_mu = 0.03
		mu = 0.5
		omega_relative_limit = 0.0002
		freq_error = 0.0
		gain_omega = .25 * gain_mu * gain_mu        # critically damped
		self.clock_recovery = digital.clock_recovery_mm_ff(omega, gain_omega, mu, gain_mu, omega_relative_limit)

		self.slice = digital.binary_slicer_fb()
		self.sink = gr.vector_sink_b(1)

		##################################################
		# Connections
		##################################################
		self.connect(self.uhd_usrp_source_0, self.fm_demod, self.freq_offset, self.invert, self.clock_recovery, self.slice, self.sink)

if __name__ == '__main__':
	gr.enable_realtime_scheduling()
	tb = simple_fsk_demod()
	tb.start()
	raw_input('Press Enter to quit: ')
	tb.stop()
	sink_data = tb.sink.data()
	ones = len([x for x in sink_data if x is 1])
	print float(ones) / len(sink_data)
	#print sink_data[-1000:]


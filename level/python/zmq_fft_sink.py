from gnuradio import gr, fft


class zmq_fft_sink_c(gr.hier_block2):
	"""
	An fft block with real/complex inputs and a zmq publisher
	"""

	def __init__(
		self,
		baseband_freq=0,
		ref_scale=2.0,
		y_per_div=10,
		y_divs=8,
		ref_level=50,
		sample_rate=1,
		fft_size=512,
		fft_rate=fft_window.DEFAULT_FRAME_RATE,
		average=False,
		avg_alpha=None,
		title='',
		size=fft_window.DEFAULT_WIN_SIZE,
		peak_hold=False,
		win=None,
		use_persistence=False,
		persist_alpha=None,
		**kwargs
	):
		#ensure avg alpha
		if avg_alpha is None: avg_alpha = 2.0 / fft_rate
			#ensure analog alpha
			if persist_alpha is None:
				actual_fft_rate = float(sample_rate / fft_size) / float(max(1, int(float((sample_rate / fft_size) / fft_rate))))
				#print "requested_fft_rate ",fft_rate
				#print "actual_fft_rate    ",actual_fft_rate
				analog_cutoff_freq = 0.5 # Hertz
				#calculate alpha from wanted cutoff freq
				persist_alpha = 1.0 - math.exp(-2.0*math.pi*analog_cutoff_freq/actual_fft_rate)

		#init
		gr.hier_block2.__init__(
			self,
			"zmq_fft_sink",
			gr.io_signature(1, 1, self.sizeof_gr_complex),
			gr.io_signature(0, 0, 0),
		)
		#blocks
		fft = fft.logpwrfft_c(
			sample_rate=sample_rate,
			fft_size=fft_size,
			frame_rate=fft_rate,
			ref_scale=ref_scale,
			avg_alpha=avg_alpha,
			average=average,
			win=win,
		)
		msgq = gr.msg_queue(2)
		sink = gr.message_sink(gr.sizeof_float*fft_size, msgq, True)

		#controller
		self.controller = pubsub()
		self.controller.subscribe(AVERAGE_KEY, fft.set_average)
		self.controller.publish(AVERAGE_KEY, fft.average)
		self.controller.subscribe(AVG_ALPHA_KEY, fft.set_avg_alpha)
		self.controller.publish(AVG_ALPHA_KEY, fft.avg_alpha)
		self.controller.subscribe(SAMPLE_RATE_KEY, fft.set_sample_rate)
		self.controller.publish(SAMPLE_RATE_KEY, fft.sample_rate)
		#start input watcher
		common.input_watcher(msgq, self.controller, MSG_KEY)

		#connect
		self.connect(self, fft, sink)
		
	def set_callback(self, callb):
		self.win.set_callback(callb)

#!/bin/sh
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/rob/workspace/gnuradio/level_basestation/gr-fft/python
export PATH=/home/rob/workspace/gnuradio/level_basestation/build/gr-fft/python:$PATH
export LD_LIBRARY_PATH=/home/rob/workspace/gnuradio/level_basestation/build/gruel/src/lib:/home/rob/workspace/gnuradio/level_basestation/build/gnuradio-core/src/lib:/home/rob/workspace/gnuradio/level_basestation/build/gr-fft/lib:$LD_LIBRARY_PATH
export PYTHONPATH=/home/rob/workspace/gnuradio/level_basestation/build/gnuradio-core/src/python:/home/rob/workspace/gnuradio/level_basestation/build/gnuradio-core/src/lib/swig:/home/rob/workspace/gnuradio/level_basestation/build/gr-fft/python:/home/rob/workspace/gnuradio/level_basestation/build/gr-fft/swig:$PYTHONPATH
/usr/bin/python /home/rob/workspace/gnuradio/level_basestation/gr-fft/python/qa_fft.py 

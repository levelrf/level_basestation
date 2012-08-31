#!/bin/sh
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/rob/workspace/gnuradio/level_basestation/gr-digital/python
export PATH=/home/rob/workspace/gnuradio/level_basestation/build/gr-digital/python:$PATH
export LD_LIBRARY_PATH=/home/rob/workspace/gnuradio/level_basestation/build/volk/lib:/home/rob/workspace/gnuradio/level_basestation/build/gruel/src/lib:/home/rob/workspace/gnuradio/level_basestation/build/gnuradio-core/src/lib:/home/rob/workspace/gnuradio/level_basestation/build/gr-digital/lib:$LD_LIBRARY_PATH
export PYTHONPATH=/home/rob/workspace/gnuradio/level_basestation/build/gnuradio-core/src/python:/home/rob/workspace/gnuradio/level_basestation/build/gnuradio-core/src/lib/swig:/home/rob/workspace/gnuradio/level_basestation/build/gr-digital/python:/home/rob/workspace/gnuradio/level_basestation/build/gr-digital/swig:$PYTHONPATH
/usr/bin/python -B /home/rob/workspace/gnuradio/level_basestation/gr-digital/python/qa_mpsk_receiver.py 

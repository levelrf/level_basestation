#!/bin/sh
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/rob/workspace/gnuradio/level_basestation/gnuradio-core/src/python/gnuradio/gr
export PATH=/home/rob/workspace/gnuradio/level_basestation/build/gnuradio-core/src/python/gnuradio/gr:$PATH
export LD_LIBRARY_PATH=/home/rob/workspace/gnuradio/level_basestation/build/volk/lib:/home/rob/workspace/gnuradio/level_basestation/build/gruel/src/lib:/home/rob/workspace/gnuradio/level_basestation/build/gnuradio-core/src/lib:$LD_LIBRARY_PATH
export PYTHONPATH=/home/rob/workspace/gnuradio/level_basestation/build/gnuradio-core/src/python:/home/rob/workspace/gnuradio/level_basestation/build/gnuradio-core/src/lib/swig:$PYTHONPATH
/usr/bin/python -B /home/rob/workspace/gnuradio/level_basestation/gnuradio-core/src/python/gnuradio/gr/qa_noise.py 

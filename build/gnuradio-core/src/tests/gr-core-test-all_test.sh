#!/bin/sh
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/rob/workspace/gnuradio/level_basestation/gnuradio-core/src/tests
export PATH=/home/rob/workspace/gnuradio/level_basestation/build/gnuradio-core/src/tests:$PATH
export LD_LIBRARY_PATH=/home/rob/workspace/gnuradio/level_basestation/build/volk/lib:/home/rob/workspace/gnuradio/level_basestation/build/gruel/src/lib:/home/rob/workspace/gnuradio/level_basestation/build/gnuradio-core/src/lib:/home/rob/workspace/gnuradio/level_basestation/build/gnuradio-core/src/lib:/home/rob/workspace/gnuradio/level_basestation/build/gnuradio-core/src/tests:$LD_LIBRARY_PATH
export PYTHONPATH=$PYTHONPATH
gr_core_test_all 

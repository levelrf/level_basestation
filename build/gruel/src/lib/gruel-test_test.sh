#!/bin/sh
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/rob/workspace/gnuradio/level_basestation/gruel/src/lib
export PATH=/home/rob/workspace/gnuradio/level_basestation/build/gruel/src/lib:$PATH
export LD_LIBRARY_PATH=/home/rob/workspace/gnuradio/level_basestation/build/gruel/src/lib:/home/rob/workspace/gnuradio/level_basestation/build/gruel/src/lib:$LD_LIBRARY_PATH
export PYTHONPATH=$PYTHONPATH
test_gruel 

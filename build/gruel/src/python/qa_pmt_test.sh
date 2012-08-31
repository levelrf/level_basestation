#!/bin/sh
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/rob/workspace/gnuradio/level_basestation/gruel/src/python
export PATH=/home/rob/workspace/gnuradio/level_basestation/build/gruel/src/python:$PATH
export LD_LIBRARY_PATH=/home/rob/workspace/gnuradio/level_basestation/build/gruel/src/lib:$LD_LIBRARY_PATH
export PYTHONPATH=/home/rob/workspace/gnuradio/level_basestation/build/gruel/src/python:/home/rob/workspace/gnuradio/level_basestation/build/gruel/src/swig:$PYTHONPATH
/usr/bin/python -B /home/rob/workspace/gnuradio/level_basestation/gruel/src/python/qa_pmt.py 

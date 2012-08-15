/* -*- c++ -*- */

#define LEVEL_API

%include "gnuradio.i"			// the common stuff

//load generated python docstrings
%include "level_doc.i"

%{
#include "level_packet_sink.h"
%}

GR_SWIG_BLOCK_MAGIC(level,packet_sink);
%include "level_packet_sink.h"

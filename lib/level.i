include $(top_srcdir)/Makefile.common

# Install this stuff so that it ends up as the gnuradio.level module
# This usually ends up at:
#   ${prefix}/lib/python${python_version}/site-packages/gnuradio

ourpythondir = $(grpythondir)
ourlibdir    = $(grpyexecdir)

INCLUDES = $(STD_DEFINES_AND_INCLUDES) $(PYTHON_CPPFLAGS)

SWIGCPPPYTHONARGS = -fvirtual -python -modern $(PYTHON_CPPFLAGS) \
	-I$(swigincludedir) -I$(grincludedir)

ALL_IFILES = 				\
	$(LOCAL_IFILES)			\
	$(NON_LOCAL_IFILES)		

NON_LOCAL_IFILES =			\
	$(GNURADIO_CORE_INCLUDEDIR)/swig/gnuradio.i


LOCAL_IFILES = 				\
	level.i

# These files are built by SWIG.  The first is the C++ glue.
# The second is the python wrapper that loads the _ucla shared library
# and knows how to call our extensions.

BUILT_SOURCES = 			\
	level.cc			\
	level.py				

# This gets ucla.py installed in the right place
ourpython_PYTHON =			\
	level.py

ourlib_LTLIBRARIES = _level.la

# These are the source files that go into the shared library
_level_la_SOURCES = 			\
	level.cc			        \
	ti_packet_sink.cc

# magic flags
_level_la_LDFLAGS = $(NO_UNDEFINED) -module -avoid-version

# link the library against some comon swig runtime code and the 
# c++ standard library
_level_la_LIBADD = 			\
	$(PYTHON_LDFLAGS)		\
	-lstdc++			

level.cc level.py: level.i $(ALL_IFILES)
	$(SWIG) $(SWIGCPPPYTHONARGS) -module level -o level.cc $<

# These headers get installed in ${prefix}/include/gnuradio
grinclude_HEADERS =			\
	ti_packet_sink.h


# These swig headers get installed in ${prefix}/include/gnuradio/swig
swiginclude_HEADERS = 			\
	$(LOCAL_IFILES)


MOSTLYCLEANFILES = $(BUILT_SOURCES) *.pyc

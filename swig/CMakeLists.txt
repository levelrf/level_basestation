########################################################################
# Include swig generation macros
########################################################################
find_package(SWIG)
find_package(PythonLibs)
if(NOT SWIG_FOUND OR NOT PYTHONLIBS_FOUND)
    return()
endif()
include(GrSwig)
include(GrPython)

########################################################################
# Setup swig generation
########################################################################
foreach(incdir ${GNURADIO_CORE_INCLUDE_DIRS})
    list(APPEND GR_SWIG_INCLUDE_DIRS ${incdir}/swig)
endforeach(incdir)

foreach(incdir ${GRUEL_INCLUDE_DIRS})
    list(APPEND GR_SWIG_INCLUDE_DIRS ${incdir}/gruel/swig)
endforeach(incdir)

set(GR_SWIG_LIBRARIES gnuradio-level)
set(GR_SWIG_DOC_FILE ${CMAKE_CURRENT_BINARY_DIR}/level_doc.i)
set(GR_SWIG_DOC_DIRS ${CMAKE_CURRENT_SOURCE_DIR}/../include)

GR_SWIG_MAKE(level level.i)

########################################################################
# Install the build swig module
########################################################################
GR_SWIG_INSTALL(TARGETS level DESTINATION ${GR_PYTHON_DIR}/level)

########################################################################
# Install swig .i files for development
########################################################################
install(
    FILES
    level.i
    ${CMAKE_CURRENT_BINARY_DIR}/level_doc.i
    DESTINATION ${GR_INCLUDE_DIR}/level/swig
)
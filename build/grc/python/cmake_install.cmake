# Install script for directory: /home/rob/workspace/gnuradio/level_basestation/grc/python

# Set the install prefix
IF(NOT DEFINED CMAKE_INSTALL_PREFIX)
  SET(CMAKE_INSTALL_PREFIX "/usr/local")
ENDIF(NOT DEFINED CMAKE_INSTALL_PREFIX)
STRING(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
IF(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  IF(BUILD_TYPE)
    STRING(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  ELSE(BUILD_TYPE)
    SET(CMAKE_INSTALL_CONFIG_NAME "Release")
  ENDIF(BUILD_TYPE)
  MESSAGE(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
ENDIF(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)

# Set the component getting installed.
IF(NOT CMAKE_INSTALL_COMPONENT)
  IF(COMPONENT)
    MESSAGE(STATUS "Install component: \"${COMPONENT}\"")
    SET(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  ELSE(COMPONENT)
    SET(CMAKE_INSTALL_COMPONENT)
  ENDIF(COMPONENT)
ENDIF(NOT CMAKE_INSTALL_COMPONENT)

# Install shared libraries without execute permission?
IF(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  SET(CMAKE_INSTALL_SO_NO_EXE "1")
ENDIF(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "grc")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages/gnuradio/grc/python" TYPE FILE FILES
    "/home/rob/workspace/gnuradio/level_basestation/grc/python/convert_hier.py"
    "/home/rob/workspace/gnuradio/level_basestation/grc/python/expr_utils.py"
    "/home/rob/workspace/gnuradio/level_basestation/grc/python/extract_docs.py"
    "/home/rob/workspace/gnuradio/level_basestation/grc/python/Block.py"
    "/home/rob/workspace/gnuradio/level_basestation/grc/python/Connection.py"
    "/home/rob/workspace/gnuradio/level_basestation/grc/python/Constants.py"
    "/home/rob/workspace/gnuradio/level_basestation/grc/python/FlowGraph.py"
    "/home/rob/workspace/gnuradio/level_basestation/grc/python/Generator.py"
    "/home/rob/workspace/gnuradio/level_basestation/grc/python/Param.py"
    "/home/rob/workspace/gnuradio/level_basestation/grc/python/Platform.py"
    "/home/rob/workspace/gnuradio/level_basestation/grc/python/Port.py"
    "/home/rob/workspace/gnuradio/level_basestation/grc/python/__init__.py"
    )
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "grc")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "grc")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages/gnuradio/grc/python" TYPE FILE FILES
    "/home/rob/workspace/gnuradio/level_basestation/build/grc/python/convert_hier.pyc"
    "/home/rob/workspace/gnuradio/level_basestation/build/grc/python/expr_utils.pyc"
    "/home/rob/workspace/gnuradio/level_basestation/build/grc/python/extract_docs.pyc"
    "/home/rob/workspace/gnuradio/level_basestation/build/grc/python/Block.pyc"
    "/home/rob/workspace/gnuradio/level_basestation/build/grc/python/Connection.pyc"
    "/home/rob/workspace/gnuradio/level_basestation/build/grc/python/Constants.pyc"
    "/home/rob/workspace/gnuradio/level_basestation/build/grc/python/FlowGraph.pyc"
    "/home/rob/workspace/gnuradio/level_basestation/build/grc/python/Generator.pyc"
    "/home/rob/workspace/gnuradio/level_basestation/build/grc/python/Param.pyc"
    "/home/rob/workspace/gnuradio/level_basestation/build/grc/python/Platform.pyc"
    "/home/rob/workspace/gnuradio/level_basestation/build/grc/python/Port.pyc"
    "/home/rob/workspace/gnuradio/level_basestation/build/grc/python/__init__.pyc"
    "/home/rob/workspace/gnuradio/level_basestation/build/grc/python/convert_hier.pyo"
    "/home/rob/workspace/gnuradio/level_basestation/build/grc/python/expr_utils.pyo"
    "/home/rob/workspace/gnuradio/level_basestation/build/grc/python/extract_docs.pyo"
    "/home/rob/workspace/gnuradio/level_basestation/build/grc/python/Block.pyo"
    "/home/rob/workspace/gnuradio/level_basestation/build/grc/python/Connection.pyo"
    "/home/rob/workspace/gnuradio/level_basestation/build/grc/python/Constants.pyo"
    "/home/rob/workspace/gnuradio/level_basestation/build/grc/python/FlowGraph.pyo"
    "/home/rob/workspace/gnuradio/level_basestation/build/grc/python/Generator.pyo"
    "/home/rob/workspace/gnuradio/level_basestation/build/grc/python/Param.pyo"
    "/home/rob/workspace/gnuradio/level_basestation/build/grc/python/Platform.pyo"
    "/home/rob/workspace/gnuradio/level_basestation/build/grc/python/Port.pyo"
    "/home/rob/workspace/gnuradio/level_basestation/build/grc/python/__init__.pyo"
    )
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "grc")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "grc")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages/gnuradio/grc/python" TYPE FILE FILES
    "/home/rob/workspace/gnuradio/level_basestation/grc/python/block.dtd"
    "/home/rob/workspace/gnuradio/level_basestation/grc/python/default_flow_graph.grc"
    "/home/rob/workspace/gnuradio/level_basestation/grc/python/flow_graph.tmpl"
    )
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "grc")


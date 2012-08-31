# Install script for directory: /home/rob/workspace/gnuradio/level_basestation/grc/base

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
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages/gnuradio/grc/base" TYPE FILE FILES
    "/home/rob/workspace/gnuradio/level_basestation/grc/base/odict.py"
    "/home/rob/workspace/gnuradio/level_basestation/grc/base/ParseXML.py"
    "/home/rob/workspace/gnuradio/level_basestation/grc/base/Block.py"
    "/home/rob/workspace/gnuradio/level_basestation/grc/base/Connection.py"
    "/home/rob/workspace/gnuradio/level_basestation/grc/base/Constants.py"
    "/home/rob/workspace/gnuradio/level_basestation/grc/base/Element.py"
    "/home/rob/workspace/gnuradio/level_basestation/grc/base/FlowGraph.py"
    "/home/rob/workspace/gnuradio/level_basestation/grc/base/Param.py"
    "/home/rob/workspace/gnuradio/level_basestation/grc/base/Platform.py"
    "/home/rob/workspace/gnuradio/level_basestation/grc/base/Port.py"
    "/home/rob/workspace/gnuradio/level_basestation/grc/base/__init__.py"
    )
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "grc")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "grc")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages/gnuradio/grc/base" TYPE FILE FILES
    "/home/rob/workspace/gnuradio/level_basestation/build/grc/base/odict.pyc"
    "/home/rob/workspace/gnuradio/level_basestation/build/grc/base/ParseXML.pyc"
    "/home/rob/workspace/gnuradio/level_basestation/build/grc/base/Block.pyc"
    "/home/rob/workspace/gnuradio/level_basestation/build/grc/base/Connection.pyc"
    "/home/rob/workspace/gnuradio/level_basestation/build/grc/base/Constants.pyc"
    "/home/rob/workspace/gnuradio/level_basestation/build/grc/base/Element.pyc"
    "/home/rob/workspace/gnuradio/level_basestation/build/grc/base/FlowGraph.pyc"
    "/home/rob/workspace/gnuradio/level_basestation/build/grc/base/Param.pyc"
    "/home/rob/workspace/gnuradio/level_basestation/build/grc/base/Platform.pyc"
    "/home/rob/workspace/gnuradio/level_basestation/build/grc/base/Port.pyc"
    "/home/rob/workspace/gnuradio/level_basestation/build/grc/base/__init__.pyc"
    "/home/rob/workspace/gnuradio/level_basestation/build/grc/base/odict.pyo"
    "/home/rob/workspace/gnuradio/level_basestation/build/grc/base/ParseXML.pyo"
    "/home/rob/workspace/gnuradio/level_basestation/build/grc/base/Block.pyo"
    "/home/rob/workspace/gnuradio/level_basestation/build/grc/base/Connection.pyo"
    "/home/rob/workspace/gnuradio/level_basestation/build/grc/base/Constants.pyo"
    "/home/rob/workspace/gnuradio/level_basestation/build/grc/base/Element.pyo"
    "/home/rob/workspace/gnuradio/level_basestation/build/grc/base/FlowGraph.pyo"
    "/home/rob/workspace/gnuradio/level_basestation/build/grc/base/Param.pyo"
    "/home/rob/workspace/gnuradio/level_basestation/build/grc/base/Platform.pyo"
    "/home/rob/workspace/gnuradio/level_basestation/build/grc/base/Port.pyo"
    "/home/rob/workspace/gnuradio/level_basestation/build/grc/base/__init__.pyo"
    )
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "grc")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "grc")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages/gnuradio/grc/base" TYPE FILE FILES
    "/home/rob/workspace/gnuradio/level_basestation/grc/base/block_tree.dtd"
    "/home/rob/workspace/gnuradio/level_basestation/grc/base/flow_graph.dtd"
    )
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "grc")


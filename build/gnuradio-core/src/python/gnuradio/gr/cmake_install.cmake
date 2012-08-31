# Install script for directory: /home/rob/workspace/gnuradio/level_basestation/gnuradio-core/src/python/gnuradio/gr

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

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "core_python")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages/gnuradio/gr" TYPE FILE FILES
    "/home/rob/workspace/gnuradio/level_basestation/gnuradio-core/src/python/gnuradio/gr/__init__.py"
    "/home/rob/workspace/gnuradio/level_basestation/gnuradio-core/src/python/gnuradio/gr/exceptions.py"
    "/home/rob/workspace/gnuradio/level_basestation/gnuradio-core/src/python/gnuradio/gr/gr_threading.py"
    "/home/rob/workspace/gnuradio/level_basestation/gnuradio-core/src/python/gnuradio/gr/gr_threading_23.py"
    "/home/rob/workspace/gnuradio/level_basestation/gnuradio-core/src/python/gnuradio/gr/gr_threading_24.py"
    "/home/rob/workspace/gnuradio/level_basestation/gnuradio-core/src/python/gnuradio/gr/hier_block2.py"
    "/home/rob/workspace/gnuradio/level_basestation/gnuradio-core/src/python/gnuradio/gr/prefs.py"
    "/home/rob/workspace/gnuradio/level_basestation/gnuradio-core/src/python/gnuradio/gr/top_block.py"
    "/home/rob/workspace/gnuradio/level_basestation/gnuradio-core/src/python/gnuradio/gr/pubsub.py"
    )
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "core_python")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "core_python")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages/gnuradio/gr" TYPE FILE FILES
    "/home/rob/workspace/gnuradio/level_basestation/build/gnuradio-core/src/python/gnuradio/gr/__init__.pyc"
    "/home/rob/workspace/gnuradio/level_basestation/build/gnuradio-core/src/python/gnuradio/gr/exceptions.pyc"
    "/home/rob/workspace/gnuradio/level_basestation/build/gnuradio-core/src/python/gnuradio/gr/gr_threading.pyc"
    "/home/rob/workspace/gnuradio/level_basestation/build/gnuradio-core/src/python/gnuradio/gr/gr_threading_23.pyc"
    "/home/rob/workspace/gnuradio/level_basestation/build/gnuradio-core/src/python/gnuradio/gr/gr_threading_24.pyc"
    "/home/rob/workspace/gnuradio/level_basestation/build/gnuradio-core/src/python/gnuradio/gr/hier_block2.pyc"
    "/home/rob/workspace/gnuradio/level_basestation/build/gnuradio-core/src/python/gnuradio/gr/prefs.pyc"
    "/home/rob/workspace/gnuradio/level_basestation/build/gnuradio-core/src/python/gnuradio/gr/top_block.pyc"
    "/home/rob/workspace/gnuradio/level_basestation/build/gnuradio-core/src/python/gnuradio/gr/pubsub.pyc"
    "/home/rob/workspace/gnuradio/level_basestation/build/gnuradio-core/src/python/gnuradio/gr/__init__.pyo"
    "/home/rob/workspace/gnuradio/level_basestation/build/gnuradio-core/src/python/gnuradio/gr/exceptions.pyo"
    "/home/rob/workspace/gnuradio/level_basestation/build/gnuradio-core/src/python/gnuradio/gr/gr_threading.pyo"
    "/home/rob/workspace/gnuradio/level_basestation/build/gnuradio-core/src/python/gnuradio/gr/gr_threading_23.pyo"
    "/home/rob/workspace/gnuradio/level_basestation/build/gnuradio-core/src/python/gnuradio/gr/gr_threading_24.pyo"
    "/home/rob/workspace/gnuradio/level_basestation/build/gnuradio-core/src/python/gnuradio/gr/hier_block2.pyo"
    "/home/rob/workspace/gnuradio/level_basestation/build/gnuradio-core/src/python/gnuradio/gr/prefs.pyo"
    "/home/rob/workspace/gnuradio/level_basestation/build/gnuradio-core/src/python/gnuradio/gr/top_block.pyo"
    "/home/rob/workspace/gnuradio/level_basestation/build/gnuradio-core/src/python/gnuradio/gr/pubsub.pyo"
    )
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "core_python")


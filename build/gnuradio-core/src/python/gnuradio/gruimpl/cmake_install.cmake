# Install script for directory: /home/rob/workspace/gnuradio/level_basestation/gnuradio-core/src/python/gnuradio/gruimpl

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
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages/gnuradio/gruimpl" TYPE FILE FILES
    "/home/rob/workspace/gnuradio/level_basestation/gnuradio-core/src/python/gnuradio/gruimpl/__init__.py"
    "/home/rob/workspace/gnuradio/level_basestation/gnuradio-core/src/python/gnuradio/gruimpl/freqz.py"
    "/home/rob/workspace/gnuradio/level_basestation/gnuradio-core/src/python/gnuradio/gruimpl/gnuplot_freqz.py"
    "/home/rob/workspace/gnuradio/level_basestation/gnuradio-core/src/python/gnuradio/gruimpl/hexint.py"
    "/home/rob/workspace/gnuradio/level_basestation/gnuradio-core/src/python/gnuradio/gruimpl/listmisc.py"
    "/home/rob/workspace/gnuradio/level_basestation/gnuradio-core/src/python/gnuradio/gruimpl/mathmisc.py"
    "/home/rob/workspace/gnuradio/level_basestation/gnuradio-core/src/python/gnuradio/gruimpl/lmx2306.py"
    "/home/rob/workspace/gnuradio/level_basestation/gnuradio-core/src/python/gnuradio/gruimpl/msgq_runner.py"
    "/home/rob/workspace/gnuradio/level_basestation/gnuradio-core/src/python/gnuradio/gruimpl/os_read_exactly.py"
    "/home/rob/workspace/gnuradio/level_basestation/gnuradio-core/src/python/gnuradio/gruimpl/sdr_1000.py"
    "/home/rob/workspace/gnuradio/level_basestation/gnuradio-core/src/python/gnuradio/gruimpl/seq_with_cursor.py"
    "/home/rob/workspace/gnuradio/level_basestation/gnuradio-core/src/python/gnuradio/gruimpl/socket_stuff.py"
    "/home/rob/workspace/gnuradio/level_basestation/gnuradio-core/src/python/gnuradio/gruimpl/daemon.py"
    )
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "core_python")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "core_python")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages/gnuradio/gruimpl" TYPE FILE FILES
    "/home/rob/workspace/gnuradio/level_basestation/build/gnuradio-core/src/python/gnuradio/gruimpl/__init__.pyc"
    "/home/rob/workspace/gnuradio/level_basestation/build/gnuradio-core/src/python/gnuradio/gruimpl/freqz.pyc"
    "/home/rob/workspace/gnuradio/level_basestation/build/gnuradio-core/src/python/gnuradio/gruimpl/gnuplot_freqz.pyc"
    "/home/rob/workspace/gnuradio/level_basestation/build/gnuradio-core/src/python/gnuradio/gruimpl/hexint.pyc"
    "/home/rob/workspace/gnuradio/level_basestation/build/gnuradio-core/src/python/gnuradio/gruimpl/listmisc.pyc"
    "/home/rob/workspace/gnuradio/level_basestation/build/gnuradio-core/src/python/gnuradio/gruimpl/mathmisc.pyc"
    "/home/rob/workspace/gnuradio/level_basestation/build/gnuradio-core/src/python/gnuradio/gruimpl/lmx2306.pyc"
    "/home/rob/workspace/gnuradio/level_basestation/build/gnuradio-core/src/python/gnuradio/gruimpl/msgq_runner.pyc"
    "/home/rob/workspace/gnuradio/level_basestation/build/gnuradio-core/src/python/gnuradio/gruimpl/os_read_exactly.pyc"
    "/home/rob/workspace/gnuradio/level_basestation/build/gnuradio-core/src/python/gnuradio/gruimpl/sdr_1000.pyc"
    "/home/rob/workspace/gnuradio/level_basestation/build/gnuradio-core/src/python/gnuradio/gruimpl/seq_with_cursor.pyc"
    "/home/rob/workspace/gnuradio/level_basestation/build/gnuradio-core/src/python/gnuradio/gruimpl/socket_stuff.pyc"
    "/home/rob/workspace/gnuradio/level_basestation/build/gnuradio-core/src/python/gnuradio/gruimpl/daemon.pyc"
    "/home/rob/workspace/gnuradio/level_basestation/build/gnuradio-core/src/python/gnuradio/gruimpl/__init__.pyo"
    "/home/rob/workspace/gnuradio/level_basestation/build/gnuradio-core/src/python/gnuradio/gruimpl/freqz.pyo"
    "/home/rob/workspace/gnuradio/level_basestation/build/gnuradio-core/src/python/gnuradio/gruimpl/gnuplot_freqz.pyo"
    "/home/rob/workspace/gnuradio/level_basestation/build/gnuradio-core/src/python/gnuradio/gruimpl/hexint.pyo"
    "/home/rob/workspace/gnuradio/level_basestation/build/gnuradio-core/src/python/gnuradio/gruimpl/listmisc.pyo"
    "/home/rob/workspace/gnuradio/level_basestation/build/gnuradio-core/src/python/gnuradio/gruimpl/mathmisc.pyo"
    "/home/rob/workspace/gnuradio/level_basestation/build/gnuradio-core/src/python/gnuradio/gruimpl/lmx2306.pyo"
    "/home/rob/workspace/gnuradio/level_basestation/build/gnuradio-core/src/python/gnuradio/gruimpl/msgq_runner.pyo"
    "/home/rob/workspace/gnuradio/level_basestation/build/gnuradio-core/src/python/gnuradio/gruimpl/os_read_exactly.pyo"
    "/home/rob/workspace/gnuradio/level_basestation/build/gnuradio-core/src/python/gnuradio/gruimpl/sdr_1000.pyo"
    "/home/rob/workspace/gnuradio/level_basestation/build/gnuradio-core/src/python/gnuradio/gruimpl/seq_with_cursor.pyo"
    "/home/rob/workspace/gnuradio/level_basestation/build/gnuradio-core/src/python/gnuradio/gruimpl/socket_stuff.pyo"
    "/home/rob/workspace/gnuradio/level_basestation/build/gnuradio-core/src/python/gnuradio/gruimpl/daemon.pyo"
    )
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "core_python")


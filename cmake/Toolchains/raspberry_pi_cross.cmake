########################################################################
# Toolchain file for building native on a ARM Cortex A8 w/ NEON
# Usage: cmake -DCMAKE_TOOLCHAIN_FILE=<this file> <source directory>
########################################################################
set(CMAKE_SYSTEM_NAME Linux)
set(CMAKE_CXX_COMPILER arm-linux-gnueabi-g++-4.6)
set(CMAKE_C_COMPILER arm-linux-gnueabi-gcc-4.6)
set(CMAKE_CXX_FLAGS "-O2 -mcpu=arm1176jzf-s -mfloat-abi=softfp -mfpu=neon")
set(CMAKE_C_FLAGS ${CMAKE_CXX_FLAGS})

set( PYTHON_EXECUTABLE /usr/bin/python )

set( CMAKE_FIND_ROOT_PATH /home/rob/workspace/rpi/libs/ )

set( CMAKE_FIND_ROOT_PATH_MODE_PROGRAM ONLY )
set( CMAKE_FIND_ROOT_PATH_MODE_LIBRARY ONLY )
set( CMAKE_FIND_ROOT_PATH_MODE_INCLUDE ONLY )

set( CMAKE_INSTALL_PREFIX /home/rob/workspace/rpi/gnuradio )
# Install script for directory: /home/rob/workspace/gnuradio/level_basestation/grc/gui

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
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages/gnuradio/grc/gui" TYPE FILE FILES
    "/home/rob/workspace/gnuradio/level_basestation/grc/gui/Block.py"
    "/home/rob/workspace/gnuradio/level_basestation/grc/gui/Colors.py"
    "/home/rob/workspace/gnuradio/level_basestation/grc/gui/Constants.py"
    "/home/rob/workspace/gnuradio/level_basestation/grc/gui/Connection.py"
    "/home/rob/workspace/gnuradio/level_basestation/grc/gui/Element.py"
    "/home/rob/workspace/gnuradio/level_basestation/grc/gui/FlowGraph.py"
    "/home/rob/workspace/gnuradio/level_basestation/grc/gui/Param.py"
    "/home/rob/workspace/gnuradio/level_basestation/grc/gui/Platform.py"
    "/home/rob/workspace/gnuradio/level_basestation/grc/gui/Port.py"
    "/home/rob/workspace/gnuradio/level_basestation/grc/gui/Utils.py"
    "/home/rob/workspace/gnuradio/level_basestation/grc/gui/ActionHandler.py"
    "/home/rob/workspace/gnuradio/level_basestation/grc/gui/Actions.py"
    "/home/rob/workspace/gnuradio/level_basestation/grc/gui/Bars.py"
    "/home/rob/workspace/gnuradio/level_basestation/grc/gui/BlockTreeWindow.py"
    "/home/rob/workspace/gnuradio/level_basestation/grc/gui/Dialogs.py"
    "/home/rob/workspace/gnuradio/level_basestation/grc/gui/DrawingArea.py"
    "/home/rob/workspace/gnuradio/level_basestation/grc/gui/FileDialogs.py"
    "/home/rob/workspace/gnuradio/level_basestation/grc/gui/MainWindow.py"
    "/home/rob/workspace/gnuradio/level_basestation/grc/gui/Messages.py"
    "/home/rob/workspace/gnuradio/level_basestation/grc/gui/NotebookPage.py"
    "/home/rob/workspace/gnuradio/level_basestation/grc/gui/PropsDialog.py"
    "/home/rob/workspace/gnuradio/level_basestation/grc/gui/Preferences.py"
    "/home/rob/workspace/gnuradio/level_basestation/grc/gui/StateCache.py"
    "/home/rob/workspace/gnuradio/level_basestation/grc/gui/__init__.py"
    )
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "grc")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "grc")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages/gnuradio/grc/gui" TYPE FILE FILES
    "/home/rob/workspace/gnuradio/level_basestation/build/grc/gui/Block.pyc"
    "/home/rob/workspace/gnuradio/level_basestation/build/grc/gui/Colors.pyc"
    "/home/rob/workspace/gnuradio/level_basestation/build/grc/gui/Constants.pyc"
    "/home/rob/workspace/gnuradio/level_basestation/build/grc/gui/Connection.pyc"
    "/home/rob/workspace/gnuradio/level_basestation/build/grc/gui/Element.pyc"
    "/home/rob/workspace/gnuradio/level_basestation/build/grc/gui/FlowGraph.pyc"
    "/home/rob/workspace/gnuradio/level_basestation/build/grc/gui/Param.pyc"
    "/home/rob/workspace/gnuradio/level_basestation/build/grc/gui/Platform.pyc"
    "/home/rob/workspace/gnuradio/level_basestation/build/grc/gui/Port.pyc"
    "/home/rob/workspace/gnuradio/level_basestation/build/grc/gui/Utils.pyc"
    "/home/rob/workspace/gnuradio/level_basestation/build/grc/gui/ActionHandler.pyc"
    "/home/rob/workspace/gnuradio/level_basestation/build/grc/gui/Actions.pyc"
    "/home/rob/workspace/gnuradio/level_basestation/build/grc/gui/Bars.pyc"
    "/home/rob/workspace/gnuradio/level_basestation/build/grc/gui/BlockTreeWindow.pyc"
    "/home/rob/workspace/gnuradio/level_basestation/build/grc/gui/Dialogs.pyc"
    "/home/rob/workspace/gnuradio/level_basestation/build/grc/gui/DrawingArea.pyc"
    "/home/rob/workspace/gnuradio/level_basestation/build/grc/gui/FileDialogs.pyc"
    "/home/rob/workspace/gnuradio/level_basestation/build/grc/gui/MainWindow.pyc"
    "/home/rob/workspace/gnuradio/level_basestation/build/grc/gui/Messages.pyc"
    "/home/rob/workspace/gnuradio/level_basestation/build/grc/gui/NotebookPage.pyc"
    "/home/rob/workspace/gnuradio/level_basestation/build/grc/gui/PropsDialog.pyc"
    "/home/rob/workspace/gnuradio/level_basestation/build/grc/gui/Preferences.pyc"
    "/home/rob/workspace/gnuradio/level_basestation/build/grc/gui/StateCache.pyc"
    "/home/rob/workspace/gnuradio/level_basestation/build/grc/gui/__init__.pyc"
    "/home/rob/workspace/gnuradio/level_basestation/build/grc/gui/Block.pyo"
    "/home/rob/workspace/gnuradio/level_basestation/build/grc/gui/Colors.pyo"
    "/home/rob/workspace/gnuradio/level_basestation/build/grc/gui/Constants.pyo"
    "/home/rob/workspace/gnuradio/level_basestation/build/grc/gui/Connection.pyo"
    "/home/rob/workspace/gnuradio/level_basestation/build/grc/gui/Element.pyo"
    "/home/rob/workspace/gnuradio/level_basestation/build/grc/gui/FlowGraph.pyo"
    "/home/rob/workspace/gnuradio/level_basestation/build/grc/gui/Param.pyo"
    "/home/rob/workspace/gnuradio/level_basestation/build/grc/gui/Platform.pyo"
    "/home/rob/workspace/gnuradio/level_basestation/build/grc/gui/Port.pyo"
    "/home/rob/workspace/gnuradio/level_basestation/build/grc/gui/Utils.pyo"
    "/home/rob/workspace/gnuradio/level_basestation/build/grc/gui/ActionHandler.pyo"
    "/home/rob/workspace/gnuradio/level_basestation/build/grc/gui/Actions.pyo"
    "/home/rob/workspace/gnuradio/level_basestation/build/grc/gui/Bars.pyo"
    "/home/rob/workspace/gnuradio/level_basestation/build/grc/gui/BlockTreeWindow.pyo"
    "/home/rob/workspace/gnuradio/level_basestation/build/grc/gui/Dialogs.pyo"
    "/home/rob/workspace/gnuradio/level_basestation/build/grc/gui/DrawingArea.pyo"
    "/home/rob/workspace/gnuradio/level_basestation/build/grc/gui/FileDialogs.pyo"
    "/home/rob/workspace/gnuradio/level_basestation/build/grc/gui/MainWindow.pyo"
    "/home/rob/workspace/gnuradio/level_basestation/build/grc/gui/Messages.pyo"
    "/home/rob/workspace/gnuradio/level_basestation/build/grc/gui/NotebookPage.pyo"
    "/home/rob/workspace/gnuradio/level_basestation/build/grc/gui/PropsDialog.pyo"
    "/home/rob/workspace/gnuradio/level_basestation/build/grc/gui/Preferences.pyo"
    "/home/rob/workspace/gnuradio/level_basestation/build/grc/gui/StateCache.pyo"
    "/home/rob/workspace/gnuradio/level_basestation/build/grc/gui/__init__.pyo"
    )
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "grc")


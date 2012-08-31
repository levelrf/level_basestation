# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 2.8

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list

# Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/rob/workspace/gnuradio/level_basestation

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/rob/workspace/gnuradio/level_basestation/build

# Include any dependencies generated for this target.
include volk/lib/CMakeFiles/test_all.dir/depend.make

# Include the progress variables for this target.
include volk/lib/CMakeFiles/test_all.dir/progress.make

# Include the compile flags for this target's objects.
include volk/lib/CMakeFiles/test_all.dir/flags.make

volk/lib/CMakeFiles/test_all.dir/testqa.cc.o: volk/lib/CMakeFiles/test_all.dir/flags.make
volk/lib/CMakeFiles/test_all.dir/testqa.cc.o: ../volk/lib/testqa.cc
	$(CMAKE_COMMAND) -E cmake_progress_report /home/rob/workspace/gnuradio/level_basestation/build/CMakeFiles $(CMAKE_PROGRESS_1)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Building CXX object volk/lib/CMakeFiles/test_all.dir/testqa.cc.o"
	cd /home/rob/workspace/gnuradio/level_basestation/build/volk/lib && /usr/bin/c++   $(CXX_DEFINES) -DBOOST_TEST_DYN_LINK -DBOOST_TEST_MAIN $(CXX_FLAGS) -o CMakeFiles/test_all.dir/testqa.cc.o -c /home/rob/workspace/gnuradio/level_basestation/volk/lib/testqa.cc

volk/lib/CMakeFiles/test_all.dir/testqa.cc.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/test_all.dir/testqa.cc.i"
	cd /home/rob/workspace/gnuradio/level_basestation/build/volk/lib && /usr/bin/c++  $(CXX_DEFINES) -DBOOST_TEST_DYN_LINK -DBOOST_TEST_MAIN $(CXX_FLAGS) -E /home/rob/workspace/gnuradio/level_basestation/volk/lib/testqa.cc > CMakeFiles/test_all.dir/testqa.cc.i

volk/lib/CMakeFiles/test_all.dir/testqa.cc.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/test_all.dir/testqa.cc.s"
	cd /home/rob/workspace/gnuradio/level_basestation/build/volk/lib && /usr/bin/c++  $(CXX_DEFINES) -DBOOST_TEST_DYN_LINK -DBOOST_TEST_MAIN $(CXX_FLAGS) -S /home/rob/workspace/gnuradio/level_basestation/volk/lib/testqa.cc -o CMakeFiles/test_all.dir/testqa.cc.s

volk/lib/CMakeFiles/test_all.dir/testqa.cc.o.requires:
.PHONY : volk/lib/CMakeFiles/test_all.dir/testqa.cc.o.requires

volk/lib/CMakeFiles/test_all.dir/testqa.cc.o.provides: volk/lib/CMakeFiles/test_all.dir/testqa.cc.o.requires
	$(MAKE) -f volk/lib/CMakeFiles/test_all.dir/build.make volk/lib/CMakeFiles/test_all.dir/testqa.cc.o.provides.build
.PHONY : volk/lib/CMakeFiles/test_all.dir/testqa.cc.o.provides

volk/lib/CMakeFiles/test_all.dir/testqa.cc.o.provides.build: volk/lib/CMakeFiles/test_all.dir/testqa.cc.o

volk/lib/CMakeFiles/test_all.dir/qa_utils.cc.o: volk/lib/CMakeFiles/test_all.dir/flags.make
volk/lib/CMakeFiles/test_all.dir/qa_utils.cc.o: ../volk/lib/qa_utils.cc
	$(CMAKE_COMMAND) -E cmake_progress_report /home/rob/workspace/gnuradio/level_basestation/build/CMakeFiles $(CMAKE_PROGRESS_2)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Building CXX object volk/lib/CMakeFiles/test_all.dir/qa_utils.cc.o"
	cd /home/rob/workspace/gnuradio/level_basestation/build/volk/lib && /usr/bin/c++   $(CXX_DEFINES) $(CXX_FLAGS) -o CMakeFiles/test_all.dir/qa_utils.cc.o -c /home/rob/workspace/gnuradio/level_basestation/volk/lib/qa_utils.cc

volk/lib/CMakeFiles/test_all.dir/qa_utils.cc.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/test_all.dir/qa_utils.cc.i"
	cd /home/rob/workspace/gnuradio/level_basestation/build/volk/lib && /usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -E /home/rob/workspace/gnuradio/level_basestation/volk/lib/qa_utils.cc > CMakeFiles/test_all.dir/qa_utils.cc.i

volk/lib/CMakeFiles/test_all.dir/qa_utils.cc.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/test_all.dir/qa_utils.cc.s"
	cd /home/rob/workspace/gnuradio/level_basestation/build/volk/lib && /usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -S /home/rob/workspace/gnuradio/level_basestation/volk/lib/qa_utils.cc -o CMakeFiles/test_all.dir/qa_utils.cc.s

volk/lib/CMakeFiles/test_all.dir/qa_utils.cc.o.requires:
.PHONY : volk/lib/CMakeFiles/test_all.dir/qa_utils.cc.o.requires

volk/lib/CMakeFiles/test_all.dir/qa_utils.cc.o.provides: volk/lib/CMakeFiles/test_all.dir/qa_utils.cc.o.requires
	$(MAKE) -f volk/lib/CMakeFiles/test_all.dir/build.make volk/lib/CMakeFiles/test_all.dir/qa_utils.cc.o.provides.build
.PHONY : volk/lib/CMakeFiles/test_all.dir/qa_utils.cc.o.provides

volk/lib/CMakeFiles/test_all.dir/qa_utils.cc.o.provides.build: volk/lib/CMakeFiles/test_all.dir/qa_utils.cc.o

# Object files for target test_all
test_all_OBJECTS = \
"CMakeFiles/test_all.dir/testqa.cc.o" \
"CMakeFiles/test_all.dir/qa_utils.cc.o"

# External object files for target test_all
test_all_EXTERNAL_OBJECTS =

volk/lib/test_all: volk/lib/CMakeFiles/test_all.dir/testqa.cc.o
volk/lib/test_all: volk/lib/CMakeFiles/test_all.dir/qa_utils.cc.o
volk/lib/test_all: volk/lib/libvolk.so.0.0.0
volk/lib/test_all: /usr/lib/libboost_unit_test_framework-mt.so
volk/lib/test_all: volk/lib/CMakeFiles/test_all.dir/build.make
volk/lib/test_all: volk/lib/CMakeFiles/test_all.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --red --bold "Linking CXX executable test_all"
	cd /home/rob/workspace/gnuradio/level_basestation/build/volk/lib && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/test_all.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
volk/lib/CMakeFiles/test_all.dir/build: volk/lib/test_all
.PHONY : volk/lib/CMakeFiles/test_all.dir/build

volk/lib/CMakeFiles/test_all.dir/requires: volk/lib/CMakeFiles/test_all.dir/testqa.cc.o.requires
volk/lib/CMakeFiles/test_all.dir/requires: volk/lib/CMakeFiles/test_all.dir/qa_utils.cc.o.requires
.PHONY : volk/lib/CMakeFiles/test_all.dir/requires

volk/lib/CMakeFiles/test_all.dir/clean:
	cd /home/rob/workspace/gnuradio/level_basestation/build/volk/lib && $(CMAKE_COMMAND) -P CMakeFiles/test_all.dir/cmake_clean.cmake
.PHONY : volk/lib/CMakeFiles/test_all.dir/clean

volk/lib/CMakeFiles/test_all.dir/depend:
	cd /home/rob/workspace/gnuradio/level_basestation/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/rob/workspace/gnuradio/level_basestation /home/rob/workspace/gnuradio/level_basestation/volk/lib /home/rob/workspace/gnuradio/level_basestation/build /home/rob/workspace/gnuradio/level_basestation/build/volk/lib /home/rob/workspace/gnuradio/level_basestation/build/volk/lib/CMakeFiles/test_all.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : volk/lib/CMakeFiles/test_all.dir/depend


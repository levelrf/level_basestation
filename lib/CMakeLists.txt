########################################################################
# Setup library
########################################################################
include(GrPlatform) #define LIB_SUFFIX

add_library(gnuradio-level SHARED level_packet_sink.cc)
target_link_libraries(gnuradio-level ${Boost_LIBRARIES} ${GRUEL_LIBRARIES} ${GNURADIO_CORE_LIBRARIES})
set_target_properties(gnuradio-level PROPERTIES DEFINE_SYMBOL "gnuradio_level_EXPORTS")

########################################################################
# Install built library files
########################################################################
install(TARGETS gnuradio-level
    LIBRARY DESTINATION lib${LIB_SUFFIX} # .so/.dylib file
    ARCHIVE DESTINATION lib${LIB_SUFFIX} # .lib file
    RUNTIME DESTINATION bin              # .dll file
)
#ifdef HAVE_CONFIG_H
#include "config.h"
#endif

#include <level_packet_sink.h>
#include <gr_io_signature.h>
#include <cstdio>
#include <errno.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <stdexcept>
#include <cstring>
#include <gr_count_bits.h>

#define VERBOSE 0

static const int DEFAULT_THRESHOLD = 0;  // detect access code with up to DEFAULT_THRESHOLD bits wrong

inline void
level_packet_sink::enter_search()
{
  if (VERBOSE)
    fprintf(stderr, "@ enter_search\n");

  d_state = STATE_SYNC_SEARCH;
  d_shift_reg = 0;
}
    
inline void
level_packet_sink::enter_have_sync()
{
  if (VERBOSE)
    fprintf(stderr, "@ enter_have_sync\n");

  d_state = STATE_HAVE_SYNC;
  d_packetlen_cnt = 0;
  d_packet_byte = 0;
  d_packet_byte_index = 0;
}

level_packet_sink_sptr
level_make_packet_sink (const std::vector<unsigned char>& sync_vector,
                        gr_msg_queue_sptr target_queue)
{
  return level_packet_sink_sptr (new level_packet_sink (sync_vector, target_queue));
}

level_packet_sink::level_packet_sink (const std::vector<unsigned char>& sync_vector,
					gr_msg_queue_sptr target_queue)
  	: gr_sync_block ("level_packet_sink",
		   gr_make_io_signature (1, 1, sizeof(float)),
		   gr_make_io_signature (0, 0, 0)),
    d_target_queue(target_queue)
{
  d_sync_vector = 0;
  for(int i=0;i<8;i++){
    d_sync_vector <<= 8;
    d_sync_vector |= sync_vector[i];
  }
  if ( VERBOSE )
    fprintf(stderr, "syncvec: %llx\n", d_sync_vector), fflush(stderr);
}

level_packet_sink::~level_packet_sink () {}

int
level_packet_sink::work (int noutput_items,
          gr_vector_const_void_star &input_items,
          gr_vector_void_star &output_items)
{
  return 0;
}

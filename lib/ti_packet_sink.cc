#ifdef HAVE_CONFIG_H
#include "config.h"
#endif

#include <ti_packet_sink.h>
#include <gr_io_signature.h>
#include <cstdio>
#include <errno.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <stdexcept>
#include <cstring>
#include <gr_count_bits.h>

# define VERBOSE 0

ti_packet_sink_sptr
make_ti_packet_sink (const std::vector<unsigned char>& sync_vector,
			   		gr_msg_queue_sptr target_queue)
{
  return ti_packet_sink_sptr (new ti_packet_sink (sync_vector, target_queue));
}

ti_packet_sink::ti_packet_sink (const std::vector<unsigned char>& sync_vector,
					gr_msg_queue_sptr target_queue)
  	: gr_sync_block ("ti_packet_sink",
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

ti_packet_sink::~ti_packet_sink () {}

int work (int noutput_items,
 	                  gr_vector_int &ninput_items,
 	                  gr_vector_const_void_star &input_items,
 	                  gr_vector_void_star &output_items)
{
	return 0;
}
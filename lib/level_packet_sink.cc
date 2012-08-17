#ifdef HAVE_CONFIG_H
#include "config.h"
#endif

#include <level_packet_sink.h>
#include <gr_io_signature.h>
#include <cstdio>
#include <stdint.h>
#include <errno.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <stdexcept>
#include <cstring>
#include <gr_count_bits.h>

#define VERBOSE 1

char tmp[FMT_BUF_SIZE];

inline void
level_packet_sink::enter_search()
{
  if (VERBOSE)
    fprintf(stderr, "@ enter_search\n");

  d_state = STATE_PREAMBLE_SEARCH;
  d_preamble_reg = 0;
}
    
inline void
level_packet_sink::enter_sync_search()
{
  if (VERBOSE)
    fprintf(stderr, "@ enter_sync_search\n");

  d_state = STATE_SYNC_SEARCH;
  d_sync_reg = 0;
}

level_packet_sink_sptr
level_make_packet_sink (const std::vector<unsigned char>& preamble,
                        gr_msg_queue_sptr target_queue)
{
  return level_packet_sink_sptr (new level_packet_sink (preamble, target_queue));
}

level_packet_sink::level_packet_sink (const std::vector<unsigned char>& preamble,
					gr_msg_queue_sptr target_queue)
  	: gr_sync_block ("level_packet_sink",
		   gr_make_io_signature (1, 1, sizeof(float)),
		   gr_make_io_signature (0, 0, 0)),
    d_target_queue(target_queue)
{
  // store preamble vector in int32_t
  d_preamble = 0;
  for(int i=0;i<4;i++){
    d_preamble <<= 8;
    d_preamble |= preamble[i];
  }

  if ( VERBOSE )
    fprintf(stderr, "preamble: %s\n", binary_fmt(d_preamble, tmp)), fflush(stderr);

  d_sync = 0x0000;
}

level_packet_sink::~level_packet_sink () {}

int
level_packet_sink::work (int noutput_items,
          gr_vector_const_void_star &input_items,
          gr_vector_void_star &output_items)
{
  float *inbuf = (float *) input_items[0];
  int count=0;
  d_threshold = 1;
  
  if (VERBOSE)
    fprintf(stderr, ">>> Entering state machine\n"), fflush(stderr);

  while (count<noutput_items) {
    switch(d_state) {
      
      case STATE_PREAMBLE_SEARCH:    // Look for sync vector
        
        if (VERBOSE)
          fprintf(stderr,"PREAMBLE Search, noutput=%d preamble=%s\n", noutput_items, 
                  binary_fmt(d_preamble, tmp)), fflush(stderr);

        while (count < noutput_items) {
          if(slice(inbuf[count++]))
            d_preamble_reg = (d_preamble_reg << 1) | 1;  // Shift bits one at a time into preamble
          else
            d_preamble_reg = d_preamble_reg << 1;
          
          //if (VERBOSE)
          //  fprintf(stderr,"d_shift=%u preamble=%u\n", d_preamble_reg, d_preamble), fflush(stderr); 

          // Compute popcnt of putative sync vector
          if(gr_count_bits64(d_preamble_reg ^ d_preamble) <= d_threshold) {
            if (VERBOSE)
              fprintf(stderr,"FOUND PREAMBLE, detected=%s preamble=%s\n", binary_fmt(d_preamble_reg, tmp), 
                  binary_fmt(d_preamble, tmp)), fflush(stderr);
            enter_sync_search();
            break;
          }
        }
        break;

      case STATE_SYNC_SEARCH:
        if (VERBOSE)
          fprintf(stderr,"SYNC Search, noutput=%d sync=%u\n", noutput_items, d_preamble), fflush(stderr);

        while (count < noutput_items) {
          if(slice(inbuf[count++]))
            d_sync_reg = (d_sync_reg << 1) | 1;  // Shift bits one at a time into sync
          else
            d_sync_reg = d_sync_reg << 1;

          // Compute popcnt of putative sync vector
          if(gr_count_bits64(d_sync_reg ^ d_preamble) <= d_threshold) {
            // Found it, set up for header decode
            if (VERBOSE)
              fprintf(stderr,"FOUND SYNC, detected=%s sync=%s\n", binary_fmt(d_sync_reg, tmp), 
                  binary_fmt(d_sync, tmp)), fflush(stderr);
            enter_decode_packet();
            break;
          }
        }

        break;
    }
  }

  return noutput_items;
}

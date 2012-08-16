#ifndef INCLUDED_LEVEL_PACKET_SINK
#define INCLUDED_LEVEL_PACKET_SINK

#include <gr_sync_block.h>
#include <gr_msg_queue.h>

class level_packet_sink;

typedef boost::shared_ptr<level_packet_sink> level_packet_sink_sptr;

level_packet_sink_sptr level_make_packet_sink (const std::vector<unsigned char>& sync_vector,
			   gr_msg_queue_sptr target_queue);

class level_packet_sink : public gr_sync_block
{
private:
 	friend level_packet_sink_sptr level_make_packet_sink (const std::vector<unsigned char>& sync_vector,
			   gr_msg_queue_sptr target_queue);	
 	
 	level_packet_sink();   // private constructor	
 	
 	enum state_t {STATE_SYNC_SEARCH, STATE_HAVE_SYNC};	
 	
 	static const int MSG_LEN_POS = 8+1;        			  	// 8 byte sos header, 1 byte AM type
 	static const int MAX_PKT_LEN = 128 - MSG_LEN_POS - 1;	// remove header and CRC	
 	
 	gr_msg_queue_sptr  d_target_queue;					  	// where to send the packet when received
 	unsigned long long d_sync_vector;						// access code to locate start of packet
 	unsigned int	   d_threshold;						    // how many bits may be wrong in sync vector
 	unsigned char      d_manchester;      				  	// do we use manchester encoding or not
				  	
 	state_t            d_state;				  	
				  	
 	unsigned long long d_shift_reg;						  	// used to look for sync_vector
				  	
 	unsigned int       d_header;							// header bits
 	int		     	   d_headerbitlen_cnt;				  	// how many so far	
 	unsigned char      d_packet[MAX_PKT_LEN];				// assembled payload
 	unsigned char	   d_packet_byte;						// byte being assembled
 	unsigned char      d_packet_byte_manchester;  		  	// byte which is needed for manchester encoding
 	int		     	   d_packet_byte_index;				  	// which bit of d_packet_byte we're working on
 	int 		       d_packetlen;						    // length of packet
 	int		     	   d_packetlen_cnt;					  	// how many so far
 	int		     	   d_payload_cnt;						// how many bytes in payload
  
protected:
 	level_packet_sink(const std::vector<unsigned char>& sync_vector, 
		       gr_msg_queue_sptr target_queue);
 	
 	void enter_search();
 	void enter_have_sync();

 public:
 	~level_packet_sink ();  // public destructor	
 	
 	// Where all the action really happens	
 	int work(int noutput_items,
	   gr_vector_const_void_star &input_items,
	   gr_vector_void_star &output_items);
 	
 	// return true if we detect carrier
 	bool carrier_sensed() const
 	{
 	  return d_state != STATE_SYNC_SEARCH;
 	}
};

#endif /* INCLUDED_LEVEL_PACKET_SINK */
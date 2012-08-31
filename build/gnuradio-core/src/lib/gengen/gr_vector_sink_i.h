/* -*- c++ -*- */
/*
 * Copyright 2004,2008,2009 Free Software Foundation, Inc.
 *
 * This file is part of GNU Radio
 *
 * GNU Radio is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3, or (at your option)
 * any later version.
 *
 * GNU Radio is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with GNU Radio; see the file COPYING.  If not, write to
 * the Free Software Foundation, Inc., 51 Franklin Street,
 * Boston, MA 02110-1301, USA.
 */

// WARNING: this file is machine generated.  Edits will be over written

#ifndef INCLUDED_GR_VECTOR_SINK_I_H
#define INCLUDED_GR_VECTOR_SINK_I_H

#include <gr_core_api.h>
#include <gr_sync_block.h>

class gr_vector_sink_i;
typedef boost::shared_ptr<gr_vector_sink_i> gr_vector_sink_i_sptr;

GR_CORE_API gr_vector_sink_i_sptr
gr_make_vector_sink_i (int vlen = 1);


/*!
 * \brief int sink that writes to a vector
 * \ingroup sink_blk
 */

class GR_CORE_API gr_vector_sink_i : public gr_sync_block {
  friend GR_CORE_API gr_vector_sink_i_sptr gr_make_vector_sink_i (int vlen);
  std::vector<int>	d_data;
  int			d_vlen;
  gr_vector_sink_i (int vlen);

 public:
  virtual int work (int noutput_items,
		    gr_vector_const_void_star &input_items,
		    gr_vector_void_star &output_items);

  void reset() {d_data.clear();}
  void clear() {reset(); }		// deprecated
  std::vector<int> data () const;
};

#endif

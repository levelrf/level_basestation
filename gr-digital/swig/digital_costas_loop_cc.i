/* -*- c++ -*- */
/*
 * Copyright 2005,2006,2011 Free Software Foundation, Inc.
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

GR_SWIG_BLOCK_MAGIC(digital,costas_loop_cc);

digital_costas_loop_cc_sptr
digital_make_costas_loop_cc (float loop_bw, int order
			     ) throw (std::invalid_argument);

class digital_costas_loop_cc : public gr_sync_block, public gri_control_loop
{
 private:
  digital_costas_loop_cc (float loop_bw, int order);
};

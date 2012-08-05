#!/usr/bin/env python
#

from gnuradio import gr, gr_unittest
import howto_swig

class qa_howto (gr_unittest.TestCase):

    def setUp (self):
        self.tb = gr.top_block ()

    def tearDown (self):
        self.tb = None

    def test_001_square_ff (self):
        src_data = (-3, 4, -5.5, 2, 3)
        expected_result = (-3, 4, -5.5, 2, 3)
        src = gr.vector_source_f (src_data)  #Block we are testing
        sqr = howto_swig.bliss_ff ()
        dst = gr.vector_sink_f ()

        self.tb.connect (src, sqr)
        self.tb.connect (sqr, dst)

        self.tb.run ()
        result_data = dst.data ()
        self.assertFloatTuplesAlmostEqual (expected_result, result_data, 6)

if __name__ == '__main__':
    gr_unittest.main ()
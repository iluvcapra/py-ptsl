from unittest import TestCase
from unittest.mock import Mock, patch

import ptsl.PTSL_pb2 as pt
from ptsl.engine import open_engine
import ptsl.ops as ops


class TestSessionBuilder(TestCase):
    """
    """

    def test_create(self):
        with patch('ptsl.Client'):
            with open_engine(company_name="none",
                             application_name="none") as engine:
                
                builder = engine.create_session(name="test",
                                                path="test/path")
                builder.aiff_format()
                builder.sample_rate(44100)
                builder.bit_depth(16)
                builder.stereo_io_settings()
                builder.create()

                engine.client.run.assert_called()
                called_op = engine.client.run.call_args.args[0]
                self.assertIsInstance(called_op, ops.CreateSession)
                self.assertEqual(called_op.request.file_type, pt.SAF_AIFF)
                self.assertEqual(called_op.request.sample_rate, pt.SR_44100)
                self.assertEqual(called_op.request.bit_depth, pt.Bit16)
                self.assertEqual(called_op.request.input_output_settings, 
                                 pt.IO_StereoMix)

    def test_create2(self):
        with patch('ptsl.Client'):
            with open_engine(company_name="none",
                             application_name="none") as engine:
                
                builder = engine.create_session(name="test",
                                                path="test/path")
                builder.wave_format()
                builder.bit_depth(32)
                builder.smpte51_io_settings()
                builder.interlaved(False)
                builder.create()

                engine.client.run.assert_called()
                called_op = engine.client.run.call_args.args[0]
                self.assertIsInstance(called_op, ops.CreateSession)
                self.assertEqual(called_op.request.file_type, pt.SAF_WAVE)
                self.assertEqual(called_op.request.sample_rate, pt.SR_48000)
                self.assertEqual(called_op.request.bit_depth, pt.Bit32Float)
                self.assertEqual(called_op.request.input_output_settings, 
                                 pt.IO_51SMPTEMix)
                     

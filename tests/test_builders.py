from unittest import TestCase
from unittest.mock import patch

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

    def test_text_export(self):
        with patch('ptsl.Client'):
            with open_engine(company_name="none",
                             application_name="none") as engine:

                builder = engine.export_session_as_text()
                builder.include_clip_list()
                builder.include_markers()
                builder.include_file_list()
                builder.include_plugin_list()
                builder.include_track_edls()
                builder.show_sub_frames()
                builder.time_type("min:sec")
                builder.all_tracks()
                builder.dont_show_crossfades()
                builder.utf8_encoding()

                builder.export_file(path="a/b/c.txt")

                engine.client.run.assert_called()
                called_op = engine.client.run.call_args.args[0]
                self.assertIsInstance(called_op, ops.ExportSessionInfoAsText)
                self.assertTrue(called_op.request.include_clip_list)
                self.assertTrue(called_op.request.include_markers)
                self.assertTrue(called_op.request.include_file_list)
                self.assertTrue(called_op.request.include_plugin_list)
                self.assertTrue(called_op.request.include_track_edls)
                self.assertTrue(called_op.request.show_sub_frames)
                self.assertEqual(called_op.request.fade_handling_type,
                                 pt.DontShowCrossfades)
                self.assertEqual(called_op.request.track_list_type,
                                 pt.AllTracks)
                self.assertEqual(called_op.request.track_offset_options,
                                 pt.MinSecs)
                self.assertEqual(called_op.request.text_as_file_format,
                                 pt.UTF8)
                self.assertEqual(called_op.request.output_type,
                                 pt.ESI_File)

    def test_text_export2(self):
        with patch('ptsl.Client'):
            with open_engine(company_name="none",
                             application_name="none") as engine:
                builder = engine.export_session_as_text()
                builder.time_type("tc")
                builder.textedit_encoding()
                builder.dont_show_crossfades()

                builder.export_file("out/file")

                engine.client.run.assert_called()
                called_op = engine.client.run.call_args.args[0]
                self.assertIsInstance(called_op, ops.ExportSessionInfoAsText)
                self.assertEqual(called_op.request.track_offset_options,
                                 pt.TimeCode)
                self.assertEqual(called_op.request.fade_handling_type,
                                 pt.DontShowCrossfades)

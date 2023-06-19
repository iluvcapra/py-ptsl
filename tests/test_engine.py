from typing import Optional, Any
from unittest import TestCase
from unittest.mock import Mock, patch
from contextlib import contextmanager

import ptsl.PTSL_pb2 as pt
from ptsl.engine import open_engine
import ptsl.ops as ops

@contextmanager 
def open_engine_with_mock_client(expected_response=Optional[Any]):
    with patch('ptsl.Client'):
        with open_engine(company_name="none", application_name="none") as engine:
            if expected_response is None:
                yield engine
            else:
                def give_response(op: ops.Operation):
                    op.response = expected_response
                
                with patch.object(engine.client, 'run', new=Mock(side_effect=give_response)):
                    yield engine

class TestEngine(TestCase):
    """
    The :class:`TestEngine` test case exercises the :class:`Engine` interface. The client
    is fully mocked. These tests are here mostly to make sure the engine is translating
    the auto-generated *Request classes from call arguments, and *Response classes into 
    return values correctly. If these fail, it probably means a breaking change has ocurred 
    in `PTSL.proto`.
    """

    def test_ptsl_version(self):
        with open_engine_with_mock_client(
            expected_response=pt.GetPTSLVersionResponseBody(version=1)) as engine:
            self.assertEqual(engine.ptsl_version(),1)

    def test_create_session(self):
        with open_engine_with_mock_client() as engine:
            self.assertIsNone(engine.create_session(name="test name",
                                  path="test/to/path",
                                  file_type=pt.SAF_AIFF,
                                  sample_rate=pt.SR_96000,
                                  bit_depth=pt.Bit32Float,
                                  io_setting=pt.IO_51FilmMix,
                                  is_interleaved=False))

    def test_create_session_from_template(self):
        with open_engine_with_mock_client() as engine:
            self.assertIsNone(
                engine.create_session_from_template(
                    template_group="xyz",                
                    template_name="template",
                    name="test",       
                    path="template/test/path",           
                    file_type=pt.SAF_AIFF,
                    sample_rate=pt.SR_176400,
                    bit_depth=pt.Bit16,
                    io_setting=pt.IO_51DTSMix,
                    is_interleaved=True))

    def test_create_aaf(self):
        with open_engine_with_mock_client() as engine:
            self.assertIsNone(
                engine.create_session_from_aaf(
                    name="test aaf",
                    path="test/path/to/aaf",
                    aaf_path="path/to/my/aaf",
                    file_type=pt.SAF_WAVE,
                    sample_rate=pt.SR_88200,
                    bit_depth=pt.Bit24,
                    io_setting=pt.IO_StereoMix,
                    is_interleaved=False))

    def test_open_session(self):
        with open_engine_with_mock_client() as engine:
            self.assertIsNone(
                engine.open_session(
                    path="path/to/session"
                )
            )

    def test_close_session(self):
        with open_engine_with_mock_client() as engine:
            self.assertIsNone(
                engine.close_session(save_on_close=True)
            )
    
    def test_save_session(self):
        with open_engine_with_mock_client() as engine:
            self.assertIsNone(
                engine.save_session()
            )

    def test_save_session_as(self):
        with open_engine_with_mock_client() as engine:
            self.assertIsNone(
                engine.save_session_as(path="path/to/session/named",
                                       name="name")
            )

    def text_export_session_as_text(self):
        resp = pt.ExportSessionInfoAsTextResponseBody(session_info="test string")        
        with open_engine_with_mock_client(expected_response=resp) as engine:
            info = engine.export_session_as_text(include_clip_list=True,
                                                 include_file_list=True,
                                                 include_markers=False,
                                                 include_plugin_list=True,
                                                 include_track_edls=True,
                                                 show_sub_frames=True,
                                                 track_list_type=pt.AllTracks,
                                                 include_user_timestamp=False,
                                                 fade_handling_type=pt.ShowCrossfades,
                                                 track_offset_options=pt.BarsBeats,
                                                 text_as_file_format=pt.TextEdit,
                                                 output_type=pt.ESI_String,
                                                 output_path=None)
            self.assertEqual(info,"test_string")

    def test_import_data(self):
        with open_engine_with_mock_client() as engine:

            session_data = pt.SessionData(
                audio_options=pt.LinkToSourceAudio,
                audio_handle_size=100,
                video_options=pt.LinkToSourceVideo,
                match_options=pt.MT_ImportAsNewTrack,
                playlist_options=pt.ImportReplaceExistingPlaylists,
                track_data_to_import=pt.TrackDataToImport(track_data_preset_path="path/to/preset",
                                                          clip_gain=False,clips_and_media=True,
                                                          volume_automation=True),
                timecode_mapping_units=pt.MapStartTimeCodeTo,
                timecode_mapping_start_time="01:00:00:00",
                adjust_session_start_time_to_match_source=False
            )

            audio_data = pt.AudioData(file_list = ["file_1","/path/to/file_2"],
                                      audio_operations=pt.CopyAudio,
                                      destination_path="path/to/destination",
                                      destination=pt.MD_NewTrack,
                                      location=pt.ML_Selection
                                      )
            self.assertIsNone(
                engine.import_data(session_path="path/to/import.ptx",
                                   import_type=pt.Audio,
                                   session_data=session_data,
                                   audio_data=audio_data)
            )

    def test_select_all_clips_on_track(self):
        with open_engine_with_mock_client() as engine:
            self.assertIsNone(
                engine.select_all_clips_on_track(track_name="yada yada")
            )

    def test_extend_track_selection(self):
        with open_engine_with_mock_client() as engine:
            self.assertIsNone(
                engine.extend_selection_to_target_tracks(tracks=["a","b"])
            )

    def test_trim_to_selection(self):
        with open_engine_with_mock_client() as engine:
            self.assertIsNone(
                engine.trim_to_selection()
            )

    def test_create_batch_fades(self):
        with open_engine_with_mock_client() as engine:
            self.assertIsNone(
                engine.create_batch_fades(preset_name="fades1",adjust_bounds=False)
            )

    def test_rename_track(self):
        with open_engine_with_mock_client() as engine:
            self.assertIsNone(
                engine.rename_selected_clip(new_name="new.01",
                                            rename_file=False,
                                            clip_location=pt.CL_Timeline)
            )

    def test_rename_selected_clip(self):
        with open_engine_with_mock_client() as engine:
            self.assertIsNone(
                engine.rename_target_clip(clip_name="x", 
                                          new_name="y", 
                                          rename_file=True)
            )

    def test_toggle_play_state(self):
        with open_engine_with_mock_client() as engine:
            self.assertIsNone(
                engine.toggle_play_state()
            )

    def test_toggle_record_enable(self):
        with open_engine_with_mock_client() as engine:
            self.assertIsNone(
                engine.toggle_record_enable()
            )

    def test_play_half_speed(self):
        with open_engine_with_mock_client() as engine:
            self.assertIsNone(
                engine.play_half_speed()
            )

    def test_record_half_speed(self):
        with open_engine_with_mock_client() as engine:
            self.assertIsNone(
                engine.record_half_speed()
            )

    def test_edit_memory_location(self):
        with open_engine_with_mock_client() as engine:
            self.assertIsNone(
                engine.edit_memory_location(location_number=1, 
                                            name="Marker 1",
                                            start_time="01:00:00:00",
                                            end_time="01:00:01:00",
                                            time_properties=pt.TP_Selection,
                                            reference=pt.MLR_Absolute,
                                            general_properties=pt.MemoryLocationProperties(zoom_settings=True,
                                                                                           pre_post_roll_times=True,
                                                                                           track_visibility=False,
                                                                                           track_heights=True,
                                                                                           group_enables=True,
                                                                                           window_configuration=True,
                                                                                           window_configuration_index=0,
                                                                                           window_configuration_name="Work"),
                                            comments="These are my marker comments.")
            )

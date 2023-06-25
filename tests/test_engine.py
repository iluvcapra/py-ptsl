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
        with open_engine(company_name="none",
                         application_name="none") as engine:
            if expected_response is None:
                yield engine
                engine.client.run.assert_called()
            else:
                def give_response(op: ops.Operation):
                    op.on_response_body(expected_response)

                with patch.object(engine.client, 'run',
                                  new=Mock(side_effect=give_response)):
                    yield engine
                    engine.client.run.assert_called()


class TestEngine(TestCase):
    """
    The :class:`TestEngine` test case exercises the :class:`Engine` interface.
    The client is fully mocked. These tests are here mostly to make sure the
    engine is translating the *Request classes from call arguments, and
    *Response classes into return values, correctly.

    If these fail, it probably means a breaking change has ocurred in
    `PTSL.proto` or the engine's interface.
    """

    MARKER_LOCATION_FIXTURE = [
        {'number': 1,
         'name': "Marker 1",
         'start_time': "01:00:00:00",
         'end_time': "01:00:01:00",
         'time_properties': pt.TP_Selection,
         'reference': pt.MLR_Absolute,
         'general_properties': pt.MemoryLocationProperties(
             zoom_settings=True,
             pre_post_roll_times=True,
             track_visibility=False,
             track_heights=True,
             group_enables=True,
             window_configuration=True,
             window_configuration_index=0,
             window_configuration_name="Work"),
         'comments': "These are my marker comments."},

        {'number': 2,
         'name': 'Location 2',
         'start_time': "00:59:59:23",
         'end_time': "",
         'time_properties': pt.TP_Marker,
         'reference': pt.MLR_Absolute,
         'general_properties': pt.MemoryLocationProperties(
             zoom_settings=True,
             pre_post_roll_times=True,
             track_visibility=False,
             track_heights=True,
             group_enables=True,
             window_configuration=True,
             window_configuration_index=0,
             window_configuration_name="Work"),
         'comments': "These are more comments."}]

    def test_ptsl_version(self):
        with open_engine_with_mock_client(
                expected_response=pt.GetPTSLVersionResponseBody(version=1)
        ) as engine:
            self.assertEqual(engine.ptsl_version(), 1)

    def test_create_session(self):
        with open_engine_with_mock_client() as engine:
            self.assertIsNone(
                engine.create_session(name="test name",
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
        resp = pt.ExportSessionInfoAsTextResponseBody(
            session_info="test string")
        with open_engine_with_mock_client(expected_response=resp) as engine:
            info = engine.export_session_as_text(
                include_clip_list=True,
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
            self.assertEqual(info, "test_string")

    def test_import_data(self):
        with open_engine_with_mock_client() as engine:

            session_data = pt.SessionData(
                audio_options=pt.LinkToSourceAudio,
                audio_handle_size=100,
                video_options=pt.LinkToSourceVideo,
                match_options=pt.MT_ImportAsNewTrack,
                playlist_options=pt.ImportReplaceExistingPlaylists,
                track_data_to_import=pt.TrackDataToImport(
                    track_data_preset_path="path/to/preset",
                    clip_gain=False,
                    clips_and_media=True,
                    volume_automation=True),
                timecode_mapping_units=pt.MapStartTimeCodeTo,
                timecode_mapping_start_time="01:00:00:00",
                adjust_session_start_time_to_match_source=False)

            audio_data = pt.AudioData(file_list=["file_1", "/path/to/file_2"],
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
                engine.extend_selection_to_target_tracks(tracks=["a", "b"])
            )

    def test_trim_to_selection(self):
        with open_engine_with_mock_client() as engine:
            self.assertIsNone(
                engine.trim_to_selection()
            )

    def test_create_batch_fades(self):
        with open_engine_with_mock_client() as engine:
            self.assertIsNone(
                engine.create_batch_fades(
                    preset_name="fades1",
                    adjust_bounds=False))

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
            for fixture in self.MARKER_LOCATION_FIXTURE:
                test_fixture = fixture.copy()
                # "number" is called "location_number" in the
                # EditmemoryLocationRequest
                test_fixture['location_number'] = test_fixture.pop('number')
                self.assertIsNone(
                    engine.edit_memory_location(**test_fixture)
                )

    def test_get_memory_locations(self):
        fixture = pt.GetMemoryLocationsResponseBody(
            memory_locations=[
                pt.MemoryLocation(
                    **x) for x in self.MARKER_LOCATION_FIXTURE])

        with open_engine_with_mock_client(expected_response=fixture) as engine:
            got = engine.get_memory_locations()
            self.assertEqual(len(got), len(self.MARKER_LOCATION_FIXTURE))
            for fixture, returned in zip(self.MARKER_LOCATION_FIXTURE, got):
                for k in fixture.keys():
                    self.assertEqual(fixture[k], getattr(returned, k))

    def test_consolidate_clip(self):
        with open_engine_with_mock_client() as engine:
            self.assertIsNone(
                engine.consolidate_clip()
            )

    def test_export_clips_as_files(self):
        with open_engine_with_mock_client() as engine:
            self.assertIsNone(
                engine.export_clips_as_files(
                    path="path/to/export",
                    ftype=pt.WAV,
                    bit_depth=pt.Bit24,
                    ex_format=pt.EF_Mono,
                    enforce_avid_compatibility=False,
                    resolve_duplicates=pt.AutoRenaming))

    def test_get_file_location(self):
        fixture = pt.GetFileLocationResponseBody(
            stats=None,
            file_locations=[
                pt.FileLocation(
                    path="path/to/a/file.wav",
                    info=pt.FileLocationInfo(
                        is_online=True)),
                pt.FileLocation(
                    path="path/to/b/file.wav",
                    info=pt.FileLocationInfo(
                        is_online=False))])

        with open_engine_with_mock_client(expected_response=fixture) as engine:
            got = engine.get_file_location(
                filters=[pt.Audio_Files, pt.Online_Files])
            self.assertEqual(len(got), 2)
            self.assertEqual(got[0].path, "path/to/a/file.wav")
            self.assertEqual(got[1].info.is_online, False)

    def test_export_mix(self):

        sources = [
            pt.EM_SourceInfo(
                source_type=pt.PhysicalOut,
                name="Output 1")]
        audio_info = pt.EM_AudioInfo(compression_type=pt.CT_PCM,
                                     export_format=pt.EF_MultipleMono,
                                     bit_depth=pt.Bit24,
                                     sample_rate=pt.SR_96000,
                                     pad_to_frame_boundary=pt.TB_False,
                                     delivery_format=pt.EM_DF_FilePerMixSource)

        video_info = pt.EM_VideoInfo(
            include_video=pt.TB_False,
            export_option=pt.VE_Transcode,
            replace_timecode_track=pt.TB_True,
            codec_info=pt.EM_CodecInfo(
                codec_name="my codec",
                property_list=[]))
        location_info = pt.EM_LocationInfo(
            import_after_bounce=pt.TB_None,
            import_options=pt.EM_ImportOptions())

        dolby_info = pt.EM_DolbyAtmosInfo(
            add_first_frame_of_action=pt.TB_False,
            timecode_value="01:00:00:00",
            property_list=[])

        with open_engine_with_mock_client() as engine:
            self.assertIsNone(engine.export_mix(base_name="outfile",
                                                file_type=pt.EM_WAV,
                                                sources=sources,
                                                audio_info=audio_info,
                                                video_info=video_info,
                                                location_info=location_info,
                                                dolby_atmos_info=dolby_info,
                                                offline_bounce=pt.TB_True))

    def test_session_name(self):
        fixture = pt.GetSessionNameResponseBody(
            session_name="My Great Session")
        with open_engine_with_mock_client(expected_response=fixture) as engine:
            got = engine.session_name()
            self.assertEqual(got, "My Great Session")

    def test_session_path(self):
        fixture = pt.GetSessionPathResponseBody(
            session_path=pt.FileLocation(
                path="path/to/my/great/session",
                info=pt.FileLocationInfo(
                    is_online=True)))

        with open_engine_with_mock_client(expected_response=fixture) as engine:
            got = engine.session_path()
            self.assertEqual(got, "path/to/my/great/session")

    def test_session_sample_rate(self):
        fixture = pt.GetSessionSampleRateResponseBody(sample_rate=pt.SR_44100)

        with open_engine_with_mock_client(expected_response=fixture) as engine:
            got = engine.session_sample_rate()
            self.assertEqual(got, 44100)

    def test_session_audio_format(self):
        fixture = pt.GetSessionAudioFormatResponseBody(
            current_setting=pt.SAF_AIFF, possible_settings=[
                pt.SAF_AIFF, pt.SAF_WAVE])

        with open_engine_with_mock_client(expected_response=fixture) as engine:
            got = engine.session_audio_format()
            self.assertEqual(got, pt.SAF_AIFF)

    def test_session_bit_depth(self):
        fixture = pt.GetSessionBitDepthResponseBody(
            current_setting=pt.Bit32Float, possible_settings=[
                pt.Bit16, pt.Bit24, pt.Bit32Float])

        with open_engine_with_mock_client(expected_response=fixture) as engine:
            got = engine.session_bit_depth()
            self.assertEqual(got, pt.Bit32Float)

    def test_session_interleaved_state(self):
        fixture = pt.GetSessionInterleavedStateResponseBody(
            current_setting=True, possible_settings=[True, False])

        with open_engine_with_mock_client(expected_response=fixture) as engine:
            got = engine.session_interleaved_state()
            self.assertTrue(got)

    def test_session_timecode_rate(self):
        fixture = pt.GetSessionTimeCodeRateResponseBody(
            current_setting=pt.STCR_Fps23976, possible_settings=[
                pt.STCR_Fps23976, pt.STCR_Fps24, pt.STCR_Fps25])

        with open_engine_with_mock_client(expected_response=fixture) as engine:
            got = engine.session_timecode_rate()
            self.assertEqual(got, pt.STCR_Fps23976)

    def test_session_start_time(self):
        fixture = pt.GetSessionStartTimeResponseBody(
            session_start_time="00:59:00:00")

        with open_engine_with_mock_client(expected_response=fixture) as engine:
            got = engine.session_start_time()
            self.assertEqual(got, "00:59:00:00")

    def test_session_length(self):
        fixture = pt.GetSessionLengthResponseBody(session_length="24:00:00:00")

        with open_engine_with_mock_client(expected_response=fixture) as engine:
            got = engine.session_length()
            self.assertEqual(got, "24:00:00:00")

    def test_session_feet_frames_rate(self):
        fixture = pt.GetSessionFeetFramesRateResponseBody(
            current_setting=pt.SFFR_Fps24, possible_settings=[
                pt.SFFR_Fps24, pt.SFFR_Fps25, pt.SFFR_Fps23976])

        with open_engine_with_mock_client(fixture) as engine:
            got = engine.session_feet_frames_rate()
            self.assertEqual(got, pt.SFFR_Fps24)

    def test_session_audio_rate_pull(self):
        fixture = pt.GetSessionAudioRatePullSettingsResponseBody(
            current_setting=pt.SRP_Up01,
            possible_settings=[
                pt.SRP_None,
                pt.SRP_Up01,
                pt.SRP_Up4Up01,
                pt.SRP_Up4,
                pt.SRP_Down01,
                pt.SRP_Down4,
                pt.SRP_Down4Up01,
                pt.SRP_Down4Down01])

        with open_engine_with_mock_client(fixture) as engine:
            got = engine.session_audio_rate_pull()
            self.assertEqual(got, pt.SRP_Up01)

    def test_session_video_rate_pull(self):
        fixture = pt.GetSessionVideoRatePullSettingsResponseBody(
            current_setting=pt.SRP_Down4Down01,
            possible_settings=[
                pt.SRP_None,
                pt.SRP_Up01,
                pt.SRP_Up4Up01,
                pt.SRP_Up4,
                pt.SRP_Down01,
                pt.SRP_Down4,
                pt.SRP_Down4Up01,
                pt.SRP_Down4Down01])

        with open_engine_with_mock_client(fixture) as engine:
            got = engine.session_video_rate_pull()
            self.assertEqual(got, pt.SRP_Down4Down01)

    def test_transport_state(self):
        fixture = pt.GetTransportStateResponseBody(
            current_setting=pt.TS_TransportFastForward,
            possible_settings=[
                pt.TS_TransportIsPreviewing,
                pt.TS_TransportFastForward,
                pt.TS_TransportIsCued,
                pt.TS_TransportRewind])

        with open_engine_with_mock_client(fixture) as engine:
            got = engine.transport_state()
            self.assertEqual(got, "TS_TransportFastForward")

    def test_transport_armed(self):
        fixture = pt.GetTransportArmedResponseBody(is_transport_armed=False)

        with open_engine_with_mock_client(fixture) as engine:
            got = engine.transport_armed()
            self.assertFalse(got)

    def test_playback_modes(self):
        fixture = pt.GetPlaybackModeResponseBody(
            current_settings=[
                pt.PM_Normal, pt.PM_DynamicTransport], possible_settings=[
                pt.PM_Normal, pt.PM_Loop, pt.PM_DynamicTransport])

        with open_engine_with_mock_client(fixture) as engine:
            got = engine.playback_modes()
            self.assertEqual(got, (True, False, True))

    def test_record_mode(self):
        fixture = pt.GetRecordModeResponseBody(
            current_setting=pt.RM_QuickPunch, possible_settings=[
                pt.RM_QuickPunch, pt.RM_Loop])

        with open_engine_with_mock_client(fixture) as engine:
            got = engine.record_mode()
            self.assertEqual(got, pt.RM_QuickPunch)

    def test_track_list(self):

        track_attriute_none = getattr(pt, "None")

        fixture = pt.GetTrackListResponseBody(
            stats=None,
            track_list=[
                pt.Track(
                    name="Track 1",
                    type=pt.AudioTrack,
                    id="xyz1",
                    index=0,
                    color="#FF0000",
                    track_attributes=pt.TrackAttributes(
                        is_inactive=pt.SetExplicitly,
                        is_hidden=pt.SetExplicitly,
                        is_selected=track_attriute_none,
                        contains_clips=False,
                        is_soloed=False,
                        is_record_enabled=False,
                        is_input_monitoring_on=track_attriute_none,
                        is_smart_dsp_on=False,
                        is_locked=False,
                        is_muted=False,
                        is_frozen=False,
                        is_open=True,
                        is_online=True),
                    id_compressed="zzzz")])

        with open_engine_with_mock_client(fixture) as engine:
            got = engine.track_list(
                filters=[
                    pt.TrackListInvertibleFilter(
                        filter=pt.All,
                        is_inverted=False)])
            self.assertEqual(len(got), 1)
            self.assertEqual(got[0].name, "Track 1")
            self.assertEqual(got[0].track_attributes.contains_clips, False)

    def test_set_playback_mode(self):
        with open_engine_with_mock_client() as engine:
            self.assertIsNone(engine.set_playback_mode(
                new_mode=pt.PM_DynamicTransport)
            )

    def test_set_record_mode(self):
        with open_engine_with_mock_client() as engine:
            self.assertIsNone(
                engine.set_record_mode(new_mode=pt.RM_Normal,
                                       record_arm_transport=True)
            )

    def test_set_session_bit_depth(self):
        with open_engine_with_mock_client() as engine:
            self.assertIsNone(
                engine.set_session_bit_depth(new_bit_depth=pt.Bit16)
            )

    def test_session_audio_format(self):
        with open_engine_with_mock_client() as engine:
            self.assertIsNone(
                engine.set_session_audio_format(new_audio_format=pt.SAF_AIFF)
            )
    
    def test_session_start_time(self):
        with open_engine_with_mock_client() as engine:
            self.assertIsNone(
                engine.set_session_start_time(new_start="01:00:00:00",
                                              track_offset_opts=pt.TimeCode,
                                              maintain_relative=False)
            )

    def test_set_session_length(self):
        with open_engine_with_mock_client() as engine:
            self.assertIsNone(
                engine.set_session_length(new_length="20:00:00:00")
            )

    def test_set_session_interleaved_state(self):
        with open_engine_with_mock_client() as engine:
            self.assertIsNone(
                engine.set_session_interleaved_state(new_state=True)
            )

    

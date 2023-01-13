from typing import Optional, Tuple, List, Set

from contextlib import contextmanager

import ptsl
import ptsl.ops as ops
import ptsl.PTSL_pb2 as pt


@contextmanager
def open_engine(*args, **kwargs):
    """
    Open a ptsl engine. Engine will close with the context.

    :param **kwargs: These are passed to `Engine.__init__()`
    """
    engine = Engine(*args, **kwargs)

    try:
        yield engine
    finally:
        engine.close()


class Engine:

    client: ptsl.client.Client

    def __init__(self, api_key_path: str, address='localhost:31416') -> None:
        """
        Open the engine.

        :param api_key_path: Path to developer json key file.
        :param address: server\:port to connect the engine to.
        """
        self.client = ptsl.client.Client(api_key_path=api_key_path, address=address)


    def close(self):
        """
        Close the engine.
        """
        self.client.close()


    def ptsl_version(self) -> int:
        """
        PTSL version number.
        """
        op = ops.GetPTSLVersion()
        self.client.run(op)
        return op.response.version


    def create_session(self, 
        name: str, 
        path: str,
        file_type: pt.SessionAudioFormat = pt.SAF_WAVE, 
        sample_rate: pt.SampleRate = pt.SR_48000,
        bit_depth: pt.BitDepth = pt.Bit24, 
        io_setting: pt.IOSettings = pt.IO_Last,
        is_interleaved: bool = True) -> None:
        """
        Create a new Pro Tools session.

        :param name: Session Name
        :param path: Path to the new session (use colon-delimited paths on MacOS)
        :param file_type: file type
        :param sample_rate: sample rate
        :param bit_depth: bit depth
        :param io_setting: The IO Setting to use
        """

        op = ops.CreateSession(
            session_name=name,
            file_type=file_type,
            sample_rate=sample_rate,
            input_output_settings=io_setting,
            is_interleaved=is_interleaved,
            session_location=path,
            bit_depth=bit_depth,
        )

        self.client.run(op)


    def create_session_from_template(self,
        template_group: str,
        template_name: str,
        name: str, 
        path: str,
        file_type: pt.SessionAudioFormat = pt.SAF_WAVE, 
        sample_rate: pt.SampleRate = pt.SR_48000,
        bit_depth: pt.BitDepth = pt.Bit24, 
        io_setting: pt.IOSettings = pt.IO_Last, 
        is_interleaved: bool = True) -> None:

        op = ops.CreateSession(
            session_name=name,
            create_from_template=True,
            template_group=template_group,
            template_name=template_name,
            file_type=file_type,
            sample_rate=sample_rate,
            input_output_settings=io_setting,
            is_interleaved=is_interleaved,
            session_location=path,
            bit_depth=bit_depth
        )

        self.client.run(op)


    def create_session_from_aaf(self,
        name: str, 
        path: str,
        aaf_path: str,
        file_type: pt.SessionAudioFormat = pt.SAF_WAVE, 
        sample_rate: pt.SampleRate = pt.SR_48000,
        bit_depth: pt.BitDepth = pt.Bit24, 
        io_setting: pt.IOSettings = pt.IO_Last, 
        is_interleaved: bool = True) -> None:

        op = ops.CreateSession(
            session_name=name,
            file_type=file_type,
            sample_rate=sample_rate,
            input_output_settings=io_setting,
            is_interleaved=is_interleaved,
            session_location=path,
            bit_depth=bit_depth,
            create_from_aaf=True,
            path_to_aaf=aaf_path
        )

        self.client.run(op)

    def open_session(self, path: str):
        op = ops.OpenSession(session_path=path)
        self.engine.run(op)

    def close_session(self, save_on_close : bool):
        op = ops.CloseSession(save_on_close=save_on_close)
        self.engine.run(op)

    def save_session(self):
        op = ops.SaveSession()
        self.engine.run(op)

    def save_session_as(self, path: str, name: str):
        op = ops.SaveSessionAs(session_name=name, session_location=path)
        self.engine.run(op)

    def import_data(self, session_path: str, 
        import_type: pt.ImportType,
        session_data: pt.SessionData,
        audio_data: pt.AudioData):
        
        op = ops.Import(session_path=session_path,
            import_type=import_type,
            session_data=session_data,
            audio_data=audio_data)

        self.client.run(op)

    def select_all_clips_on_track(self, track_name: str):
        op = ops.SelectAllClipsOnTrack(track_name=track_name)
        self.client.run(op)

    def extend_selection_to_target_tracks(self, tracks: List[str]):
        op = ops.ExtendSelectionToTargetTracks(tracks_to_extend_to=tracks)
        self.client.run(op)

    def rename_target_track(self, old_name: str, new_name: str):
        op = ops.RenameTargetTrack(track_id=old_name, new_name=new_name)
        self.client.run(op)

    def get_file_location(self, 
        filters = [pt.Audio_Files] ) -> List[pt.FileLocation]:
        op = ops.GetFileLocation(
            page_limit=10000,
            file_filters=filters)
        self.client.run(op)

        return op.response.file_locations

        

    def session_name(self) -> str:
        """
        Name of the current open session.
        """
        op = ops.GetSessionName()
        self.client.run(op)
        return op.response.session_name

    def session_path(self) -> str:
        """
        Path to the current open session.
        """
        op = ops.GetSessionPath()
        self.client.run(op)
        return op.response.session_path.path

    def session_sample_rate(self) -> Optional[int]:
        """
        Open session sample rate.
        """
        op = ops.GetSessionSampleRate()
        self.client.run(op)
        map_dict = {
            pt.SR_192000: 192000,
            pt.SR_176400: 176400,
            pt.SR_96000: 96000,
            pt.SR_48000: 48000,
            pt.SR_44100: 44100
        }
        return map_dict.get(op.response.sample_rate, None)

    def session_audio_format(self) -> pt.SessionAudioFormat:
        """
        Open session audio format.
        """
        op = ops.GetSessionAudioFormat()
        self.client.run(op)
        # map_dict = {
        #     pt.SAF_WAVE: 'WAVE',
        #     pt.SAF_AIFF: 'AIFF',
        # }
        return op.response.current_setting

    def session_bit_depth(self) -> pt.BitDepth:
        op = ops.GetSessionBitDepth()
        self.client.run(op)
        return op.response.current_setting

    def session_interleaved_state(self) -> bool:
        """
        Session audio file interleaved state.
        """
        op = ops.GetSessionInterleavedState()
        self.client.run(op)
        return op.response.current_setting

    def session_timecode_rate(self) -> pt.SessionTimeCodeRate:
        """
        Session timecode rate.
        """
        op = ops.GetSessionTimeCodeRate()
        self.client.run(op)
        # map_dict = {
        #     pt.STCR_Fps120: (120, 1, False),
        #     pt.STCR_Fps120Drop: (120, 1, True),
        #     pt.STCR_Fps11988: (120_000, 1001, False),
        #     pt.STCR_Fps11988Drop: (120_000, 1001, True),
        #     pt.STCR_Fps100: (100, 1, False),
        #     pt.STCR_Fps60: (60, 1, False),
        #     pt.STCR_Fps60Drop: (60, 1, True),
        #     pt.STCR_Fps5994: (60000, 1001, False),
        #     pt.STCR_Fps5994Drop: (60000, 1001, True),
        #     pt.STCR_Fps50: (50, 1, False),
        #     pt.STCR_Fps48: (48, 1, False),
        #     pt.STCR_Fps47952: (48000, 1001, False),
        #     pt.STCR_Fps30: (30, 1, False),
        #     pt.STCR_Fps30Drop: (30, 1, True),
        #     pt.STCR_Fps2997: (30000, 1001, False),
        #     pt.STCR_Fps2997Drop: (30000, 1001, True),
        #     pt.STCR_Fps25: (25, 1, False),
        #     pt.STCR_Fps24: (24, 1, False),
        #     pt.STCR_Fps23976: (24000, 1001, False)
        # }
        return op.response.current_setting

    def session_start_time(self) -> str:
        """
        Session start time.
        """
        op = ops.GetSessionStartTime()
        self.client.run(op)
        return op.response.session_start_time

    def session_length(self) -> str:
        op = ops.GetSessionLength()
        self.client.run(op)
        return op.response.session_length

    def session_feet_frames_rate(self) -> Tuple[int, int]:
        op = ops.GetSessionFeetFramesRate()
        self.client.run(op)
        # map_dict = {
        #     pt.SFFR_Fps25: (25, 1),
        #     pt.SFFR_Fps24: (24, 1),
        #     pt.SFFR_Fps23976: (24000, 1001)
        # }
        return op.response.current_setting

    # PULL_DICT = {
    #     pt.SRP_None: (0,0),
    #     pt.SRP_Down01: (0,-1),
    #     pt.SRP_Down4: (-1,0),
    #     pt.SRP_Down4Down01: (-1,-1),
    #     pt.SRP_Down4Up01: (-1,1),
    #     pt.SRP_Up01: (0, 1),
    #     pt.SRP_Up4: (1, 0),
    #     pt.SRP_Up4Up01: (1, 1),
    #     pt.SRP_Up4Down01: (1, -1),
    # }

    def session_audio_pull(self) -> pt.SessionRatePull:
        """
        
        """
        op = ops.GetSessionAudioRatePullSettings()
        self.client.run(op)
        return op.response.current_setting

    def session_video_pull(self) -> pt.SessionRatePull:
        """
        
        """
        op = ops.GetSessionVideoRatePullSettings()
        self.client.run(op)
        return op.response.current_setting

    def transport_state(self) -> str:
        op = ops.GetTransportState()
        self.client.run(op)
        return pt.TS_TransportState.Name(op.response.current_setting)

    def transport_armed(self) -> bool:
        """
        :returns: The transport's record arm state.
        """
        op = ops.GetTransportArmed()
        self.client.run(op)
        return op.response.is_transport_armed

    def playback_modes(self) -> Tuple[bool, bool, bool]:
        """
        :returns: A Tuple of (`is_normal`, `is_loop`, `is_dynamic_transport`)
        """
        op = ops.GetPlaybackMode()
        self.client.run(op)
        return (pt.PM_Normal in op.response.current_settings, 
                pt.PM_Loop in op.response.current_settings,
                pt.PM_DynamicTransport in op.response.current_settings)

    def record_mode(self) -> str:
        """
        :returns: The active record mode.
        """
        op = ops.GetRecordMode()
        self.client.run(op)
        return pt.RM_RecordMode.Name(op.response.current_setting)

    def track_list(self, filters = [pt.TrackListInvertibleFilter(filter=pt.AllTracks, is_inverted=False)]) -> List[pt.Track]:
        """
        :param filters: a list of `TrackListInvertibleFilter`s
        :returns: list of tracks
        """
        op = ops.GetTrackList(
            page_limit=1000, 
            track_filter_list=filters
        )

        self.client.run(op)

        return op.track_list

    def set_playback_mode(self, new_mode: pt.PM_PlaybackMode):
        op = ops.SetPlaybackMode(playback_mode=new_mode)
        self.client.run(op)

    def set_record_mode(self, new_mode: pt.RM_RecordMode, record_arm_transport: bool):
        op = ops.SetRecordMode(record_mode=new_mode, 
            record_arm_transport=record_arm_transport)
        self.client.run(op)

    # FIXME: This seems to work but it doesn't update the session setup window
    def set_session_bit_depth(self, new_bit_depth: pt.BitDepth):
        op = ops.SetSessionBitDepth(bit_depth=new_bit_depth)
        self.client.run(op)

    # FIXME: This seems to work but it doesn't update the session setup window
    def set_session_audio_format(self, new_audio_format: pt.SessionAudioFormat):
        op = ops.SetSessionAudioFormat(audio_format=new_audio_format)
        self.client.run(op)

    def set_session_start_time(self, new_start: str, 
        track_offset_opts: pt.TrackOffsetOptions, 
        maintain_relative: bool):
        op = ops.SetSessionStartTime(session_start_time=new_start,
            track_offset_opts=track_offset_opts,
            maintain_relative_position=maintain_relative)

        self.client.run(op)

    # FIXME: This seems to work but it doesn't update the session setup window
    def set_session_length(self, new_length: str):
        op = ops.SetSessionLength(session_length=new_length)
        self.client.run(op)

    def set_session_interleaved_state(self, new_state: bool):
        op = ops.SetSessionInterleavedState(interleaved_state=new_state)
        self.client.run(op)

    def set_session_time_code_rate(self, tc_rate: pt.SessionTimeCodeRate):
        op = ops.SetSessionTimeCodeRate(time_code_rate=tc_rate)
        self.client.run(op)

    def set_session_feet_frames_rate(self, ff_rate: pt.SessionFeetFramesRate):
        op = ops.SetSessionFeetFramesRate(feet_frames_rate=ff_rate)
        self.client.run(op)

    def set_session_audio_rate_pull(self, pull_rate: pt.SessionRatePull):
        op = ops.SetSessionAudioRatePullSettings(audio_rate_pull=pull_rate)
        self.client.run(op)

    def set_session_video_rate_pull(self, pull_rate: pt.SessionRatePull):
        op = ops.SetSessionVideoRatePullSettings(video_rate_pull=pull_rate)
        self.client.run(op)

    def cut(self, special = None):
        if special is not None:
            op = ops.CutSpecial(automation_data_option=special)
        else:
            op = ops.Cut()

        self.client.run(op)

    def copy(self, special = None):
        if special is not None:
            op = ops.CopySpecial(automation_data_option=special)
        else:
            op = ops.Copy()

        self.client.run(op)

    # FIXME: Paste-to-current doesn't seem to work when you call it
    def paste(self, special = None):
        if special is not None:
            op = ops.PasteSpecial(paste_special_option=special)
        else:
            op = ops.Paste()
        
        self.client.run(op)

    def clear(self, special = None):
        if special is not None:
            op = ops.ClearSpecial(automation_data_option=special)
        else:
            op = ops.Clear()

        self.client.run(op)

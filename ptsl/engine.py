from typing import Optional, Tuple, List
import os

from contextlib import contextmanager

import ptsl
import ptsl.ops as ops
import ptsl.PTSL_pb2 as pt
from ptsl.PTSL_pb2 import SessionAudioFormat, SampleRate, BitDepth, \
    IOSettings, ImportType, SessionData, AudioData, FileLocation, \
    EM_FileType, EM_SourceInfo, EM_AudioInfo, EM_VideoInfo, \
    EM_LocationInfo, EM_DolbyAtmosInfo, TripleBool, SessionTimeCodeRate, \
    SessionFeetFramesRate, SessionRatePull, RM_RecordMode, Track, \
    PM_PlaybackMode, RM_RecordMode, AutomationDataOptions, \
    PasteSpecialOptions, TrackOffsetOptions


@contextmanager
def open_engine(*args, **kwargs):
    """
    Open a ptsl engine. Engine will close with the context.
    """
    engine = Engine(*args, **kwargs)

    try:
        yield engine
    finally:
        engine.close()


class Engine:

    client: ptsl.client.Client

    def __init__(self, certificate_path: Optional[str] = None, address='localhost:31416'):
        """
        Open the engine.

        :param certificate_path: Path to developer json key file. Pass :py:class:`None`
            and the engine will read a path in from the "PTSL_KEY" environment variable.
        :param address: server\:port to connect the engine to.
        """
        certificate_path = certificate_path or os.getenv('PTSL_KEY')
        self.client = ptsl.client.Client(certificate_path=certificate_path, address=address)


    def close(self):
        """
        Close the engine.
        """
        self.client.close()


    def ptsl_version(self) -> int:
        """
        Requests the current PTSL version running on the server and returns the
        reponse value.
        """
        op = ops.GetPTSLVersion()
        self.client.run(op)
        return op.response.version


    def create_session(self, 
        name: str, 
        path: str,
        file_type: 'SessionAudioFormat' = pt.SAF_WAVE, 
        sample_rate: 'SampleRate' = pt.SR_48000,
        bit_depth: 'BitDepth' = pt.Bit24, 
        io_setting: 'IOSettings' = pt.IO_Last,
        is_interleaved: bool = True) -> None:
        """
        Create a new Pro Tools session.

        :param name: Session Name
        :param path: Path to the new session (use colon-delimited paths on MacOS)
        :param file_type: file type, defaults to :attr:`~ptsl.PTSL_pb2.SessionAudioFormat.SAF_WAVE`
        :param sample_rate: sample rate, defaults to :attr:`~ptsl.PTSL_pb2.SampleRate.SR_48000`
        :param bit_depth: bit depth, defaults to :attr:`~ptsl.PTSL_pb2.BitDepth.Bit24`
        :param io_setting: The IO Setting to use, defaults to :attr:`~ptsl.PTSL_pb2.IOSettings.IO_Last`
        :param is_interelaved: Interleaved state
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
        file_type: 'SessionAudioFormat' = pt.SAF_WAVE, 
        sample_rate: 'SampleRate' = pt.SR_48000,
        bit_depth: 'BitDepth' = pt.Bit24, 
        io_setting: 'IOSettings' = pt.IO_Last, 
        is_interleaved: bool = True) -> None:
        """
        Create a new session with an installed template.
        """

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
        file_type: 'SessionAudioFormat' = pt.SAF_WAVE, 
        sample_rate: 'SampleRate' = pt.SR_48000,
        bit_depth: 'BitDepth' = pt.Bit24, 
        io_setting: 'IOSettings' = pt.IO_Last, 
        is_interleaved: bool = True) -> None:
        """
        Create a session from an AAF.
        """

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
        """
        Open a session.
        """
        op = ops.OpenSession(session_path=path)
        self.engine.run(op)


    def close_session(self, save_on_close : bool):
        """
        Close the currently-open session.
        """
        op = ops.CloseSession(save_on_close=save_on_close)
        self.engine.run(op)


    def save_session(self):
        """
        Save the currently-open session.
        """
        op = ops.SaveSession()
        self.engine.run(op)


    def save_session_as(self, path: str, name: str):
        """
        Save the currently-open session as a new name toa different path.
        :param path: Path to the new session
        :param name: New name for the session
        """
        op = ops.SaveSessionAs(session_name=name, session_location=path)
        self.engine.run(op)


    def import_data(self, session_path: str, 
        import_type: 'ImportType',
        session_data: 'SessionData',
        audio_data: 'AudioData'):
        """
        Import session data into the currently-open session.
        """
        
        op = ops.Import(session_path=session_path,
            import_type=import_type,
            session_data=session_data,
            audio_data=audio_data)

        self.client.run(op)


    def select_all_clips_on_track(self, track_name: str):
        """
        Select all clips on track.

        :param track_name: Name of the track to select all clips on.
        """
        op = ops.SelectAllClipsOnTrack(track_name=track_name)
        self.client.run(op)


    def extend_selection_to_target_tracks(self, tracks: List[str]):
        """
        Extend selection to target tracks.

        :param tracks: A list of track names to extend the selection to.
        """
        op = ops.ExtendSelectionToTargetTracks(tracks_to_extend_to=tracks)
        self.client.run(op)


    def trim_to_selection(self):
        """
        Trim selected clips to the edit selection range.
        """
        op = ops.TrimToSelection()
        self.client.run(op)


    def create_batch_fades(self, preset_name: str, adjust_bounds: bool):
        """
        Create batch fades for the timeline selection based on a preset.

        :param preset_name: Name of the batch fades preset to use.
        :param adjust_bounds: Auto-adjust clip boundaries to accomodate
            fades.
        """
        op = ops.CreateFadesBasedOnPreset(
            preset_name=preset_name, 
            auto_adjust_bounds=adjust_bounds)
        self.client.run(op)

    def rename_target_track(self, old_name: str, new_name: str):
        """
        Renames a track in the currently-open session.

        :param old_name: The name of the track to rename.
        :param new_name: The new name to give the track.
        """
        op = ops.RenameTargetTrack(track_id=old_name, new_name=new_name)
        self.client.run(op)

    def get_file_location(self, 
        filters = [pt.Audio_Files] ) -> List['FileLocation']:
        """
        Get a list of file locations meeting a set of criteria.

        :param filters: a List of :py:class:`~ptsl.FileLocationTypeFilter`
        :returns: a List of :py:class:`~ptsl.FileLocation`
        """
        op = ops.GetFileLocation(
            page_limit=10000,
            file_filters=filters)
        self.client.run(op)

        return op.response.file_locations

    def export_mix(self, base_name: str, 
        file_type: 'EM_FileType',
        path_list: List['EM_SourceInfo'],
        audio_info: 'EM_AudioInfo',
        video_info: 'EM_VideoInfo',
        location_info: 'EM_LocationInfo',
        dolby_atmos_info: 'EM_DolbyAtmosInfo',
        offline_bounce: 'TripleBool'
        ):
        """
        Export mixes/"Bounce to Disk" busses in the currently-open session.

        *Note: This method runs synchronously and will not return until the
        bounce has completed.*

        :param file_type: Export file type as a :py:class:`~ptsl.EM_FileType`
        :param path_list: Busses to bounce, a List of :py:class:`~ptsl.EM_SourceInfo`
        :param audio_info: Audio options, a :py:class:`~ptsl.EM_AudioInfo`
        :param video_info: Video options, a :py:class:`~ptsl.EM_VideoInfo`
        :param location_info: Output folder settings, a :py:class:`~ptsl.EM_LocationInfo`
        :param dolby_atmos_info: Dolby Atmos output settings
        :param offline_bounce: Will bounce offline if this is :py:attr:`~ptsl.TripleBool.TB_True`
        """
        op = ops.ExportMix(
            file_name=base_name,
            file_type=file_type,
            files_list=path_list,
            audio_info=audio_info,
            video_info=video_info,
            location_info=location_info,
            dolby_atmos_info=dolby_atmos_info,
            offline_bounce=offline_bounce
            )
        self.client.run(op) 

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

    def session_audio_format(self) -> 'SessionAudioFormat':
        """
        Open session audio format.
        """
        op = ops.GetSessionAudioFormat()
        self.client.run(op)
        return op.response.current_setting

    def session_bit_depth(self) -> 'BitDepth':
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

    def session_timecode_rate(self) -> 'SessionTimeCodeRate':
        """
        Session timecode rate.
        """
        op = ops.GetSessionTimeCodeRate()
        self.client.run(op)
        return op.response.current_setting

    def session_start_time(self) -> str:
        """
        Session start time.
        """
        op = ops.GetSessionStartTime()
        self.client.run(op)
        return op.response.session_start_time

    def session_length(self) -> str:
        """
        """
        op = ops.GetSessionLength()
        self.client.run(op)
        return op.response.session_length

    def session_feet_frames_rate(self) -> 'SessionFeetFramesRate':
        """
        """
        op = ops.GetSessionFeetFramesRate()
        self.client.run(op)
        return op.response.current_setting


    def session_audio_rate_pull(self) -> 'SessionRatePull':
        """
        Audio pull setting of the currently-open session.

        :returns: a :class:`SessionRatePull` enum.
        """
        op = ops.GetSessionAudioRatePullSettings()
        self.client.run(op)
        return op.response.current_setting


    def session_video_rate_pull(self) -> 'SessionRatePull':
        """
        Video pull setting of the currently-open session.

        :returns: a :class:`SessionRatePull` enum.
        """
        op = ops.GetSessionVideoRatePullSettings()
        self.client.run(op)
        return op.response.current_setting


    def transport_state(self) -> str:
        """
        Current transport state.
        """
        op = ops.GetTransportState()
        self.client.run(op)
        return pt.TS_TransportState.Name(op.response.current_setting)


    def transport_armed(self) -> bool:
        """
        Transport record-arm state.

        :returns: The transport's record arm state.
        """
        op = ops.GetTransportArmed()
        self.client.run(op)
        return op.response.is_transport_armed


    def playback_modes(self) -> Tuple[bool, bool, bool]:
        """
        Transport's current set of playback modes.

        :returns: A Tuple of (`is_normal`, `is_loop`, `is_dynamic_transport`)
        """
        op = ops.GetPlaybackMode()
        self.client.run(op)
        return (pt.PM_Normal in op.response.current_settings, 
                pt.PM_Loop in op.response.current_settings,
                pt.PM_DynamicTransport in op.response.current_settings)

    def record_mode(self) -> 'RM_RecordMode':
        """
        Transport's current record mode.

        :returns: The active record mode.
        """
        op = ops.GetRecordMode()
        self.client.run(op)
        return op.response.current_setting

    def track_list(self, filters = [pt.TrackListInvertibleFilter(filter=pt.AllTracks, is_inverted=False)]) -> List['Track']:
        """
        Get a list of the tracks in the current session.

        :param filters: a list of :class:`~ptsl.PTSL_pb2.TrackListInvertibleFilter`
        :returns: list of :class:`~ptsl.PTSL_pb2.Track`
        """
        op = ops.GetTrackList(
            page_limit=1000, 
            track_filter_list=filters
        )

        self.client.run(op)

        return op.track_list

    def set_playback_mode(self, new_mode: 'PM_PlaybackMode'):
        """
        Set the playback mode.
        """
        op = ops.SetPlaybackMode(playback_mode=new_mode)
        self.client.run(op)

    def set_record_mode(self, new_mode: 'RM_RecordMode', record_arm_transport: bool):
        """
        Set the record mode.
        """
        op = ops.SetRecordMode(record_mode=new_mode, 
            record_arm_transport=record_arm_transport)
        self.client.run(op)

    def set_session_bit_depth(self, new_bit_depth: 'BitDepth'):
        """
        """
        op = ops.SetSessionBitDepth(bit_depth=new_bit_depth)
        self.client.run(op)

    def set_session_audio_format(self, new_audio_format: 'SessionAudioFormat'):
        """
        """
        op = ops.SetSessionAudioFormat(audio_format=new_audio_format)
        self.client.run(op)

    def set_session_start_time(self, new_start: str, 
        track_offset_opts: 'TrackOffsetOptions', 
        maintain_relative: bool):
        """
        """
        op = ops.SetSessionStartTime(session_start_time=new_start,
            track_offset_opts=track_offset_opts,
            maintain_relative_position=maintain_relative)

        self.client.run(op)

    def set_session_length(self, new_length: str):
        """
        """
        op = ops.SetSessionLength(session_length=new_length)
        self.client.run(op)

    def set_session_interleaved_state(self, new_state: bool):
        """
        """
        op = ops.SetSessionInterleavedState(interleaved_state=new_state)
        self.client.run(op)

    def set_session_time_code_rate(self, tc_rate: 'SessionTimeCodeRate'):
        """
        """
        op = ops.SetSessionTimeCodeRate(time_code_rate=tc_rate)
        self.client.run(op)

    def set_session_feet_frames_rate(self, ff_rate: 'SessionFeetFramesRate'):
        """
        """
        op = ops.SetSessionFeetFramesRate(feet_frames_rate=ff_rate)
        self.client.run(op)

    def set_session_audio_rate_pull(self, pull_rate: 'SessionRatePull'):
        """
        """
        op = ops.SetSessionAudioRatePullSettings(audio_rate_pull=pull_rate)
        self.client.run(op)

    def set_session_video_rate_pull(self, pull_rate: 'SessionRatePull'):
        """
        """
        op = ops.SetSessionVideoRatePullSettings(video_rate_pull=pull_rate)
        self.client.run(op)

    def cut(self, special: Optional['AutomationDataOptions'] = None):
        """
        Execute an Edit > Cut.

        :param special: An :class:`AutomationDataOptions` value.
        """
        if special is not None:
            op = ops.CutSpecial(automation_data_option=special)
        else:
            op = ops.Cut()

        self.client.run(op)

    def copy(self, special : Optional['AutomationDataOptions'] = None):
        """
        Execute an Edit > Copy.

        :param special: An :class:`AutomationDataOptions` value.
        """
        if special is not None:
            op = ops.CopySpecial(automation_data_option=special)
        else:
            op = ops.Copy()

        self.client.run(op)

    def paste(self, special : Optional['PasteSpecialOptions'] = None):
        """
        Execute an Edit > Paste.

        :param special: A :class:`PasteSpecialOption` value.
        """
        if special is not None:
            op = ops.PasteSpecial(paste_special_option=special)
        else:
            op = ops.Paste()
        
        self.client.run(op)

    def clear(self, special: Optional['AutomationDataOptions'] = None):
        """
        Execute an Edit > Clear.

        :param special: An :class:`AutomationDataOptions` value.
        """
        if special is not None:
            op = ops.ClearSpecial(automation_data_option=special)
        else:
            op = ops.Clear()

        self.client.run(op)

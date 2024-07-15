"""
ptsl Engine - Engine class and context manager
"""

from __future__ import annotations
from typing import Optional, Tuple, List

from contextlib import contextmanager

import ptsl
from ptsl import ops
from ptsl.builders.create_session_builder import \
    CreateSessionBuilder, CreateSessionFromTemplateBuilder, \
    CreateSessionFromAAFBuilder
from ptsl.builders.export_text_builder import \
    ExportSessionTextBuilder
from ptsl.builders.import_builder import \
    ImportSessionDataBuilder

import ptsl.PTSL_pb2 as pt
from ptsl.PTSL_pb2 import SessionAudioFormat, BitDepth, FileLocation, \
    EM_FileType, EM_SourceInfo, EM_AudioInfo, EM_VideoInfo, \
    EM_LocationInfo, EM_DolbyAtmosInfo, TripleBool, SessionTimeCodeRate, \
    SessionFeetFramesRate, SessionRatePull, Track, \
    PM_PlaybackMode, RM_RecordMode, AutomationDataOptions, \
    PasteSpecialOptions, TrackOffsetOptions, TrackListInvertibleFilter, \
    ExportFileType, ResolveDuplicateNamesBy, ExportFormat, \
    MemoryLocationReference, MemoryLocationProperties, \
    TimeProperties, CL_ClipLocation, \
    TrackFormat, TrackType, TrackTimebase, \
    AudioOperations, MediaDestination, MediaLocation, \
    SpotLocationType, Start, TimeCode, \
    TimelineUpdateVideo, SelectionMode


@contextmanager
def open_engine(*args, **kwargs):
    """
    Open a ptsl engine. Engine will close with the context.
    :param company_name: The company name to register.
    :param application_name: The application name to register.
    :param certificate_path: A path to a certificate (deprecated).
    """
    engine = Engine(*args, **kwargs)

    try:
        yield engine
    finally:
        engine.close()


class Engine:
    """
    A callable interface for PTSL.

    The Engine exposes PTSL commands as methods, translating call
    arguments into corresponding requests, and then translating
    responses into return objects. So, instead of creating a request,
    dispatching a command to the client with the request object,
    receving a response (or error) and processing it, you can simply
    call a method on the Engine with parameters, and that method returns
    a value.

    One of the goals of the engine class is to hide as many redundant
    value classes from the PTSL protocol as possible, so where the PTSL
    client may return an enumeration value for the session sample rate,
    the Engine returns a simple integer. Entity types, like :class:`Track`
    or :class:`MemoryLocation` objects are retained.

    The `Engine` initializes a new :class:`Client` object by passing its
    initialization parameters to :meth:`~ptsl.Client.__init__`
    """

    client: ptsl.Client

    def __init__(self,
                 company_name: Optional[str] = None,
                 application_name: Optional[str] = None,
                 certificate_path: Optional[str] = None,
                 address='localhost:31416'):

        self.client = ptsl.Client(certificate_path=certificate_path,
                                  company_name=company_name,
                                  application_name=application_name,
                                  address=address)

    def close(self):
        """
        Close the engine.
        """
        self.client.close()

    def ptsl_version(self) -> int:
        """
        Requests the current PTSL version running on the server and returns the
        reponse value.

        :returns: The server's PTSL version number.
        :rtype: int
        """
        op = ops.GetPTSLVersion()
        self.client.run(op)
        assert isinstance(
            op.response, pt.GetPTSLVersionResponseBody), \
            f"Expected response body, encountered {op.response}"

        return op.response.version

    def host_ready_check(self):
        """
        Runs the `HostReadyCheck` message on the host, any error
        is returned as an exception.

        .. note:: This method will succeed even if the client
            connection is not registered.
        """
        self.client.run(ops.HostReadyCheck())

    def create_session(self,
                       name: str,
                       path: str) -> CreateSessionBuilder:
        """
        Create a new Pro Tools session. Returns a
        :class:`~ptsl.builders.create_session_builder.CreateSessionBuilder`
        object used to customize the creation request.

        .. sourcecode:: python
           :caption: Creating a session with a builder

           b = engine.create_session("My Session", "/Path/to/Session")
           b.wave_format()
           b.sample_rate(96000)
           b.bit_depth(32)
           b.create() # Session is created

        :param str name: Session Name
        :param str path: Path to the new session
        """
        return CreateSessionBuilder(engine=self, name=name, path=path)

    def create_session_from_template(
            self,
            template_group: str,
            template_name: str,
            name: str,
            path: str) -> CreateSessionFromTemplateBuilder:
        """
        Create a new session with an installed template.

        :param str template_group: Name of the template group
        :param str template_name: Name of the template to use
        :param str name: Name of the new session
        :param str path: Path for the new session
        """
        return CreateSessionFromTemplateBuilder(self,
                                                template_name,
                                                template_group,
                                                name,
                                                path)

    def create_session_from_aaf(
            self,
            name: str,
            path: str,
            aaf_path: str) -> CreateSessionFromAAFBuilder:
        """
        Create a session from an AAF.

        :param str name: Name of the new session
        :param str path: Path for the new session
        :param str aaf_path: Path to the AAF file to convert
        """
        return CreateSessionFromAAFBuilder(self,
                                           aaf_path=aaf_path,
                                           name=name,
                                           path=path)

    def open_session(self, path: str):
        """
        Open a session.
        """
        op = ops.OpenSession(session_path=path)
        self.client.run(op)

    def close_session(self, save_on_close: bool):
        """
        Close the currently-open session.
        """
        op = ops.CloseSession(save_on_close=save_on_close)
        self.client.run(op)

    def save_session(self):
        """
        Save the currently-open session.
        """
        op = ops.SaveSession()
        self.client.run(op)

    def save_session_as(self, path: str, name: str):
        """
        Save the currently-open session as a new name to a different path.

        :param str path: Path to the new session
        :param str name: New name for the session
        """
        op = ops.SaveSessionAs(session_name=name, session_location=path)
        self.client.run(op)

    def export_session_as_text(self) -> ExportSessionTextBuilder:
        """
        Export the open session as text.
        """
        return ExportSessionTextBuilder(self)

    def import_data(self,
                    session_path: str
                    ) -> ImportSessionDataBuilder:
        """
        Import session data into the currently-open session.
        """
        return ImportSessionDataBuilder(self, session_path)

    def import_audio(self,
                     file_list: List[str],
                     destination_path: Optional[str] = None,
                     audio_operations: Optional[AudioOperations] = None,
                     audio_destination: Optional[MediaDestination] = None,
                     audio_location: Optional[MediaLocation] = None,
                     timecode: Optional[str] = None,
                     location_type: Optional[SpotLocationType] = Start,
                     location_options: Optional[TrackOffsetOptions] = TimeCode
                     ) -> None:
        """
        Import audio data into the currently-open session.
        location_data needs to be provided regardless if empty.
        Just a basic implementation for audio data import TC based only.
        """
        location_data = pt.SpotLocationData(location_type=location_type,
                                            location_options=location_options,
                                            location_value=timecode
                                            )
        audio_data = pt.AudioData(file_list=file_list,
                                  destination_path=destination_path,
                                  audio_operations=audio_operations,
                                  audio_destination=audio_destination,
                                  audio_location=audio_location,
                                  location_data=location_data
                                  )
        op = ops.Import(import_type=1, audio_data=audio_data)
        self.client.run(op)

    def select_all_clips_on_track(self, track_name: str):
        """
        Select all clips on track.

        :param str track_name: Name of the track to select all clips on.
        """
        op = ops.SelectAllClipsOnTrack(track_name=track_name)
        self.client.run(op)

    def extend_selection_to_target_tracks(self, tracks: List[str]):
        """
        Extend selection to target tracks.

        :param List[str] tracks: A list of track names to extend
            the selection to.
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

        :param str preset_name: Name of the batch fades preset to use.
        :param bool adjust_bounds: Auto-adjust clip boundaries to accomodate
            fades.
        """
        rq = pt.CreateFadesBasedOnPresetRequestBody()
        rq.fade_preset_name = preset_name
        rq.auto_adjust_bounds = adjust_bounds
        op = ops.CreateFadesBasedOnPreset()
        op.request = rq
        self.client.run(op)

    def rename_target_track(self, old_name: str, new_name: str):
        """
        Renames a track in the currently-open session.

        :param str old_name: The name of the track to rename.
        :param str new_name: The new name to give the track.
        """
        op = ops.RenameTargetTrack(current_name=old_name,
                                   new_name=new_name)
        self.client.run(op)

    def rename_selected_clip(
            self,
            new_name: str,
            rename_file: bool = True,
            clip_location: 'CL_ClipLocation' = pt.CL_Timeline):
        """
        Renames a clip in the current session.

        :param str new_name: New name for the clip
        :param bool rename_file: If true, file will be renamed as well
        :param CL_ClipLocation clip_location: Clip selection location,
            defaults to :attr:`~ptsl.PTSL_pb2.CL_ClipLocation.CL_Timeline`
        """
        op = ops.RenameSelectedClip(clip_location=clip_location,
                                    new_name=new_name,
                                    rename_file=rename_file)

        self.client.run(op)

    def rename_target_clip(self, clip_name: str,
                           new_name: str,
                           rename_file: bool = True):
        """
        Renames a named clip in the current session.
        """
        op = ops.RenameTargetClip(clip_name=clip_name,
                                  new_name=new_name,
                                  rename_file=rename_file)

        self.client.run(op)

    def toggle_play_state(self):
        """
        Toggle the play state.
        """
        self.client.run(ops.TogglePlayState())

    def toggle_record_enable(self):
        """
        Toggle record enable.
        """
        self.client.run(ops.ToggleRecordEnable())

    def play_half_speed(self):
        """
        Play at half speed.
        """
        self.client.run(ops.PlayHalfSpeed())

    def record_half_speed(self):
        """
        Record at half speed.
        """
        self.client.run(ops.RecordHalfSpeed())

    def create_memory_location(
            self,
            start_time: Optional[str] = None,
            memory_number: Optional[int] = None,
            name: Optional[str] = None,
            end_time: Optional[str] = None,
            location: Optional[str] = None,
            track_name: Optional[str] = None,
            time_properties:
            Optional[TimeProperties] = None,
            reference: Optional[MemoryLocationReference] = None,
            general_properties: Optional[MemoryLocationProperties] = None,
            comments: Optional[str] = None,
            color_index: Optional[int] = None
    ) -> None:
        """
        Create a new memory location.
        """
        if general_properties is None:
            general_properties = MemoryLocationProperties(
                track_visibility=False)
        op = ops.CreateMemoryLocation(
            number=memory_number,
            name=name,
            start_time=start_time,
            end_time=end_time,
            track_name=track_name,
            time_properties=time_properties,
            reference=reference,
            general_properties=general_properties,
            comments=comments,
            location=location,
            color_index=color_index
        )
        self.client.run(op)

    def get_edit_mode(self):
        """
        :returns: The current edit mode and options:
        """
        op = ops.GetEditMode()
        self.client.run(op)
        # mode = op.response.current_setting

        op2 = ops.GetEditModeOptions()
        self.client.run(op2)
        # options = op.response.edit_mode_options

    def edit_memory_location(self, location_number: int,
                             name: str,
                             start_time: str, end_time: str,
                             time_properties: 'TimeProperties',
                             reference: 'MemoryLocationReference',
                             general_properties: 'MemoryLocationProperties',
                             comments: str):
        """
        Edit a memory location.

        :param int location_number: Location number to edit (if location
            does not exist, this will create a new location in 2023.6)
        :param str name: Location name
        :param str start_time: Start time
        :param str end_time: End time
        :param TimeProperties time_properties: Time properties, either this
            is a range or a marker
        :param MemoryLocationReference reference: Reference
        :param MemoryLocationProperties general_properties: Location properties
        :param str comments: Comment field
        """
        op = ops.EditMemoryLocation(
            number=location_number,
            name=name,
            start_time=start_time,
            end_time=end_time,
            time_properties=time_properties,
            reference=reference,
            general_properties=general_properties,
            comments=comments
        )

        self.client.run(op)

    def get_memory_locations(self) -> List[pt.MemoryLocation]:
        """
        Get a list of all memory locations in currently-open session.
        """
        op = ops.GetMemoryLocations(
            pagination_request=pt.PaginationRequest(limit=1000, offset=0)
        )
        self.client.run(op)
        return op.response.memory_locations

    def consolidate_clip(self):
        """
        Consolidate time selection.
        """
        op = ops.ConsolidateClip()
        self.client.run(op)

    def export_clips_as_files(
            self,
            path: str,
            ftype: 'ExportFileType', bit_depth: 'BitDepth',
            ex_format: Optional['ExportFormat'] = None,
            enforce_avid_compatibility: bool = False,
            resolve_duplicates: Optional['ResolveDuplicateNamesBy'] = None
    ):
        """
        Export clips as files.

        :param path: Export directory path. (A MacOS path to a folder, must
            end with a colon ":".)
        :param ftype: File type, WAV/AIFF/etc.
        :param bit_depth: Bit Depth
        :param ex_format: Export file format, mono/multiple mono/interleaved
        :param enforce_avid_compatibilty: Enforce Avid compatibility
        :param resolve_duplicates: Duplicate name resolution method
        :raises: :class:`~ptls.errors.CommandError` A :attr:`PT_UnknownError`
            if the ``path`` argument does not end with a colon.
        """
        rq = pt.ExportClipsAsFilesRequestBody()
        rq.bit_depth = bit_depth
        rq.enforce_avid_compatibility = enforce_avid_compatibility
        rq.file_path = path
        rq.file_type = ftype

        if resolve_duplicates is not None:
            rq.duplicate_names = resolve_duplicates

        if ex_format is not None:
            rq.format = ex_format

        op = ops.ExportClipsAsFiles()
        op.request = rq
        self.client.run(op)

    def get_file_location(
            self,
            filters=None) -> List['FileLocation']:
        """
        Get a list of file locations meeting a set of criteria.

        :param filters: a List of
            :py:class:`~ptsl.PTSL_pb2.FileLocationTypeFilter`
            If none, defaults
            to [:attr:`~ptsl.PTSL_pb2.FileLocationTypeFilter.All_Files`]
        :returns: a List of :py:class:`~ptsl.PTSL_pb2.FileLocation`
        """
        if filters is None:
            filters = [pt.All_Files]
        op = ops.GetFileLocation(
            pagination_request=pt.PaginationRequest(limit=1000, offset=0),
            file_filters=filters)
        self.client.run(op)

        return op.response.file_locations

    def export_mix(
            self,
            base_name: str,
            file_type: 'EM_FileType',
            sources: List['EM_SourceInfo'],
            audio_info: 'EM_AudioInfo',
            video_info: 'EM_VideoInfo',
            location_info: 'EM_LocationInfo',
            dolby_atmos_info: 'EM_DolbyAtmosInfo',
            offline_bounce: 'TripleBool'
    ):
        """
        Export mixes/"Bounce to Disk" busses in the currently-open session.

        .. note:: This method runs synchronously and will not return until the
                bounce has completed.

        :param EM_FileType file_type: Export file type
        :param List[EM_SourceInfo] sources: Busses to bounce
        :param EM_AudioInfo audio_info: Audio options
        :param EM_VideoInfo video_info: Video options
        :param EM_LocationInfo location_info: Output folder settings
        :param EM_DolbyAtmosInfo dolby_atmos_info: Dolby Atmos output settings
        :param bool offline_bounce: Bounce offline option
        """
        op = ops.ExportMix(
            file_name=base_name,
            file_type=file_type,
            mix_source_list=sources,
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
            pt.SR_88200: 88200,
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
        Session length.

        :returns: Session length, as a string in the current
            time code format.
        """
        op = ops.GetSessionLength()
        self.client.run(op)
        return op.response.session_length

    def session_feet_frames_rate(self) -> 'SessionFeetFramesRate':
        """
        Session feet-frames rate.
        """
        op = ops.GetSessionFeetFramesRate()
        self.client.run(op)
        return op.response.current_setting

    def session_audio_rate_pull(self) -> 'SessionRatePull':
        """
        Audio pull setting of the currently-open session.
        """
        op = ops.GetSessionAudioRatePullSettings()
        self.client.run(op)
        return op.response.current_setting

    def session_video_rate_pull(self) -> 'SessionRatePull':
        """
        Video pull setting of the currently-open session.
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
        """
        op = ops.GetRecordMode()
        self.client.run(op)
        return op.response.current_setting

    def track_list(
            self,
            filters: List['TrackListInvertibleFilter'] = []
    ) -> List['Track']:
        """
        Get a list of the tracks in the current session.

        :param filters: Track list filters. Defaults to
            [:attr:`ptsl.PTSL_pb2.TrackListFilter.All`]
        """
        if len(filters) == 0:
            filters = [pt.TrackListInvertibleFilter(filter=pt.All,
                                                    is_inverted=False)]

        op = ops.GetTrackList(
            track_filter_list=filters,
            pagination_request=pt.PaginationRequest(limit=1000, offset=0)
        )

        self.client.run(op)

        return op.track_list

    def set_playback_mode(self, new_mode: 'PM_PlaybackMode'):
        """
        Set the playback mode.
        """
        op = ops.SetPlaybackMode(playback_mode=new_mode)
        self.client.run(op)

    def set_record_mode(
            self,
            new_mode: 'RM_RecordMode',
            record_arm_transport: bool):
        """
        Set the record mode.
        """
        op = ops.SetRecordMode(
            record_mode=new_mode,
            record_arm_transport=record_arm_transport
        )
        self.client.run(op)

    def set_session_bit_depth(self, new_bit_depth: 'BitDepth'):
        """
        Set session bit depth.
        """
        op = ops.SetSessionBitDepth(bit_depth=new_bit_depth)
        self.client.run(op)

    def set_session_audio_format(self, new_audio_format: 'SessionAudioFormat'):
        """
        Set session audio format.
        """
        op = ops.SetSessionAudioFormat(audio_format=new_audio_format)
        self.client.run(op)

    def set_session_start_time(
            self,
            new_start: str,
            track_offset_opts: 'TrackOffsetOptions',
            maintain_relative: bool
    ):
        """
        Set session start time.

        :param new_start: New timecode start time
        :param track_offset_opts: The time format of ``new_start``.
        :param maintain_relative: If `True`, clips will retain their time
            position relative to the beginning of the session.
        """
        op = ops.SetSessionStartTime(
            session_start_time=new_start,
            track_offset_opts=track_offset_opts,
            maintain_relative_position=maintain_relative
        )

        self.client.run(op)

    def set_session_length(self, new_length: str):
        """
        Set the session length as a timecode value string.

        .. important:: The ``new_length`` value must be greater
            than "06:00:00:00", the PTSL server will reject the
            change and return an error otherwise.
        """
        op = ops.SetSessionLength(session_length=new_length)
        self.client.run(op)

    def set_session_interleaved_state(self, new_state: bool):
        """
        Set session interleaved state.
        """
        op = ops.SetSessionInterleavedState(interleaved_state=new_state)
        self.client.run(op)

    def set_session_time_code_rate(self, tc_rate: 'SessionTimeCodeRate'):
        """
        Set session timecode rate.
        """
        op = ops.SetSessionTimeCodeRate(time_code_rate=tc_rate)
        self.client.run(op)

    def set_session_feet_frames_rate(self, ff_rate: 'SessionFeetFramesRate'):
        """
        Set session feet+frames rate.
        """
        op = ops.SetSessionFeetFramesRate(feet_frames_rate=ff_rate)
        self.client.run(op)

    def set_session_audio_rate_pull(self, pull_rate: 'SessionRatePull'):
        """
        Set session audio rate pull.
        """
        op = ops.SetSessionAudioRatePullSettings(audio_rate_pull=pull_rate)
        self.client.run(op)

    def set_session_video_rate_pull(self, pull_rate: 'SessionRatePull'):
        """
        Set session video rate pull.
        """
        op = ops.SetSessionVideoRatePullSettings(video_rate_pull=pull_rate)
        self.client.run(op)

    def set_timeline_selection(self,
                               in_time: Optional[str],
                               play_start_marker_time: Optional[str] = None,
                               out_time: Optional[str] = None,
                               pre_roll_start_time: Optional[str] = None,
                               post_roll_stop_time: Optional[str] = None,
                               pre_roll_enabled: Optional[TripleBool] = None,
                               update_video_to:
                               Optional[TimelineUpdateVideo] = None,
                               propagate_to_satellites:
                               Optional[TripleBool] = None
                               ):
        """
        Set Selection at Timecode
        """
        op = ops.SetTimelineSelection(
            play_start_marker_time=play_start_marker_time,
            in_time=in_time,
            out_time=out_time,
            pre_roll_start_time=pre_roll_start_time,
            post_roll_stop_time=post_roll_stop_time,
            pre_roll_enabled=pre_roll_enabled,
            update_video_to=update_video_to,
            propagate_to_satellites=propagate_to_satellites
        )
        self.client.run(op)

    def create_new_tracks(self,
                          number_of_tracks: Optional[int] = None,
                          track_name: Optional[str] = None,
                          track_format: Optional[TrackFormat] = None,
                          track_type: Optional[TrackType] = None,
                          track_timebase: Optional[TrackTimebase] = None
                          ):
        """
        Create new Tracks
        """
        op = ops.CreateNewTracks(number_of_tracks=number_of_tracks,
                                 track_name=track_name,
                                 track_format=track_format,
                                 track_type=track_type,
                                 track_timebase=track_timebase
                                 )
        self.client.run(op)

    def cut(self, special: Optional['AutomationDataOptions'] = None):
        """
        Execute an Edit > Cut.
        """
        if special is not None:
            op = ops.CutSpecial(automation_data_option=special)
        else:
            op = ops.Cut()

        self.client.run(op)

    def copy(self, special: Optional['AutomationDataOptions'] = None):
        """
        Execute an Edit > Copy.
        """
        if special is not None:
            op = ops.CopySpecial(automation_data_option=special)
        else:
            op = ops.Copy()

        self.client.run(op)

    def paste(self, special: Optional['PasteSpecialOptions'] = None):
        """
        Execute an Edit > Paste.
        """
        if special is not None:
            op = ops.PasteSpecial(paste_special_option=special)
        else:
            op = ops.Paste()

        self.client.run(op)

    def clear(self, special: Optional['AutomationDataOptions'] = None):
        """
        Execute an Edit > Clear.
        """
        if special is not None:
            op = ops.ClearSpecial(automation_data_option=special)
        else:
            op = ops.Clear()

        self.client.run(op)

    def refresh_target_audio_files(self, files: List[str]):
        """
        Refresh target audio files.

        :param files: A list of files to refresh.
        """
        op = ops.RefreshAllModifiedAudioFiles(file_list=files)
        self.client.run(op)

    def refresh_all_modified_audio_files(self):
        """
        Refreshes all modified audio files.
        """
        self.client.run(ops.RefreshAllModifiedAudioFiles())

    # PT 2023.9
    # TODO add remaining new methods, add proper docstrings, expose
    # remaining parameters
    # CreateNewTracks
    # GetEditMode, SetEditMode, GetEditModeOptions, SetEditModeOptions
    # GetEditTool, SetEditTool
    # RecallZoomPreset

    def select_tracks_by_name(self, names: List[str],
                              mode: Optional['SelectionMode'] = pt.SM_Replace):
        """
        Selects all tracks matching any of the passed names literally.
        """
        op = ops.SelectTracksByName(
            track_names=names, selection_mode=mode,
            pagination_request=pt.PaginationRequest(limit=1000, offset=0))

        self.client.run(op)

    def get_timeline_selection(self, format: TrackOffsetOptions = TimeCode
                               ) -> Tuple[str, str]:
        """
        Returns data about the current timeline selection.

        :returns: a Tuple of the In and Out time.
        """
        op = ops.GetTimelineSelection(time_scale=format)
        self.client.run(op)

        return (op.response.in_time, op.response.out_time)

    def get_system_delay(self) -> int:
        """
        Get the current system delay.

        :returns: the delay in samples.
        """
        op = ops.GetSessionSystemDelayInfo()
        self.client.run(op)

        return op.response.samples

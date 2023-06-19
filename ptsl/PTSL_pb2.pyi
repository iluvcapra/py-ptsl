from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

AAF_AIFF: ExportAsAAFFileType
AAF_Bit16: AAFFileBitDepth
AAF_Bit24: AAFFileBitDepth
AAF_Embedded: ExportAsAAFFileType
AAF_MXF: ExportAsAAFFileType
AAF_WAV: ExportAsAAFFileType
AIFF: ExportFileType
AddAudio: AudioOperations
All: TrackListFilter
AllTracks: TrackListType
All_Automation: AutomationDataOptions
All_Files: FileLocationTypeFilter
Audio: ImportType
AudioTrack: TrackType
Audio_Files: FileLocationTypeFilter
AuthorizeConnection: CommandId
AutoRenaming: ResolveDuplicateNamesBy
Aux: TrackType
BarsBeats: TrackOffsetOptions
BasicFolder: TrackType
Best: ConversionQuality
Better: ConversionQuality
Bit16: BitDepth
Bit24: BitDepth
Bit32Float: BitDepth
Bit_None: BitDepth
Bus: EM_SourceType
CL_ClipsList: CL_ClipLocation
CL_Timeline: CL_ClipLocation
CT_None: CompressionType
CT_PCM: CompressionType
ChordSymbols: TrackType
Clear: CommandId
ClearMemoryLocation: CommandId
ClearSpecial: CommandId
ClipGroups: ImportType
Clip_Effects: AutomationDataOptions
Clip_Gain: AutomationDataOptions
CloseSession: CommandId
CombineCrossfadedClips: FadeHandlingType
CompLane: TrackType
Completed: TaskStatus
CompletedWithBadResponse: TaskStatus
ConsolidateClip: CommandId
ConsolidateFromSourceAudio: AudioMediaOptions
ConsolidateFromSourceMedia: CopyOption
ConvertAudio: AudioOperations
Copy: CommandId
CopyAudio: AudioOperations
CopyFromSourceAudio: AudioMediaOptions
CopyFromSourceMedia: CopyOption
CopyFromSourceVideo: VideoMediaOptions
CopySpecial: CommandId
CreateFadesBasedOnPreset: CommandId
CreateMemoryLocation: CommandId
CreateSession: CommandId
Cut: CommandId
CutSpecial: CommandId
DESCRIPTOR: _descriptor.FileDescriptor
DP_EM_CodecInfo: DynamicPropertyType
DP_EM_DolbyAtmosInfo: DynamicPropertyType
DP_VT_bool: DP_ValueTypes
DP_VT_bytes: DP_ValueTypes
DP_VT_double: DP_ValueTypes
DP_VT_enum: DP_ValueTypes
DP_VT_fixed32: DP_ValueTypes
DP_VT_fixed64: DP_ValueTypes
DP_VT_float: DP_ValueTypes
DP_VT_int32: DP_ValueTypes
DP_VT_int64: DP_ValueTypes
DP_VT_object: DP_ValueTypes
DP_VT_sfixed32: DP_ValueTypes
DP_VT_sfixed64: DP_ValueTypes
DP_VT_sint32: DP_ValueTypes
DP_VT_sint64: DP_ValueTypes
DP_VT_string: DP_ValueTypes
DP_VT_uint32: DP_ValueTypes
DP_VT_uint64: DP_ValueTypes
Default: AudioOperations
DoNotImport: MainPlaylistOptions
DontShowCrossfades: FadeHandlingType
EF_Interleaved: ExportFormat
EF_Mono: ExportFormat
EF_MultipleMono: ExportFormat
EF_None: ExportFormat
EM_AIFF: EM_FileType
EM_DF_FilePerMixSource: EM_DeliveryFormat
EM_DF_None: EM_DeliveryFormat
EM_DF_SingleFile: EM_DeliveryFormat
EM_FD_Directory: EM_FileDestination
EM_FD_None: EM_FileDestination
EM_FD_SessionFolder: EM_FileDestination
EM_MOV: EM_FileType
EM_MP3: EM_FileType
EM_MXFOPAtom: EM_FileType
EM_None: EM_FileType
EM_WAV: EM_FileType
EM_WAVADM: EM_FileType
ESI_File: ESI_OutputType
ESI_String: ESI_OutputType
EditMemoryLocation: CommandId
End: SpotLocationType
ExportClipsAsFiles: CommandId
ExportMix: CommandId
ExportSelectedTracksAsAAFOMF: CommandId
ExportSessionInfoAsText: CommandId
ExtendSelectionToTargetTracks: CommandId
FT_AAF: FileType
FT_AIFF: FileType
FT_OMF: FileType
FT_WAVE: FileType
Failed: TaskStatus
FailedWithBadErrorResponse: TaskStatus
FeetFrames: TrackOffsetOptions
ForceToTargetSessionFormat: AudioMediaOptions
Frozen: TrackListFilter
GetDynamicProperties: CommandId
GetFileLocation: CommandId
GetMemoryLocations: CommandId
GetPTSLVersion: CommandId
GetPlaybackMode: CommandId
GetRecordMode: CommandId
GetSessionAudioFormat: CommandId
GetSessionAudioRatePullSettings: CommandId
GetSessionBitDepth: CommandId
GetSessionFeetFramesRate: CommandId
GetSessionInterleavedState: CommandId
GetSessionLength: CommandId
GetSessionName: CommandId
GetSessionPath: CommandId
GetSessionSampleRate: CommandId
GetSessionStartTime: CommandId
GetSessionTimeCodeRate: CommandId
GetSessionVideoRatePullSettings: CommandId
GetTaskStatus: CommandId
GetTrackList: CommandId
GetTransportArmed: CommandId
GetTransportState: CommandId
Good: ConversionQuality
Heat: TrackType
Hidden: TrackListFilter
HiddenExplicitly: TrackListFilter
HiddenImplicitly: TrackListFilter
HostReadyCheck: CommandId
IO_51DTSMix: IOSettings
IO_51FilmMix: IOSettings
IO_51SMPTEMix: IOSettings
IO_Last: IOSettings
IO_None: IOSettings
IO_StereoMix: IOSettings
IO_UserDefined: IOSettings
Import: CommandId
ImportAsOfflineSatelliteMedia: VideoMediaOptions
ImportOverlayNewOnExistingPlaylists: MainPlaylistOptions
ImportReplaceExistingPlaylists: MainPlaylistOptions
InProgress: TaskStatus
Inactive: TrackListFilter
InactiveExplicitly: TrackListFilter
InactiveImplicitly: TrackListFilter
Instrument: TrackType
KeySignature: TrackType
LinkFromSourceMedia: CopyOption
LinkToSourceAudio: AudioMediaOptions
LinkToSourceVideo: VideoMediaOptions
Locked: TrackListFilter
Low: ConversionQuality
MD_ClipList: MediaDestination
MD_MainVideoTrack: MediaDestination
MD_NewTrack: MediaDestination
MD_None: MediaDestination
MIDI: ImportType
MLR_Absolute: MemoryLocationReference
MLR_BarBeat: MemoryLocationReference
ML_None: MediaLocation
ML_Selection: MediaLocation
ML_SessionStart: MediaLocation
ML_SongStart: MediaLocation
ML_Spot: MediaLocation
MP3: ExportFileType
MT_ImportAsNewTrack: MatchTrackOptions
MT_MatchTracks: MatchTrackOptions
MT_None: MatchTrackOptions
MXF: ExportFileType
MaintainAbsoluteTimeCodeValues: TimeCodeMappingOptions
MaintainRelativeTimeCodeValues: TimeCodeMappingOptions
MapStartTimeCodeTo: TimeCodeMappingOptions
Markers: TrackType
Master: TrackType
Merge: PasteSpecialOptions
Meter: TrackType
Midi: TrackType
MinSecs: TrackOffsetOptions
Muted: TrackListFilter
None: TrackAttributeState
NotOnTimeline_Files: FileLocationTypeFilter
OS_CharactersLimit: CommandErrorType
OS_DiskSpace: CommandErrorType
OS_DuplicateName: CommandErrorType
OS_ErrorCode: CommandErrorType
OS_FilePathLocation: CommandErrorType
OS_IllegalCharacters: CommandErrorType
OS_NoFilePathFound: CommandErrorType
OS_NoLocationFound: CommandErrorType
OS_NoSessionFound: CommandErrorType
OS_ProToolsIsNotAvailable: CommandErrorType
OS_ReadError: CommandErrorType
OS_WritePermissions: CommandErrorType
Offline_Files: FileLocationTypeFilter
OnTimeline_Files: FileLocationTypeFilter
Online: TrackListFilter
Online_Files: FileLocationTypeFilter
Open: TrackListFilter
OpenSession: CommandId
Output: EM_SourceType
PM_DynamicTransport: PM_PlaybackMode
PM_Loop: PM_PlaybackMode
PM_Normal: PM_PlaybackMode
PT_CopyOptionCopy: CommandErrorType
PT_CopyOptionLink: CommandErrorType
PT_ExportAsMultichannel: CommandErrorType
PT_FileNotFound: CommandErrorType
PT_FileTypeMXF: CommandErrorType
PT_IllegalCharactersComments: CommandErrorType
PT_IllegalCharactersSequenceName: CommandErrorType
PT_InvalidParameter: CommandErrorType
PT_InvalidSelection: CommandErrorType
PT_InvalidTask: CommandErrorType
PT_MaxCharactersComments: CommandErrorType
PT_MaxCharactersSequenceName: CommandErrorType
PT_NoClipsFound: CommandErrorType
PT_NoOpenedSession: CommandErrorType
PT_NoPresetFound: CommandErrorType
PT_NoSelection: CommandErrorType
PT_NoSequenceName: CommandErrorType
PT_NoTemplate: CommandErrorType
PT_NoTemplateGroup: CommandErrorType
PT_NoTrackFound: CommandErrorType
PT_NoTracksFound: CommandErrorType
PT_NoVideoTrackFound: CommandErrorType
PT_QuantizeEdits: CommandErrorType
PT_ReadOnlySession: CommandErrorType
PT_RecordDrive: CommandErrorType
PT_SampleRateMismatch: CommandErrorType
PT_UnknownError: CommandErrorType
Pan_Automation: AutomationDataOptions
Paste: CommandId
PasteSpecial: CommandId
Pending: TaskStatus
PhysicalOut: EM_SourceType
PlayHalfSpeed: CommandId
PlugIn_Automation: AutomationDataOptions
Queued: TaskStatus
QuickTime: ExportFileType
RM_Destructive: RM_RecordMode
RM_DestructivePunch: RM_RecordMode
RM_Loop: RM_RecordMode
RM_Normal: RM_RecordMode
RM_QuickPunch: RM_RecordMode
RM_TrackPunch: RM_RecordMode
RecordHalfSpeed: CommandId
RefreshAllModifiedAudioFiles: CommandId
RefreshTargetAudioFiles: CommandId
RegisterConnection: CommandId
RenameSelectedClip: CommandId
RenameTargetClip: CommandId
RenameTargetTrack: CommandId
Rendered_Files: FileLocationTypeFilter
Repeat_To_Fill_Selection: PasteSpecialOptions
ReplacingWithNewFiles: ResolveDuplicateNamesBy
RoutingFolder: TrackType
SAF_AIFF: SessionAudioFormat
SAF_WAVE: SessionAudioFormat
SDK_NotImplemented: CommandErrorType
SDK_VersionMismatch: CommandErrorType
SFFR_Fps23976: SessionFeetFramesRate
SFFR_Fps24: SessionFeetFramesRate
SFFR_Fps25: SessionFeetFramesRate
SRP_Down01: SessionRatePull
SRP_Down4: SessionRatePull
SRP_Down4Down01: SessionRatePull
SRP_Down4Up01: SessionRatePull
SRP_None: SessionRatePull
SRP_Up01: SessionRatePull
SRP_Up4: SessionRatePull
SRP_Up4Down01: SessionRatePull
SRP_Up4Up01: SessionRatePull
SR_176400: SampleRate
SR_192000: SampleRate
SR_44100: SampleRate
SR_48000: SampleRate
SR_88200: SampleRate
SR_96000: SampleRate
SR_None: SampleRate
STCR_Fps100: SessionTimeCodeRate
STCR_Fps11988: SessionTimeCodeRate
STCR_Fps11988Drop: SessionTimeCodeRate
STCR_Fps120: SessionTimeCodeRate
STCR_Fps120Drop: SessionTimeCodeRate
STCR_Fps23976: SessionTimeCodeRate
STCR_Fps24: SessionTimeCodeRate
STCR_Fps25: SessionTimeCodeRate
STCR_Fps2997: SessionTimeCodeRate
STCR_Fps2997Drop: SessionTimeCodeRate
STCR_Fps30: SessionTimeCodeRate
STCR_Fps30Drop: SessionTimeCodeRate
STCR_Fps47952: SessionTimeCodeRate
STCR_Fps48: SessionTimeCodeRate
STCR_Fps50: SessionTimeCodeRate
STCR_Fps5994: SessionTimeCodeRate
STCR_Fps5994Drop: SessionTimeCodeRate
STCR_Fps60: SessionTimeCodeRate
STCR_Fps60Drop: SessionTimeCodeRate
Samples: TrackOffsetOptions
SaveSession: CommandId
SaveSessionAs: CommandId
SelectAllClipsOnTrack: CommandId
Selected: TrackListFilter
SelectedClipsClipsList: FileLocationTypeFilter
SelectedClipsTimeline: FileLocationTypeFilter
SelectedExplicitly: TrackListFilter
SelectedImplicitly: TrackListFilter
SelectedTracksOnly: TrackListType
Session: ImportType
SetExplicitly: TrackAttributeState
SetExplicitlyAndImplicitly: TrackAttributeState
SetImplicitly: TrackAttributeState
SetPlaybackMode: CommandId
SetRecordMode: CommandId
SetSessionAudioFormat: CommandId
SetSessionAudioRatePullSettings: CommandId
SetSessionBitDepth: CommandId
SetSessionFeetFramesRate: CommandId
SetSessionInterleavedState: CommandId
SetSessionLength: CommandId
SetSessionStartTime: CommandId
SetSessionTimeCodeRate: CommandId
SetSessionVideoRatePullSettings: CommandId
ShowCrossfades: FadeHandlingType
Spot: CommandId
Start: SpotLocationType
SyncPoint: SpotLocationType
TB_False: TripleBool
TB_None: TripleBool
TB_True: TripleBool
TP_Marker: TimeProperties
TP_None: TimeProperties
TP_Selection: TimeProperties
TS_TransportFastForward: TS_TransportState
TS_TransportIsCued: TS_TransportState
TS_TransportIsCuedForPreview: TS_TransportState
TS_TransportIsCueing: TS_TransportState
TS_TransportIsPreviewing: TS_TransportState
TS_TransportIsStopping: TS_TransportState
TS_TransportPlaying: TS_TransportState
TS_TransportPlayingHalfSpeed: TS_TransportState
TS_TransportPrimed: TS_TransportState
TS_TransportRecording: TS_TransportState
TS_TransportRecordingHalfSpeed: TS_TransportState
TS_TransportRewind: TS_TransportState
TS_TransportScrub: TS_TransportState
TS_TransportShuttle: TS_TransportState
TS_TransportStopped: TS_TransportState
Tempo: TrackType
TextEdit: TextAsFileFormat
TimeCode: TrackOffsetOptions
To_Current_Automation_Type: PasteSpecialOptions
TogglePlayState: CommandId
ToggleRecordEnable: CommandId
TrimToSelection: CommandId
TweakHead: ConversionQuality
UTF8: TextAsFileFormat
Unknown: TrackType
VE_None: EM_VideoExportOptions
VE_SameAsSource: EM_VideoExportOptions
VE_Transcode: EM_VideoExportOptions
Vca: TrackType
Video: ImportType
VideoTrack: TrackType
Video_Files: FileLocationTypeFilter
WAV: ExportFileType
WaitingForUserInput: TaskStatus
WithAutomationOnMainPlaylist: TrackListFilter
WithClipsOnMainPlaylist: TrackListFilter

class AudioData(_message.Message):
    __slots__ = ["audio_operations", "destination", "destination_path", "file_list", "location", "location_data"]
    AUDIO_OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_PATH_FIELD_NUMBER: _ClassVar[int]
    FILE_LIST_FIELD_NUMBER: _ClassVar[int]
    LOCATION_DATA_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    audio_operations: AudioOperations
    destination: MediaDestination
    destination_path: str
    file_list: _containers.RepeatedScalarFieldContainer[str]
    location: MediaLocation
    location_data: SpotLocationData
    def __init__(self, file_list: _Optional[_Iterable[str]] = ..., audio_operations: _Optional[_Union[AudioOperations, str]] = ..., destination_path: _Optional[str] = ..., destination: _Optional[_Union[MediaDestination, str]] = ..., location: _Optional[_Union[MediaLocation, str]] = ..., location_data: _Optional[_Union[SpotLocationData, _Mapping]] = ...) -> None: ...

class AuthorizeConnectionRequestBody(_message.Message):
    __slots__ = ["auth_string"]
    AUTH_STRING_FIELD_NUMBER: _ClassVar[int]
    auth_string: str
    def __init__(self, auth_string: _Optional[str] = ...) -> None: ...

class AuthorizeConnectionResponseBody(_message.Message):
    __slots__ = ["is_authorized", "message", "session_id"]
    IS_AUTHORIZED_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    is_authorized: bool
    message: str
    session_id: str
    def __init__(self, is_authorized: bool = ..., message: _Optional[str] = ..., session_id: _Optional[str] = ...) -> None: ...

class ClearMemoryLocationRequestBody(_message.Message):
    __slots__ = ["location_list"]
    LOCATION_LIST_FIELD_NUMBER: _ClassVar[int]
    location_list: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, location_list: _Optional[_Iterable[int]] = ...) -> None: ...

class ClearSpecialRequestBody(_message.Message):
    __slots__ = ["automation_data_option"]
    AUTOMATION_DATA_OPTION_FIELD_NUMBER: _ClassVar[int]
    automation_data_option: AutomationDataOptions
    def __init__(self, automation_data_option: _Optional[_Union[AutomationDataOptions, str]] = ...) -> None: ...

class ClipGroupsData(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class CloseSessionRequestBody(_message.Message):
    __slots__ = ["save_on_close"]
    SAVE_ON_CLOSE_FIELD_NUMBER: _ClassVar[int]
    save_on_close: bool
    def __init__(self, save_on_close: bool = ...) -> None: ...

class CommandError(_message.Message):
    __slots__ = ["command_error_message", "command_error_type", "is_warning"]
    COMMAND_ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    COMMAND_ERROR_TYPE_FIELD_NUMBER: _ClassVar[int]
    IS_WARNING_FIELD_NUMBER: _ClassVar[int]
    command_error_message: str
    command_error_type: CommandErrorType
    is_warning: bool
    def __init__(self, command_error_type: _Optional[_Union[CommandErrorType, str]] = ..., command_error_message: _Optional[str] = ..., is_warning: bool = ...) -> None: ...

class CopySpecialRequestBody(_message.Message):
    __slots__ = ["automation_data_option"]
    AUTOMATION_DATA_OPTION_FIELD_NUMBER: _ClassVar[int]
    automation_data_option: AutomationDataOptions
    def __init__(self, automation_data_option: _Optional[_Union[AutomationDataOptions, str]] = ...) -> None: ...

class CreateFadesBasedOnPresetRequestBody(_message.Message):
    __slots__ = ["auto_adjust_bounds", "fade_preset_name"]
    AUTO_ADJUST_BOUNDS_FIELD_NUMBER: _ClassVar[int]
    FADE_PRESET_NAME_FIELD_NUMBER: _ClassVar[int]
    auto_adjust_bounds: bool
    fade_preset_name: str
    def __init__(self, fade_preset_name: _Optional[str] = ..., auto_adjust_bounds: bool = ...) -> None: ...

class CreateFadesBasedOnPresetResponseBody(_message.Message):
    __slots__ = ["fade_preset_name"]
    FADE_PRESET_NAME_FIELD_NUMBER: _ClassVar[int]
    fade_preset_name: str
    def __init__(self, fade_preset_name: _Optional[str] = ...) -> None: ...

class CreateMemoryLocationRequestBody(_message.Message):
    __slots__ = ["comments", "end_time", "general_properties", "name", "number", "reference", "start_time", "time_properties"]
    COMMENTS_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    GENERAL_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    TIME_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    comments: str
    end_time: str
    general_properties: MemoryLocationProperties
    name: str
    number: int
    reference: MemoryLocationReference
    start_time: str
    time_properties: TimeProperties
    def __init__(self, number: _Optional[int] = ..., name: _Optional[str] = ..., start_time: _Optional[str] = ..., end_time: _Optional[str] = ..., time_properties: _Optional[_Union[TimeProperties, str]] = ..., reference: _Optional[_Union[MemoryLocationReference, str]] = ..., general_properties: _Optional[_Union[MemoryLocationProperties, _Mapping]] = ..., comments: _Optional[str] = ...) -> None: ...

class CreateMemoryLocationResponseBody(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class CreateSessionRequestBody(_message.Message):
    __slots__ = ["bit_depth", "create_from_aaf", "create_from_template", "file_type", "input_output_settings", "is_cloud_project", "is_interleaved", "path_to_aaf", "sample_rate", "session_location", "session_name", "template_group", "template_name"]
    BIT_DEPTH_FIELD_NUMBER: _ClassVar[int]
    CREATE_FROM_AAF_FIELD_NUMBER: _ClassVar[int]
    CREATE_FROM_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    FILE_TYPE_FIELD_NUMBER: _ClassVar[int]
    INPUT_OUTPUT_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    IS_CLOUD_PROJECT_FIELD_NUMBER: _ClassVar[int]
    IS_INTERLEAVED_FIELD_NUMBER: _ClassVar[int]
    PATH_TO_AAF_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_RATE_FIELD_NUMBER: _ClassVar[int]
    SESSION_LOCATION_FIELD_NUMBER: _ClassVar[int]
    SESSION_NAME_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_GROUP_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_NAME_FIELD_NUMBER: _ClassVar[int]
    bit_depth: BitDepth
    create_from_aaf: bool
    create_from_template: bool
    file_type: FileType
    input_output_settings: IOSettings
    is_cloud_project: bool
    is_interleaved: bool
    path_to_aaf: str
    sample_rate: SampleRate
    session_location: str
    session_name: str
    template_group: str
    template_name: str
    def __init__(self, session_name: _Optional[str] = ..., create_from_template: bool = ..., template_group: _Optional[str] = ..., template_name: _Optional[str] = ..., file_type: _Optional[_Union[FileType, str]] = ..., sample_rate: _Optional[_Union[SampleRate, str]] = ..., input_output_settings: _Optional[_Union[IOSettings, str]] = ..., is_interleaved: bool = ..., session_location: _Optional[str] = ..., is_cloud_project: bool = ..., create_from_aaf: bool = ..., path_to_aaf: _Optional[str] = ..., bit_depth: _Optional[_Union[BitDepth, str]] = ...) -> None: ...

class CutSpecialRequestBody(_message.Message):
    __slots__ = ["automation_data_option"]
    AUTOMATION_DATA_OPTION_FIELD_NUMBER: _ClassVar[int]
    automation_data_option: AutomationDataOptions
    def __init__(self, automation_data_option: _Optional[_Union[AutomationDataOptions, str]] = ...) -> None: ...

class EM_AudioInfo(_message.Message):
    __slots__ = ["bit_depth", "compression_type", "delivery_format", "export_format", "pad_to_frame_boundary", "sample_rate"]
    BIT_DEPTH_FIELD_NUMBER: _ClassVar[int]
    COMPRESSION_TYPE_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_FORMAT_FIELD_NUMBER: _ClassVar[int]
    EXPORT_FORMAT_FIELD_NUMBER: _ClassVar[int]
    PAD_TO_FRAME_BOUNDARY_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_RATE_FIELD_NUMBER: _ClassVar[int]
    bit_depth: BitDepth
    compression_type: CompressionType
    delivery_format: EM_DeliveryFormat
    export_format: ExportFormat
    pad_to_frame_boundary: TripleBool
    sample_rate: SampleRate
    def __init__(self, compression_type: _Optional[_Union[CompressionType, str]] = ..., export_format: _Optional[_Union[ExportFormat, str]] = ..., bit_depth: _Optional[_Union[BitDepth, str]] = ..., sample_rate: _Optional[_Union[SampleRate, str]] = ..., pad_to_frame_boundary: _Optional[_Union[TripleBool, str]] = ..., delivery_format: _Optional[_Union[EM_DeliveryFormat, str]] = ...) -> None: ...

class EM_CodecInfo(_message.Message):
    __slots__ = ["codec_name", "property_list"]
    CODEC_NAME_FIELD_NUMBER: _ClassVar[int]
    PROPERTY_LIST_FIELD_NUMBER: _ClassVar[int]
    codec_name: str
    property_list: _containers.RepeatedCompositeFieldContainer[PropertyContainer]
    def __init__(self, codec_name: _Optional[str] = ..., property_list: _Optional[_Iterable[_Union[PropertyContainer, _Mapping]]] = ...) -> None: ...

class EM_DolbyAtmosInfo(_message.Message):
    __slots__ = ["add_first_frame_of_action", "frame_rate", "property_list", "timecode_value"]
    ADD_FIRST_FRAME_OF_ACTION_FIELD_NUMBER: _ClassVar[int]
    FRAME_RATE_FIELD_NUMBER: _ClassVar[int]
    PROPERTY_LIST_FIELD_NUMBER: _ClassVar[int]
    TIMECODE_VALUE_FIELD_NUMBER: _ClassVar[int]
    add_first_frame_of_action: TripleBool
    frame_rate: int
    property_list: _containers.RepeatedCompositeFieldContainer[PropertyContainer]
    timecode_value: str
    def __init__(self, add_first_frame_of_action: _Optional[_Union[TripleBool, str]] = ..., timecode_value: _Optional[str] = ..., frame_rate: _Optional[int] = ..., property_list: _Optional[_Iterable[_Union[PropertyContainer, _Mapping]]] = ...) -> None: ...

class EM_ImportOptions(_message.Message):
    __slots__ = ["clear_destination_video_track_playlist", "gaps_between_clips", "import_audio_from_file", "import_destination", "import_location", "remove_existing_video_clips", "remove_existing_video_tracks"]
    CLEAR_DESTINATION_VIDEO_TRACK_PLAYLIST_FIELD_NUMBER: _ClassVar[int]
    GAPS_BETWEEN_CLIPS_FIELD_NUMBER: _ClassVar[int]
    IMPORT_AUDIO_FROM_FILE_FIELD_NUMBER: _ClassVar[int]
    IMPORT_DESTINATION_FIELD_NUMBER: _ClassVar[int]
    IMPORT_LOCATION_FIELD_NUMBER: _ClassVar[int]
    REMOVE_EXISTING_VIDEO_CLIPS_FIELD_NUMBER: _ClassVar[int]
    REMOVE_EXISTING_VIDEO_TRACKS_FIELD_NUMBER: _ClassVar[int]
    clear_destination_video_track_playlist: TripleBool
    gaps_between_clips: int
    import_audio_from_file: TripleBool
    import_destination: MediaDestination
    import_location: MediaLocation
    remove_existing_video_clips: TripleBool
    remove_existing_video_tracks: TripleBool
    def __init__(self, import_destination: _Optional[_Union[MediaDestination, str]] = ..., import_location: _Optional[_Union[MediaLocation, str]] = ..., gaps_between_clips: _Optional[int] = ..., import_audio_from_file: _Optional[_Union[TripleBool, str]] = ..., remove_existing_video_tracks: _Optional[_Union[TripleBool, str]] = ..., remove_existing_video_clips: _Optional[_Union[TripleBool, str]] = ..., clear_destination_video_track_playlist: _Optional[_Union[TripleBool, str]] = ...) -> None: ...

class EM_LocationInfo(_message.Message):
    __slots__ = ["directory", "file_destination", "import_after_bounce", "import_options"]
    DIRECTORY_FIELD_NUMBER: _ClassVar[int]
    FILE_DESTINATION_FIELD_NUMBER: _ClassVar[int]
    IMPORT_AFTER_BOUNCE_FIELD_NUMBER: _ClassVar[int]
    IMPORT_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    directory: str
    file_destination: EM_FileDestination
    import_after_bounce: TripleBool
    import_options: EM_ImportOptions
    def __init__(self, import_after_bounce: _Optional[_Union[TripleBool, str]] = ..., import_options: _Optional[_Union[EM_ImportOptions, _Mapping]] = ..., file_destination: _Optional[_Union[EM_FileDestination, str]] = ..., directory: _Optional[str] = ...) -> None: ...

class EM_SourceInfo(_message.Message):
    __slots__ = ["name", "source_type"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    name: str
    source_type: EM_SourceType
    def __init__(self, source_type: _Optional[_Union[EM_SourceType, str]] = ..., name: _Optional[str] = ...) -> None: ...

class EM_VideoInfo(_message.Message):
    __slots__ = ["codec_info", "export_option", "include_video", "replace_timecode_track"]
    CODEC_INFO_FIELD_NUMBER: _ClassVar[int]
    EXPORT_OPTION_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_VIDEO_FIELD_NUMBER: _ClassVar[int]
    REPLACE_TIMECODE_TRACK_FIELD_NUMBER: _ClassVar[int]
    codec_info: EM_CodecInfo
    export_option: EM_VideoExportOptions
    include_video: TripleBool
    replace_timecode_track: TripleBool
    def __init__(self, include_video: _Optional[_Union[TripleBool, str]] = ..., export_option: _Optional[_Union[EM_VideoExportOptions, str]] = ..., replace_timecode_track: _Optional[_Union[TripleBool, str]] = ..., codec_info: _Optional[_Union[EM_CodecInfo, _Mapping]] = ...) -> None: ...

class EditMemoryLocationRequestBody(_message.Message):
    __slots__ = ["comments", "end_time", "general_properties", "name", "number", "reference", "start_time", "time_properties"]
    COMMENTS_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    GENERAL_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    TIME_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    comments: str
    end_time: str
    general_properties: MemoryLocationProperties
    name: str
    number: int
    reference: MemoryLocationReference
    start_time: str
    time_properties: TimeProperties
    def __init__(self, number: _Optional[int] = ..., name: _Optional[str] = ..., start_time: _Optional[str] = ..., end_time: _Optional[str] = ..., time_properties: _Optional[_Union[TimeProperties, str]] = ..., reference: _Optional[_Union[MemoryLocationReference, str]] = ..., general_properties: _Optional[_Union[MemoryLocationProperties, _Mapping]] = ..., comments: _Optional[str] = ...) -> None: ...

class EditMemoryLocationResponseBody(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class EmptyMessage(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExportClipsAsFilesRequestBody(_message.Message):
    __slots__ = ["bit_depth", "duplicate_names", "enforce_avid_compatibility", "file_path", "file_type", "format"]
    BIT_DEPTH_FIELD_NUMBER: _ClassVar[int]
    DUPLICATE_NAMES_FIELD_NUMBER: _ClassVar[int]
    ENFORCE_AVID_COMPATIBILITY_FIELD_NUMBER: _ClassVar[int]
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    FILE_TYPE_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    bit_depth: BitDepth
    duplicate_names: ResolveDuplicateNamesBy
    enforce_avid_compatibility: bool
    file_path: str
    file_type: ExportFileType
    format: ExportFormat
    def __init__(self, file_path: _Optional[str] = ..., format: _Optional[_Union[ExportFormat, str]] = ..., file_type: _Optional[_Union[ExportFileType, str]] = ..., bit_depth: _Optional[_Union[BitDepth, str]] = ..., duplicate_names: _Optional[_Union[ResolveDuplicateNamesBy, str]] = ..., enforce_avid_compatibility: bool = ...) -> None: ...

class ExportMixRequestBody(_message.Message):
    __slots__ = ["audio_info", "dolby_atmos_info", "file_name", "file_type", "files_list", "location_info", "mix_source_list", "offline_bounce", "preset_path", "video_info"]
    AUDIO_INFO_FIELD_NUMBER: _ClassVar[int]
    DOLBY_ATMOS_INFO_FIELD_NUMBER: _ClassVar[int]
    FILES_LIST_FIELD_NUMBER: _ClassVar[int]
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    FILE_TYPE_FIELD_NUMBER: _ClassVar[int]
    LOCATION_INFO_FIELD_NUMBER: _ClassVar[int]
    MIX_SOURCE_LIST_FIELD_NUMBER: _ClassVar[int]
    OFFLINE_BOUNCE_FIELD_NUMBER: _ClassVar[int]
    PRESET_PATH_FIELD_NUMBER: _ClassVar[int]
    VIDEO_INFO_FIELD_NUMBER: _ClassVar[int]
    audio_info: EM_AudioInfo
    dolby_atmos_info: EM_DolbyAtmosInfo
    file_name: str
    file_type: EM_FileType
    files_list: _containers.RepeatedCompositeFieldContainer[EM_SourceInfo]
    location_info: EM_LocationInfo
    mix_source_list: _containers.RepeatedCompositeFieldContainer[EM_SourceInfo]
    offline_bounce: TripleBool
    preset_path: str
    video_info: EM_VideoInfo
    def __init__(self, preset_path: _Optional[str] = ..., file_name: _Optional[str] = ..., file_type: _Optional[_Union[EM_FileType, str]] = ..., files_list: _Optional[_Iterable[_Union[EM_SourceInfo, _Mapping]]] = ..., audio_info: _Optional[_Union[EM_AudioInfo, _Mapping]] = ..., video_info: _Optional[_Union[EM_VideoInfo, _Mapping]] = ..., location_info: _Optional[_Union[EM_LocationInfo, _Mapping]] = ..., dolby_atmos_info: _Optional[_Union[EM_DolbyAtmosInfo, _Mapping]] = ..., offline_bounce: _Optional[_Union[TripleBool, str]] = ..., mix_source_list: _Optional[_Iterable[_Union[EM_SourceInfo, _Mapping]]] = ...) -> None: ...

class ExportSelectedTracksAsAAFOMFRequestBody(_message.Message):
    __slots__ = ["asset_file_location", "bit_depth", "comments", "container_file_location", "container_file_name", "copy_option", "enforce_media_composer_compatibility", "export_stereo_as_multichannel", "file_type", "quantize_edits_to_frame_boundaries", "sequence_name"]
    ASSET_FILE_LOCATION_FIELD_NUMBER: _ClassVar[int]
    BIT_DEPTH_FIELD_NUMBER: _ClassVar[int]
    COMMENTS_FIELD_NUMBER: _ClassVar[int]
    CONTAINER_FILE_LOCATION_FIELD_NUMBER: _ClassVar[int]
    CONTAINER_FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    COPY_OPTION_FIELD_NUMBER: _ClassVar[int]
    ENFORCE_MEDIA_COMPOSER_COMPATIBILITY_FIELD_NUMBER: _ClassVar[int]
    EXPORT_STEREO_AS_MULTICHANNEL_FIELD_NUMBER: _ClassVar[int]
    FILE_TYPE_FIELD_NUMBER: _ClassVar[int]
    QUANTIZE_EDITS_TO_FRAME_BOUNDARIES_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_NAME_FIELD_NUMBER: _ClassVar[int]
    asset_file_location: str
    bit_depth: AAFFileBitDepth
    comments: str
    container_file_location: str
    container_file_name: str
    copy_option: CopyOption
    enforce_media_composer_compatibility: bool
    export_stereo_as_multichannel: bool
    file_type: ExportAsAAFFileType
    quantize_edits_to_frame_boundaries: bool
    sequence_name: str
    def __init__(self, file_type: _Optional[_Union[ExportAsAAFFileType, str]] = ..., bit_depth: _Optional[_Union[AAFFileBitDepth, str]] = ..., copy_option: _Optional[_Union[CopyOption, str]] = ..., enforce_media_composer_compatibility: bool = ..., quantize_edits_to_frame_boundaries: bool = ..., export_stereo_as_multichannel: bool = ..., container_file_name: _Optional[str] = ..., container_file_location: _Optional[str] = ..., asset_file_location: _Optional[str] = ..., comments: _Optional[str] = ..., sequence_name: _Optional[str] = ...) -> None: ...

class ExportSessionInfoAsTextRequestBody(_message.Message):
    __slots__ = ["fade_handling_type", "include_clip_list", "include_file_list", "include_markers", "include_plugin_list", "include_track_edls", "include_user_timestamps", "output_path", "output_type", "show_sub_frames", "text_as_file_format", "track_list_type", "track_offset_options"]
    FADE_HANDLING_TYPE_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_CLIP_LIST_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_FILE_LIST_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_MARKERS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_PLUGIN_LIST_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_TRACK_EDLS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_USER_TIMESTAMPS_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_PATH_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_TYPE_FIELD_NUMBER: _ClassVar[int]
    SHOW_SUB_FRAMES_FIELD_NUMBER: _ClassVar[int]
    TEXT_AS_FILE_FORMAT_FIELD_NUMBER: _ClassVar[int]
    TRACK_LIST_TYPE_FIELD_NUMBER: _ClassVar[int]
    TRACK_OFFSET_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    fade_handling_type: FadeHandlingType
    include_clip_list: bool
    include_file_list: bool
    include_markers: bool
    include_plugin_list: bool
    include_track_edls: bool
    include_user_timestamps: bool
    output_path: str
    output_type: ESI_OutputType
    show_sub_frames: bool
    text_as_file_format: TextAsFileFormat
    track_list_type: TrackListType
    track_offset_options: TrackOffsetOptions
    def __init__(self, include_file_list: bool = ..., include_clip_list: bool = ..., include_markers: bool = ..., include_plugin_list: bool = ..., include_track_edls: bool = ..., show_sub_frames: bool = ..., include_user_timestamps: bool = ..., track_list_type: _Optional[_Union[TrackListType, str]] = ..., fade_handling_type: _Optional[_Union[FadeHandlingType, str]] = ..., track_offset_options: _Optional[_Union[TrackOffsetOptions, str]] = ..., text_as_file_format: _Optional[_Union[TextAsFileFormat, str]] = ..., output_type: _Optional[_Union[ESI_OutputType, str]] = ..., output_path: _Optional[str] = ...) -> None: ...

class ExportSessionInfoAsTextResponseBody(_message.Message):
    __slots__ = ["session_info"]
    SESSION_INFO_FIELD_NUMBER: _ClassVar[int]
    session_info: str
    def __init__(self, session_info: _Optional[str] = ...) -> None: ...

class ExtendSelectionToTargetTracksRequestBody(_message.Message):
    __slots__ = ["tracks_to_extend_to"]
    TRACKS_TO_EXTEND_TO_FIELD_NUMBER: _ClassVar[int]
    tracks_to_extend_to: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, tracks_to_extend_to: _Optional[_Iterable[str]] = ...) -> None: ...

class ExtendSelectionToTargetTracksResponseBody(_message.Message):
    __slots__ = ["tracks_to_extend_to"]
    TRACKS_TO_EXTEND_TO_FIELD_NUMBER: _ClassVar[int]
    tracks_to_extend_to: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, tracks_to_extend_to: _Optional[_Iterable[str]] = ...) -> None: ...

class FileLocation(_message.Message):
    __slots__ = ["info", "path"]
    INFO_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    info: FileLocationInfo
    path: str
    def __init__(self, path: _Optional[str] = ..., info: _Optional[_Union[FileLocationInfo, _Mapping]] = ...) -> None: ...

class FileLocationInfo(_message.Message):
    __slots__ = ["is_online"]
    IS_ONLINE_FIELD_NUMBER: _ClassVar[int]
    is_online: bool
    def __init__(self, is_online: bool = ...) -> None: ...

class GetDynamicPropertiesGroup(_message.Message):
    __slots__ = ["key_list", "property_list"]
    KEY_LIST_FIELD_NUMBER: _ClassVar[int]
    PROPERTY_LIST_FIELD_NUMBER: _ClassVar[int]
    key_list: _containers.RepeatedCompositeFieldContainer[PropertyContainer]
    property_list: _containers.RepeatedCompositeFieldContainer[PropertyDescriptor]
    def __init__(self, key_list: _Optional[_Iterable[_Union[PropertyContainer, _Mapping]]] = ..., property_list: _Optional[_Iterable[_Union[PropertyDescriptor, _Mapping]]] = ...) -> None: ...

class GetDynamicPropertiesRequestBody(_message.Message):
    __slots__ = ["property_type"]
    PROPERTY_TYPE_FIELD_NUMBER: _ClassVar[int]
    property_type: DynamicPropertyType
    def __init__(self, property_type: _Optional[_Union[DynamicPropertyType, str]] = ...) -> None: ...

class GetDynamicPropertiesResponseBody(_message.Message):
    __slots__ = ["group_list", "property_type"]
    GROUP_LIST_FIELD_NUMBER: _ClassVar[int]
    PROPERTY_TYPE_FIELD_NUMBER: _ClassVar[int]
    group_list: _containers.RepeatedCompositeFieldContainer[GetDynamicPropertiesGroup]
    property_type: DynamicPropertyType
    def __init__(self, property_type: _Optional[_Union[DynamicPropertyType, str]] = ..., group_list: _Optional[_Iterable[_Union[GetDynamicPropertiesGroup, _Mapping]]] = ...) -> None: ...

class GetFileLocationRequestBody(_message.Message):
    __slots__ = ["file_filters", "page_limit"]
    FILE_FILTERS_FIELD_NUMBER: _ClassVar[int]
    PAGE_LIMIT_FIELD_NUMBER: _ClassVar[int]
    file_filters: _containers.RepeatedScalarFieldContainer[FileLocationTypeFilter]
    page_limit: int
    def __init__(self, page_limit: _Optional[int] = ..., file_filters: _Optional[_Iterable[_Union[FileLocationTypeFilter, str]]] = ...) -> None: ...

class GetFileLocationResponseBody(_message.Message):
    __slots__ = ["file_locations", "stats"]
    FILE_LOCATIONS_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    file_locations: _containers.RepeatedCompositeFieldContainer[FileLocation]
    stats: Pagination
    def __init__(self, stats: _Optional[_Union[Pagination, _Mapping]] = ..., file_locations: _Optional[_Iterable[_Union[FileLocation, _Mapping]]] = ...) -> None: ...

class GetMemoryLocationsRequestBody(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetMemoryLocationsResponseBody(_message.Message):
    __slots__ = ["memory_locations"]
    MEMORY_LOCATIONS_FIELD_NUMBER: _ClassVar[int]
    memory_locations: _containers.RepeatedCompositeFieldContainer[MemoryLocation]
    def __init__(self, memory_locations: _Optional[_Iterable[_Union[MemoryLocation, _Mapping]]] = ...) -> None: ...

class GetPTSLVersionResponseBody(_message.Message):
    __slots__ = ["version"]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    version: int
    def __init__(self, version: _Optional[int] = ...) -> None: ...

class GetPlaybackModeResponseBody(_message.Message):
    __slots__ = ["current_settings", "possible_settings"]
    CURRENT_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    POSSIBLE_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    current_settings: _containers.RepeatedScalarFieldContainer[PM_PlaybackMode]
    possible_settings: _containers.RepeatedScalarFieldContainer[PM_PlaybackMode]
    def __init__(self, current_settings: _Optional[_Iterable[_Union[PM_PlaybackMode, str]]] = ..., possible_settings: _Optional[_Iterable[_Union[PM_PlaybackMode, str]]] = ...) -> None: ...

class GetRecordModeResponseBody(_message.Message):
    __slots__ = ["current_setting", "possible_settings"]
    CURRENT_SETTING_FIELD_NUMBER: _ClassVar[int]
    POSSIBLE_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    current_setting: RM_RecordMode
    possible_settings: _containers.RepeatedScalarFieldContainer[RM_RecordMode]
    def __init__(self, current_setting: _Optional[_Union[RM_RecordMode, str]] = ..., possible_settings: _Optional[_Iterable[_Union[RM_RecordMode, str]]] = ...) -> None: ...

class GetSessionAudioFormatResponseBody(_message.Message):
    __slots__ = ["current_setting", "possible_settings"]
    CURRENT_SETTING_FIELD_NUMBER: _ClassVar[int]
    POSSIBLE_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    current_setting: SessionAudioFormat
    possible_settings: _containers.RepeatedScalarFieldContainer[SessionAudioFormat]
    def __init__(self, current_setting: _Optional[_Union[SessionAudioFormat, str]] = ..., possible_settings: _Optional[_Iterable[_Union[SessionAudioFormat, str]]] = ...) -> None: ...

class GetSessionAudioRatePullSettingsResponseBody(_message.Message):
    __slots__ = ["current_setting", "possible_settings"]
    CURRENT_SETTING_FIELD_NUMBER: _ClassVar[int]
    POSSIBLE_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    current_setting: SessionRatePull
    possible_settings: _containers.RepeatedScalarFieldContainer[SessionRatePull]
    def __init__(self, current_setting: _Optional[_Union[SessionRatePull, str]] = ..., possible_settings: _Optional[_Iterable[_Union[SessionRatePull, str]]] = ...) -> None: ...

class GetSessionBitDepthResponseBody(_message.Message):
    __slots__ = ["current_setting", "possible_settings"]
    CURRENT_SETTING_FIELD_NUMBER: _ClassVar[int]
    POSSIBLE_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    current_setting: BitDepth
    possible_settings: _containers.RepeatedScalarFieldContainer[BitDepth]
    def __init__(self, current_setting: _Optional[_Union[BitDepth, str]] = ..., possible_settings: _Optional[_Iterable[_Union[BitDepth, str]]] = ...) -> None: ...

class GetSessionFeetFramesRateResponseBody(_message.Message):
    __slots__ = ["current_setting", "possible_settings"]
    CURRENT_SETTING_FIELD_NUMBER: _ClassVar[int]
    POSSIBLE_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    current_setting: SessionFeetFramesRate
    possible_settings: _containers.RepeatedScalarFieldContainer[SessionFeetFramesRate]
    def __init__(self, current_setting: _Optional[_Union[SessionFeetFramesRate, str]] = ..., possible_settings: _Optional[_Iterable[_Union[SessionFeetFramesRate, str]]] = ...) -> None: ...

class GetSessionInterleavedStateResponseBody(_message.Message):
    __slots__ = ["current_setting", "possible_settings"]
    CURRENT_SETTING_FIELD_NUMBER: _ClassVar[int]
    POSSIBLE_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    current_setting: bool
    possible_settings: _containers.RepeatedScalarFieldContainer[bool]
    def __init__(self, current_setting: bool = ..., possible_settings: _Optional[_Iterable[bool]] = ...) -> None: ...

class GetSessionLengthResponseBody(_message.Message):
    __slots__ = ["session_length"]
    SESSION_LENGTH_FIELD_NUMBER: _ClassVar[int]
    session_length: str
    def __init__(self, session_length: _Optional[str] = ...) -> None: ...

class GetSessionNameResponseBody(_message.Message):
    __slots__ = ["session_name"]
    SESSION_NAME_FIELD_NUMBER: _ClassVar[int]
    session_name: str
    def __init__(self, session_name: _Optional[str] = ...) -> None: ...

class GetSessionPathResponseBody(_message.Message):
    __slots__ = ["session_path"]
    SESSION_PATH_FIELD_NUMBER: _ClassVar[int]
    session_path: FileLocation
    def __init__(self, session_path: _Optional[_Union[FileLocation, _Mapping]] = ...) -> None: ...

class GetSessionSampleRateResponseBody(_message.Message):
    __slots__ = ["sample_rate"]
    SAMPLE_RATE_FIELD_NUMBER: _ClassVar[int]
    sample_rate: SampleRate
    def __init__(self, sample_rate: _Optional[_Union[SampleRate, str]] = ...) -> None: ...

class GetSessionStartTimeResponseBody(_message.Message):
    __slots__ = ["session_start_time"]
    SESSION_START_TIME_FIELD_NUMBER: _ClassVar[int]
    session_start_time: str
    def __init__(self, session_start_time: _Optional[str] = ...) -> None: ...

class GetSessionTimeCodeRateResponseBody(_message.Message):
    __slots__ = ["current_setting", "possible_settings"]
    CURRENT_SETTING_FIELD_NUMBER: _ClassVar[int]
    POSSIBLE_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    current_setting: SessionTimeCodeRate
    possible_settings: _containers.RepeatedScalarFieldContainer[SessionTimeCodeRate]
    def __init__(self, current_setting: _Optional[_Union[SessionTimeCodeRate, str]] = ..., possible_settings: _Optional[_Iterable[_Union[SessionTimeCodeRate, str]]] = ...) -> None: ...

class GetSessionVideoRatePullSettingsResponseBody(_message.Message):
    __slots__ = ["current_setting", "possible_settings"]
    CURRENT_SETTING_FIELD_NUMBER: _ClassVar[int]
    POSSIBLE_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    current_setting: SessionRatePull
    possible_settings: _containers.RepeatedScalarFieldContainer[SessionRatePull]
    def __init__(self, current_setting: _Optional[_Union[SessionRatePull, str]] = ..., possible_settings: _Optional[_Iterable[_Union[SessionRatePull, str]]] = ...) -> None: ...

class GetTaskStatusRequestBody(_message.Message):
    __slots__ = ["task_id"]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    task_id: str
    def __init__(self, task_id: _Optional[str] = ...) -> None: ...

class GetTaskStatusResponseBody(_message.Message):
    __slots__ = ["progress", "status", "task_id"]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    progress: int
    status: TaskStatus
    task_id: str
    def __init__(self, task_id: _Optional[str] = ..., status: _Optional[_Union[TaskStatus, str]] = ..., progress: _Optional[int] = ...) -> None: ...

class GetTrackListRequestBody(_message.Message):
    __slots__ = ["is_filter_list_additive", "page_limit", "track_filter_list"]
    IS_FILTER_LIST_ADDITIVE_FIELD_NUMBER: _ClassVar[int]
    PAGE_LIMIT_FIELD_NUMBER: _ClassVar[int]
    TRACK_FILTER_LIST_FIELD_NUMBER: _ClassVar[int]
    is_filter_list_additive: bool
    page_limit: int
    track_filter_list: _containers.RepeatedCompositeFieldContainer[TrackListInvertibleFilter]
    def __init__(self, page_limit: _Optional[int] = ..., track_filter_list: _Optional[_Iterable[_Union[TrackListInvertibleFilter, _Mapping]]] = ..., is_filter_list_additive: bool = ...) -> None: ...

class GetTrackListResponseBody(_message.Message):
    __slots__ = ["stats", "track_list"]
    STATS_FIELD_NUMBER: _ClassVar[int]
    TRACK_LIST_FIELD_NUMBER: _ClassVar[int]
    stats: Pagination
    track_list: _containers.RepeatedCompositeFieldContainer[Track]
    def __init__(self, stats: _Optional[_Union[Pagination, _Mapping]] = ..., track_list: _Optional[_Iterable[_Union[Track, _Mapping]]] = ...) -> None: ...

class GetTransportArmedResponseBody(_message.Message):
    __slots__ = ["is_transport_armed"]
    IS_TRANSPORT_ARMED_FIELD_NUMBER: _ClassVar[int]
    is_transport_armed: bool
    def __init__(self, is_transport_armed: bool = ...) -> None: ...

class GetTransportStateResponseBody(_message.Message):
    __slots__ = ["current_setting", "possible_settings"]
    CURRENT_SETTING_FIELD_NUMBER: _ClassVar[int]
    POSSIBLE_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    current_setting: TS_TransportState
    possible_settings: _containers.RepeatedScalarFieldContainer[TS_TransportState]
    def __init__(self, current_setting: _Optional[_Union[TS_TransportState, str]] = ..., possible_settings: _Optional[_Iterable[_Union[TS_TransportState, str]]] = ...) -> None: ...

class ImportRequestBody(_message.Message):
    __slots__ = ["audio_data", "import_type", "session_data", "session_path"]
    AUDIO_DATA_FIELD_NUMBER: _ClassVar[int]
    IMPORT_TYPE_FIELD_NUMBER: _ClassVar[int]
    SESSION_DATA_FIELD_NUMBER: _ClassVar[int]
    SESSION_PATH_FIELD_NUMBER: _ClassVar[int]
    audio_data: AudioData
    import_type: ImportType
    session_data: SessionData
    session_path: str
    def __init__(self, session_path: _Optional[str] = ..., import_type: _Optional[_Union[ImportType, str]] = ..., session_data: _Optional[_Union[SessionData, _Mapping]] = ..., audio_data: _Optional[_Union[AudioData, _Mapping]] = ...) -> None: ...

class ImportResponseBody(_message.Message):
    __slots__ = ["audio_operations", "destination_path", "file_list"]
    AUDIO_OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_PATH_FIELD_NUMBER: _ClassVar[int]
    FILE_LIST_FIELD_NUMBER: _ClassVar[int]
    audio_operations: AudioOperations
    destination_path: str
    file_list: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, file_list: _Optional[_Iterable[str]] = ..., audio_operations: _Optional[_Union[AudioOperations, str]] = ..., destination_path: _Optional[str] = ...) -> None: ...

class MemoryLocation(_message.Message):
    __slots__ = ["comments", "end_time", "general_properties", "name", "number", "reference", "start_time", "time_properties"]
    COMMENTS_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    GENERAL_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    TIME_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    comments: str
    end_time: str
    general_properties: MemoryLocationProperties
    name: str
    number: int
    reference: MemoryLocationReference
    start_time: str
    time_properties: TimeProperties
    def __init__(self, number: _Optional[int] = ..., name: _Optional[str] = ..., start_time: _Optional[str] = ..., end_time: _Optional[str] = ..., time_properties: _Optional[_Union[TimeProperties, str]] = ..., reference: _Optional[_Union[MemoryLocationReference, str]] = ..., general_properties: _Optional[_Union[MemoryLocationProperties, _Mapping]] = ..., comments: _Optional[str] = ...) -> None: ...

class MemoryLocationProperties(_message.Message):
    __slots__ = ["group_enables", "pre_post_roll_times", "track_heights", "track_visibility", "window_configuration", "window_configuration_index", "window_configuration_name", "zoom_settings"]
    GROUP_ENABLES_FIELD_NUMBER: _ClassVar[int]
    PRE_POST_ROLL_TIMES_FIELD_NUMBER: _ClassVar[int]
    TRACK_HEIGHTS_FIELD_NUMBER: _ClassVar[int]
    TRACK_VISIBILITY_FIELD_NUMBER: _ClassVar[int]
    WINDOW_CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    WINDOW_CONFIGURATION_INDEX_FIELD_NUMBER: _ClassVar[int]
    WINDOW_CONFIGURATION_NAME_FIELD_NUMBER: _ClassVar[int]
    ZOOM_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    group_enables: bool
    pre_post_roll_times: bool
    track_heights: bool
    track_visibility: bool
    window_configuration: bool
    window_configuration_index: int
    window_configuration_name: str
    zoom_settings: bool
    def __init__(self, zoom_settings: bool = ..., pre_post_roll_times: bool = ..., track_visibility: bool = ..., track_heights: bool = ..., group_enables: bool = ..., window_configuration: bool = ..., window_configuration_index: _Optional[int] = ..., window_configuration_name: _Optional[str] = ...) -> None: ...

class MidiData(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class OpenSessionRequestBody(_message.Message):
    __slots__ = ["session_path"]
    SESSION_PATH_FIELD_NUMBER: _ClassVar[int]
    session_path: str
    def __init__(self, session_path: _Optional[str] = ...) -> None: ...

class Pagination(_message.Message):
    __slots__ = ["limit", "offset", "total"]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    limit: int
    offset: int
    total: int
    def __init__(self, total: _Optional[int] = ..., limit: _Optional[int] = ..., offset: _Optional[int] = ...) -> None: ...

class PasteSpecialRequestBody(_message.Message):
    __slots__ = ["paste_special_option"]
    PASTE_SPECIAL_OPTION_FIELD_NUMBER: _ClassVar[int]
    paste_special_option: PasteSpecialOptions
    def __init__(self, paste_special_option: _Optional[_Union[PasteSpecialOptions, str]] = ...) -> None: ...

class PropertyContainer(_message.Message):
    __slots__ = ["container_name", "type", "value"]
    CONTAINER_NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    container_name: str
    type: DP_ValueTypes
    value: str
    def __init__(self, container_name: _Optional[str] = ..., type: _Optional[_Union[DP_ValueTypes, str]] = ..., value: _Optional[str] = ...) -> None: ...

class PropertyDescriptor(_message.Message):
    __slots__ = ["accepted_values", "description", "max_value", "min_value", "name", "object_type", "required", "units", "value_type"]
    ACCEPTED_VALUES_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    MAX_VALUE_FIELD_NUMBER: _ClassVar[int]
    MIN_VALUE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_FIELD_NUMBER: _ClassVar[int]
    UNITS_FIELD_NUMBER: _ClassVar[int]
    VALUE_TYPE_FIELD_NUMBER: _ClassVar[int]
    accepted_values: _containers.RepeatedScalarFieldContainer[str]
    description: str
    max_value: str
    min_value: str
    name: str
    object_type: str
    required: bool
    units: str
    value_type: DP_ValueTypes
    def __init__(self, name: _Optional[str] = ..., value_type: _Optional[_Union[DP_ValueTypes, str]] = ..., object_type: _Optional[str] = ..., required: bool = ..., description: _Optional[str] = ..., units: _Optional[str] = ..., accepted_values: _Optional[_Iterable[str]] = ..., max_value: _Optional[str] = ..., min_value: _Optional[str] = ...) -> None: ...

class RefreshTargetAudioFilesRequestBody(_message.Message):
    __slots__ = ["file_list"]
    FILE_LIST_FIELD_NUMBER: _ClassVar[int]
    file_list: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, file_list: _Optional[_Iterable[str]] = ...) -> None: ...

class RefreshTargetAudioFilesResponseBody(_message.Message):
    __slots__ = ["failure_count", "failure_list", "success_count"]
    FAILURE_COUNT_FIELD_NUMBER: _ClassVar[int]
    FAILURE_LIST_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_COUNT_FIELD_NUMBER: _ClassVar[int]
    failure_count: int
    failure_list: _containers.RepeatedScalarFieldContainer[str]
    success_count: int
    def __init__(self, success_count: _Optional[int] = ..., failure_count: _Optional[int] = ..., failure_list: _Optional[_Iterable[str]] = ...) -> None: ...

class RegisterConnectionRequestBody(_message.Message):
    __slots__ = ["application_name", "company_name"]
    APPLICATION_NAME_FIELD_NUMBER: _ClassVar[int]
    COMPANY_NAME_FIELD_NUMBER: _ClassVar[int]
    application_name: str
    company_name: str
    def __init__(self, company_name: _Optional[str] = ..., application_name: _Optional[str] = ...) -> None: ...

class RegisterConnectionResponseBody(_message.Message):
    __slots__ = ["session_id"]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    def __init__(self, session_id: _Optional[str] = ...) -> None: ...

class RenameSelectedClipRequestBody(_message.Message):
    __slots__ = ["clip_location", "new_name", "rename_file"]
    CLIP_LOCATION_FIELD_NUMBER: _ClassVar[int]
    NEW_NAME_FIELD_NUMBER: _ClassVar[int]
    RENAME_FILE_FIELD_NUMBER: _ClassVar[int]
    clip_location: CL_ClipLocation
    new_name: str
    rename_file: bool
    def __init__(self, clip_location: _Optional[_Union[CL_ClipLocation, str]] = ..., new_name: _Optional[str] = ..., rename_file: bool = ...) -> None: ...

class RenameTargetClipRequestBody(_message.Message):
    __slots__ = ["clip_name", "new_name", "rename_file"]
    CLIP_NAME_FIELD_NUMBER: _ClassVar[int]
    NEW_NAME_FIELD_NUMBER: _ClassVar[int]
    RENAME_FILE_FIELD_NUMBER: _ClassVar[int]
    clip_name: str
    new_name: str
    rename_file: bool
    def __init__(self, clip_name: _Optional[str] = ..., new_name: _Optional[str] = ..., rename_file: bool = ...) -> None: ...

class RenameTargetTrackRequestBody(_message.Message):
    __slots__ = ["current_name", "new_name", "track_id"]
    CURRENT_NAME_FIELD_NUMBER: _ClassVar[int]
    NEW_NAME_FIELD_NUMBER: _ClassVar[int]
    TRACK_ID_FIELD_NUMBER: _ClassVar[int]
    current_name: str
    new_name: str
    track_id: str
    def __init__(self, track_id: _Optional[str] = ..., new_name: _Optional[str] = ..., current_name: _Optional[str] = ...) -> None: ...

class Request(_message.Message):
    __slots__ = ["header", "request_body_json"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    REQUEST_BODY_JSON_FIELD_NUMBER: _ClassVar[int]
    header: RequestHeader
    request_body_json: str
    def __init__(self, header: _Optional[_Union[RequestHeader, _Mapping]] = ..., request_body_json: _Optional[str] = ...) -> None: ...

class RequestHeader(_message.Message):
    __slots__ = ["command", "session_id", "task_id", "version"]
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    command: CommandId
    session_id: str
    task_id: str
    version: int
    def __init__(self, task_id: _Optional[str] = ..., command: _Optional[_Union[CommandId, str]] = ..., version: _Optional[int] = ..., session_id: _Optional[str] = ...) -> None: ...

class Response(_message.Message):
    __slots__ = ["header", "response_body_json", "response_error_json"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_BODY_JSON_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_ERROR_JSON_FIELD_NUMBER: _ClassVar[int]
    header: ResponseHeader
    response_body_json: str
    response_error_json: str
    def __init__(self, header: _Optional[_Union[ResponseHeader, _Mapping]] = ..., response_body_json: _Optional[str] = ..., response_error_json: _Optional[str] = ...) -> None: ...

class ResponseHeader(_message.Message):
    __slots__ = ["command", "progress", "status", "task_id"]
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    command: CommandId
    progress: int
    status: TaskStatus
    task_id: str
    def __init__(self, task_id: _Optional[str] = ..., command: _Optional[_Union[CommandId, str]] = ..., status: _Optional[_Union[TaskStatus, str]] = ..., progress: _Optional[int] = ...) -> None: ...

class SaveSessionAsRequestBody(_message.Message):
    __slots__ = ["session_location", "session_name"]
    SESSION_LOCATION_FIELD_NUMBER: _ClassVar[int]
    SESSION_NAME_FIELD_NUMBER: _ClassVar[int]
    session_location: str
    session_name: str
    def __init__(self, session_name: _Optional[str] = ..., session_location: _Optional[str] = ...) -> None: ...

class SelectAllClipsOnTrackRequestBody(_message.Message):
    __slots__ = ["track_name"]
    TRACK_NAME_FIELD_NUMBER: _ClassVar[int]
    track_name: str
    def __init__(self, track_name: _Optional[str] = ...) -> None: ...

class SelectAllClipsOnTrackResponseBody(_message.Message):
    __slots__ = ["track_name"]
    TRACK_NAME_FIELD_NUMBER: _ClassVar[int]
    track_name: str
    def __init__(self, track_name: _Optional[str] = ...) -> None: ...

class SessionData(_message.Message):
    __slots__ = ["adjust_session_start_time_to_match_source", "audio_handle_size", "audio_options", "match_options", "playlist_options", "timecode_mapping_start_time", "timecode_mapping_units", "track_data_to_import", "video_options"]
    ADJUST_SESSION_START_TIME_TO_MATCH_SOURCE_FIELD_NUMBER: _ClassVar[int]
    AUDIO_HANDLE_SIZE_FIELD_NUMBER: _ClassVar[int]
    AUDIO_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    MATCH_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    PLAYLIST_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    TIMECODE_MAPPING_START_TIME_FIELD_NUMBER: _ClassVar[int]
    TIMECODE_MAPPING_UNITS_FIELD_NUMBER: _ClassVar[int]
    TRACK_DATA_TO_IMPORT_FIELD_NUMBER: _ClassVar[int]
    VIDEO_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    adjust_session_start_time_to_match_source: bool
    audio_handle_size: int
    audio_options: AudioMediaOptions
    match_options: MatchTrackOptions
    playlist_options: MainPlaylistOptions
    timecode_mapping_start_time: str
    timecode_mapping_units: TimeCodeMappingOptions
    track_data_to_import: TrackDataToImport
    video_options: VideoMediaOptions
    def __init__(self, audio_options: _Optional[_Union[AudioMediaOptions, str]] = ..., audio_handle_size: _Optional[int] = ..., video_options: _Optional[_Union[VideoMediaOptions, str]] = ..., match_options: _Optional[_Union[MatchTrackOptions, str]] = ..., playlist_options: _Optional[_Union[MainPlaylistOptions, str]] = ..., track_data_to_import: _Optional[_Union[TrackDataToImport, _Mapping]] = ..., timecode_mapping_units: _Optional[_Union[TimeCodeMappingOptions, str]] = ..., timecode_mapping_start_time: _Optional[str] = ..., adjust_session_start_time_to_match_source: bool = ...) -> None: ...

class SessionDataImport(_message.Message):
    __slots__ = ["heat_master_settings", "key_signature_choed_map", "markers_memory_locations", "mic_pre_settings", "tempo_meter_map", "window_configurations"]
    HEAT_MASTER_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    KEY_SIGNATURE_CHOED_MAP_FIELD_NUMBER: _ClassVar[int]
    MARKERS_MEMORY_LOCATIONS_FIELD_NUMBER: _ClassVar[int]
    MIC_PRE_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    TEMPO_METER_MAP_FIELD_NUMBER: _ClassVar[int]
    WINDOW_CONFIGURATIONS_FIELD_NUMBER: _ClassVar[int]
    heat_master_settings: bool
    key_signature_choed_map: bool
    markers_memory_locations: bool
    mic_pre_settings: bool
    tempo_meter_map: bool
    window_configurations: bool
    def __init__(self, tempo_meter_map: bool = ..., key_signature_choed_map: bool = ..., markers_memory_locations: bool = ..., window_configurations: bool = ..., mic_pre_settings: bool = ..., heat_master_settings: bool = ...) -> None: ...

class SetPlaybackModeRequestBody(_message.Message):
    __slots__ = ["playback_mode"]
    PLAYBACK_MODE_FIELD_NUMBER: _ClassVar[int]
    playback_mode: PM_PlaybackMode
    def __init__(self, playback_mode: _Optional[_Union[PM_PlaybackMode, str]] = ...) -> None: ...

class SetPlaybackModeResponseBody(_message.Message):
    __slots__ = ["current_playback_mode", "playback_mode_list"]
    CURRENT_PLAYBACK_MODE_FIELD_NUMBER: _ClassVar[int]
    PLAYBACK_MODE_LIST_FIELD_NUMBER: _ClassVar[int]
    current_playback_mode: PM_PlaybackMode
    playback_mode_list: _containers.RepeatedScalarFieldContainer[PM_PlaybackMode]
    def __init__(self, current_playback_mode: _Optional[_Union[PM_PlaybackMode, str]] = ..., playback_mode_list: _Optional[_Iterable[_Union[PM_PlaybackMode, str]]] = ...) -> None: ...

class SetRecordModeRequestBody(_message.Message):
    __slots__ = ["record_arm_transport", "record_mode"]
    RECORD_ARM_TRANSPORT_FIELD_NUMBER: _ClassVar[int]
    RECORD_MODE_FIELD_NUMBER: _ClassVar[int]
    record_arm_transport: bool
    record_mode: RM_RecordMode
    def __init__(self, record_mode: _Optional[_Union[RM_RecordMode, str]] = ..., record_arm_transport: bool = ...) -> None: ...

class SetRecordModeResponseBody(_message.Message):
    __slots__ = ["current_record_mode", "record_mode_list"]
    CURRENT_RECORD_MODE_FIELD_NUMBER: _ClassVar[int]
    RECORD_MODE_LIST_FIELD_NUMBER: _ClassVar[int]
    current_record_mode: RM_RecordMode
    record_mode_list: _containers.RepeatedScalarFieldContainer[RM_RecordMode]
    def __init__(self, current_record_mode: _Optional[_Union[RM_RecordMode, str]] = ..., record_mode_list: _Optional[_Iterable[_Union[RM_RecordMode, str]]] = ...) -> None: ...

class SetSessionAudioFormatRequestBody(_message.Message):
    __slots__ = ["audio_format"]
    AUDIO_FORMAT_FIELD_NUMBER: _ClassVar[int]
    audio_format: SessionAudioFormat
    def __init__(self, audio_format: _Optional[_Union[SessionAudioFormat, str]] = ...) -> None: ...

class SetSessionAudioRatePullSettingsRequestBody(_message.Message):
    __slots__ = ["audio_rate_pull"]
    AUDIO_RATE_PULL_FIELD_NUMBER: _ClassVar[int]
    audio_rate_pull: SessionRatePull
    def __init__(self, audio_rate_pull: _Optional[_Union[SessionRatePull, str]] = ...) -> None: ...

class SetSessionBitDepthRequestBody(_message.Message):
    __slots__ = ["bit_depth"]
    BIT_DEPTH_FIELD_NUMBER: _ClassVar[int]
    bit_depth: BitDepth
    def __init__(self, bit_depth: _Optional[_Union[BitDepth, str]] = ...) -> None: ...

class SetSessionFeetFramesRateRequestBody(_message.Message):
    __slots__ = ["feet_frames_rate"]
    FEET_FRAMES_RATE_FIELD_NUMBER: _ClassVar[int]
    feet_frames_rate: SessionFeetFramesRate
    def __init__(self, feet_frames_rate: _Optional[_Union[SessionFeetFramesRate, str]] = ...) -> None: ...

class SetSessionInterleavedStateRequestBody(_message.Message):
    __slots__ = ["interleaved_state"]
    INTERLEAVED_STATE_FIELD_NUMBER: _ClassVar[int]
    interleaved_state: bool
    def __init__(self, interleaved_state: bool = ...) -> None: ...

class SetSessionLengthRequestBody(_message.Message):
    __slots__ = ["session_length"]
    SESSION_LENGTH_FIELD_NUMBER: _ClassVar[int]
    session_length: str
    def __init__(self, session_length: _Optional[str] = ...) -> None: ...

class SetSessionStartTimeRequestBody(_message.Message):
    __slots__ = ["maintain_relative_position", "session_start_time", "track_offset_opts"]
    MAINTAIN_RELATIVE_POSITION_FIELD_NUMBER: _ClassVar[int]
    SESSION_START_TIME_FIELD_NUMBER: _ClassVar[int]
    TRACK_OFFSET_OPTS_FIELD_NUMBER: _ClassVar[int]
    maintain_relative_position: bool
    session_start_time: str
    track_offset_opts: TrackOffsetOptions
    def __init__(self, session_start_time: _Optional[str] = ..., track_offset_opts: _Optional[_Union[TrackOffsetOptions, str]] = ..., maintain_relative_position: bool = ...) -> None: ...

class SetSessionTimeCodeRateRequestBody(_message.Message):
    __slots__ = ["time_code_rate"]
    TIME_CODE_RATE_FIELD_NUMBER: _ClassVar[int]
    time_code_rate: SessionTimeCodeRate
    def __init__(self, time_code_rate: _Optional[_Union[SessionTimeCodeRate, str]] = ...) -> None: ...

class SetSessionVideoRatePullSettingsRequestBody(_message.Message):
    __slots__ = ["video_rate_pull"]
    VIDEO_RATE_PULL_FIELD_NUMBER: _ClassVar[int]
    video_rate_pull: SessionRatePull
    def __init__(self, video_rate_pull: _Optional[_Union[SessionRatePull, str]] = ...) -> None: ...

class SpotLocationData(_message.Message):
    __slots__ = ["location_options", "location_type", "location_value"]
    LOCATION_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    LOCATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    LOCATION_VALUE_FIELD_NUMBER: _ClassVar[int]
    location_options: TrackOffsetOptions
    location_type: SpotLocationType
    location_value: str
    def __init__(self, location_type: _Optional[_Union[SpotLocationType, str]] = ..., location_value: _Optional[str] = ..., location_options: _Optional[_Union[TrackOffsetOptions, str]] = ...) -> None: ...

class SpotRequestBody(_message.Message):
    __slots__ = ["location_data", "track_offset_options"]
    LOCATION_DATA_FIELD_NUMBER: _ClassVar[int]
    TRACK_OFFSET_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    location_data: SpotLocationData
    track_offset_options: TrackOffsetOptions
    def __init__(self, track_offset_options: _Optional[_Union[TrackOffsetOptions, str]] = ..., location_data: _Optional[_Union[SpotLocationData, _Mapping]] = ...) -> None: ...

class Track(_message.Message):
    __slots__ = ["color", "id", "id_compressed", "index", "name", "track_attributes", "type"]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    ID_COMPRESSED_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TRACK_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    color: str
    id: str
    id_compressed: str
    index: int
    name: str
    track_attributes: TrackAttributes
    type: TrackType
    def __init__(self, name: _Optional[str] = ..., type: _Optional[_Union[TrackType, str]] = ..., id: _Optional[str] = ..., index: _Optional[int] = ..., color: _Optional[str] = ..., track_attributes: _Optional[_Union[TrackAttributes, _Mapping]] = ..., id_compressed: _Optional[str] = ...) -> None: ...

class TrackAttributes(_message.Message):
    __slots__ = ["contains_automation", "contains_clips", "is_frozen", "is_hidden", "is_inactive", "is_input_monitoring_on", "is_locked", "is_muted", "is_online", "is_open", "is_record_enabled", "is_selected", "is_smart_dsp_on", "is_soloed"]
    CONTAINS_AUTOMATION_FIELD_NUMBER: _ClassVar[int]
    CONTAINS_CLIPS_FIELD_NUMBER: _ClassVar[int]
    IS_FROZEN_FIELD_NUMBER: _ClassVar[int]
    IS_HIDDEN_FIELD_NUMBER: _ClassVar[int]
    IS_INACTIVE_FIELD_NUMBER: _ClassVar[int]
    IS_INPUT_MONITORING_ON_FIELD_NUMBER: _ClassVar[int]
    IS_LOCKED_FIELD_NUMBER: _ClassVar[int]
    IS_MUTED_FIELD_NUMBER: _ClassVar[int]
    IS_ONLINE_FIELD_NUMBER: _ClassVar[int]
    IS_OPEN_FIELD_NUMBER: _ClassVar[int]
    IS_RECORD_ENABLED_FIELD_NUMBER: _ClassVar[int]
    IS_SELECTED_FIELD_NUMBER: _ClassVar[int]
    IS_SMART_DSP_ON_FIELD_NUMBER: _ClassVar[int]
    IS_SOLOED_FIELD_NUMBER: _ClassVar[int]
    contains_automation: bool
    contains_clips: bool
    is_frozen: bool
    is_hidden: TrackAttributeState
    is_inactive: TrackAttributeState
    is_input_monitoring_on: TrackAttributeState
    is_locked: bool
    is_muted: bool
    is_online: bool
    is_open: bool
    is_record_enabled: bool
    is_selected: TrackAttributeState
    is_smart_dsp_on: bool
    is_soloed: bool
    def __init__(self, is_inactive: _Optional[_Union[TrackAttributeState, str]] = ..., is_hidden: _Optional[_Union[TrackAttributeState, str]] = ..., is_selected: _Optional[_Union[TrackAttributeState, str]] = ..., contains_clips: bool = ..., contains_automation: bool = ..., is_soloed: bool = ..., is_record_enabled: bool = ..., is_input_monitoring_on: _Optional[_Union[TrackAttributeState, str]] = ..., is_smart_dsp_on: bool = ..., is_locked: bool = ..., is_muted: bool = ..., is_frozen: bool = ..., is_open: bool = ..., is_online: bool = ...) -> None: ...

class TrackDataToImport(_message.Message):
    __slots__ = ["clip_gain", "clips_and_media", "track_data_preset_path", "volume_automation"]
    CLIPS_AND_MEDIA_FIELD_NUMBER: _ClassVar[int]
    CLIP_GAIN_FIELD_NUMBER: _ClassVar[int]
    TRACK_DATA_PRESET_PATH_FIELD_NUMBER: _ClassVar[int]
    VOLUME_AUTOMATION_FIELD_NUMBER: _ClassVar[int]
    clip_gain: bool
    clips_and_media: bool
    track_data_preset_path: str
    volume_automation: bool
    def __init__(self, track_data_preset_path: _Optional[str] = ..., clip_gain: bool = ..., clips_and_media: bool = ..., volume_automation: bool = ...) -> None: ...

class TrackListInvertibleFilter(_message.Message):
    __slots__ = ["filter", "is_inverted"]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    IS_INVERTED_FIELD_NUMBER: _ClassVar[int]
    filter: TrackListFilter
    is_inverted: bool
    def __init__(self, filter: _Optional[_Union[TrackListFilter, str]] = ..., is_inverted: bool = ...) -> None: ...

class VideoData(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class CommandId(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class TaskStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class CommandErrorType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class TrackType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class TrackAttributeState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class FileType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class IOSettings(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class ImportType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class AudioMediaOptions(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class VideoMediaOptions(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class MatchTrackOptions(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class TimeCodeMappingOptions(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class TrackOffsetOptions(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class ConversionQuality(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class MainPlaylistOptions(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class AudioOperations(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class MediaDestination(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class MediaLocation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class TrackListFilter(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class SpotLocationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class ExportFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class ExportFileType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class BitDepth(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class ResolveDuplicateNamesBy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class ExportAsAAFFileType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class AAFFileBitDepth(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class CopyOption(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class FileLocationTypeFilter(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class AutomationDataOptions(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class PasteSpecialOptions(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class TripleBool(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class EM_SourceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class CompressionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class SampleRate(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class EM_VideoExportOptions(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class EM_FileType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class EM_FileDestination(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class EM_DeliveryFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class DP_ValueTypes(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class DynamicPropertyType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class TrackListType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class FadeHandlingType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class TextAsFileFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class ESI_OutputType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class PM_PlaybackMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class RM_RecordMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class SessionAudioFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class SessionTimeCodeRate(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class SessionFeetFramesRate(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class SessionRatePull(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class TS_TransportState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class CL_ClipLocation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class TimeProperties(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class MemoryLocationReference(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

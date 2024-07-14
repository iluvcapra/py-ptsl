from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CommandId(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CreateSession: _ClassVar[CommandId]
    OpenSession: _ClassVar[CommandId]
    Import: _ClassVar[CommandId]
    GetTrackList: _ClassVar[CommandId]
    SelectAllClipsOnTrack: _ClassVar[CommandId]
    ExtendSelectionToTargetTracks: _ClassVar[CommandId]
    TrimToSelection: _ClassVar[CommandId]
    CreateFadesBasedOnPreset: _ClassVar[CommandId]
    RenameTargetTrack: _ClassVar[CommandId]
    ConsolidateClip: _ClassVar[CommandId]
    ExportClipsAsFiles: _ClassVar[CommandId]
    ExportSelectedTracksAsAAFOMF: _ClassVar[CommandId]
    GetTaskStatus: _ClassVar[CommandId]
    HostReadyCheck: _ClassVar[CommandId]
    RefreshTargetAudioFiles: _ClassVar[CommandId]
    RefreshAllModifiedAudioFiles: _ClassVar[CommandId]
    GetFileLocation: _ClassVar[CommandId]
    CloseSession: _ClassVar[CommandId]
    SaveSession: _ClassVar[CommandId]
    SaveSessionAs: _ClassVar[CommandId]
    Cut: _ClassVar[CommandId]
    Copy: _ClassVar[CommandId]
    Paste: _ClassVar[CommandId]
    Clear: _ClassVar[CommandId]
    CutSpecial: _ClassVar[CommandId]
    CopySpecial: _ClassVar[CommandId]
    ClearSpecial: _ClassVar[CommandId]
    PasteSpecial: _ClassVar[CommandId]
    ExportMix: _ClassVar[CommandId]
    Spot: _ClassVar[CommandId]
    ExportSessionInfoAsText: _ClassVar[CommandId]
    GetDynamicProperties: _ClassVar[CommandId]
    SetPlaybackMode: _ClassVar[CommandId]
    SetRecordMode: _ClassVar[CommandId]
    GetSessionAudioFormat: _ClassVar[CommandId]
    GetSessionSampleRate: _ClassVar[CommandId]
    GetSessionBitDepth: _ClassVar[CommandId]
    GetSessionInterleavedState: _ClassVar[CommandId]
    GetSessionTimeCodeRate: _ClassVar[CommandId]
    GetSessionFeetFramesRate: _ClassVar[CommandId]
    GetSessionAudioRatePullSettings: _ClassVar[CommandId]
    GetSessionVideoRatePullSettings: _ClassVar[CommandId]
    GetSessionName: _ClassVar[CommandId]
    GetSessionPath: _ClassVar[CommandId]
    GetSessionStartTime: _ClassVar[CommandId]
    GetSessionLength: _ClassVar[CommandId]
    SetSessionAudioFormat: _ClassVar[CommandId]
    SetSessionBitDepth: _ClassVar[CommandId]
    SetSessionInterleavedState: _ClassVar[CommandId]
    SetSessionTimeCodeRate: _ClassVar[CommandId]
    SetSessionFeetFramesRate: _ClassVar[CommandId]
    SetSessionAudioRatePullSettings: _ClassVar[CommandId]
    SetSessionVideoRatePullSettings: _ClassVar[CommandId]
    SetSessionStartTime: _ClassVar[CommandId]
    SetSessionLength: _ClassVar[CommandId]
    GetPTSLVersion: _ClassVar[CommandId]
    GetPlaybackMode: _ClassVar[CommandId]
    GetRecordMode: _ClassVar[CommandId]
    GetTransportArmed: _ClassVar[CommandId]
    GetTransportState: _ClassVar[CommandId]
    ClearMemoryLocation: _ClassVar[CommandId]
    RenameSelectedClip: _ClassVar[CommandId]
    RenameTargetClip: _ClassVar[CommandId]
    TogglePlayState: _ClassVar[CommandId]
    ToggleRecordEnable: _ClassVar[CommandId]
    PlayHalfSpeed: _ClassVar[CommandId]
    RecordHalfSpeed: _ClassVar[CommandId]
    EditMemoryLocation: _ClassVar[CommandId]
    GetMemoryLocations: _ClassVar[CommandId]
    RegisterConnection: _ClassVar[CommandId]
    CreateMemoryLocation: _ClassVar[CommandId]
    CreateNewTracks: _ClassVar[CommandId]
    SelectTracksByName: _ClassVar[CommandId]
    GetEditMode: _ClassVar[CommandId]
    SetEditMode: _ClassVar[CommandId]
    GetEditTool: _ClassVar[CommandId]
    SetEditTool: _ClassVar[CommandId]
    RecallZoomPreset: _ClassVar[CommandId]
    GetEditModeOptions: _ClassVar[CommandId]
    SetEditModeOptions: _ClassVar[CommandId]
    SetTimelineSelection: _ClassVar[CommandId]
    GetTimelineSelection: _ClassVar[CommandId]
    ImportVideo: _ClassVar[CommandId]
    SelectMemoryLocation: _ClassVar[CommandId]
    SetTrackMuteState: _ClassVar[CommandId]
    SetTrackSoloState: _ClassVar[CommandId]
    SetTrackSoloSafeState: _ClassVar[CommandId]
    SetTrackRecordEnableState: _ClassVar[CommandId]
    SetTrackRecordSafeEnableState: _ClassVar[CommandId]
    SetTrackInputMonitorState: _ClassVar[CommandId]
    SetTrackSmartDspState: _ClassVar[CommandId]
    SetTrackHiddenState: _ClassVar[CommandId]
    SetTrackInactiveState: _ClassVar[CommandId]
    SetTrackFrozenState: _ClassVar[CommandId]
    SetTrackOnlineState: _ClassVar[CommandId]
    SetTrackOpenState: _ClassVar[CommandId]
    GetSessionIDs: _ClassVar[CommandId]
    GetMemoryLocationsManageMode: _ClassVar[CommandId]
    SetMemoryLocationsManageMode: _ClassVar[CommandId]
    SetMainCounterFormat: _ClassVar[CommandId]
    SetSubCounterFormat: _ClassVar[CommandId]
    GetMainCounterFormat: _ClassVar[CommandId]
    GetSubCounterFormat: _ClassVar[CommandId]
    Undo: _ClassVar[CommandId]
    Redo: _ClassVar[CommandId]
    UndoAll: _ClassVar[CommandId]
    RedoAll: _ClassVar[CommandId]
    ClearUndoQueue: _ClassVar[CommandId]
    SetTrackDSPModeSafeState: _ClassVar[CommandId]
    GetSessionSystemDelayInfo: _ClassVar[CommandId]
    GroupClips: _ClassVar[CommandId]
    UngroupClips: _ClassVar[CommandId]
    UngroupAllClips: _ClassVar[CommandId]
    RegroupClips: _ClassVar[CommandId]
    RepeatSelection: _ClassVar[CommandId]
    DuplicateSelection: _ClassVar[CommandId]

class TaskStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    Queued: _ClassVar[TaskStatus]
    Pending: _ClassVar[TaskStatus]
    InProgress: _ClassVar[TaskStatus]
    Completed: _ClassVar[TaskStatus]
    Failed: _ClassVar[TaskStatus]
    WaitingForUserInput: _ClassVar[TaskStatus]
    CompletedWithBadResponse: _ClassVar[TaskStatus]
    FailedWithBadErrorResponse: _ClassVar[TaskStatus]

class CommandErrorType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    OS_WritePermissions: _ClassVar[CommandErrorType]
    OS_ErrorCode: _ClassVar[CommandErrorType]
    OS_NoLocationFound: _ClassVar[CommandErrorType]
    OS_NoSessionFound: _ClassVar[CommandErrorType]
    OS_FilePathLocation: _ClassVar[CommandErrorType]
    OS_ReadError: _ClassVar[CommandErrorType]
    OS_DiskSpace: _ClassVar[CommandErrorType]
    OS_DuplicateName: _ClassVar[CommandErrorType]
    OS_IllegalCharacters: _ClassVar[CommandErrorType]
    OS_CharactersLimit: _ClassVar[CommandErrorType]
    OS_ProToolsIsNotAvailable: _ClassVar[CommandErrorType]
    OS_NoFilePathFound: _ClassVar[CommandErrorType]
    PT_UnknownError: _ClassVar[CommandErrorType]
    PT_NoTemplateGroup: _ClassVar[CommandErrorType]
    PT_NoTemplate: _ClassVar[CommandErrorType]
    PT_SampleRateMismatch: _ClassVar[CommandErrorType]
    PT_NoVideoTrackFound: _ClassVar[CommandErrorType]
    PT_NoTracksFound: _ClassVar[CommandErrorType]
    PT_NoOpenedSession: _ClassVar[CommandErrorType]
    PT_NoTrackFound: _ClassVar[CommandErrorType]
    PT_NoClipsFound: _ClassVar[CommandErrorType]
    PT_NoSelection: _ClassVar[CommandErrorType]
    PT_RecordDrive: _ClassVar[CommandErrorType]
    PT_NoPresetFound: _ClassVar[CommandErrorType]
    PT_FileTypeMXF: _ClassVar[CommandErrorType]
    PT_CopyOptionCopy: _ClassVar[CommandErrorType]
    PT_CopyOptionLink: _ClassVar[CommandErrorType]
    PT_QuantizeEdits: _ClassVar[CommandErrorType]
    PT_ExportAsMultichannel: _ClassVar[CommandErrorType]
    PT_IllegalCharactersComments: _ClassVar[CommandErrorType]
    PT_IllegalCharactersSequenceName: _ClassVar[CommandErrorType]
    PT_MaxCharactersComments: _ClassVar[CommandErrorType]
    PT_MaxCharactersSequenceName: _ClassVar[CommandErrorType]
    PT_NoSequenceName: _ClassVar[CommandErrorType]
    PT_InvalidTask: _ClassVar[CommandErrorType]
    PT_FileNotFound: _ClassVar[CommandErrorType]
    PT_InvalidSelection: _ClassVar[CommandErrorType]
    PT_ReadOnlySession: _ClassVar[CommandErrorType]
    PT_InvalidParameter: _ClassVar[CommandErrorType]
    PT_Forbidden: _ClassVar[CommandErrorType]
    PT_NoTimelineFound: _ClassVar[CommandErrorType]
    PT_ArgumentOutOfRange: _ClassVar[CommandErrorType]
    PT_ForbiddenTrackType: _ClassVar[CommandErrorType]
    PT_NoVideoEngineFound: _ClassVar[CommandErrorType]
    PT_NoDspHardwareFound: _ClassVar[CommandErrorType]
    PT_UnsupportedCommand: _ClassVar[CommandErrorType]
    PT_HostNotReady: _ClassVar[CommandErrorType]
    PT_CannotBeDone: _ClassVar[CommandErrorType]
    PT_ResponseLengthExceeded: _ClassVar[CommandErrorType]
    PT_Info: _ClassVar[CommandErrorType]
    SDK_VersionMismatch: _ClassVar[CommandErrorType]
    SDK_NotImplemented: _ClassVar[CommandErrorType]

class TrackType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TT_Unknown: _ClassVar[TrackType]
    Unknown: _ClassVar[TrackType]
    TT_Midi: _ClassVar[TrackType]
    Midi: _ClassVar[TrackType]
    TT_Audio: _ClassVar[TrackType]
    AudioTrack: _ClassVar[TrackType]
    TT_Aux: _ClassVar[TrackType]
    Aux: _ClassVar[TrackType]
    TT_Video: _ClassVar[TrackType]
    VideoTrack: _ClassVar[TrackType]
    TT_Vca: _ClassVar[TrackType]
    Vca: _ClassVar[TrackType]
    TT_Tempo: _ClassVar[TrackType]
    Tempo: _ClassVar[TrackType]
    TT_Markers: _ClassVar[TrackType]
    Markers: _ClassVar[TrackType]
    TT_Meter: _ClassVar[TrackType]
    Meter: _ClassVar[TrackType]
    TT_KeySignature: _ClassVar[TrackType]
    KeySignature: _ClassVar[TrackType]
    TT_ChordSymbols: _ClassVar[TrackType]
    ChordSymbols: _ClassVar[TrackType]
    TT_Instrument: _ClassVar[TrackType]
    Instrument: _ClassVar[TrackType]
    TT_Master: _ClassVar[TrackType]
    Master: _ClassVar[TrackType]
    TT_Heat: _ClassVar[TrackType]
    Heat: _ClassVar[TrackType]
    TT_BasicFolder: _ClassVar[TrackType]
    BasicFolder: _ClassVar[TrackType]
    TT_RoutingFolder: _ClassVar[TrackType]
    RoutingFolder: _ClassVar[TrackType]
    TT_CompLane: _ClassVar[TrackType]
    CompLane: _ClassVar[TrackType]

class TrackFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TF_Unknown: _ClassVar[TrackFormat]
    TF_Mono: _ClassVar[TrackFormat]
    TF_Stereo: _ClassVar[TrackFormat]
    TF_LCR: _ClassVar[TrackFormat]
    TF_LCRS: _ClassVar[TrackFormat]
    TF_Quad: _ClassVar[TrackFormat]
    TF_5_0: _ClassVar[TrackFormat]
    TF_5_1: _ClassVar[TrackFormat]
    TF_5_0_2: _ClassVar[TrackFormat]
    TF_5_1_2: _ClassVar[TrackFormat]
    TF_5_0_4: _ClassVar[TrackFormat]
    TF_5_1_4: _ClassVar[TrackFormat]
    TF_6_0: _ClassVar[TrackFormat]
    TF_6_1: _ClassVar[TrackFormat]
    TF_7_0: _ClassVar[TrackFormat]
    TF_7_1: _ClassVar[TrackFormat]
    TF_7_0_SDDS: _ClassVar[TrackFormat]
    TF_7_1_SDDS: _ClassVar[TrackFormat]
    TF_7_0_2: _ClassVar[TrackFormat]
    TF_7_1_2: _ClassVar[TrackFormat]
    TF_7_0_4: _ClassVar[TrackFormat]
    TF_7_1_4: _ClassVar[TrackFormat]
    TF_7_0_6: _ClassVar[TrackFormat]
    TF_7_1_6: _ClassVar[TrackFormat]
    TF_9_0_4: _ClassVar[TrackFormat]
    TF_9_1_4: _ClassVar[TrackFormat]
    TF_9_0_6: _ClassVar[TrackFormat]
    TF_9_1_6: _ClassVar[TrackFormat]
    TF_1stOrderAmbisonics: _ClassVar[TrackFormat]
    TF_2ndOrderAmbisonics: _ClassVar[TrackFormat]
    TF_3rdOrderAmbisonics: _ClassVar[TrackFormat]
    TF_4thOrderAmbisonics: _ClassVar[TrackFormat]
    TF_5thOrderAmbisonics: _ClassVar[TrackFormat]
    TF_6thOrderAmbisonics: _ClassVar[TrackFormat]
    TF_7thOrderAmbisonics: _ClassVar[TrackFormat]
    TF_None: _ClassVar[TrackFormat]
    TF_2_1: _ClassVar[TrackFormat]
    TF_Overhead: _ClassVar[TrackFormat]

class TrackTimebase(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TTB_Unknown: _ClassVar[TrackTimebase]
    TTB_Samples: _ClassVar[TrackTimebase]
    TTB_Ticks: _ClassVar[TrackTimebase]
    TTB_None: _ClassVar[TrackTimebase]

class TrackAttributeState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    None: _ClassVar[TrackAttributeState]
    SetExplicitly: _ClassVar[TrackAttributeState]
    SetImplicitly: _ClassVar[TrackAttributeState]
    SetExplicitlyAndImplicitly: _ClassVar[TrackAttributeState]

class FileType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FT_WAVE: _ClassVar[FileType]
    FT_AIFF: _ClassVar[FileType]
    FT_AAF: _ClassVar[FileType]
    FT_OMF: _ClassVar[FileType]

class IOSettings(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    IO_None: _ClassVar[IOSettings]
    IO_Last: _ClassVar[IOSettings]
    IO_StereoMix: _ClassVar[IOSettings]
    IO_51FilmMix: _ClassVar[IOSettings]
    IO_51SMPTEMix: _ClassVar[IOSettings]
    IO_51DTSMix: _ClassVar[IOSettings]
    IO_UserDefined: _ClassVar[IOSettings]

class ImportType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    Session: _ClassVar[ImportType]
    Audio: _ClassVar[ImportType]

class AudioMediaOptions(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LinkToSourceAudio: _ClassVar[AudioMediaOptions]
    CopyFromSourceAudio: _ClassVar[AudioMediaOptions]
    ConsolidateFromSourceAudio: _ClassVar[AudioMediaOptions]
    ForceToTargetSessionFormat: _ClassVar[AudioMediaOptions]

class VideoMediaOptions(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LinkToSourceVideo: _ClassVar[VideoMediaOptions]
    CopyFromSourceVideo: _ClassVar[VideoMediaOptions]
    ImportAsOfflineSatelliteMedia: _ClassVar[VideoMediaOptions]

class MatchTrackOptions(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MT_None: _ClassVar[MatchTrackOptions]
    MT_MatchTracks: _ClassVar[MatchTrackOptions]
    MT_ImportAsNewTrack: _ClassVar[MatchTrackOptions]

class TimeCodeMappingOptions(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MaintainAbsoluteTimeCodeValues: _ClassVar[TimeCodeMappingOptions]
    MaintainRelativeTimeCodeValues: _ClassVar[TimeCodeMappingOptions]
    MapStartTimeCodeTo: _ClassVar[TimeCodeMappingOptions]

class TrackOffsetOptions(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BarsBeats: _ClassVar[TrackOffsetOptions]
    MinSecs: _ClassVar[TrackOffsetOptions]
    TimeCode: _ClassVar[TrackOffsetOptions]
    FeetFrames: _ClassVar[TrackOffsetOptions]
    Samples: _ClassVar[TrackOffsetOptions]

class ConversionQuality(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    Low: _ClassVar[ConversionQuality]
    Good: _ClassVar[ConversionQuality]
    Better: _ClassVar[ConversionQuality]
    Best: _ClassVar[ConversionQuality]
    TweakHead: _ClassVar[ConversionQuality]

class MainPlaylistOptions(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ImportReplaceExistingPlaylists: _ClassVar[MainPlaylistOptions]
    ImportOverlayNewOnExistingPlaylists: _ClassVar[MainPlaylistOptions]
    DoNotImport: _ClassVar[MainPlaylistOptions]

class AudioOperations(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AddAudio: _ClassVar[AudioOperations]
    CopyAudio: _ClassVar[AudioOperations]
    ConvertAudio: _ClassVar[AudioOperations]
    Default: _ClassVar[AudioOperations]

class MediaDestination(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MD_None: _ClassVar[MediaDestination]
    MD_MainVideoTrack: _ClassVar[MediaDestination]
    MD_NewTrack: _ClassVar[MediaDestination]
    MD_ClipList: _ClassVar[MediaDestination]

class MediaLocation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ML_None: _ClassVar[MediaLocation]
    ML_SessionStart: _ClassVar[MediaLocation]
    ML_SongStart: _ClassVar[MediaLocation]
    ML_Selection: _ClassVar[MediaLocation]
    ML_Spot: _ClassVar[MediaLocation]

class TrackListFilter(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    All: _ClassVar[TrackListFilter]
    Selected: _ClassVar[TrackListFilter]
    SelectedExplicitly: _ClassVar[TrackListFilter]
    SelectedImplicitly: _ClassVar[TrackListFilter]
    WithClipsOnMainPlaylist: _ClassVar[TrackListFilter]
    WithAutomationOnMainPlaylist: _ClassVar[TrackListFilter]
    Inactive: _ClassVar[TrackListFilter]
    InactiveExplicitly: _ClassVar[TrackListFilter]
    InactiveImplicitly: _ClassVar[TrackListFilter]
    Hidden: _ClassVar[TrackListFilter]
    HiddenExplicitly: _ClassVar[TrackListFilter]
    HiddenImplicitly: _ClassVar[TrackListFilter]
    Locked: _ClassVar[TrackListFilter]
    Muted: _ClassVar[TrackListFilter]
    Frozen: _ClassVar[TrackListFilter]
    Open: _ClassVar[TrackListFilter]
    Online: _ClassVar[TrackListFilter]

class SpotLocationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    Start: _ClassVar[SpotLocationType]
    SyncPoint: _ClassVar[SpotLocationType]
    End: _ClassVar[SpotLocationType]

class ExportFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EF_None: _ClassVar[ExportFormat]
    EF_Mono: _ClassVar[ExportFormat]
    EF_MultipleMono: _ClassVar[ExportFormat]
    EF_Interleaved: _ClassVar[ExportFormat]

class ExportFileType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    WAV: _ClassVar[ExportFileType]
    AIFF: _ClassVar[ExportFileType]
    MXF: _ClassVar[ExportFileType]
    MP3: _ClassVar[ExportFileType]
    QuickTime: _ClassVar[ExportFileType]

class BitDepth(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    Bit_None: _ClassVar[BitDepth]
    Bit16: _ClassVar[BitDepth]
    Bit24: _ClassVar[BitDepth]
    Bit32Float: _ClassVar[BitDepth]

class ResolveDuplicateNamesBy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AutoRenaming: _ClassVar[ResolveDuplicateNamesBy]
    ReplacingWithNewFiles: _ClassVar[ResolveDuplicateNamesBy]

class ExportAsAAFFileType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AAF_WAV: _ClassVar[ExportAsAAFFileType]
    AAF_AIFF: _ClassVar[ExportAsAAFFileType]
    AAF_MXF: _ClassVar[ExportAsAAFFileType]
    AAF_Embedded: _ClassVar[ExportAsAAFFileType]

class AAFFileBitDepth(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AAF_Bit16: _ClassVar[AAFFileBitDepth]
    AAF_Bit24: _ClassVar[AAFFileBitDepth]

class CopyOption(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ConsolidateFromSourceMedia: _ClassVar[CopyOption]
    CopyFromSourceMedia: _ClassVar[CopyOption]
    LinkFromSourceMedia: _ClassVar[CopyOption]

class FileLocationTypeFilter(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    All_Files: _ClassVar[FileLocationTypeFilter]
    OnTimeline_Files: _ClassVar[FileLocationTypeFilter]
    NotOnTimeline_Files: _ClassVar[FileLocationTypeFilter]
    Online_Files: _ClassVar[FileLocationTypeFilter]
    Offline_Files: _ClassVar[FileLocationTypeFilter]
    Audio_Files: _ClassVar[FileLocationTypeFilter]
    Video_Files: _ClassVar[FileLocationTypeFilter]
    Rendered_Files: _ClassVar[FileLocationTypeFilter]
    SelectedClipsTimeline: _ClassVar[FileLocationTypeFilter]
    SelectedClipsClipsList: _ClassVar[FileLocationTypeFilter]

class AutomationDataOptions(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    All_Automation: _ClassVar[AutomationDataOptions]
    Pan_Automation: _ClassVar[AutomationDataOptions]
    PlugIn_Automation: _ClassVar[AutomationDataOptions]
    Clip_Gain: _ClassVar[AutomationDataOptions]
    Clip_Effects: _ClassVar[AutomationDataOptions]

class PasteSpecialOptions(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    Merge: _ClassVar[PasteSpecialOptions]
    MergeMidi: _ClassVar[PasteSpecialOptions]
    Repeat_To_Fill_Selection: _ClassVar[PasteSpecialOptions]
    To_Current_Automation_Type: _ClassVar[PasteSpecialOptions]
    MergeMarkers: _ClassVar[PasteSpecialOptions]

class TripleBool(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TB_None: _ClassVar[TripleBool]
    TB_False: _ClassVar[TripleBool]
    TB_True: _ClassVar[TripleBool]

class EM_SourceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PhysicalOut: _ClassVar[EM_SourceType]
    Bus: _ClassVar[EM_SourceType]
    Output: _ClassVar[EM_SourceType]

class CompressionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CT_None: _ClassVar[CompressionType]
    CT_PCM: _ClassVar[CompressionType]

class SampleRate(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SR_None: _ClassVar[SampleRate]
    SR_44100: _ClassVar[SampleRate]
    SR_48000: _ClassVar[SampleRate]
    SR_96000: _ClassVar[SampleRate]
    SR_176400: _ClassVar[SampleRate]
    SR_192000: _ClassVar[SampleRate]
    SR_88200: _ClassVar[SampleRate]

class EM_VideoExportOptions(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    VE_None: _ClassVar[EM_VideoExportOptions]
    VE_SameAsSource: _ClassVar[EM_VideoExportOptions]
    VE_Transcode: _ClassVar[EM_VideoExportOptions]

class EM_FileType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EM_None: _ClassVar[EM_FileType]
    EM_MOV: _ClassVar[EM_FileType]
    EM_WAV: _ClassVar[EM_FileType]
    EM_AIFF: _ClassVar[EM_FileType]
    EM_MP3: _ClassVar[EM_FileType]
    EM_MXFOPAtom: _ClassVar[EM_FileType]
    EM_WAVADM: _ClassVar[EM_FileType]

class EM_FileDestination(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EM_FD_None: _ClassVar[EM_FileDestination]
    EM_FD_SessionFolder: _ClassVar[EM_FileDestination]
    EM_FD_Directory: _ClassVar[EM_FileDestination]

class EM_DeliveryFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EM_DF_None: _ClassVar[EM_DeliveryFormat]
    EM_DF_FilePerMixSource: _ClassVar[EM_DeliveryFormat]
    EM_DF_SingleFile: _ClassVar[EM_DeliveryFormat]

class DP_ValueTypes(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DP_VT_double: _ClassVar[DP_ValueTypes]
    DP_VT_float: _ClassVar[DP_ValueTypes]
    DP_VT_int32: _ClassVar[DP_ValueTypes]
    DP_VT_int64: _ClassVar[DP_ValueTypes]
    DP_VT_uint32: _ClassVar[DP_ValueTypes]
    DP_VT_uint64: _ClassVar[DP_ValueTypes]
    DP_VT_sint32: _ClassVar[DP_ValueTypes]
    DP_VT_sint64: _ClassVar[DP_ValueTypes]
    DP_VT_fixed32: _ClassVar[DP_ValueTypes]
    DP_VT_fixed64: _ClassVar[DP_ValueTypes]
    DP_VT_sfixed32: _ClassVar[DP_ValueTypes]
    DP_VT_sfixed64: _ClassVar[DP_ValueTypes]
    DP_VT_bool: _ClassVar[DP_ValueTypes]
    DP_VT_string: _ClassVar[DP_ValueTypes]
    DP_VT_bytes: _ClassVar[DP_ValueTypes]
    DP_VT_enum: _ClassVar[DP_ValueTypes]
    DP_VT_object: _ClassVar[DP_ValueTypes]

class DynamicPropertyType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DP_EM_CodecInfo: _ClassVar[DynamicPropertyType]
    DP_EM_DolbyAtmosInfo: _ClassVar[DynamicPropertyType]

class TrackListType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AllTracks: _ClassVar[TrackListType]
    SelectedTracksOnly: _ClassVar[TrackListType]

class FadeHandlingType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ShowCrossfades: _ClassVar[FadeHandlingType]
    DontShowCrossfades: _ClassVar[FadeHandlingType]
    CombineCrossfadedClips: _ClassVar[FadeHandlingType]

class TextAsFileFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TextEdit: _ClassVar[TextAsFileFormat]
    UTF8: _ClassVar[TextAsFileFormat]

class ESI_OutputType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ESI_File: _ClassVar[ESI_OutputType]
    ESI_String: _ClassVar[ESI_OutputType]
    ESI_Unknown: _ClassVar[ESI_OutputType]

class PM_PlaybackMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PM_Normal: _ClassVar[PM_PlaybackMode]
    PM_Loop: _ClassVar[PM_PlaybackMode]
    PM_DynamicTransport: _ClassVar[PM_PlaybackMode]

class RM_RecordMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RM_Normal: _ClassVar[RM_RecordMode]
    RM_Loop: _ClassVar[RM_RecordMode]
    RM_Destructive: _ClassVar[RM_RecordMode]
    RM_QuickPunch: _ClassVar[RM_RecordMode]
    RM_TrackPunch: _ClassVar[RM_RecordMode]
    RM_DestructivePunch: _ClassVar[RM_RecordMode]

class SessionAudioFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SAF_WAVE: _ClassVar[SessionAudioFormat]
    SAF_AIFF: _ClassVar[SessionAudioFormat]

class SessionTimeCodeRate(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    STCR_Fps23976: _ClassVar[SessionTimeCodeRate]
    STCR_Fps24: _ClassVar[SessionTimeCodeRate]
    STCR_Fps25: _ClassVar[SessionTimeCodeRate]
    STCR_Fps2997: _ClassVar[SessionTimeCodeRate]
    STCR_Fps2997Drop: _ClassVar[SessionTimeCodeRate]
    STCR_Fps30: _ClassVar[SessionTimeCodeRate]
    STCR_Fps30Drop: _ClassVar[SessionTimeCodeRate]
    STCR_Fps47952: _ClassVar[SessionTimeCodeRate]
    STCR_Fps48: _ClassVar[SessionTimeCodeRate]
    STCR_Fps50: _ClassVar[SessionTimeCodeRate]
    STCR_Fps5994: _ClassVar[SessionTimeCodeRate]
    STCR_Fps5994Drop: _ClassVar[SessionTimeCodeRate]
    STCR_Fps60: _ClassVar[SessionTimeCodeRate]
    STCR_Fps60Drop: _ClassVar[SessionTimeCodeRate]
    STCR_Fps100: _ClassVar[SessionTimeCodeRate]
    STCR_Fps11988: _ClassVar[SessionTimeCodeRate]
    STCR_Fps11988Drop: _ClassVar[SessionTimeCodeRate]
    STCR_Fps120: _ClassVar[SessionTimeCodeRate]
    STCR_Fps120Drop: _ClassVar[SessionTimeCodeRate]

class SessionFeetFramesRate(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SFFR_Fps23976: _ClassVar[SessionFeetFramesRate]
    SFFR_Fps24: _ClassVar[SessionFeetFramesRate]
    SFFR_Fps25: _ClassVar[SessionFeetFramesRate]

class SessionRatePull(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SRP_None: _ClassVar[SessionRatePull]
    SRP_Up01: _ClassVar[SessionRatePull]
    SRP_Down01: _ClassVar[SessionRatePull]
    SRP_Up4: _ClassVar[SessionRatePull]
    SRP_Up4Up01: _ClassVar[SessionRatePull]
    SRP_Up4Down01: _ClassVar[SessionRatePull]
    SRP_Down4: _ClassVar[SessionRatePull]
    SRP_Down4Up01: _ClassVar[SessionRatePull]
    SRP_Down4Down01: _ClassVar[SessionRatePull]

class TS_TransportState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TS_TransportPlaying: _ClassVar[TS_TransportState]
    TS_TransportStopped: _ClassVar[TS_TransportState]
    TS_TransportRecording: _ClassVar[TS_TransportState]
    TS_TransportPlayingHalfSpeed: _ClassVar[TS_TransportState]
    TS_TransportRecordingHalfSpeed: _ClassVar[TS_TransportState]
    TS_TransportFastForward: _ClassVar[TS_TransportState]
    TS_TransportRewind: _ClassVar[TS_TransportState]
    TS_TransportScrub: _ClassVar[TS_TransportState]
    TS_TransportShuttle: _ClassVar[TS_TransportState]
    TS_TransportPrimed: _ClassVar[TS_TransportState]
    TS_TransportIsCueing: _ClassVar[TS_TransportState]
    TS_TransportIsCued: _ClassVar[TS_TransportState]
    TS_TransportIsCuedForPreview: _ClassVar[TS_TransportState]
    TS_TransportIsStopping: _ClassVar[TS_TransportState]
    TS_TransportIsPreviewing: _ClassVar[TS_TransportState]

class CL_ClipLocation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CL_ClipsList: _ClassVar[CL_ClipLocation]
    CL_Timeline: _ClassVar[CL_ClipLocation]

class TimeProperties(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TP_Marker: _ClassVar[TimeProperties]
    TP_Selection: _ClassVar[TimeProperties]
    TP_None: _ClassVar[TimeProperties]

class MemoryLocationReference(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MLR_BarBeat: _ClassVar[MemoryLocationReference]
    MLR_Absolute: _ClassVar[MemoryLocationReference]
    MLR_FollowTrackTimebase: _ClassVar[MemoryLocationReference]

class MarkerLocation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MLC_Unknown: _ClassVar[MarkerLocation]
    MLC_MainRuler: _ClassVar[MarkerLocation]
    MLC_Track: _ClassVar[MarkerLocation]

class TrackInsertionPoint(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TIPoint_Unknown: _ClassVar[TrackInsertionPoint]
    TIPoint_Before: _ClassVar[TrackInsertionPoint]
    TIPoint_After: _ClassVar[TrackInsertionPoint]
    TIPoint_First: _ClassVar[TrackInsertionPoint]
    TIPoint_Last: _ClassVar[TrackInsertionPoint]

class EditMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EMO_Unknown: _ClassVar[EditMode]
    EMO_Shuffle: _ClassVar[EditMode]
    EMO_Slip: _ClassVar[EditMode]
    EMO_Spot: _ClassVar[EditMode]
    EMO_GridAbsolute: _ClassVar[EditMode]
    EMO_GridRelative: _ClassVar[EditMode]
    EMO_ShuffleSnapToGridAbsolute: _ClassVar[EditMode]
    EMO_SlipSnapToGridAbsolute: _ClassVar[EditMode]
    EMO_SpotSnapToGridAbsolute: _ClassVar[EditMode]
    EMO_ShuffleSnapToGridRelative: _ClassVar[EditMode]
    EMO_SlipSnapToGridRelative: _ClassVar[EditMode]
    EMO_SpotSnapToGridRelative: _ClassVar[EditMode]

class EditTool(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ET_Unknown: _ClassVar[EditTool]
    ET_ZoomNormal: _ClassVar[EditTool]
    ET_ZoomSingle: _ClassVar[EditTool]
    ET_TrimStandard: _ClassVar[EditTool]
    ET_TrimTce: _ClassVar[EditTool]
    ET_TrimScrub: _ClassVar[EditTool]
    ET_TrimLoop: _ClassVar[EditTool]
    ET_Selector: _ClassVar[EditTool]
    ET_GrabberTime: _ClassVar[EditTool]
    ET_GrabberSeparation: _ClassVar[EditTool]
    ET_GrabberObject: _ClassVar[EditTool]
    ET_SmartTool: _ClassVar[EditTool]
    ET_Scrubber: _ClassVar[EditTool]
    ET_PencilFreeHand: _ClassVar[EditTool]
    ET_PencilLine: _ClassVar[EditTool]
    ET_PencilTriangle: _ClassVar[EditTool]
    ET_PencilSquare: _ClassVar[EditTool]
    ET_PencilRandom: _ClassVar[EditTool]
    ET_PencilParabolic: _ClassVar[EditTool]
    ET_PencilSCurve: _ClassVar[EditTool]

class TimelineUpdateVideo(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TUV_Unknown: _ClassVar[TimelineUpdateVideo]
    TUV_None: _ClassVar[TimelineUpdateVideo]
    TUV_In: _ClassVar[TimelineUpdateVideo]
    TUV_Out: _ClassVar[TimelineUpdateVideo]

class SelectionMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SM_Unknown: _ClassVar[SelectionMode]
    SM_Replace: _ClassVar[SelectionMode]
    SM_Add: _ClassVar[SelectionMode]
    SM_Subtract: _ClassVar[SelectionMode]

class TrackFromClipGroupExclusionReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TCGEReason_Unknown: _ClassVar[TrackFromClipGroupExclusionReason]
    TCGEReason_TrackTypeIsNotAllowed: _ClassVar[TrackFromClipGroupExclusionReason]
    TCGEReason_TrackIsFrozen: _ClassVar[TrackFromClipGroupExclusionReason]
    TCGEReason_TrackIsClosed: _ClassVar[TrackFromClipGroupExclusionReason]
    TCGEReason_TrackIsLocked: _ClassVar[TrackFromClipGroupExclusionReason]
    TCGEReason_TrackIsInPlaylistView: _ClassVar[TrackFromClipGroupExclusionReason]
    TCGEReason_TrackIsElasticAudioWithFades: _ClassVar[TrackFromClipGroupExclusionReason]
CreateSession: CommandId
OpenSession: CommandId
Import: CommandId
GetTrackList: CommandId
SelectAllClipsOnTrack: CommandId
ExtendSelectionToTargetTracks: CommandId
TrimToSelection: CommandId
CreateFadesBasedOnPreset: CommandId
RenameTargetTrack: CommandId
ConsolidateClip: CommandId
ExportClipsAsFiles: CommandId
ExportSelectedTracksAsAAFOMF: CommandId
GetTaskStatus: CommandId
HostReadyCheck: CommandId
RefreshTargetAudioFiles: CommandId
RefreshAllModifiedAudioFiles: CommandId
GetFileLocation: CommandId
CloseSession: CommandId
SaveSession: CommandId
SaveSessionAs: CommandId
Cut: CommandId
Copy: CommandId
Paste: CommandId
Clear: CommandId
CutSpecial: CommandId
CopySpecial: CommandId
ClearSpecial: CommandId
PasteSpecial: CommandId
ExportMix: CommandId
Spot: CommandId
ExportSessionInfoAsText: CommandId
GetDynamicProperties: CommandId
SetPlaybackMode: CommandId
SetRecordMode: CommandId
GetSessionAudioFormat: CommandId
GetSessionSampleRate: CommandId
GetSessionBitDepth: CommandId
GetSessionInterleavedState: CommandId
GetSessionTimeCodeRate: CommandId
GetSessionFeetFramesRate: CommandId
GetSessionAudioRatePullSettings: CommandId
GetSessionVideoRatePullSettings: CommandId
GetSessionName: CommandId
GetSessionPath: CommandId
GetSessionStartTime: CommandId
GetSessionLength: CommandId
SetSessionAudioFormat: CommandId
SetSessionBitDepth: CommandId
SetSessionInterleavedState: CommandId
SetSessionTimeCodeRate: CommandId
SetSessionFeetFramesRate: CommandId
SetSessionAudioRatePullSettings: CommandId
SetSessionVideoRatePullSettings: CommandId
SetSessionStartTime: CommandId
SetSessionLength: CommandId
GetPTSLVersion: CommandId
GetPlaybackMode: CommandId
GetRecordMode: CommandId
GetTransportArmed: CommandId
GetTransportState: CommandId
ClearMemoryLocation: CommandId
RenameSelectedClip: CommandId
RenameTargetClip: CommandId
TogglePlayState: CommandId
ToggleRecordEnable: CommandId
PlayHalfSpeed: CommandId
RecordHalfSpeed: CommandId
EditMemoryLocation: CommandId
GetMemoryLocations: CommandId
RegisterConnection: CommandId
CreateMemoryLocation: CommandId
CreateNewTracks: CommandId
SelectTracksByName: CommandId
GetEditMode: CommandId
SetEditMode: CommandId
GetEditTool: CommandId
SetEditTool: CommandId
RecallZoomPreset: CommandId
GetEditModeOptions: CommandId
SetEditModeOptions: CommandId
SetTimelineSelection: CommandId
GetTimelineSelection: CommandId
ImportVideo: CommandId
SelectMemoryLocation: CommandId
SetTrackMuteState: CommandId
SetTrackSoloState: CommandId
SetTrackSoloSafeState: CommandId
SetTrackRecordEnableState: CommandId
SetTrackRecordSafeEnableState: CommandId
SetTrackInputMonitorState: CommandId
SetTrackSmartDspState: CommandId
SetTrackHiddenState: CommandId
SetTrackInactiveState: CommandId
SetTrackFrozenState: CommandId
SetTrackOnlineState: CommandId
SetTrackOpenState: CommandId
GetSessionIDs: CommandId
GetMemoryLocationsManageMode: CommandId
SetMemoryLocationsManageMode: CommandId
SetMainCounterFormat: CommandId
SetSubCounterFormat: CommandId
GetMainCounterFormat: CommandId
GetSubCounterFormat: CommandId
Undo: CommandId
Redo: CommandId
UndoAll: CommandId
RedoAll: CommandId
ClearUndoQueue: CommandId
SetTrackDSPModeSafeState: CommandId
GetSessionSystemDelayInfo: CommandId
GroupClips: CommandId
UngroupClips: CommandId
UngroupAllClips: CommandId
RegroupClips: CommandId
RepeatSelection: CommandId
DuplicateSelection: CommandId
Queued: TaskStatus
Pending: TaskStatus
InProgress: TaskStatus
Completed: TaskStatus
Failed: TaskStatus
WaitingForUserInput: TaskStatus
CompletedWithBadResponse: TaskStatus
FailedWithBadErrorResponse: TaskStatus
OS_WritePermissions: CommandErrorType
OS_ErrorCode: CommandErrorType
OS_NoLocationFound: CommandErrorType
OS_NoSessionFound: CommandErrorType
OS_FilePathLocation: CommandErrorType
OS_ReadError: CommandErrorType
OS_DiskSpace: CommandErrorType
OS_DuplicateName: CommandErrorType
OS_IllegalCharacters: CommandErrorType
OS_CharactersLimit: CommandErrorType
OS_ProToolsIsNotAvailable: CommandErrorType
OS_NoFilePathFound: CommandErrorType
PT_UnknownError: CommandErrorType
PT_NoTemplateGroup: CommandErrorType
PT_NoTemplate: CommandErrorType
PT_SampleRateMismatch: CommandErrorType
PT_NoVideoTrackFound: CommandErrorType
PT_NoTracksFound: CommandErrorType
PT_NoOpenedSession: CommandErrorType
PT_NoTrackFound: CommandErrorType
PT_NoClipsFound: CommandErrorType
PT_NoSelection: CommandErrorType
PT_RecordDrive: CommandErrorType
PT_NoPresetFound: CommandErrorType
PT_FileTypeMXF: CommandErrorType
PT_CopyOptionCopy: CommandErrorType
PT_CopyOptionLink: CommandErrorType
PT_QuantizeEdits: CommandErrorType
PT_ExportAsMultichannel: CommandErrorType
PT_IllegalCharactersComments: CommandErrorType
PT_IllegalCharactersSequenceName: CommandErrorType
PT_MaxCharactersComments: CommandErrorType
PT_MaxCharactersSequenceName: CommandErrorType
PT_NoSequenceName: CommandErrorType
PT_InvalidTask: CommandErrorType
PT_FileNotFound: CommandErrorType
PT_InvalidSelection: CommandErrorType
PT_ReadOnlySession: CommandErrorType
PT_InvalidParameter: CommandErrorType
PT_Forbidden: CommandErrorType
PT_NoTimelineFound: CommandErrorType
PT_ArgumentOutOfRange: CommandErrorType
PT_ForbiddenTrackType: CommandErrorType
PT_NoVideoEngineFound: CommandErrorType
PT_NoDspHardwareFound: CommandErrorType
PT_UnsupportedCommand: CommandErrorType
PT_HostNotReady: CommandErrorType
PT_CannotBeDone: CommandErrorType
PT_ResponseLengthExceeded: CommandErrorType
PT_Info: CommandErrorType
SDK_VersionMismatch: CommandErrorType
SDK_NotImplemented: CommandErrorType
TT_Unknown: TrackType
Unknown: TrackType
TT_Midi: TrackType
Midi: TrackType
TT_Audio: TrackType
AudioTrack: TrackType
TT_Aux: TrackType
Aux: TrackType
TT_Video: TrackType
VideoTrack: TrackType
TT_Vca: TrackType
Vca: TrackType
TT_Tempo: TrackType
Tempo: TrackType
TT_Markers: TrackType
Markers: TrackType
TT_Meter: TrackType
Meter: TrackType
TT_KeySignature: TrackType
KeySignature: TrackType
TT_ChordSymbols: TrackType
ChordSymbols: TrackType
TT_Instrument: TrackType
Instrument: TrackType
TT_Master: TrackType
Master: TrackType
TT_Heat: TrackType
Heat: TrackType
TT_BasicFolder: TrackType
BasicFolder: TrackType
TT_RoutingFolder: TrackType
RoutingFolder: TrackType
TT_CompLane: TrackType
CompLane: TrackType
TF_Unknown: TrackFormat
TF_Mono: TrackFormat
TF_Stereo: TrackFormat
TF_LCR: TrackFormat
TF_LCRS: TrackFormat
TF_Quad: TrackFormat
TF_5_0: TrackFormat
TF_5_1: TrackFormat
TF_5_0_2: TrackFormat
TF_5_1_2: TrackFormat
TF_5_0_4: TrackFormat
TF_5_1_4: TrackFormat
TF_6_0: TrackFormat
TF_6_1: TrackFormat
TF_7_0: TrackFormat
TF_7_1: TrackFormat
TF_7_0_SDDS: TrackFormat
TF_7_1_SDDS: TrackFormat
TF_7_0_2: TrackFormat
TF_7_1_2: TrackFormat
TF_7_0_4: TrackFormat
TF_7_1_4: TrackFormat
TF_7_0_6: TrackFormat
TF_7_1_6: TrackFormat
TF_9_0_4: TrackFormat
TF_9_1_4: TrackFormat
TF_9_0_6: TrackFormat
TF_9_1_6: TrackFormat
TF_1stOrderAmbisonics: TrackFormat
TF_2ndOrderAmbisonics: TrackFormat
TF_3rdOrderAmbisonics: TrackFormat
TF_4thOrderAmbisonics: TrackFormat
TF_5thOrderAmbisonics: TrackFormat
TF_6thOrderAmbisonics: TrackFormat
TF_7thOrderAmbisonics: TrackFormat
TF_None: TrackFormat
TF_2_1: TrackFormat
TF_Overhead: TrackFormat
TTB_Unknown: TrackTimebase
TTB_Samples: TrackTimebase
TTB_Ticks: TrackTimebase
TTB_None: TrackTimebase
None: TrackAttributeState
SetExplicitly: TrackAttributeState
SetImplicitly: TrackAttributeState
SetExplicitlyAndImplicitly: TrackAttributeState
FT_WAVE: FileType
FT_AIFF: FileType
FT_AAF: FileType
FT_OMF: FileType
IO_None: IOSettings
IO_Last: IOSettings
IO_StereoMix: IOSettings
IO_51FilmMix: IOSettings
IO_51SMPTEMix: IOSettings
IO_51DTSMix: IOSettings
IO_UserDefined: IOSettings
Session: ImportType
Audio: ImportType
LinkToSourceAudio: AudioMediaOptions
CopyFromSourceAudio: AudioMediaOptions
ConsolidateFromSourceAudio: AudioMediaOptions
ForceToTargetSessionFormat: AudioMediaOptions
LinkToSourceVideo: VideoMediaOptions
CopyFromSourceVideo: VideoMediaOptions
ImportAsOfflineSatelliteMedia: VideoMediaOptions
MT_None: MatchTrackOptions
MT_MatchTracks: MatchTrackOptions
MT_ImportAsNewTrack: MatchTrackOptions
MaintainAbsoluteTimeCodeValues: TimeCodeMappingOptions
MaintainRelativeTimeCodeValues: TimeCodeMappingOptions
MapStartTimeCodeTo: TimeCodeMappingOptions
BarsBeats: TrackOffsetOptions
MinSecs: TrackOffsetOptions
TimeCode: TrackOffsetOptions
FeetFrames: TrackOffsetOptions
Samples: TrackOffsetOptions
Low: ConversionQuality
Good: ConversionQuality
Better: ConversionQuality
Best: ConversionQuality
TweakHead: ConversionQuality
ImportReplaceExistingPlaylists: MainPlaylistOptions
ImportOverlayNewOnExistingPlaylists: MainPlaylistOptions
DoNotImport: MainPlaylistOptions
AddAudio: AudioOperations
CopyAudio: AudioOperations
ConvertAudio: AudioOperations
Default: AudioOperations
MD_None: MediaDestination
MD_MainVideoTrack: MediaDestination
MD_NewTrack: MediaDestination
MD_ClipList: MediaDestination
ML_None: MediaLocation
ML_SessionStart: MediaLocation
ML_SongStart: MediaLocation
ML_Selection: MediaLocation
ML_Spot: MediaLocation
All: TrackListFilter
Selected: TrackListFilter
SelectedExplicitly: TrackListFilter
SelectedImplicitly: TrackListFilter
WithClipsOnMainPlaylist: TrackListFilter
WithAutomationOnMainPlaylist: TrackListFilter
Inactive: TrackListFilter
InactiveExplicitly: TrackListFilter
InactiveImplicitly: TrackListFilter
Hidden: TrackListFilter
HiddenExplicitly: TrackListFilter
HiddenImplicitly: TrackListFilter
Locked: TrackListFilter
Muted: TrackListFilter
Frozen: TrackListFilter
Open: TrackListFilter
Online: TrackListFilter
Start: SpotLocationType
SyncPoint: SpotLocationType
End: SpotLocationType
EF_None: ExportFormat
EF_Mono: ExportFormat
EF_MultipleMono: ExportFormat
EF_Interleaved: ExportFormat
WAV: ExportFileType
AIFF: ExportFileType
MXF: ExportFileType
MP3: ExportFileType
QuickTime: ExportFileType
Bit_None: BitDepth
Bit16: BitDepth
Bit24: BitDepth
Bit32Float: BitDepth
AutoRenaming: ResolveDuplicateNamesBy
ReplacingWithNewFiles: ResolveDuplicateNamesBy
AAF_WAV: ExportAsAAFFileType
AAF_AIFF: ExportAsAAFFileType
AAF_MXF: ExportAsAAFFileType
AAF_Embedded: ExportAsAAFFileType
AAF_Bit16: AAFFileBitDepth
AAF_Bit24: AAFFileBitDepth
ConsolidateFromSourceMedia: CopyOption
CopyFromSourceMedia: CopyOption
LinkFromSourceMedia: CopyOption
All_Files: FileLocationTypeFilter
OnTimeline_Files: FileLocationTypeFilter
NotOnTimeline_Files: FileLocationTypeFilter
Online_Files: FileLocationTypeFilter
Offline_Files: FileLocationTypeFilter
Audio_Files: FileLocationTypeFilter
Video_Files: FileLocationTypeFilter
Rendered_Files: FileLocationTypeFilter
SelectedClipsTimeline: FileLocationTypeFilter
SelectedClipsClipsList: FileLocationTypeFilter
All_Automation: AutomationDataOptions
Pan_Automation: AutomationDataOptions
PlugIn_Automation: AutomationDataOptions
Clip_Gain: AutomationDataOptions
Clip_Effects: AutomationDataOptions
Merge: PasteSpecialOptions
MergeMidi: PasteSpecialOptions
Repeat_To_Fill_Selection: PasteSpecialOptions
To_Current_Automation_Type: PasteSpecialOptions
MergeMarkers: PasteSpecialOptions
TB_None: TripleBool
TB_False: TripleBool
TB_True: TripleBool
PhysicalOut: EM_SourceType
Bus: EM_SourceType
Output: EM_SourceType
CT_None: CompressionType
CT_PCM: CompressionType
SR_None: SampleRate
SR_44100: SampleRate
SR_48000: SampleRate
SR_96000: SampleRate
SR_176400: SampleRate
SR_192000: SampleRate
SR_88200: SampleRate
VE_None: EM_VideoExportOptions
VE_SameAsSource: EM_VideoExportOptions
VE_Transcode: EM_VideoExportOptions
EM_None: EM_FileType
EM_MOV: EM_FileType
EM_WAV: EM_FileType
EM_AIFF: EM_FileType
EM_MP3: EM_FileType
EM_MXFOPAtom: EM_FileType
EM_WAVADM: EM_FileType
EM_FD_None: EM_FileDestination
EM_FD_SessionFolder: EM_FileDestination
EM_FD_Directory: EM_FileDestination
EM_DF_None: EM_DeliveryFormat
EM_DF_FilePerMixSource: EM_DeliveryFormat
EM_DF_SingleFile: EM_DeliveryFormat
DP_VT_double: DP_ValueTypes
DP_VT_float: DP_ValueTypes
DP_VT_int32: DP_ValueTypes
DP_VT_int64: DP_ValueTypes
DP_VT_uint32: DP_ValueTypes
DP_VT_uint64: DP_ValueTypes
DP_VT_sint32: DP_ValueTypes
DP_VT_sint64: DP_ValueTypes
DP_VT_fixed32: DP_ValueTypes
DP_VT_fixed64: DP_ValueTypes
DP_VT_sfixed32: DP_ValueTypes
DP_VT_sfixed64: DP_ValueTypes
DP_VT_bool: DP_ValueTypes
DP_VT_string: DP_ValueTypes
DP_VT_bytes: DP_ValueTypes
DP_VT_enum: DP_ValueTypes
DP_VT_object: DP_ValueTypes
DP_EM_CodecInfo: DynamicPropertyType
DP_EM_DolbyAtmosInfo: DynamicPropertyType
AllTracks: TrackListType
SelectedTracksOnly: TrackListType
ShowCrossfades: FadeHandlingType
DontShowCrossfades: FadeHandlingType
CombineCrossfadedClips: FadeHandlingType
TextEdit: TextAsFileFormat
UTF8: TextAsFileFormat
ESI_File: ESI_OutputType
ESI_String: ESI_OutputType
ESI_Unknown: ESI_OutputType
PM_Normal: PM_PlaybackMode
PM_Loop: PM_PlaybackMode
PM_DynamicTransport: PM_PlaybackMode
RM_Normal: RM_RecordMode
RM_Loop: RM_RecordMode
RM_Destructive: RM_RecordMode
RM_QuickPunch: RM_RecordMode
RM_TrackPunch: RM_RecordMode
RM_DestructivePunch: RM_RecordMode
SAF_WAVE: SessionAudioFormat
SAF_AIFF: SessionAudioFormat
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
STCR_Fps100: SessionTimeCodeRate
STCR_Fps11988: SessionTimeCodeRate
STCR_Fps11988Drop: SessionTimeCodeRate
STCR_Fps120: SessionTimeCodeRate
STCR_Fps120Drop: SessionTimeCodeRate
SFFR_Fps23976: SessionFeetFramesRate
SFFR_Fps24: SessionFeetFramesRate
SFFR_Fps25: SessionFeetFramesRate
SRP_None: SessionRatePull
SRP_Up01: SessionRatePull
SRP_Down01: SessionRatePull
SRP_Up4: SessionRatePull
SRP_Up4Up01: SessionRatePull
SRP_Up4Down01: SessionRatePull
SRP_Down4: SessionRatePull
SRP_Down4Up01: SessionRatePull
SRP_Down4Down01: SessionRatePull
TS_TransportPlaying: TS_TransportState
TS_TransportStopped: TS_TransportState
TS_TransportRecording: TS_TransportState
TS_TransportPlayingHalfSpeed: TS_TransportState
TS_TransportRecordingHalfSpeed: TS_TransportState
TS_TransportFastForward: TS_TransportState
TS_TransportRewind: TS_TransportState
TS_TransportScrub: TS_TransportState
TS_TransportShuttle: TS_TransportState
TS_TransportPrimed: TS_TransportState
TS_TransportIsCueing: TS_TransportState
TS_TransportIsCued: TS_TransportState
TS_TransportIsCuedForPreview: TS_TransportState
TS_TransportIsStopping: TS_TransportState
TS_TransportIsPreviewing: TS_TransportState
CL_ClipsList: CL_ClipLocation
CL_Timeline: CL_ClipLocation
TP_Marker: TimeProperties
TP_Selection: TimeProperties
TP_None: TimeProperties
MLR_BarBeat: MemoryLocationReference
MLR_Absolute: MemoryLocationReference
MLR_FollowTrackTimebase: MemoryLocationReference
MLC_Unknown: MarkerLocation
MLC_MainRuler: MarkerLocation
MLC_Track: MarkerLocation
TIPoint_Unknown: TrackInsertionPoint
TIPoint_Before: TrackInsertionPoint
TIPoint_After: TrackInsertionPoint
TIPoint_First: TrackInsertionPoint
TIPoint_Last: TrackInsertionPoint
EMO_Unknown: EditMode
EMO_Shuffle: EditMode
EMO_Slip: EditMode
EMO_Spot: EditMode
EMO_GridAbsolute: EditMode
EMO_GridRelative: EditMode
EMO_ShuffleSnapToGridAbsolute: EditMode
EMO_SlipSnapToGridAbsolute: EditMode
EMO_SpotSnapToGridAbsolute: EditMode
EMO_ShuffleSnapToGridRelative: EditMode
EMO_SlipSnapToGridRelative: EditMode
EMO_SpotSnapToGridRelative: EditMode
ET_Unknown: EditTool
ET_ZoomNormal: EditTool
ET_ZoomSingle: EditTool
ET_TrimStandard: EditTool
ET_TrimTce: EditTool
ET_TrimScrub: EditTool
ET_TrimLoop: EditTool
ET_Selector: EditTool
ET_GrabberTime: EditTool
ET_GrabberSeparation: EditTool
ET_GrabberObject: EditTool
ET_SmartTool: EditTool
ET_Scrubber: EditTool
ET_PencilFreeHand: EditTool
ET_PencilLine: EditTool
ET_PencilTriangle: EditTool
ET_PencilSquare: EditTool
ET_PencilRandom: EditTool
ET_PencilParabolic: EditTool
ET_PencilSCurve: EditTool
TUV_Unknown: TimelineUpdateVideo
TUV_None: TimelineUpdateVideo
TUV_In: TimelineUpdateVideo
TUV_Out: TimelineUpdateVideo
SM_Unknown: SelectionMode
SM_Replace: SelectionMode
SM_Add: SelectionMode
SM_Subtract: SelectionMode
TCGEReason_Unknown: TrackFromClipGroupExclusionReason
TCGEReason_TrackTypeIsNotAllowed: TrackFromClipGroupExclusionReason
TCGEReason_TrackIsFrozen: TrackFromClipGroupExclusionReason
TCGEReason_TrackIsClosed: TrackFromClipGroupExclusionReason
TCGEReason_TrackIsLocked: TrackFromClipGroupExclusionReason
TCGEReason_TrackIsInPlaylistView: TrackFromClipGroupExclusionReason
TCGEReason_TrackIsElasticAudioWithFades: TrackFromClipGroupExclusionReason

class EmptyMessage(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CommandError(_message.Message):
    __slots__ = ("command_error_type", "command_error_message", "is_warning")
    COMMAND_ERROR_TYPE_FIELD_NUMBER: _ClassVar[int]
    COMMAND_ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    IS_WARNING_FIELD_NUMBER: _ClassVar[int]
    command_error_type: CommandErrorType
    command_error_message: str
    is_warning: bool
    def __init__(self, command_error_type: _Optional[_Union[CommandErrorType, str]] = ..., command_error_message: _Optional[str] = ..., is_warning: bool = ...) -> None: ...

class ResponseError(_message.Message):
    __slots__ = ("errors",)
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    errors: _containers.RepeatedCompositeFieldContainer[CommandError]
    def __init__(self, errors: _Optional[_Iterable[_Union[CommandError, _Mapping]]] = ...) -> None: ...

class RequestHeader(_message.Message):
    __slots__ = ("task_id", "command", "version", "session_id")
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    task_id: str
    command: CommandId
    version: int
    session_id: str
    def __init__(self, task_id: _Optional[str] = ..., command: _Optional[_Union[CommandId, str]] = ..., version: _Optional[int] = ..., session_id: _Optional[str] = ...) -> None: ...

class Request(_message.Message):
    __slots__ = ("header", "request_body_json")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    REQUEST_BODY_JSON_FIELD_NUMBER: _ClassVar[int]
    header: RequestHeader
    request_body_json: str
    def __init__(self, header: _Optional[_Union[RequestHeader, _Mapping]] = ..., request_body_json: _Optional[str] = ...) -> None: ...

class ResponseHeader(_message.Message):
    __slots__ = ("task_id", "command", "status", "progress")
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    task_id: str
    command: CommandId
    status: TaskStatus
    progress: int
    def __init__(self, task_id: _Optional[str] = ..., command: _Optional[_Union[CommandId, str]] = ..., status: _Optional[_Union[TaskStatus, str]] = ..., progress: _Optional[int] = ...) -> None: ...

class Response(_message.Message):
    __slots__ = ("header", "response_body_json", "response_error_json")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_BODY_JSON_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_ERROR_JSON_FIELD_NUMBER: _ClassVar[int]
    header: ResponseHeader
    response_body_json: str
    response_error_json: str
    def __init__(self, header: _Optional[_Union[ResponseHeader, _Mapping]] = ..., response_body_json: _Optional[str] = ..., response_error_json: _Optional[str] = ...) -> None: ...

class PaginationRequest(_message.Message):
    __slots__ = ("limit", "offset")
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    limit: int
    offset: int
    def __init__(self, limit: _Optional[int] = ..., offset: _Optional[int] = ...) -> None: ...

class Pagination(_message.Message):
    __slots__ = ("total", "limit", "offset")
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    total: int
    limit: int
    offset: int
    def __init__(self, total: _Optional[int] = ..., limit: _Optional[int] = ..., offset: _Optional[int] = ...) -> None: ...

class PaginationResponse(_message.Message):
    __slots__ = ("total", "limit", "offset")
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    total: int
    limit: int
    offset: int
    def __init__(self, total: _Optional[int] = ..., limit: _Optional[int] = ..., offset: _Optional[int] = ...) -> None: ...

class TrackAttributes(_message.Message):
    __slots__ = ("is_inactive", "is_hidden", "is_selected", "contains_clips", "contains_automation", "is_soloed", "is_record_enabled", "is_input_monitoring_on", "is_smart_dsp_on", "is_locked", "is_muted", "is_frozen", "is_open", "is_online", "is_record_enabled_safe", "is_smart_dsp_on_safe", "is_soloed_safe")
    IS_INACTIVE_FIELD_NUMBER: _ClassVar[int]
    IS_HIDDEN_FIELD_NUMBER: _ClassVar[int]
    IS_SELECTED_FIELD_NUMBER: _ClassVar[int]
    CONTAINS_CLIPS_FIELD_NUMBER: _ClassVar[int]
    CONTAINS_AUTOMATION_FIELD_NUMBER: _ClassVar[int]
    IS_SOLOED_FIELD_NUMBER: _ClassVar[int]
    IS_RECORD_ENABLED_FIELD_NUMBER: _ClassVar[int]
    IS_INPUT_MONITORING_ON_FIELD_NUMBER: _ClassVar[int]
    IS_SMART_DSP_ON_FIELD_NUMBER: _ClassVar[int]
    IS_LOCKED_FIELD_NUMBER: _ClassVar[int]
    IS_MUTED_FIELD_NUMBER: _ClassVar[int]
    IS_FROZEN_FIELD_NUMBER: _ClassVar[int]
    IS_OPEN_FIELD_NUMBER: _ClassVar[int]
    IS_ONLINE_FIELD_NUMBER: _ClassVar[int]
    IS_RECORD_ENABLED_SAFE_FIELD_NUMBER: _ClassVar[int]
    IS_SMART_DSP_ON_SAFE_FIELD_NUMBER: _ClassVar[int]
    IS_SOLOED_SAFE_FIELD_NUMBER: _ClassVar[int]
    is_inactive: TrackAttributeState
    is_hidden: TrackAttributeState
    is_selected: TrackAttributeState
    contains_clips: bool
    contains_automation: bool
    is_soloed: bool
    is_record_enabled: bool
    is_input_monitoring_on: TrackAttributeState
    is_smart_dsp_on: bool
    is_locked: bool
    is_muted: bool
    is_frozen: bool
    is_open: bool
    is_online: bool
    is_record_enabled_safe: bool
    is_smart_dsp_on_safe: bool
    is_soloed_safe: bool
    def __init__(self, is_inactive: _Optional[_Union[TrackAttributeState, str]] = ..., is_hidden: _Optional[_Union[TrackAttributeState, str]] = ..., is_selected: _Optional[_Union[TrackAttributeState, str]] = ..., contains_clips: bool = ..., contains_automation: bool = ..., is_soloed: bool = ..., is_record_enabled: bool = ..., is_input_monitoring_on: _Optional[_Union[TrackAttributeState, str]] = ..., is_smart_dsp_on: bool = ..., is_locked: bool = ..., is_muted: bool = ..., is_frozen: bool = ..., is_open: bool = ..., is_online: bool = ..., is_record_enabled_safe: bool = ..., is_smart_dsp_on_safe: bool = ..., is_soloed_safe: bool = ...) -> None: ...

class Track(_message.Message):
    __slots__ = ("name", "type", "id", "index", "color", "track_attributes", "id_compressed", "format", "timebase")
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    TRACK_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    ID_COMPRESSED_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    TIMEBASE_FIELD_NUMBER: _ClassVar[int]
    name: str
    type: TrackType
    id: str
    index: int
    color: str
    track_attributes: TrackAttributes
    id_compressed: str
    format: TrackFormat
    timebase: TrackTimebase
    def __init__(self, name: _Optional[str] = ..., type: _Optional[_Union[TrackType, str]] = ..., id: _Optional[str] = ..., index: _Optional[int] = ..., color: _Optional[str] = ..., track_attributes: _Optional[_Union[TrackAttributes, _Mapping]] = ..., id_compressed: _Optional[str] = ..., format: _Optional[_Union[TrackFormat, str]] = ..., timebase: _Optional[_Union[TrackTimebase, str]] = ...) -> None: ...

class GetTaskStatusRequestBody(_message.Message):
    __slots__ = ("task_id",)
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    task_id: str
    def __init__(self, task_id: _Optional[str] = ...) -> None: ...

class GetTaskStatusResponseBody(_message.Message):
    __slots__ = ("task_id", "status", "progress")
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    task_id: str
    status: TaskStatus
    progress: int
    def __init__(self, task_id: _Optional[str] = ..., status: _Optional[_Union[TaskStatus, str]] = ..., progress: _Optional[int] = ...) -> None: ...

class CreateSessionRequestBody(_message.Message):
    __slots__ = ("session_name", "create_from_template", "template_group", "template_name", "file_type", "sample_rate", "input_output_settings", "is_interleaved", "session_location", "is_cloud_project", "create_from_aaf", "path_to_aaf", "bit_depth")
    SESSION_NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_FROM_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_GROUP_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_NAME_FIELD_NUMBER: _ClassVar[int]
    FILE_TYPE_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_RATE_FIELD_NUMBER: _ClassVar[int]
    INPUT_OUTPUT_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    IS_INTERLEAVED_FIELD_NUMBER: _ClassVar[int]
    SESSION_LOCATION_FIELD_NUMBER: _ClassVar[int]
    IS_CLOUD_PROJECT_FIELD_NUMBER: _ClassVar[int]
    CREATE_FROM_AAF_FIELD_NUMBER: _ClassVar[int]
    PATH_TO_AAF_FIELD_NUMBER: _ClassVar[int]
    BIT_DEPTH_FIELD_NUMBER: _ClassVar[int]
    session_name: str
    create_from_template: bool
    template_group: str
    template_name: str
    file_type: FileType
    sample_rate: SampleRate
    input_output_settings: IOSettings
    is_interleaved: bool
    session_location: str
    is_cloud_project: bool
    create_from_aaf: bool
    path_to_aaf: str
    bit_depth: BitDepth
    def __init__(self, session_name: _Optional[str] = ..., create_from_template: bool = ..., template_group: _Optional[str] = ..., template_name: _Optional[str] = ..., file_type: _Optional[_Union[FileType, str]] = ..., sample_rate: _Optional[_Union[SampleRate, str]] = ..., input_output_settings: _Optional[_Union[IOSettings, str]] = ..., is_interleaved: bool = ..., session_location: _Optional[str] = ..., is_cloud_project: bool = ..., create_from_aaf: bool = ..., path_to_aaf: _Optional[str] = ..., bit_depth: _Optional[_Union[BitDepth, str]] = ...) -> None: ...

class OpenSessionRequestBody(_message.Message):
    __slots__ = ("session_path",)
    SESSION_PATH_FIELD_NUMBER: _ClassVar[int]
    session_path: str
    def __init__(self, session_path: _Optional[str] = ...) -> None: ...

class TrackDataToImport(_message.Message):
    __slots__ = ("track_data_preset_path", "clip_gain", "clips_and_media", "volume_automation")
    TRACK_DATA_PRESET_PATH_FIELD_NUMBER: _ClassVar[int]
    CLIP_GAIN_FIELD_NUMBER: _ClassVar[int]
    CLIPS_AND_MEDIA_FIELD_NUMBER: _ClassVar[int]
    VOLUME_AUTOMATION_FIELD_NUMBER: _ClassVar[int]
    track_data_preset_path: str
    clip_gain: bool
    clips_and_media: bool
    volume_automation: bool
    def __init__(self, track_data_preset_path: _Optional[str] = ..., clip_gain: bool = ..., clips_and_media: bool = ..., volume_automation: bool = ...) -> None: ...

class SessionDataImport(_message.Message):
    __slots__ = ("tempo_meter_map", "key_signature_choed_map", "markers_memory_locations", "window_configurations", "mic_pre_settings", "heat_master_settings")
    TEMPO_METER_MAP_FIELD_NUMBER: _ClassVar[int]
    KEY_SIGNATURE_CHOED_MAP_FIELD_NUMBER: _ClassVar[int]
    MARKERS_MEMORY_LOCATIONS_FIELD_NUMBER: _ClassVar[int]
    WINDOW_CONFIGURATIONS_FIELD_NUMBER: _ClassVar[int]
    MIC_PRE_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    HEAT_MASTER_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    tempo_meter_map: bool
    key_signature_choed_map: bool
    markers_memory_locations: bool
    window_configurations: bool
    mic_pre_settings: bool
    heat_master_settings: bool
    def __init__(self, tempo_meter_map: bool = ..., key_signature_choed_map: bool = ..., markers_memory_locations: bool = ..., window_configurations: bool = ..., mic_pre_settings: bool = ..., heat_master_settings: bool = ...) -> None: ...

class SessionData(_message.Message):
    __slots__ = ("audio_options", "audio_handle_size", "video_options", "match_options", "playlist_options", "track_data_to_import", "timecode_mapping_units", "timecode_mapping_start_time", "adjust_session_start_time_to_match_source")
    AUDIO_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    AUDIO_HANDLE_SIZE_FIELD_NUMBER: _ClassVar[int]
    VIDEO_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    MATCH_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    PLAYLIST_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    TRACK_DATA_TO_IMPORT_FIELD_NUMBER: _ClassVar[int]
    TIMECODE_MAPPING_UNITS_FIELD_NUMBER: _ClassVar[int]
    TIMECODE_MAPPING_START_TIME_FIELD_NUMBER: _ClassVar[int]
    ADJUST_SESSION_START_TIME_TO_MATCH_SOURCE_FIELD_NUMBER: _ClassVar[int]
    audio_options: AudioMediaOptions
    audio_handle_size: int
    video_options: VideoMediaOptions
    match_options: MatchTrackOptions
    playlist_options: MainPlaylistOptions
    track_data_to_import: TrackDataToImport
    timecode_mapping_units: TimeCodeMappingOptions
    timecode_mapping_start_time: str
    adjust_session_start_time_to_match_source: bool
    def __init__(self, audio_options: _Optional[_Union[AudioMediaOptions, str]] = ..., audio_handle_size: _Optional[int] = ..., video_options: _Optional[_Union[VideoMediaOptions, str]] = ..., match_options: _Optional[_Union[MatchTrackOptions, str]] = ..., playlist_options: _Optional[_Union[MainPlaylistOptions, str]] = ..., track_data_to_import: _Optional[_Union[TrackDataToImport, _Mapping]] = ..., timecode_mapping_units: _Optional[_Union[TimeCodeMappingOptions, str]] = ..., timecode_mapping_start_time: _Optional[str] = ..., adjust_session_start_time_to_match_source: bool = ...) -> None: ...

class SpotLocationData(_message.Message):
    __slots__ = ("location_type", "location_value", "location_options")
    LOCATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    LOCATION_VALUE_FIELD_NUMBER: _ClassVar[int]
    LOCATION_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    location_type: SpotLocationType
    location_value: str
    location_options: TrackOffsetOptions
    def __init__(self, location_type: _Optional[_Union[SpotLocationType, str]] = ..., location_value: _Optional[str] = ..., location_options: _Optional[_Union[TrackOffsetOptions, str]] = ...) -> None: ...

class AudioData(_message.Message):
    __slots__ = ("file_list", "audio_operations", "destination_path", "destination", "location", "location_data", "audio_destination", "audio_location")
    FILE_LIST_FIELD_NUMBER: _ClassVar[int]
    AUDIO_OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_PATH_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    LOCATION_DATA_FIELD_NUMBER: _ClassVar[int]
    AUDIO_DESTINATION_FIELD_NUMBER: _ClassVar[int]
    AUDIO_LOCATION_FIELD_NUMBER: _ClassVar[int]
    file_list: _containers.RepeatedScalarFieldContainer[str]
    audio_operations: AudioOperations
    destination_path: str
    destination: MediaDestination
    location: MediaLocation
    location_data: SpotLocationData
    audio_destination: MediaDestination
    audio_location: MediaLocation
    def __init__(self, file_list: _Optional[_Iterable[str]] = ..., audio_operations: _Optional[_Union[AudioOperations, str]] = ..., destination_path: _Optional[str] = ..., destination: _Optional[_Union[MediaDestination, str]] = ..., location: _Optional[_Union[MediaLocation, str]] = ..., location_data: _Optional[_Union[SpotLocationData, _Mapping]] = ..., audio_destination: _Optional[_Union[MediaDestination, str]] = ..., audio_location: _Optional[_Union[MediaLocation, str]] = ...) -> None: ...

class ImportRequestBody(_message.Message):
    __slots__ = ("session_path", "import_type", "session_data", "audio_data")
    SESSION_PATH_FIELD_NUMBER: _ClassVar[int]
    IMPORT_TYPE_FIELD_NUMBER: _ClassVar[int]
    SESSION_DATA_FIELD_NUMBER: _ClassVar[int]
    AUDIO_DATA_FIELD_NUMBER: _ClassVar[int]
    session_path: str
    import_type: ImportType
    session_data: SessionData
    audio_data: AudioData
    def __init__(self, session_path: _Optional[str] = ..., import_type: _Optional[_Union[ImportType, str]] = ..., session_data: _Optional[_Union[SessionData, _Mapping]] = ..., audio_data: _Optional[_Union[AudioData, _Mapping]] = ...) -> None: ...

class ImportResponseBody(_message.Message):
    __slots__ = ("file_list", "audio_operations", "destination_path", "audio_data")
    FILE_LIST_FIELD_NUMBER: _ClassVar[int]
    AUDIO_OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_PATH_FIELD_NUMBER: _ClassVar[int]
    AUDIO_DATA_FIELD_NUMBER: _ClassVar[int]
    file_list: _containers.RepeatedScalarFieldContainer[str]
    audio_operations: AudioOperations
    destination_path: str
    audio_data: AudioData
    def __init__(self, file_list: _Optional[_Iterable[str]] = ..., audio_operations: _Optional[_Union[AudioOperations, str]] = ..., destination_path: _Optional[str] = ..., audio_data: _Optional[_Union[AudioData, _Mapping]] = ...) -> None: ...

class TrackListInvertibleFilter(_message.Message):
    __slots__ = ("filter", "is_inverted")
    FILTER_FIELD_NUMBER: _ClassVar[int]
    IS_INVERTED_FIELD_NUMBER: _ClassVar[int]
    filter: TrackListFilter
    is_inverted: bool
    def __init__(self, filter: _Optional[_Union[TrackListFilter, str]] = ..., is_inverted: bool = ...) -> None: ...

class GetTrackListRequestBody(_message.Message):
    __slots__ = ("page_limit", "track_filter_list", "is_filter_list_additive", "pagination_request")
    PAGE_LIMIT_FIELD_NUMBER: _ClassVar[int]
    TRACK_FILTER_LIST_FIELD_NUMBER: _ClassVar[int]
    IS_FILTER_LIST_ADDITIVE_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_REQUEST_FIELD_NUMBER: _ClassVar[int]
    page_limit: int
    track_filter_list: _containers.RepeatedCompositeFieldContainer[TrackListInvertibleFilter]
    is_filter_list_additive: bool
    pagination_request: PaginationRequest
    def __init__(self, page_limit: _Optional[int] = ..., track_filter_list: _Optional[_Iterable[_Union[TrackListInvertibleFilter, _Mapping]]] = ..., is_filter_list_additive: bool = ..., pagination_request: _Optional[_Union[PaginationRequest, _Mapping]] = ...) -> None: ...

class GetTrackListResponseBody(_message.Message):
    __slots__ = ("stats", "track_list", "pagination_response")
    STATS_FIELD_NUMBER: _ClassVar[int]
    TRACK_LIST_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    stats: Pagination
    track_list: _containers.RepeatedCompositeFieldContainer[Track]
    pagination_response: PaginationResponse
    def __init__(self, stats: _Optional[_Union[Pagination, _Mapping]] = ..., track_list: _Optional[_Iterable[_Union[Track, _Mapping]]] = ..., pagination_response: _Optional[_Union[PaginationResponse, _Mapping]] = ...) -> None: ...

class SelectAllClipsOnTrackRequestBody(_message.Message):
    __slots__ = ("track_name",)
    TRACK_NAME_FIELD_NUMBER: _ClassVar[int]
    track_name: str
    def __init__(self, track_name: _Optional[str] = ...) -> None: ...

class SelectAllClipsOnTrackResponseBody(_message.Message):
    __slots__ = ("track_name",)
    TRACK_NAME_FIELD_NUMBER: _ClassVar[int]
    track_name: str
    def __init__(self, track_name: _Optional[str] = ...) -> None: ...

class ExtendSelectionToTargetTracksRequestBody(_message.Message):
    __slots__ = ("tracks_to_extend_to",)
    TRACKS_TO_EXTEND_TO_FIELD_NUMBER: _ClassVar[int]
    tracks_to_extend_to: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, tracks_to_extend_to: _Optional[_Iterable[str]] = ...) -> None: ...

class ExtendSelectionToTargetTracksResponseBody(_message.Message):
    __slots__ = ("tracks_to_extend_to",)
    TRACKS_TO_EXTEND_TO_FIELD_NUMBER: _ClassVar[int]
    tracks_to_extend_to: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, tracks_to_extend_to: _Optional[_Iterable[str]] = ...) -> None: ...

class CreateFadesBasedOnPresetRequestBody(_message.Message):
    __slots__ = ("fade_preset_name", "auto_adjust_bounds")
    FADE_PRESET_NAME_FIELD_NUMBER: _ClassVar[int]
    AUTO_ADJUST_BOUNDS_FIELD_NUMBER: _ClassVar[int]
    fade_preset_name: str
    auto_adjust_bounds: bool
    def __init__(self, fade_preset_name: _Optional[str] = ..., auto_adjust_bounds: bool = ...) -> None: ...

class CreateFadesBasedOnPresetResponseBody(_message.Message):
    __slots__ = ("fade_preset_name",)
    FADE_PRESET_NAME_FIELD_NUMBER: _ClassVar[int]
    fade_preset_name: str
    def __init__(self, fade_preset_name: _Optional[str] = ...) -> None: ...

class RenameTargetTrackRequestBody(_message.Message):
    __slots__ = ("track_id", "new_name", "current_name")
    TRACK_ID_FIELD_NUMBER: _ClassVar[int]
    NEW_NAME_FIELD_NUMBER: _ClassVar[int]
    CURRENT_NAME_FIELD_NUMBER: _ClassVar[int]
    track_id: str
    new_name: str
    current_name: str
    def __init__(self, track_id: _Optional[str] = ..., new_name: _Optional[str] = ..., current_name: _Optional[str] = ...) -> None: ...

class ExportClipsAsFilesRequestBody(_message.Message):
    __slots__ = ("file_path", "format", "file_type", "bit_depth", "duplicate_names", "enforce_avid_compatibility", "sample_rate_custom")
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    FILE_TYPE_FIELD_NUMBER: _ClassVar[int]
    BIT_DEPTH_FIELD_NUMBER: _ClassVar[int]
    DUPLICATE_NAMES_FIELD_NUMBER: _ClassVar[int]
    ENFORCE_AVID_COMPATIBILITY_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_RATE_CUSTOM_FIELD_NUMBER: _ClassVar[int]
    file_path: str
    format: ExportFormat
    file_type: ExportFileType
    bit_depth: BitDepth
    duplicate_names: ResolveDuplicateNamesBy
    enforce_avid_compatibility: bool
    sample_rate_custom: int
    def __init__(self, file_path: _Optional[str] = ..., format: _Optional[_Union[ExportFormat, str]] = ..., file_type: _Optional[_Union[ExportFileType, str]] = ..., bit_depth: _Optional[_Union[BitDepth, str]] = ..., duplicate_names: _Optional[_Union[ResolveDuplicateNamesBy, str]] = ..., enforce_avid_compatibility: bool = ..., sample_rate_custom: _Optional[int] = ...) -> None: ...

class ExportSelectedTracksAsAAFOMFRequestBody(_message.Message):
    __slots__ = ("file_type", "bit_depth", "copy_option", "enforce_media_composer_compatibility", "quantize_edits_to_frame_boundaries", "export_stereo_as_multichannel", "container_file_name", "container_file_location", "asset_file_location", "comments", "sequence_name")
    FILE_TYPE_FIELD_NUMBER: _ClassVar[int]
    BIT_DEPTH_FIELD_NUMBER: _ClassVar[int]
    COPY_OPTION_FIELD_NUMBER: _ClassVar[int]
    ENFORCE_MEDIA_COMPOSER_COMPATIBILITY_FIELD_NUMBER: _ClassVar[int]
    QUANTIZE_EDITS_TO_FRAME_BOUNDARIES_FIELD_NUMBER: _ClassVar[int]
    EXPORT_STEREO_AS_MULTICHANNEL_FIELD_NUMBER: _ClassVar[int]
    CONTAINER_FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    CONTAINER_FILE_LOCATION_FIELD_NUMBER: _ClassVar[int]
    ASSET_FILE_LOCATION_FIELD_NUMBER: _ClassVar[int]
    COMMENTS_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_NAME_FIELD_NUMBER: _ClassVar[int]
    file_type: ExportAsAAFFileType
    bit_depth: AAFFileBitDepth
    copy_option: CopyOption
    enforce_media_composer_compatibility: bool
    quantize_edits_to_frame_boundaries: bool
    export_stereo_as_multichannel: bool
    container_file_name: str
    container_file_location: str
    asset_file_location: str
    comments: str
    sequence_name: str
    def __init__(self, file_type: _Optional[_Union[ExportAsAAFFileType, str]] = ..., bit_depth: _Optional[_Union[AAFFileBitDepth, str]] = ..., copy_option: _Optional[_Union[CopyOption, str]] = ..., enforce_media_composer_compatibility: bool = ..., quantize_edits_to_frame_boundaries: bool = ..., export_stereo_as_multichannel: bool = ..., container_file_name: _Optional[str] = ..., container_file_location: _Optional[str] = ..., asset_file_location: _Optional[str] = ..., comments: _Optional[str] = ..., sequence_name: _Optional[str] = ...) -> None: ...

class RefreshTargetAudioFilesRequestBody(_message.Message):
    __slots__ = ("file_list",)
    FILE_LIST_FIELD_NUMBER: _ClassVar[int]
    file_list: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, file_list: _Optional[_Iterable[str]] = ...) -> None: ...

class RefreshTargetAudioFilesResponseBody(_message.Message):
    __slots__ = ("success_count", "failure_count", "failure_list")
    SUCCESS_COUNT_FIELD_NUMBER: _ClassVar[int]
    FAILURE_COUNT_FIELD_NUMBER: _ClassVar[int]
    FAILURE_LIST_FIELD_NUMBER: _ClassVar[int]
    success_count: int
    failure_count: int
    failure_list: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, success_count: _Optional[int] = ..., failure_count: _Optional[int] = ..., failure_list: _Optional[_Iterable[str]] = ...) -> None: ...

class FileLocationInfo(_message.Message):
    __slots__ = ("is_online",)
    IS_ONLINE_FIELD_NUMBER: _ClassVar[int]
    is_online: bool
    def __init__(self, is_online: bool = ...) -> None: ...

class FileLocation(_message.Message):
    __slots__ = ("path", "info")
    PATH_FIELD_NUMBER: _ClassVar[int]
    INFO_FIELD_NUMBER: _ClassVar[int]
    path: str
    info: FileLocationInfo
    def __init__(self, path: _Optional[str] = ..., info: _Optional[_Union[FileLocationInfo, _Mapping]] = ...) -> None: ...

class GetFileLocationRequestBody(_message.Message):
    __slots__ = ("page_limit", "file_filters", "pagination_request")
    PAGE_LIMIT_FIELD_NUMBER: _ClassVar[int]
    FILE_FILTERS_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_REQUEST_FIELD_NUMBER: _ClassVar[int]
    page_limit: int
    file_filters: _containers.RepeatedScalarFieldContainer[FileLocationTypeFilter]
    pagination_request: PaginationRequest
    def __init__(self, page_limit: _Optional[int] = ..., file_filters: _Optional[_Iterable[_Union[FileLocationTypeFilter, str]]] = ..., pagination_request: _Optional[_Union[PaginationRequest, _Mapping]] = ...) -> None: ...

class GetFileLocationResponseBody(_message.Message):
    __slots__ = ("stats", "file_locations", "pagination_response")
    STATS_FIELD_NUMBER: _ClassVar[int]
    FILE_LOCATIONS_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    stats: Pagination
    file_locations: _containers.RepeatedCompositeFieldContainer[FileLocation]
    pagination_response: PaginationResponse
    def __init__(self, stats: _Optional[_Union[Pagination, _Mapping]] = ..., file_locations: _Optional[_Iterable[_Union[FileLocation, _Mapping]]] = ..., pagination_response: _Optional[_Union[PaginationResponse, _Mapping]] = ...) -> None: ...

class CloseSessionRequestBody(_message.Message):
    __slots__ = ("save_on_close",)
    SAVE_ON_CLOSE_FIELD_NUMBER: _ClassVar[int]
    save_on_close: bool
    def __init__(self, save_on_close: bool = ...) -> None: ...

class SaveSessionAsRequestBody(_message.Message):
    __slots__ = ("session_name", "session_location")
    SESSION_NAME_FIELD_NUMBER: _ClassVar[int]
    SESSION_LOCATION_FIELD_NUMBER: _ClassVar[int]
    session_name: str
    session_location: str
    def __init__(self, session_name: _Optional[str] = ..., session_location: _Optional[str] = ...) -> None: ...

class CutSpecialRequestBody(_message.Message):
    __slots__ = ("automation_data_option",)
    AUTOMATION_DATA_OPTION_FIELD_NUMBER: _ClassVar[int]
    automation_data_option: AutomationDataOptions
    def __init__(self, automation_data_option: _Optional[_Union[AutomationDataOptions, str]] = ...) -> None: ...

class CopySpecialRequestBody(_message.Message):
    __slots__ = ("automation_data_option",)
    AUTOMATION_DATA_OPTION_FIELD_NUMBER: _ClassVar[int]
    automation_data_option: AutomationDataOptions
    def __init__(self, automation_data_option: _Optional[_Union[AutomationDataOptions, str]] = ...) -> None: ...

class ClearSpecialRequestBody(_message.Message):
    __slots__ = ("automation_data_option",)
    AUTOMATION_DATA_OPTION_FIELD_NUMBER: _ClassVar[int]
    automation_data_option: AutomationDataOptions
    def __init__(self, automation_data_option: _Optional[_Union[AutomationDataOptions, str]] = ...) -> None: ...

class PasteSpecialRequestBody(_message.Message):
    __slots__ = ("paste_special_option",)
    PASTE_SPECIAL_OPTION_FIELD_NUMBER: _ClassVar[int]
    paste_special_option: PasteSpecialOptions
    def __init__(self, paste_special_option: _Optional[_Union[PasteSpecialOptions, str]] = ...) -> None: ...

class EM_SourceInfo(_message.Message):
    __slots__ = ("source_type", "name")
    SOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    source_type: EM_SourceType
    name: str
    def __init__(self, source_type: _Optional[_Union[EM_SourceType, str]] = ..., name: _Optional[str] = ...) -> None: ...

class EM_AudioInfo(_message.Message):
    __slots__ = ("compression_type", "export_format", "bit_depth", "sample_rate", "pad_to_frame_boundary", "delivery_format", "sample_rate_custom")
    COMPRESSION_TYPE_FIELD_NUMBER: _ClassVar[int]
    EXPORT_FORMAT_FIELD_NUMBER: _ClassVar[int]
    BIT_DEPTH_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_RATE_FIELD_NUMBER: _ClassVar[int]
    PAD_TO_FRAME_BOUNDARY_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_FORMAT_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_RATE_CUSTOM_FIELD_NUMBER: _ClassVar[int]
    compression_type: CompressionType
    export_format: ExportFormat
    bit_depth: BitDepth
    sample_rate: SampleRate
    pad_to_frame_boundary: TripleBool
    delivery_format: EM_DeliveryFormat
    sample_rate_custom: int
    def __init__(self, compression_type: _Optional[_Union[CompressionType, str]] = ..., export_format: _Optional[_Union[ExportFormat, str]] = ..., bit_depth: _Optional[_Union[BitDepth, str]] = ..., sample_rate: _Optional[_Union[SampleRate, str]] = ..., pad_to_frame_boundary: _Optional[_Union[TripleBool, str]] = ..., delivery_format: _Optional[_Union[EM_DeliveryFormat, str]] = ..., sample_rate_custom: _Optional[int] = ...) -> None: ...

class PropertyContainer(_message.Message):
    __slots__ = ("container_name", "type", "value")
    CONTAINER_NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    container_name: str
    type: DP_ValueTypes
    value: str
    def __init__(self, container_name: _Optional[str] = ..., type: _Optional[_Union[DP_ValueTypes, str]] = ..., value: _Optional[str] = ...) -> None: ...

class EM_CodecInfo(_message.Message):
    __slots__ = ("codec_name", "property_list")
    CODEC_NAME_FIELD_NUMBER: _ClassVar[int]
    PROPERTY_LIST_FIELD_NUMBER: _ClassVar[int]
    codec_name: str
    property_list: _containers.RepeatedCompositeFieldContainer[PropertyContainer]
    def __init__(self, codec_name: _Optional[str] = ..., property_list: _Optional[_Iterable[_Union[PropertyContainer, _Mapping]]] = ...) -> None: ...

class EM_VideoInfo(_message.Message):
    __slots__ = ("include_video", "export_option", "replace_timecode_track", "codec_info")
    INCLUDE_VIDEO_FIELD_NUMBER: _ClassVar[int]
    EXPORT_OPTION_FIELD_NUMBER: _ClassVar[int]
    REPLACE_TIMECODE_TRACK_FIELD_NUMBER: _ClassVar[int]
    CODEC_INFO_FIELD_NUMBER: _ClassVar[int]
    include_video: TripleBool
    export_option: EM_VideoExportOptions
    replace_timecode_track: TripleBool
    codec_info: EM_CodecInfo
    def __init__(self, include_video: _Optional[_Union[TripleBool, str]] = ..., export_option: _Optional[_Union[EM_VideoExportOptions, str]] = ..., replace_timecode_track: _Optional[_Union[TripleBool, str]] = ..., codec_info: _Optional[_Union[EM_CodecInfo, _Mapping]] = ...) -> None: ...

class EM_ImportOptions(_message.Message):
    __slots__ = ("import_destination", "import_location", "gaps_between_clips", "import_audio_from_file", "remove_existing_video_tracks", "remove_existing_video_clips", "clear_destination_video_track_playlist")
    IMPORT_DESTINATION_FIELD_NUMBER: _ClassVar[int]
    IMPORT_LOCATION_FIELD_NUMBER: _ClassVar[int]
    GAPS_BETWEEN_CLIPS_FIELD_NUMBER: _ClassVar[int]
    IMPORT_AUDIO_FROM_FILE_FIELD_NUMBER: _ClassVar[int]
    REMOVE_EXISTING_VIDEO_TRACKS_FIELD_NUMBER: _ClassVar[int]
    REMOVE_EXISTING_VIDEO_CLIPS_FIELD_NUMBER: _ClassVar[int]
    CLEAR_DESTINATION_VIDEO_TRACK_PLAYLIST_FIELD_NUMBER: _ClassVar[int]
    import_destination: MediaDestination
    import_location: MediaLocation
    gaps_between_clips: int
    import_audio_from_file: TripleBool
    remove_existing_video_tracks: TripleBool
    remove_existing_video_clips: TripleBool
    clear_destination_video_track_playlist: TripleBool
    def __init__(self, import_destination: _Optional[_Union[MediaDestination, str]] = ..., import_location: _Optional[_Union[MediaLocation, str]] = ..., gaps_between_clips: _Optional[int] = ..., import_audio_from_file: _Optional[_Union[TripleBool, str]] = ..., remove_existing_video_tracks: _Optional[_Union[TripleBool, str]] = ..., remove_existing_video_clips: _Optional[_Union[TripleBool, str]] = ..., clear_destination_video_track_playlist: _Optional[_Union[TripleBool, str]] = ...) -> None: ...

class EM_LocationInfo(_message.Message):
    __slots__ = ("import_after_bounce", "import_options", "file_destination", "directory")
    IMPORT_AFTER_BOUNCE_FIELD_NUMBER: _ClassVar[int]
    IMPORT_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    FILE_DESTINATION_FIELD_NUMBER: _ClassVar[int]
    DIRECTORY_FIELD_NUMBER: _ClassVar[int]
    import_after_bounce: TripleBool
    import_options: EM_ImportOptions
    file_destination: EM_FileDestination
    directory: str
    def __init__(self, import_after_bounce: _Optional[_Union[TripleBool, str]] = ..., import_options: _Optional[_Union[EM_ImportOptions, _Mapping]] = ..., file_destination: _Optional[_Union[EM_FileDestination, str]] = ..., directory: _Optional[str] = ...) -> None: ...

class EM_DolbyAtmosInfo(_message.Message):
    __slots__ = ("add_first_frame_of_action", "timecode_value", "frame_rate", "property_list")
    ADD_FIRST_FRAME_OF_ACTION_FIELD_NUMBER: _ClassVar[int]
    TIMECODE_VALUE_FIELD_NUMBER: _ClassVar[int]
    FRAME_RATE_FIELD_NUMBER: _ClassVar[int]
    PROPERTY_LIST_FIELD_NUMBER: _ClassVar[int]
    add_first_frame_of_action: TripleBool
    timecode_value: str
    frame_rate: int
    property_list: _containers.RepeatedCompositeFieldContainer[PropertyContainer]
    def __init__(self, add_first_frame_of_action: _Optional[_Union[TripleBool, str]] = ..., timecode_value: _Optional[str] = ..., frame_rate: _Optional[int] = ..., property_list: _Optional[_Iterable[_Union[PropertyContainer, _Mapping]]] = ...) -> None: ...

class ExportMixRequestBody(_message.Message):
    __slots__ = ("preset_path", "file_name", "file_type", "files_list", "audio_info", "video_info", "location_info", "dolby_atmos_info", "offline_bounce", "mix_source_list")
    PRESET_PATH_FIELD_NUMBER: _ClassVar[int]
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    FILE_TYPE_FIELD_NUMBER: _ClassVar[int]
    FILES_LIST_FIELD_NUMBER: _ClassVar[int]
    AUDIO_INFO_FIELD_NUMBER: _ClassVar[int]
    VIDEO_INFO_FIELD_NUMBER: _ClassVar[int]
    LOCATION_INFO_FIELD_NUMBER: _ClassVar[int]
    DOLBY_ATMOS_INFO_FIELD_NUMBER: _ClassVar[int]
    OFFLINE_BOUNCE_FIELD_NUMBER: _ClassVar[int]
    MIX_SOURCE_LIST_FIELD_NUMBER: _ClassVar[int]
    preset_path: str
    file_name: str
    file_type: EM_FileType
    files_list: _containers.RepeatedCompositeFieldContainer[EM_SourceInfo]
    audio_info: EM_AudioInfo
    video_info: EM_VideoInfo
    location_info: EM_LocationInfo
    dolby_atmos_info: EM_DolbyAtmosInfo
    offline_bounce: TripleBool
    mix_source_list: _containers.RepeatedCompositeFieldContainer[EM_SourceInfo]
    def __init__(self, preset_path: _Optional[str] = ..., file_name: _Optional[str] = ..., file_type: _Optional[_Union[EM_FileType, str]] = ..., files_list: _Optional[_Iterable[_Union[EM_SourceInfo, _Mapping]]] = ..., audio_info: _Optional[_Union[EM_AudioInfo, _Mapping]] = ..., video_info: _Optional[_Union[EM_VideoInfo, _Mapping]] = ..., location_info: _Optional[_Union[EM_LocationInfo, _Mapping]] = ..., dolby_atmos_info: _Optional[_Union[EM_DolbyAtmosInfo, _Mapping]] = ..., offline_bounce: _Optional[_Union[TripleBool, str]] = ..., mix_source_list: _Optional[_Iterable[_Union[EM_SourceInfo, _Mapping]]] = ...) -> None: ...

class PropertyDescriptor(_message.Message):
    __slots__ = ("name", "value_type", "object_type", "required", "description", "units", "accepted_values", "max_value", "min_value")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_TYPE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    UNITS_FIELD_NUMBER: _ClassVar[int]
    ACCEPTED_VALUES_FIELD_NUMBER: _ClassVar[int]
    MAX_VALUE_FIELD_NUMBER: _ClassVar[int]
    MIN_VALUE_FIELD_NUMBER: _ClassVar[int]
    name: str
    value_type: DP_ValueTypes
    object_type: str
    required: bool
    description: str
    units: str
    accepted_values: _containers.RepeatedScalarFieldContainer[str]
    max_value: str
    min_value: str
    def __init__(self, name: _Optional[str] = ..., value_type: _Optional[_Union[DP_ValueTypes, str]] = ..., object_type: _Optional[str] = ..., required: bool = ..., description: _Optional[str] = ..., units: _Optional[str] = ..., accepted_values: _Optional[_Iterable[str]] = ..., max_value: _Optional[str] = ..., min_value: _Optional[str] = ...) -> None: ...

class GetDynamicPropertiesRequestBody(_message.Message):
    __slots__ = ("property_type",)
    PROPERTY_TYPE_FIELD_NUMBER: _ClassVar[int]
    property_type: DynamicPropertyType
    def __init__(self, property_type: _Optional[_Union[DynamicPropertyType, str]] = ...) -> None: ...

class GetDynamicPropertiesGroup(_message.Message):
    __slots__ = ("key_list", "property_list")
    KEY_LIST_FIELD_NUMBER: _ClassVar[int]
    PROPERTY_LIST_FIELD_NUMBER: _ClassVar[int]
    key_list: _containers.RepeatedCompositeFieldContainer[PropertyContainer]
    property_list: _containers.RepeatedCompositeFieldContainer[PropertyDescriptor]
    def __init__(self, key_list: _Optional[_Iterable[_Union[PropertyContainer, _Mapping]]] = ..., property_list: _Optional[_Iterable[_Union[PropertyDescriptor, _Mapping]]] = ...) -> None: ...

class GetDynamicPropertiesResponseBody(_message.Message):
    __slots__ = ("property_type", "group_list")
    PROPERTY_TYPE_FIELD_NUMBER: _ClassVar[int]
    GROUP_LIST_FIELD_NUMBER: _ClassVar[int]
    property_type: DynamicPropertyType
    group_list: _containers.RepeatedCompositeFieldContainer[GetDynamicPropertiesGroup]
    def __init__(self, property_type: _Optional[_Union[DynamicPropertyType, str]] = ..., group_list: _Optional[_Iterable[_Union[GetDynamicPropertiesGroup, _Mapping]]] = ...) -> None: ...

class SpotRequestBody(_message.Message):
    __slots__ = ("track_offset_options", "location_data")
    TRACK_OFFSET_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    LOCATION_DATA_FIELD_NUMBER: _ClassVar[int]
    track_offset_options: TrackOffsetOptions
    location_data: SpotLocationData
    def __init__(self, track_offset_options: _Optional[_Union[TrackOffsetOptions, str]] = ..., location_data: _Optional[_Union[SpotLocationData, _Mapping]] = ...) -> None: ...

class ExportSessionInfoAsTextRequestBody(_message.Message):
    __slots__ = ("include_file_list", "include_clip_list", "include_markers", "include_plugin_list", "include_track_edls", "show_sub_frames", "include_user_timestamps", "track_list_type", "fade_handling_type", "track_offset_options", "text_as_file_format", "output_type", "output_path")
    INCLUDE_FILE_LIST_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_CLIP_LIST_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_MARKERS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_PLUGIN_LIST_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_TRACK_EDLS_FIELD_NUMBER: _ClassVar[int]
    SHOW_SUB_FRAMES_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_USER_TIMESTAMPS_FIELD_NUMBER: _ClassVar[int]
    TRACK_LIST_TYPE_FIELD_NUMBER: _ClassVar[int]
    FADE_HANDLING_TYPE_FIELD_NUMBER: _ClassVar[int]
    TRACK_OFFSET_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    TEXT_AS_FILE_FORMAT_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_TYPE_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_PATH_FIELD_NUMBER: _ClassVar[int]
    include_file_list: bool
    include_clip_list: bool
    include_markers: bool
    include_plugin_list: bool
    include_track_edls: bool
    show_sub_frames: bool
    include_user_timestamps: bool
    track_list_type: TrackListType
    fade_handling_type: FadeHandlingType
    track_offset_options: TrackOffsetOptions
    text_as_file_format: TextAsFileFormat
    output_type: ESI_OutputType
    output_path: str
    def __init__(self, include_file_list: bool = ..., include_clip_list: bool = ..., include_markers: bool = ..., include_plugin_list: bool = ..., include_track_edls: bool = ..., show_sub_frames: bool = ..., include_user_timestamps: bool = ..., track_list_type: _Optional[_Union[TrackListType, str]] = ..., fade_handling_type: _Optional[_Union[FadeHandlingType, str]] = ..., track_offset_options: _Optional[_Union[TrackOffsetOptions, str]] = ..., text_as_file_format: _Optional[_Union[TextAsFileFormat, str]] = ..., output_type: _Optional[_Union[ESI_OutputType, str]] = ..., output_path: _Optional[str] = ...) -> None: ...

class ExportSessionInfoAsTextResponseBody(_message.Message):
    __slots__ = ("session_info",)
    SESSION_INFO_FIELD_NUMBER: _ClassVar[int]
    session_info: str
    def __init__(self, session_info: _Optional[str] = ...) -> None: ...

class SetPlaybackModeRequestBody(_message.Message):
    __slots__ = ("playback_mode",)
    PLAYBACK_MODE_FIELD_NUMBER: _ClassVar[int]
    playback_mode: PM_PlaybackMode
    def __init__(self, playback_mode: _Optional[_Union[PM_PlaybackMode, str]] = ...) -> None: ...

class SetPlaybackModeResponseBody(_message.Message):
    __slots__ = ("current_playback_mode", "playback_mode_list")
    CURRENT_PLAYBACK_MODE_FIELD_NUMBER: _ClassVar[int]
    PLAYBACK_MODE_LIST_FIELD_NUMBER: _ClassVar[int]
    current_playback_mode: PM_PlaybackMode
    playback_mode_list: _containers.RepeatedScalarFieldContainer[PM_PlaybackMode]
    def __init__(self, current_playback_mode: _Optional[_Union[PM_PlaybackMode, str]] = ..., playback_mode_list: _Optional[_Iterable[_Union[PM_PlaybackMode, str]]] = ...) -> None: ...

class SetRecordModeRequestBody(_message.Message):
    __slots__ = ("record_mode", "record_arm_transport")
    RECORD_MODE_FIELD_NUMBER: _ClassVar[int]
    RECORD_ARM_TRANSPORT_FIELD_NUMBER: _ClassVar[int]
    record_mode: RM_RecordMode
    record_arm_transport: bool
    def __init__(self, record_mode: _Optional[_Union[RM_RecordMode, str]] = ..., record_arm_transport: bool = ...) -> None: ...

class SetRecordModeResponseBody(_message.Message):
    __slots__ = ("current_record_mode", "record_mode_list")
    CURRENT_RECORD_MODE_FIELD_NUMBER: _ClassVar[int]
    RECORD_MODE_LIST_FIELD_NUMBER: _ClassVar[int]
    current_record_mode: RM_RecordMode
    record_mode_list: _containers.RepeatedScalarFieldContainer[RM_RecordMode]
    def __init__(self, current_record_mode: _Optional[_Union[RM_RecordMode, str]] = ..., record_mode_list: _Optional[_Iterable[_Union[RM_RecordMode, str]]] = ...) -> None: ...

class GetSessionAudioFormatResponseBody(_message.Message):
    __slots__ = ("current_setting", "possible_settings")
    CURRENT_SETTING_FIELD_NUMBER: _ClassVar[int]
    POSSIBLE_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    current_setting: SessionAudioFormat
    possible_settings: _containers.RepeatedScalarFieldContainer[SessionAudioFormat]
    def __init__(self, current_setting: _Optional[_Union[SessionAudioFormat, str]] = ..., possible_settings: _Optional[_Iterable[_Union[SessionAudioFormat, str]]] = ...) -> None: ...

class GetSessionSampleRateResponseBody(_message.Message):
    __slots__ = ("sample_rate",)
    SAMPLE_RATE_FIELD_NUMBER: _ClassVar[int]
    sample_rate: SampleRate
    def __init__(self, sample_rate: _Optional[_Union[SampleRate, str]] = ...) -> None: ...

class GetSessionBitDepthResponseBody(_message.Message):
    __slots__ = ("current_setting", "possible_settings")
    CURRENT_SETTING_FIELD_NUMBER: _ClassVar[int]
    POSSIBLE_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    current_setting: BitDepth
    possible_settings: _containers.RepeatedScalarFieldContainer[BitDepth]
    def __init__(self, current_setting: _Optional[_Union[BitDepth, str]] = ..., possible_settings: _Optional[_Iterable[_Union[BitDepth, str]]] = ...) -> None: ...

class GetSessionInterleavedStateResponseBody(_message.Message):
    __slots__ = ("current_setting", "possible_settings")
    CURRENT_SETTING_FIELD_NUMBER: _ClassVar[int]
    POSSIBLE_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    current_setting: bool
    possible_settings: _containers.RepeatedScalarFieldContainer[bool]
    def __init__(self, current_setting: bool = ..., possible_settings: _Optional[_Iterable[bool]] = ...) -> None: ...

class GetSessionTimeCodeRateResponseBody(_message.Message):
    __slots__ = ("current_setting", "possible_settings")
    CURRENT_SETTING_FIELD_NUMBER: _ClassVar[int]
    POSSIBLE_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    current_setting: SessionTimeCodeRate
    possible_settings: _containers.RepeatedScalarFieldContainer[SessionTimeCodeRate]
    def __init__(self, current_setting: _Optional[_Union[SessionTimeCodeRate, str]] = ..., possible_settings: _Optional[_Iterable[_Union[SessionTimeCodeRate, str]]] = ...) -> None: ...

class GetSessionFeetFramesRateResponseBody(_message.Message):
    __slots__ = ("current_setting", "possible_settings")
    CURRENT_SETTING_FIELD_NUMBER: _ClassVar[int]
    POSSIBLE_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    current_setting: SessionFeetFramesRate
    possible_settings: _containers.RepeatedScalarFieldContainer[SessionFeetFramesRate]
    def __init__(self, current_setting: _Optional[_Union[SessionFeetFramesRate, str]] = ..., possible_settings: _Optional[_Iterable[_Union[SessionFeetFramesRate, str]]] = ...) -> None: ...

class GetSessionAudioRatePullSettingsResponseBody(_message.Message):
    __slots__ = ("current_setting", "possible_settings")
    CURRENT_SETTING_FIELD_NUMBER: _ClassVar[int]
    POSSIBLE_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    current_setting: SessionRatePull
    possible_settings: _containers.RepeatedScalarFieldContainer[SessionRatePull]
    def __init__(self, current_setting: _Optional[_Union[SessionRatePull, str]] = ..., possible_settings: _Optional[_Iterable[_Union[SessionRatePull, str]]] = ...) -> None: ...

class GetSessionVideoRatePullSettingsResponseBody(_message.Message):
    __slots__ = ("current_setting", "possible_settings")
    CURRENT_SETTING_FIELD_NUMBER: _ClassVar[int]
    POSSIBLE_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    current_setting: SessionRatePull
    possible_settings: _containers.RepeatedScalarFieldContainer[SessionRatePull]
    def __init__(self, current_setting: _Optional[_Union[SessionRatePull, str]] = ..., possible_settings: _Optional[_Iterable[_Union[SessionRatePull, str]]] = ...) -> None: ...

class GetSessionNameResponseBody(_message.Message):
    __slots__ = ("session_name",)
    SESSION_NAME_FIELD_NUMBER: _ClassVar[int]
    session_name: str
    def __init__(self, session_name: _Optional[str] = ...) -> None: ...

class GetSessionPathResponseBody(_message.Message):
    __slots__ = ("session_path",)
    SESSION_PATH_FIELD_NUMBER: _ClassVar[int]
    session_path: FileLocation
    def __init__(self, session_path: _Optional[_Union[FileLocation, _Mapping]] = ...) -> None: ...

class GetSessionStartTimeResponseBody(_message.Message):
    __slots__ = ("session_start_time",)
    SESSION_START_TIME_FIELD_NUMBER: _ClassVar[int]
    session_start_time: str
    def __init__(self, session_start_time: _Optional[str] = ...) -> None: ...

class GetSessionLengthResponseBody(_message.Message):
    __slots__ = ("session_length",)
    SESSION_LENGTH_FIELD_NUMBER: _ClassVar[int]
    session_length: str
    def __init__(self, session_length: _Optional[str] = ...) -> None: ...

class SetSessionAudioFormatRequestBody(_message.Message):
    __slots__ = ("audio_format",)
    AUDIO_FORMAT_FIELD_NUMBER: _ClassVar[int]
    audio_format: SessionAudioFormat
    def __init__(self, audio_format: _Optional[_Union[SessionAudioFormat, str]] = ...) -> None: ...

class SetSessionBitDepthRequestBody(_message.Message):
    __slots__ = ("bit_depth",)
    BIT_DEPTH_FIELD_NUMBER: _ClassVar[int]
    bit_depth: BitDepth
    def __init__(self, bit_depth: _Optional[_Union[BitDepth, str]] = ...) -> None: ...

class SetSessionInterleavedStateRequestBody(_message.Message):
    __slots__ = ("interleaved_state",)
    INTERLEAVED_STATE_FIELD_NUMBER: _ClassVar[int]
    interleaved_state: bool
    def __init__(self, interleaved_state: bool = ...) -> None: ...

class SetSessionTimeCodeRateRequestBody(_message.Message):
    __slots__ = ("time_code_rate",)
    TIME_CODE_RATE_FIELD_NUMBER: _ClassVar[int]
    time_code_rate: SessionTimeCodeRate
    def __init__(self, time_code_rate: _Optional[_Union[SessionTimeCodeRate, str]] = ...) -> None: ...

class SetSessionFeetFramesRateRequestBody(_message.Message):
    __slots__ = ("feet_frames_rate",)
    FEET_FRAMES_RATE_FIELD_NUMBER: _ClassVar[int]
    feet_frames_rate: SessionFeetFramesRate
    def __init__(self, feet_frames_rate: _Optional[_Union[SessionFeetFramesRate, str]] = ...) -> None: ...

class SetSessionAudioRatePullSettingsRequestBody(_message.Message):
    __slots__ = ("audio_rate_pull",)
    AUDIO_RATE_PULL_FIELD_NUMBER: _ClassVar[int]
    audio_rate_pull: SessionRatePull
    def __init__(self, audio_rate_pull: _Optional[_Union[SessionRatePull, str]] = ...) -> None: ...

class SetSessionVideoRatePullSettingsRequestBody(_message.Message):
    __slots__ = ("video_rate_pull",)
    VIDEO_RATE_PULL_FIELD_NUMBER: _ClassVar[int]
    video_rate_pull: SessionRatePull
    def __init__(self, video_rate_pull: _Optional[_Union[SessionRatePull, str]] = ...) -> None: ...

class SetSessionStartTimeRequestBody(_message.Message):
    __slots__ = ("session_start_time", "track_offset_opts", "maintain_relative_position")
    SESSION_START_TIME_FIELD_NUMBER: _ClassVar[int]
    TRACK_OFFSET_OPTS_FIELD_NUMBER: _ClassVar[int]
    MAINTAIN_RELATIVE_POSITION_FIELD_NUMBER: _ClassVar[int]
    session_start_time: str
    track_offset_opts: TrackOffsetOptions
    maintain_relative_position: bool
    def __init__(self, session_start_time: _Optional[str] = ..., track_offset_opts: _Optional[_Union[TrackOffsetOptions, str]] = ..., maintain_relative_position: bool = ...) -> None: ...

class SetSessionLengthRequestBody(_message.Message):
    __slots__ = ("session_length",)
    SESSION_LENGTH_FIELD_NUMBER: _ClassVar[int]
    session_length: str
    def __init__(self, session_length: _Optional[str] = ...) -> None: ...

class GetPTSLVersionResponseBody(_message.Message):
    __slots__ = ("version",)
    VERSION_FIELD_NUMBER: _ClassVar[int]
    version: int
    def __init__(self, version: _Optional[int] = ...) -> None: ...

class GetPlaybackModeResponseBody(_message.Message):
    __slots__ = ("current_settings", "possible_settings")
    CURRENT_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    POSSIBLE_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    current_settings: _containers.RepeatedScalarFieldContainer[PM_PlaybackMode]
    possible_settings: _containers.RepeatedScalarFieldContainer[PM_PlaybackMode]
    def __init__(self, current_settings: _Optional[_Iterable[_Union[PM_PlaybackMode, str]]] = ..., possible_settings: _Optional[_Iterable[_Union[PM_PlaybackMode, str]]] = ...) -> None: ...

class GetRecordModeResponseBody(_message.Message):
    __slots__ = ("current_setting", "possible_settings")
    CURRENT_SETTING_FIELD_NUMBER: _ClassVar[int]
    POSSIBLE_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    current_setting: RM_RecordMode
    possible_settings: _containers.RepeatedScalarFieldContainer[RM_RecordMode]
    def __init__(self, current_setting: _Optional[_Union[RM_RecordMode, str]] = ..., possible_settings: _Optional[_Iterable[_Union[RM_RecordMode, str]]] = ...) -> None: ...

class GetTransportStateResponseBody(_message.Message):
    __slots__ = ("current_setting", "possible_settings")
    CURRENT_SETTING_FIELD_NUMBER: _ClassVar[int]
    POSSIBLE_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    current_setting: TS_TransportState
    possible_settings: _containers.RepeatedScalarFieldContainer[TS_TransportState]
    def __init__(self, current_setting: _Optional[_Union[TS_TransportState, str]] = ..., possible_settings: _Optional[_Iterable[_Union[TS_TransportState, str]]] = ...) -> None: ...

class GetTransportArmedResponseBody(_message.Message):
    __slots__ = ("is_transport_armed",)
    IS_TRANSPORT_ARMED_FIELD_NUMBER: _ClassVar[int]
    is_transport_armed: bool
    def __init__(self, is_transport_armed: bool = ...) -> None: ...

class ClearMemoryLocationRequestBody(_message.Message):
    __slots__ = ("location_list",)
    LOCATION_LIST_FIELD_NUMBER: _ClassVar[int]
    location_list: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, location_list: _Optional[_Iterable[int]] = ...) -> None: ...

class ClearMemoryLocationResponseBody(_message.Message):
    __slots__ = ("success_count", "failure_count", "failure_list")
    SUCCESS_COUNT_FIELD_NUMBER: _ClassVar[int]
    FAILURE_COUNT_FIELD_NUMBER: _ClassVar[int]
    FAILURE_LIST_FIELD_NUMBER: _ClassVar[int]
    success_count: int
    failure_count: int
    failure_list: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, success_count: _Optional[int] = ..., failure_count: _Optional[int] = ..., failure_list: _Optional[_Iterable[int]] = ...) -> None: ...

class RenameSelectedClipRequestBody(_message.Message):
    __slots__ = ("clip_location", "new_name", "rename_file")
    CLIP_LOCATION_FIELD_NUMBER: _ClassVar[int]
    NEW_NAME_FIELD_NUMBER: _ClassVar[int]
    RENAME_FILE_FIELD_NUMBER: _ClassVar[int]
    clip_location: CL_ClipLocation
    new_name: str
    rename_file: bool
    def __init__(self, clip_location: _Optional[_Union[CL_ClipLocation, str]] = ..., new_name: _Optional[str] = ..., rename_file: bool = ...) -> None: ...

class RenameTargetClipRequestBody(_message.Message):
    __slots__ = ("clip_name", "new_name", "rename_file")
    CLIP_NAME_FIELD_NUMBER: _ClassVar[int]
    NEW_NAME_FIELD_NUMBER: _ClassVar[int]
    RENAME_FILE_FIELD_NUMBER: _ClassVar[int]
    clip_name: str
    new_name: str
    rename_file: bool
    def __init__(self, clip_name: _Optional[str] = ..., new_name: _Optional[str] = ..., rename_file: bool = ...) -> None: ...

class MemoryLocation(_message.Message):
    __slots__ = ("number", "name", "start_time", "end_time", "time_properties", "reference", "general_properties", "comments", "location", "track_name", "color_index")
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    TIME_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_FIELD_NUMBER: _ClassVar[int]
    GENERAL_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    COMMENTS_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    TRACK_NAME_FIELD_NUMBER: _ClassVar[int]
    COLOR_INDEX_FIELD_NUMBER: _ClassVar[int]
    number: int
    name: str
    start_time: str
    end_time: str
    time_properties: TimeProperties
    reference: MemoryLocationReference
    general_properties: MemoryLocationProperties
    comments: str
    location: MarkerLocation
    track_name: str
    color_index: int
    def __init__(self, number: _Optional[int] = ..., name: _Optional[str] = ..., start_time: _Optional[str] = ..., end_time: _Optional[str] = ..., time_properties: _Optional[_Union[TimeProperties, str]] = ..., reference: _Optional[_Union[MemoryLocationReference, str]] = ..., general_properties: _Optional[_Union[MemoryLocationProperties, _Mapping]] = ..., comments: _Optional[str] = ..., location: _Optional[_Union[MarkerLocation, str]] = ..., track_name: _Optional[str] = ..., color_index: _Optional[int] = ...) -> None: ...

class MemoryLocationProperties(_message.Message):
    __slots__ = ("zoom_settings", "pre_post_roll_times", "track_visibility", "track_heights", "group_enables", "window_configuration", "window_configuration_index", "window_configuration_name", "venue_snapshot_index", "venue_snapshot_name")
    ZOOM_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    PRE_POST_ROLL_TIMES_FIELD_NUMBER: _ClassVar[int]
    TRACK_VISIBILITY_FIELD_NUMBER: _ClassVar[int]
    TRACK_HEIGHTS_FIELD_NUMBER: _ClassVar[int]
    GROUP_ENABLES_FIELD_NUMBER: _ClassVar[int]
    WINDOW_CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    WINDOW_CONFIGURATION_INDEX_FIELD_NUMBER: _ClassVar[int]
    WINDOW_CONFIGURATION_NAME_FIELD_NUMBER: _ClassVar[int]
    VENUE_SNAPSHOT_INDEX_FIELD_NUMBER: _ClassVar[int]
    VENUE_SNAPSHOT_NAME_FIELD_NUMBER: _ClassVar[int]
    zoom_settings: bool
    pre_post_roll_times: bool
    track_visibility: bool
    track_heights: bool
    group_enables: bool
    window_configuration: bool
    window_configuration_index: int
    window_configuration_name: str
    venue_snapshot_index: int
    venue_snapshot_name: str
    def __init__(self, zoom_settings: bool = ..., pre_post_roll_times: bool = ..., track_visibility: bool = ..., track_heights: bool = ..., group_enables: bool = ..., window_configuration: bool = ..., window_configuration_index: _Optional[int] = ..., window_configuration_name: _Optional[str] = ..., venue_snapshot_index: _Optional[int] = ..., venue_snapshot_name: _Optional[str] = ...) -> None: ...

class EditMemoryLocationRequestBody(_message.Message):
    __slots__ = ("number", "name", "start_time", "end_time", "time_properties", "reference", "general_properties", "comments", "color_index", "location", "track_name")
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    TIME_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_FIELD_NUMBER: _ClassVar[int]
    GENERAL_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    COMMENTS_FIELD_NUMBER: _ClassVar[int]
    COLOR_INDEX_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    TRACK_NAME_FIELD_NUMBER: _ClassVar[int]
    number: int
    name: str
    start_time: str
    end_time: str
    time_properties: TimeProperties
    reference: MemoryLocationReference
    general_properties: MemoryLocationProperties
    comments: str
    color_index: int
    location: MarkerLocation
    track_name: str
    def __init__(self, number: _Optional[int] = ..., name: _Optional[str] = ..., start_time: _Optional[str] = ..., end_time: _Optional[str] = ..., time_properties: _Optional[_Union[TimeProperties, str]] = ..., reference: _Optional[_Union[MemoryLocationReference, str]] = ..., general_properties: _Optional[_Union[MemoryLocationProperties, _Mapping]] = ..., comments: _Optional[str] = ..., color_index: _Optional[int] = ..., location: _Optional[_Union[MarkerLocation, str]] = ..., track_name: _Optional[str] = ...) -> None: ...

class EditMemoryLocationResponseBody(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CreateMemoryLocationRequestBody(_message.Message):
    __slots__ = ("number", "name", "start_time", "end_time", "time_properties", "reference", "general_properties", "comments", "color_index", "location", "track_name")
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    TIME_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_FIELD_NUMBER: _ClassVar[int]
    GENERAL_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    COMMENTS_FIELD_NUMBER: _ClassVar[int]
    COLOR_INDEX_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    TRACK_NAME_FIELD_NUMBER: _ClassVar[int]
    number: int
    name: str
    start_time: str
    end_time: str
    time_properties: TimeProperties
    reference: MemoryLocationReference
    general_properties: MemoryLocationProperties
    comments: str
    color_index: int
    location: MarkerLocation
    track_name: str
    def __init__(self, number: _Optional[int] = ..., name: _Optional[str] = ..., start_time: _Optional[str] = ..., end_time: _Optional[str] = ..., time_properties: _Optional[_Union[TimeProperties, str]] = ..., reference: _Optional[_Union[MemoryLocationReference, str]] = ..., general_properties: _Optional[_Union[MemoryLocationProperties, _Mapping]] = ..., comments: _Optional[str] = ..., color_index: _Optional[int] = ..., location: _Optional[_Union[MarkerLocation, str]] = ..., track_name: _Optional[str] = ...) -> None: ...

class CreateMemoryLocationResponseBody(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetMemoryLocationsRequestBody(_message.Message):
    __slots__ = ("pagination_request",)
    PAGINATION_REQUEST_FIELD_NUMBER: _ClassVar[int]
    pagination_request: PaginationRequest
    def __init__(self, pagination_request: _Optional[_Union[PaginationRequest, _Mapping]] = ...) -> None: ...

class GetMemoryLocationsResponseBody(_message.Message):
    __slots__ = ("memory_locations", "stats", "pagination_response")
    MEMORY_LOCATIONS_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    memory_locations: _containers.RepeatedCompositeFieldContainer[MemoryLocation]
    stats: Pagination
    pagination_response: PaginationResponse
    def __init__(self, memory_locations: _Optional[_Iterable[_Union[MemoryLocation, _Mapping]]] = ..., stats: _Optional[_Union[Pagination, _Mapping]] = ..., pagination_response: _Optional[_Union[PaginationResponse, _Mapping]] = ...) -> None: ...

class RegisterConnectionRequestBody(_message.Message):
    __slots__ = ("company_name", "application_name")
    COMPANY_NAME_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_NAME_FIELD_NUMBER: _ClassVar[int]
    company_name: str
    application_name: str
    def __init__(self, company_name: _Optional[str] = ..., application_name: _Optional[str] = ...) -> None: ...

class RegisterConnectionResponseBody(_message.Message):
    __slots__ = ("session_id",)
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    def __init__(self, session_id: _Optional[str] = ...) -> None: ...

class CreateNewTracksRequestBody(_message.Message):
    __slots__ = ("number_of_tracks", "track_name", "track_format", "track_type", "track_timebase", "pagination_request", "insertion_point_position", "insertion_point_track_name")
    NUMBER_OF_TRACKS_FIELD_NUMBER: _ClassVar[int]
    TRACK_NAME_FIELD_NUMBER: _ClassVar[int]
    TRACK_FORMAT_FIELD_NUMBER: _ClassVar[int]
    TRACK_TYPE_FIELD_NUMBER: _ClassVar[int]
    TRACK_TIMEBASE_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_REQUEST_FIELD_NUMBER: _ClassVar[int]
    INSERTION_POINT_POSITION_FIELD_NUMBER: _ClassVar[int]
    INSERTION_POINT_TRACK_NAME_FIELD_NUMBER: _ClassVar[int]
    number_of_tracks: int
    track_name: str
    track_format: TrackFormat
    track_type: TrackType
    track_timebase: TrackTimebase
    pagination_request: PaginationRequest
    insertion_point_position: TrackInsertionPoint
    insertion_point_track_name: str
    def __init__(self, number_of_tracks: _Optional[int] = ..., track_name: _Optional[str] = ..., track_format: _Optional[_Union[TrackFormat, str]] = ..., track_type: _Optional[_Union[TrackType, str]] = ..., track_timebase: _Optional[_Union[TrackTimebase, str]] = ..., pagination_request: _Optional[_Union[PaginationRequest, _Mapping]] = ..., insertion_point_position: _Optional[_Union[TrackInsertionPoint, str]] = ..., insertion_point_track_name: _Optional[str] = ...) -> None: ...

class CreateNewTracksResponseBody(_message.Message):
    __slots__ = ("number_of_tracks", "created_track_names", "pagination_response")
    NUMBER_OF_TRACKS_FIELD_NUMBER: _ClassVar[int]
    CREATED_TRACK_NAMES_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    number_of_tracks: int
    created_track_names: _containers.RepeatedScalarFieldContainer[str]
    pagination_response: PaginationResponse
    def __init__(self, number_of_tracks: _Optional[int] = ..., created_track_names: _Optional[_Iterable[str]] = ..., pagination_response: _Optional[_Union[PaginationResponse, _Mapping]] = ...) -> None: ...

class EditModeOptions(_message.Message):
    __slots__ = ("tab_to_transients", "link_timeline_and_edit_selection", "link_track_and_edit_selection", "insertion_follows_playback", "automation_follows_edit", "markers_follow_edit", "mirrored_midi_editing", "layered_editing")
    TAB_TO_TRANSIENTS_FIELD_NUMBER: _ClassVar[int]
    LINK_TIMELINE_AND_EDIT_SELECTION_FIELD_NUMBER: _ClassVar[int]
    LINK_TRACK_AND_EDIT_SELECTION_FIELD_NUMBER: _ClassVar[int]
    INSERTION_FOLLOWS_PLAYBACK_FIELD_NUMBER: _ClassVar[int]
    AUTOMATION_FOLLOWS_EDIT_FIELD_NUMBER: _ClassVar[int]
    MARKERS_FOLLOW_EDIT_FIELD_NUMBER: _ClassVar[int]
    MIRRORED_MIDI_EDITING_FIELD_NUMBER: _ClassVar[int]
    LAYERED_EDITING_FIELD_NUMBER: _ClassVar[int]
    tab_to_transients: bool
    link_timeline_and_edit_selection: bool
    link_track_and_edit_selection: bool
    insertion_follows_playback: bool
    automation_follows_edit: bool
    markers_follow_edit: bool
    mirrored_midi_editing: bool
    layered_editing: bool
    def __init__(self, tab_to_transients: bool = ..., link_timeline_and_edit_selection: bool = ..., link_track_and_edit_selection: bool = ..., insertion_follows_playback: bool = ..., automation_follows_edit: bool = ..., markers_follow_edit: bool = ..., mirrored_midi_editing: bool = ..., layered_editing: bool = ...) -> None: ...

class GetEditModeResponseBody(_message.Message):
    __slots__ = ("current_setting", "possible_settings")
    CURRENT_SETTING_FIELD_NUMBER: _ClassVar[int]
    POSSIBLE_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    current_setting: EditMode
    possible_settings: _containers.RepeatedScalarFieldContainer[EditMode]
    def __init__(self, current_setting: _Optional[_Union[EditMode, str]] = ..., possible_settings: _Optional[_Iterable[_Union[EditMode, str]]] = ...) -> None: ...

class SetEditModeRequestBody(_message.Message):
    __slots__ = ("edit_mode",)
    EDIT_MODE_FIELD_NUMBER: _ClassVar[int]
    edit_mode: EditMode
    def __init__(self, edit_mode: _Optional[_Union[EditMode, str]] = ...) -> None: ...

class GetEditToolResponseBody(_message.Message):
    __slots__ = ("current_setting", "possible_settings")
    CURRENT_SETTING_FIELD_NUMBER: _ClassVar[int]
    POSSIBLE_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    current_setting: EditTool
    possible_settings: _containers.RepeatedScalarFieldContainer[EditTool]
    def __init__(self, current_setting: _Optional[_Union[EditTool, str]] = ..., possible_settings: _Optional[_Iterable[_Union[EditTool, str]]] = ...) -> None: ...

class SetEditToolRequestBody(_message.Message):
    __slots__ = ("edit_tool",)
    EDIT_TOOL_FIELD_NUMBER: _ClassVar[int]
    edit_tool: EditTool
    def __init__(self, edit_tool: _Optional[_Union[EditTool, str]] = ...) -> None: ...

class RecallZoomPresetRequestBody(_message.Message):
    __slots__ = ("zoom_preset",)
    ZOOM_PRESET_FIELD_NUMBER: _ClassVar[int]
    zoom_preset: int
    def __init__(self, zoom_preset: _Optional[int] = ...) -> None: ...

class GetEditModeOptionsResponseBody(_message.Message):
    __slots__ = ("edit_mode_options",)
    EDIT_MODE_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    edit_mode_options: EditModeOptions
    def __init__(self, edit_mode_options: _Optional[_Union[EditModeOptions, _Mapping]] = ...) -> None: ...

class SetEditModeOptionsRequestBody(_message.Message):
    __slots__ = ("edit_mode_options",)
    EDIT_MODE_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    edit_mode_options: EditModeOptions
    def __init__(self, edit_mode_options: _Optional[_Union[EditModeOptions, _Mapping]] = ...) -> None: ...

class SetTimelineSelectionRequestBody(_message.Message):
    __slots__ = ("play_start_marker_time", "in_time", "out_time", "pre_roll_start_time", "post_roll_stop_time", "pre_roll_enabled", "post_roll_enabled", "update_video_to", "propagate_to_satellites")
    PLAY_START_MARKER_TIME_FIELD_NUMBER: _ClassVar[int]
    IN_TIME_FIELD_NUMBER: _ClassVar[int]
    OUT_TIME_FIELD_NUMBER: _ClassVar[int]
    PRE_ROLL_START_TIME_FIELD_NUMBER: _ClassVar[int]
    POST_ROLL_STOP_TIME_FIELD_NUMBER: _ClassVar[int]
    PRE_ROLL_ENABLED_FIELD_NUMBER: _ClassVar[int]
    POST_ROLL_ENABLED_FIELD_NUMBER: _ClassVar[int]
    UPDATE_VIDEO_TO_FIELD_NUMBER: _ClassVar[int]
    PROPAGATE_TO_SATELLITES_FIELD_NUMBER: _ClassVar[int]
    play_start_marker_time: str
    in_time: str
    out_time: str
    pre_roll_start_time: str
    post_roll_stop_time: str
    pre_roll_enabled: TripleBool
    post_roll_enabled: TripleBool
    update_video_to: TimelineUpdateVideo
    propagate_to_satellites: TripleBool
    def __init__(self, play_start_marker_time: _Optional[str] = ..., in_time: _Optional[str] = ..., out_time: _Optional[str] = ..., pre_roll_start_time: _Optional[str] = ..., post_roll_stop_time: _Optional[str] = ..., pre_roll_enabled: _Optional[_Union[TripleBool, str]] = ..., post_roll_enabled: _Optional[_Union[TripleBool, str]] = ..., update_video_to: _Optional[_Union[TimelineUpdateVideo, str]] = ..., propagate_to_satellites: _Optional[_Union[TripleBool, str]] = ...) -> None: ...

class GetTimelineSelectionRequestBody(_message.Message):
    __slots__ = ("time_scale",)
    TIME_SCALE_FIELD_NUMBER: _ClassVar[int]
    time_scale: TrackOffsetOptions
    def __init__(self, time_scale: _Optional[_Union[TrackOffsetOptions, str]] = ...) -> None: ...

class GetTimelineSelectionResponseBody(_message.Message):
    __slots__ = ("play_start_marker_time", "in_time", "out_time", "pre_roll_start_time", "post_roll_stop_time", "pre_roll_enabled", "post_roll_enabled")
    PLAY_START_MARKER_TIME_FIELD_NUMBER: _ClassVar[int]
    IN_TIME_FIELD_NUMBER: _ClassVar[int]
    OUT_TIME_FIELD_NUMBER: _ClassVar[int]
    PRE_ROLL_START_TIME_FIELD_NUMBER: _ClassVar[int]
    POST_ROLL_STOP_TIME_FIELD_NUMBER: _ClassVar[int]
    PRE_ROLL_ENABLED_FIELD_NUMBER: _ClassVar[int]
    POST_ROLL_ENABLED_FIELD_NUMBER: _ClassVar[int]
    play_start_marker_time: str
    in_time: str
    out_time: str
    pre_roll_start_time: str
    post_roll_stop_time: str
    pre_roll_enabled: bool
    post_roll_enabled: bool
    def __init__(self, play_start_marker_time: _Optional[str] = ..., in_time: _Optional[str] = ..., out_time: _Optional[str] = ..., pre_roll_start_time: _Optional[str] = ..., post_roll_stop_time: _Optional[str] = ..., pre_roll_enabled: bool = ..., post_roll_enabled: bool = ...) -> None: ...

class SelectTracksByNameRequestBody(_message.Message):
    __slots__ = ("track_names", "selection_mode", "pagination_request")
    TRACK_NAMES_FIELD_NUMBER: _ClassVar[int]
    SELECTION_MODE_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_REQUEST_FIELD_NUMBER: _ClassVar[int]
    track_names: _containers.RepeatedScalarFieldContainer[str]
    selection_mode: SelectionMode
    pagination_request: PaginationRequest
    def __init__(self, track_names: _Optional[_Iterable[str]] = ..., selection_mode: _Optional[_Union[SelectionMode, str]] = ..., pagination_request: _Optional[_Union[PaginationRequest, _Mapping]] = ...) -> None: ...

class SelectTracksByNameResponseBody(_message.Message):
    __slots__ = ("stats", "track_list", "pagination_response")
    STATS_FIELD_NUMBER: _ClassVar[int]
    TRACK_LIST_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    stats: Pagination
    track_list: _containers.RepeatedCompositeFieldContainer[Track]
    pagination_response: PaginationResponse
    def __init__(self, stats: _Optional[_Union[Pagination, _Mapping]] = ..., track_list: _Optional[_Iterable[_Union[Track, _Mapping]]] = ..., pagination_response: _Optional[_Union[PaginationResponse, _Mapping]] = ...) -> None: ...

class ImportFailureInfo(_message.Message):
    __slots__ = ("file_path", "failure_message")
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    FAILURE_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    file_path: str
    failure_message: str
    def __init__(self, file_path: _Optional[str] = ..., failure_message: _Optional[str] = ...) -> None: ...

class ImportVideoRequestBody(_message.Message):
    __slots__ = ("video_file_list", "destination", "location", "spot_location_data", "gaps_between_clips", "import_audio_from_file", "audio_destination_path", "remove_existing_video_tracks", "remove_existing_video_clips", "clear_destination_video_track_playlist")
    VIDEO_FILE_LIST_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    SPOT_LOCATION_DATA_FIELD_NUMBER: _ClassVar[int]
    GAPS_BETWEEN_CLIPS_FIELD_NUMBER: _ClassVar[int]
    IMPORT_AUDIO_FROM_FILE_FIELD_NUMBER: _ClassVar[int]
    AUDIO_DESTINATION_PATH_FIELD_NUMBER: _ClassVar[int]
    REMOVE_EXISTING_VIDEO_TRACKS_FIELD_NUMBER: _ClassVar[int]
    REMOVE_EXISTING_VIDEO_CLIPS_FIELD_NUMBER: _ClassVar[int]
    CLEAR_DESTINATION_VIDEO_TRACK_PLAYLIST_FIELD_NUMBER: _ClassVar[int]
    video_file_list: _containers.RepeatedScalarFieldContainer[str]
    destination: MediaDestination
    location: MediaLocation
    spot_location_data: SpotLocationData
    gaps_between_clips: int
    import_audio_from_file: bool
    audio_destination_path: str
    remove_existing_video_tracks: bool
    remove_existing_video_clips: bool
    clear_destination_video_track_playlist: bool
    def __init__(self, video_file_list: _Optional[_Iterable[str]] = ..., destination: _Optional[_Union[MediaDestination, str]] = ..., location: _Optional[_Union[MediaLocation, str]] = ..., spot_location_data: _Optional[_Union[SpotLocationData, _Mapping]] = ..., gaps_between_clips: _Optional[int] = ..., import_audio_from_file: bool = ..., audio_destination_path: _Optional[str] = ..., remove_existing_video_tracks: bool = ..., remove_existing_video_clips: bool = ..., clear_destination_video_track_playlist: bool = ...) -> None: ...

class ImportVideoResponseBody(_message.Message):
    __slots__ = ("failure_list",)
    FAILURE_LIST_FIELD_NUMBER: _ClassVar[int]
    failure_list: _containers.RepeatedCompositeFieldContainer[ImportFailureInfo]
    def __init__(self, failure_list: _Optional[_Iterable[_Union[ImportFailureInfo, _Mapping]]] = ...) -> None: ...

class SelectMemoryLocationRequestBody(_message.Message):
    __slots__ = ("number",)
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    number: int
    def __init__(self, number: _Optional[int] = ...) -> None: ...

class SetTrackMuteStateRequestBody(_message.Message):
    __slots__ = ("track_names", "enabled")
    TRACK_NAMES_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    track_names: _containers.RepeatedScalarFieldContainer[str]
    enabled: bool
    def __init__(self, track_names: _Optional[_Iterable[str]] = ..., enabled: bool = ...) -> None: ...

class SetTrackSoloStateRequestBody(_message.Message):
    __slots__ = ("track_names", "enabled")
    TRACK_NAMES_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    track_names: _containers.RepeatedScalarFieldContainer[str]
    enabled: bool
    def __init__(self, track_names: _Optional[_Iterable[str]] = ..., enabled: bool = ...) -> None: ...

class SetTrackSoloSafeStateRequestBody(_message.Message):
    __slots__ = ("track_names", "enabled")
    TRACK_NAMES_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    track_names: _containers.RepeatedScalarFieldContainer[str]
    enabled: bool
    def __init__(self, track_names: _Optional[_Iterable[str]] = ..., enabled: bool = ...) -> None: ...

class SetTrackRecordEnableStateRequestBody(_message.Message):
    __slots__ = ("track_names", "enabled")
    TRACK_NAMES_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    track_names: _containers.RepeatedScalarFieldContainer[str]
    enabled: bool
    def __init__(self, track_names: _Optional[_Iterable[str]] = ..., enabled: bool = ...) -> None: ...

class SetTrackRecordSafeEnableStateRequestBody(_message.Message):
    __slots__ = ("track_names", "enabled")
    TRACK_NAMES_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    track_names: _containers.RepeatedScalarFieldContainer[str]
    enabled: bool
    def __init__(self, track_names: _Optional[_Iterable[str]] = ..., enabled: bool = ...) -> None: ...

class SetTrackInputMonitorStateRequestBody(_message.Message):
    __slots__ = ("track_names", "enabled")
    TRACK_NAMES_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    track_names: _containers.RepeatedScalarFieldContainer[str]
    enabled: bool
    def __init__(self, track_names: _Optional[_Iterable[str]] = ..., enabled: bool = ...) -> None: ...

class SetTrackSmartDspStateRequestBody(_message.Message):
    __slots__ = ("track_names", "enabled")
    TRACK_NAMES_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    track_names: _containers.RepeatedScalarFieldContainer[str]
    enabled: bool
    def __init__(self, track_names: _Optional[_Iterable[str]] = ..., enabled: bool = ...) -> None: ...

class SetTrackHiddenStateRequestBody(_message.Message):
    __slots__ = ("track_names", "enabled")
    TRACK_NAMES_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    track_names: _containers.RepeatedScalarFieldContainer[str]
    enabled: bool
    def __init__(self, track_names: _Optional[_Iterable[str]] = ..., enabled: bool = ...) -> None: ...

class SetTrackInactiveStateRequestBody(_message.Message):
    __slots__ = ("track_names", "enabled")
    TRACK_NAMES_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    track_names: _containers.RepeatedScalarFieldContainer[str]
    enabled: bool
    def __init__(self, track_names: _Optional[_Iterable[str]] = ..., enabled: bool = ...) -> None: ...

class SetTrackFrozenStateRequestBody(_message.Message):
    __slots__ = ("track_names", "enabled")
    TRACK_NAMES_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    track_names: _containers.RepeatedScalarFieldContainer[str]
    enabled: bool
    def __init__(self, track_names: _Optional[_Iterable[str]] = ..., enabled: bool = ...) -> None: ...

class SetTrackOnlineStateRequestBody(_message.Message):
    __slots__ = ("track_name", "enabled")
    TRACK_NAME_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    track_name: str
    enabled: bool
    def __init__(self, track_name: _Optional[str] = ..., enabled: bool = ...) -> None: ...

class SetTrackOpenStateRequestBody(_message.Message):
    __slots__ = ("track_names", "enabled")
    TRACK_NAMES_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    track_names: _containers.RepeatedScalarFieldContainer[str]
    enabled: bool
    def __init__(self, track_names: _Optional[_Iterable[str]] = ..., enabled: bool = ...) -> None: ...

class GetSessionIDsResponseBody(_message.Message):
    __slots__ = ("origin_id", "instance_id", "parent_id")
    ORIGIN_ID_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_ID_FIELD_NUMBER: _ClassVar[int]
    origin_id: str
    instance_id: str
    parent_id: str
    def __init__(self, origin_id: _Optional[str] = ..., instance_id: _Optional[str] = ..., parent_id: _Optional[str] = ...) -> None: ...

class GetMemoryLocationsManageModeResponseBody(_message.Message):
    __slots__ = ("enabled",)
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    def __init__(self, enabled: bool = ...) -> None: ...

class SetMemoryLocationsManageModeRequestBody(_message.Message):
    __slots__ = ("enabled",)
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    def __init__(self, enabled: bool = ...) -> None: ...

class HostReadyCheckResponseBody(_message.Message):
    __slots__ = ("is_host_ready",)
    IS_HOST_READY_FIELD_NUMBER: _ClassVar[int]
    is_host_ready: bool
    def __init__(self, is_host_ready: bool = ...) -> None: ...

class SetMainCounterFormatRequestBody(_message.Message):
    __slots__ = ("time_scale",)
    TIME_SCALE_FIELD_NUMBER: _ClassVar[int]
    time_scale: TrackOffsetOptions
    def __init__(self, time_scale: _Optional[_Union[TrackOffsetOptions, str]] = ...) -> None: ...

class SetSubCounterFormatRequestBody(_message.Message):
    __slots__ = ("time_scale",)
    TIME_SCALE_FIELD_NUMBER: _ClassVar[int]
    time_scale: TrackOffsetOptions
    def __init__(self, time_scale: _Optional[_Union[TrackOffsetOptions, str]] = ...) -> None: ...

class GetMainCounterFormatResponseBody(_message.Message):
    __slots__ = ("current_setting", "possible_settings")
    CURRENT_SETTING_FIELD_NUMBER: _ClassVar[int]
    POSSIBLE_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    current_setting: TrackOffsetOptions
    possible_settings: _containers.RepeatedScalarFieldContainer[TrackOffsetOptions]
    def __init__(self, current_setting: _Optional[_Union[TrackOffsetOptions, str]] = ..., possible_settings: _Optional[_Iterable[_Union[TrackOffsetOptions, str]]] = ...) -> None: ...

class GetSubCounterFormatResponseBody(_message.Message):
    __slots__ = ("current_setting", "possible_settings")
    CURRENT_SETTING_FIELD_NUMBER: _ClassVar[int]
    POSSIBLE_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    current_setting: TrackOffsetOptions
    possible_settings: _containers.RepeatedScalarFieldContainer[TrackOffsetOptions]
    def __init__(self, current_setting: _Optional[_Union[TrackOffsetOptions, str]] = ..., possible_settings: _Optional[_Iterable[_Union[TrackOffsetOptions, str]]] = ...) -> None: ...

class UndoHistoryOperation(_message.Message):
    __slots__ = ("time", "operation", "details")
    TIME_FIELD_NUMBER: _ClassVar[int]
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    time: str
    operation: str
    details: str
    def __init__(self, time: _Optional[str] = ..., operation: _Optional[str] = ..., details: _Optional[str] = ...) -> None: ...

class UndoRequestBody(_message.Message):
    __slots__ = ("levels",)
    LEVELS_FIELD_NUMBER: _ClassVar[int]
    levels: int
    def __init__(self, levels: _Optional[int] = ...) -> None: ...

class UndoResponseBody(_message.Message):
    __slots__ = ("operations",)
    OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    operations: _containers.RepeatedCompositeFieldContainer[UndoHistoryOperation]
    def __init__(self, operations: _Optional[_Iterable[_Union[UndoHistoryOperation, _Mapping]]] = ...) -> None: ...

class RedoRequestBody(_message.Message):
    __slots__ = ("levels",)
    LEVELS_FIELD_NUMBER: _ClassVar[int]
    levels: int
    def __init__(self, levels: _Optional[int] = ...) -> None: ...

class RedoResponseBody(_message.Message):
    __slots__ = ("operations",)
    OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    operations: _containers.RepeatedCompositeFieldContainer[UndoHistoryOperation]
    def __init__(self, operations: _Optional[_Iterable[_Union[UndoHistoryOperation, _Mapping]]] = ...) -> None: ...

class UndoAllResponseBody(_message.Message):
    __slots__ = ("operations",)
    OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    operations: _containers.RepeatedCompositeFieldContainer[UndoHistoryOperation]
    def __init__(self, operations: _Optional[_Iterable[_Union[UndoHistoryOperation, _Mapping]]] = ...) -> None: ...

class RedoAllResponseBody(_message.Message):
    __slots__ = ("operations",)
    OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    operations: _containers.RepeatedCompositeFieldContainer[UndoHistoryOperation]
    def __init__(self, operations: _Optional[_Iterable[_Union[UndoHistoryOperation, _Mapping]]] = ...) -> None: ...

class SetTrackDSPModeSafeStateRequestBody(_message.Message):
    __slots__ = ("track_names", "enabled")
    TRACK_NAMES_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    track_names: _containers.RepeatedScalarFieldContainer[str]
    enabled: bool
    def __init__(self, track_names: _Optional[_Iterable[str]] = ..., enabled: bool = ...) -> None: ...

class GetSessionSystemDelayInfoResponseBody(_message.Message):
    __slots__ = ("samples", "delay_compensation_enabled")
    SAMPLES_FIELD_NUMBER: _ClassVar[int]
    DELAY_COMPENSATION_ENABLED_FIELD_NUMBER: _ClassVar[int]
    samples: int
    delay_compensation_enabled: bool
    def __init__(self, samples: _Optional[int] = ..., delay_compensation_enabled: bool = ...) -> None: ...

class TrackExcludedFromClipGroupInfo(_message.Message):
    __slots__ = ("track_name", "reason")
    TRACK_NAME_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    track_name: str
    reason: TrackFromClipGroupExclusionReason
    def __init__(self, track_name: _Optional[str] = ..., reason: _Optional[_Union[TrackFromClipGroupExclusionReason, str]] = ...) -> None: ...

class RepeatSelectionRequestBody(_message.Message):
    __slots__ = ("num_repeats",)
    NUM_REPEATS_FIELD_NUMBER: _ClassVar[int]
    num_repeats: int
    def __init__(self, num_repeats: _Optional[int] = ...) -> None: ...

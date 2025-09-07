from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CommandId(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CreateSession: _ClassVar[CommandId]
    CId_CreateSession: _ClassVar[CommandId]
    OpenSession: _ClassVar[CommandId]
    CId_OpenSession: _ClassVar[CommandId]
    Import: _ClassVar[CommandId]
    CId_Import: _ClassVar[CommandId]
    GetTrackList: _ClassVar[CommandId]
    CId_GetTrackList: _ClassVar[CommandId]
    SelectAllClipsOnTrack: _ClassVar[CommandId]
    CId_SelectAllClipsOnTrack: _ClassVar[CommandId]
    ExtendSelectionToTargetTracks: _ClassVar[CommandId]
    CId_ExtendSelectionToTargetTracks: _ClassVar[CommandId]
    TrimToSelection: _ClassVar[CommandId]
    CId_TrimToSelection: _ClassVar[CommandId]
    CreateFadesBasedOnPreset: _ClassVar[CommandId]
    CId_CreateFadesBasedOnPreset: _ClassVar[CommandId]
    RenameTargetTrack: _ClassVar[CommandId]
    CId_RenameTargetTrack: _ClassVar[CommandId]
    ConsolidateClip: _ClassVar[CommandId]
    CId_ConsolidateClip: _ClassVar[CommandId]
    ExportClipsAsFiles: _ClassVar[CommandId]
    CId_ExportClipsAsFiles: _ClassVar[CommandId]
    ExportSelectedTracksAsAAFOMF: _ClassVar[CommandId]
    CId_ExportSelectedTracksAsAAFOMF: _ClassVar[CommandId]
    GetTaskStatus: _ClassVar[CommandId]
    CId_GetTaskStatus: _ClassVar[CommandId]
    HostReadyCheck: _ClassVar[CommandId]
    CId_HostReadyCheck: _ClassVar[CommandId]
    RefreshTargetAudioFiles: _ClassVar[CommandId]
    CId_RefreshTargetAudioFiles: _ClassVar[CommandId]
    RefreshAllModifiedAudioFiles: _ClassVar[CommandId]
    CId_RefreshAllModifiedAudioFiles: _ClassVar[CommandId]
    GetFileLocation: _ClassVar[CommandId]
    CId_GetFileLocation: _ClassVar[CommandId]
    CloseSession: _ClassVar[CommandId]
    CId_CloseSession: _ClassVar[CommandId]
    SaveSession: _ClassVar[CommandId]
    CId_SaveSession: _ClassVar[CommandId]
    SaveSessionAs: _ClassVar[CommandId]
    CId_SaveSessionAs: _ClassVar[CommandId]
    Cut: _ClassVar[CommandId]
    CId_Cut: _ClassVar[CommandId]
    Copy: _ClassVar[CommandId]
    CId_Copy: _ClassVar[CommandId]
    Paste: _ClassVar[CommandId]
    CId_Paste: _ClassVar[CommandId]
    Clear: _ClassVar[CommandId]
    CId_Clear: _ClassVar[CommandId]
    CutSpecial: _ClassVar[CommandId]
    CId_CutSpecial: _ClassVar[CommandId]
    CopySpecial: _ClassVar[CommandId]
    CId_CopySpecial: _ClassVar[CommandId]
    ClearSpecial: _ClassVar[CommandId]
    CId_ClearSpecial: _ClassVar[CommandId]
    PasteSpecial: _ClassVar[CommandId]
    CId_PasteSpecial: _ClassVar[CommandId]
    ExportMix: _ClassVar[CommandId]
    CId_ExportMix: _ClassVar[CommandId]
    Spot: _ClassVar[CommandId]
    CId_Spot: _ClassVar[CommandId]
    ExportSessionInfoAsText: _ClassVar[CommandId]
    CId_ExportSessionInfoAsText: _ClassVar[CommandId]
    GetDynamicProperties: _ClassVar[CommandId]
    CId_GetDynamicProperties: _ClassVar[CommandId]
    SetPlaybackMode: _ClassVar[CommandId]
    CId_SetPlaybackMode: _ClassVar[CommandId]
    SetRecordMode: _ClassVar[CommandId]
    CId_SetRecordMode: _ClassVar[CommandId]
    GetSessionAudioFormat: _ClassVar[CommandId]
    CId_GetSessionAudioFormat: _ClassVar[CommandId]
    GetSessionSampleRate: _ClassVar[CommandId]
    CId_GetSessionSampleRate: _ClassVar[CommandId]
    GetSessionBitDepth: _ClassVar[CommandId]
    CId_GetSessionBitDepth: _ClassVar[CommandId]
    GetSessionInterleavedState: _ClassVar[CommandId]
    CId_GetSessionInterleavedState: _ClassVar[CommandId]
    GetSessionTimeCodeRate: _ClassVar[CommandId]
    CId_GetSessionTimeCodeRate: _ClassVar[CommandId]
    GetSessionFeetFramesRate: _ClassVar[CommandId]
    CId_GetSessionFeetFramesRate: _ClassVar[CommandId]
    GetSessionAudioRatePullSettings: _ClassVar[CommandId]
    CId_GetSessionAudioRatePullSettings: _ClassVar[CommandId]
    GetSessionVideoRatePullSettings: _ClassVar[CommandId]
    CId_GetSessionVideoRatePullSettings: _ClassVar[CommandId]
    GetSessionName: _ClassVar[CommandId]
    CId_GetSessionName: _ClassVar[CommandId]
    GetSessionPath: _ClassVar[CommandId]
    CId_GetSessionPath: _ClassVar[CommandId]
    GetSessionStartTime: _ClassVar[CommandId]
    CId_GetSessionStartTime: _ClassVar[CommandId]
    GetSessionLength: _ClassVar[CommandId]
    CId_GetSessionLength: _ClassVar[CommandId]
    SetSessionAudioFormat: _ClassVar[CommandId]
    CId_SetSessionAudioFormat: _ClassVar[CommandId]
    SetSessionBitDepth: _ClassVar[CommandId]
    CId_SetSessionBitDepth: _ClassVar[CommandId]
    SetSessionInterleavedState: _ClassVar[CommandId]
    CId_SetSessionInterleavedState: _ClassVar[CommandId]
    SetSessionTimeCodeRate: _ClassVar[CommandId]
    CId_SetSessionTimeCodeRate: _ClassVar[CommandId]
    SetSessionFeetFramesRate: _ClassVar[CommandId]
    CId_SetSessionFeetFramesRate: _ClassVar[CommandId]
    SetSessionAudioRatePullSettings: _ClassVar[CommandId]
    CId_SetSessionAudioRatePullSettings: _ClassVar[CommandId]
    SetSessionVideoRatePullSettings: _ClassVar[CommandId]
    CId_SetSessionVideoRatePullSettings: _ClassVar[CommandId]
    SetSessionStartTime: _ClassVar[CommandId]
    CId_SetSessionStartTime: _ClassVar[CommandId]
    SetSessionLength: _ClassVar[CommandId]
    CId_SetSessionLength: _ClassVar[CommandId]
    GetPTSLVersion: _ClassVar[CommandId]
    CId_GetPTSLVersion: _ClassVar[CommandId]
    GetPlaybackMode: _ClassVar[CommandId]
    CId_GetPlaybackMode: _ClassVar[CommandId]
    GetRecordMode: _ClassVar[CommandId]
    CId_GetRecordMode: _ClassVar[CommandId]
    GetTransportArmed: _ClassVar[CommandId]
    CId_GetTransportArmed: _ClassVar[CommandId]
    GetTransportState: _ClassVar[CommandId]
    CId_GetTransportState: _ClassVar[CommandId]
    ClearMemoryLocation: _ClassVar[CommandId]
    CId_ClearMemoryLocation: _ClassVar[CommandId]
    RenameSelectedClip: _ClassVar[CommandId]
    CId_RenameSelectedClip: _ClassVar[CommandId]
    RenameTargetClip: _ClassVar[CommandId]
    CId_RenameTargetClip: _ClassVar[CommandId]
    TogglePlayState: _ClassVar[CommandId]
    CId_TogglePlayState: _ClassVar[CommandId]
    ToggleRecordEnable: _ClassVar[CommandId]
    CId_ToggleRecordEnable: _ClassVar[CommandId]
    PlayHalfSpeed: _ClassVar[CommandId]
    CId_PlayHalfSpeed: _ClassVar[CommandId]
    RecordHalfSpeed: _ClassVar[CommandId]
    CId_RecordHalfSpeed: _ClassVar[CommandId]
    EditMemoryLocation: _ClassVar[CommandId]
    CId_EditMemoryLocation: _ClassVar[CommandId]
    GetMemoryLocations: _ClassVar[CommandId]
    CId_GetMemoryLocations: _ClassVar[CommandId]
    RegisterConnection: _ClassVar[CommandId]
    CId_RegisterConnection: _ClassVar[CommandId]
    CreateMemoryLocation: _ClassVar[CommandId]
    CId_CreateMemoryLocation: _ClassVar[CommandId]
    CreateNewTracks: _ClassVar[CommandId]
    CId_CreateNewTracks: _ClassVar[CommandId]
    SelectTracksByName: _ClassVar[CommandId]
    CId_SelectTracksByName: _ClassVar[CommandId]
    GetEditMode: _ClassVar[CommandId]
    CId_GetEditMode: _ClassVar[CommandId]
    SetEditMode: _ClassVar[CommandId]
    CId_SetEditMode: _ClassVar[CommandId]
    GetEditTool: _ClassVar[CommandId]
    CId_GetEditTool: _ClassVar[CommandId]
    SetEditTool: _ClassVar[CommandId]
    CId_SetEditTool: _ClassVar[CommandId]
    RecallZoomPreset: _ClassVar[CommandId]
    CId_RecallZoomPreset: _ClassVar[CommandId]
    GetEditModeOptions: _ClassVar[CommandId]
    CId_GetEditModeOptions: _ClassVar[CommandId]
    SetEditModeOptions: _ClassVar[CommandId]
    CId_SetEditModeOptions: _ClassVar[CommandId]
    SetTimelineSelection: _ClassVar[CommandId]
    CId_SetTimelineSelection: _ClassVar[CommandId]
    GetTimelineSelection: _ClassVar[CommandId]
    CId_GetTimelineSelection: _ClassVar[CommandId]
    ImportVideo: _ClassVar[CommandId]
    CId_ImportVideo: _ClassVar[CommandId]
    SelectMemoryLocation: _ClassVar[CommandId]
    CId_SelectMemoryLocation: _ClassVar[CommandId]
    SetTrackMuteState: _ClassVar[CommandId]
    CId_SetTrackMuteState: _ClassVar[CommandId]
    SetTrackSoloState: _ClassVar[CommandId]
    CId_SetTrackSoloState: _ClassVar[CommandId]
    SetTrackSoloSafeState: _ClassVar[CommandId]
    CId_SetTrackSoloSafeState: _ClassVar[CommandId]
    SetTrackRecordEnableState: _ClassVar[CommandId]
    CId_SetTrackRecordEnableState: _ClassVar[CommandId]
    SetTrackRecordSafeEnableState: _ClassVar[CommandId]
    CId_SetTrackRecordSafeEnableState: _ClassVar[CommandId]
    SetTrackInputMonitorState: _ClassVar[CommandId]
    CId_SetTrackInputMonitorState: _ClassVar[CommandId]
    SetTrackSmartDspState: _ClassVar[CommandId]
    CId_SetTrackSmartDspState: _ClassVar[CommandId]
    SetTrackHiddenState: _ClassVar[CommandId]
    CId_SetTrackHiddenState: _ClassVar[CommandId]
    SetTrackInactiveState: _ClassVar[CommandId]
    CId_SetTrackInactiveState: _ClassVar[CommandId]
    SetTrackFrozenState: _ClassVar[CommandId]
    CId_SetTrackFrozenState: _ClassVar[CommandId]
    SetTrackOnlineState: _ClassVar[CommandId]
    CId_SetTrackOnlineState: _ClassVar[CommandId]
    SetTrackOpenState: _ClassVar[CommandId]
    CId_SetTrackOpenState: _ClassVar[CommandId]
    GetSessionIDs: _ClassVar[CommandId]
    CId_GetSessionIDs: _ClassVar[CommandId]
    GetMemoryLocationsManageMode: _ClassVar[CommandId]
    CId_GetMemoryLocationsManageMode: _ClassVar[CommandId]
    SetMemoryLocationsManageMode: _ClassVar[CommandId]
    CId_SetMemoryLocationsManageMode: _ClassVar[CommandId]
    SetMainCounterFormat: _ClassVar[CommandId]
    CId_SetMainCounterFormat: _ClassVar[CommandId]
    SetSubCounterFormat: _ClassVar[CommandId]
    CId_SetSubCounterFormat: _ClassVar[CommandId]
    GetMainCounterFormat: _ClassVar[CommandId]
    CId_GetMainCounterFormat: _ClassVar[CommandId]
    GetSubCounterFormat: _ClassVar[CommandId]
    CId_GetSubCounterFormat: _ClassVar[CommandId]
    Undo: _ClassVar[CommandId]
    CId_Undo: _ClassVar[CommandId]
    Redo: _ClassVar[CommandId]
    CId_Redo: _ClassVar[CommandId]
    UndoAll: _ClassVar[CommandId]
    CId_UndoAll: _ClassVar[CommandId]
    RedoAll: _ClassVar[CommandId]
    CId_RedoAll: _ClassVar[CommandId]
    ClearUndoQueue: _ClassVar[CommandId]
    CId_ClearUndoQueue: _ClassVar[CommandId]
    SetTrackDSPModeSafeState: _ClassVar[CommandId]
    CId_SetTrackDSPModeSafeState: _ClassVar[CommandId]
    GetSessionSystemDelayInfo: _ClassVar[CommandId]
    CId_GetSessionSystemDelayInfo: _ClassVar[CommandId]
    GroupClips: _ClassVar[CommandId]
    CId_GroupClips: _ClassVar[CommandId]
    UngroupClips: _ClassVar[CommandId]
    CId_UngroupClips: _ClassVar[CommandId]
    UngroupAllClips: _ClassVar[CommandId]
    CId_UngroupAllClips: _ClassVar[CommandId]
    RegroupClips: _ClassVar[CommandId]
    CId_RegroupClips: _ClassVar[CommandId]
    RepeatSelection: _ClassVar[CommandId]
    CId_RepeatSelection: _ClassVar[CommandId]
    DuplicateSelection: _ClassVar[CommandId]
    CId_DuplicateSelection: _ClassVar[CommandId]
    ClearAllMemoryLocations: _ClassVar[CommandId]
    CId_ClearAllMemoryLocations: _ClassVar[CommandId]
    CId_GetTimeAsType: _ClassVar[CommandId]
    CId_SubtractLocations: _ClassVar[CommandId]
    CId_AddLengthToLocation: _ClassVar[CommandId]
    CId_SubtractPositions: _ClassVar[CommandId]
    CId_AddLengthToPosition: _ClassVar[CommandId]
    CId_ImportAudioToClipList: _ClassVar[CommandId]
    CId_SpotClipsByID: _ClassVar[CommandId]
    CId_GetClipList: _ClassVar[CommandId]
    CId_GetMediaFileInfo: _ClassVar[CommandId]
    CId_CreateAudioClips: _ClassVar[CommandId]
    CId_GetExportMixSourceList: _ClassVar[CommandId]
    CId_CreateBatchJob: _ClassVar[CommandId]
    CId_GetMonitorOutputPath: _ClassVar[CommandId]
    CId_GetEditSelection: _ClassVar[CommandId]
    CId_SubscribeToEvents: _ClassVar[CommandId]
    CId_GetBatchJobStatus: _ClassVar[CommandId]
    CId_BounceTrack: _ClassVar[CommandId]
    CId_PollEvents: _ClassVar[CommandId]
    CId_UnsubscribeFromEvents: _ClassVar[CommandId]
    CId_CompleteBatchJob: _ClassVar[CommandId]
    CId_CancelBatchJob: _ClassVar[CommandId]
    CId_BeginScrub: _ClassVar[CommandId]
    CId_EndScrub: _ClassVar[CommandId]
    CId_ContinueScrub: _ClassVar[CommandId]
    CId_EnableCueProVideoPlugIn: _ClassVar[CommandId]
    CId_UpdateVideo: _ClassVar[CommandId]
    CId_EnableAPI: _ClassVar[CommandId]
    CId_ExchangePublicKeys: _ClassVar[CommandId]

class EventId(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EId_Unknown: _ClassVar[EventId]
    EId_SessionOpened: _ClassVar[EventId]
    EId_SessionCreated: _ClassVar[EventId]
    EId_SessionClosed: _ClassVar[EventId]

class TaskStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    Queued: _ClassVar[TaskStatus]
    TStatus_Queued: _ClassVar[TaskStatus]
    Pending: _ClassVar[TaskStatus]
    TStatus_Pending: _ClassVar[TaskStatus]
    InProgress: _ClassVar[TaskStatus]
    TStatus_InProgress: _ClassVar[TaskStatus]
    Completed: _ClassVar[TaskStatus]
    TStatus_Completed: _ClassVar[TaskStatus]
    Failed: _ClassVar[TaskStatus]
    TStatus_Failed: _ClassVar[TaskStatus]
    WaitingForUserInput: _ClassVar[TaskStatus]
    TStatus_WaitingForUserInput: _ClassVar[TaskStatus]
    CompletedWithBadResponse: _ClassVar[TaskStatus]
    TStatus_CompletedWithBadResponse: _ClassVar[TaskStatus]
    FailedWithBadErrorResponse: _ClassVar[TaskStatus]
    TStatus_FailedWithBadErrorResponse: _ClassVar[TaskStatus]

class CommandErrorType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    OS_WritePermissions: _ClassVar[CommandErrorType]
    CEType_OS_WritePermissions: _ClassVar[CommandErrorType]
    OS_ErrorCode: _ClassVar[CommandErrorType]
    CEType_OS_ErrorCode: _ClassVar[CommandErrorType]
    OS_NoLocationFound: _ClassVar[CommandErrorType]
    CEType_OS_NoLocationFound: _ClassVar[CommandErrorType]
    OS_NoSessionFound: _ClassVar[CommandErrorType]
    CEType_OS_NoSessionFound: _ClassVar[CommandErrorType]
    OS_FilePathLocation: _ClassVar[CommandErrorType]
    OS_ReadError: _ClassVar[CommandErrorType]
    CEType_OS_ReadError: _ClassVar[CommandErrorType]
    OS_DiskSpace: _ClassVar[CommandErrorType]
    CEType_OS_DiskSpace: _ClassVar[CommandErrorType]
    OS_DuplicateName: _ClassVar[CommandErrorType]
    CEType_OS_DuplicateName: _ClassVar[CommandErrorType]
    OS_IllegalCharacters: _ClassVar[CommandErrorType]
    CEType_OS_IllegalCharacters: _ClassVar[CommandErrorType]
    OS_CharactersLimit: _ClassVar[CommandErrorType]
    CEType_OS_CharactersLimit: _ClassVar[CommandErrorType]
    OS_ProToolsIsNotAvailable: _ClassVar[CommandErrorType]
    CEType_OS_ProToolsIsNotAvailable: _ClassVar[CommandErrorType]
    OS_NoFilePathFound: _ClassVar[CommandErrorType]
    CEType_OS_NoFilePathFound: _ClassVar[CommandErrorType]
    PT_UnknownError: _ClassVar[CommandErrorType]
    CEType_PT_UnknownError: _ClassVar[CommandErrorType]
    PT_NoTemplateGroup: _ClassVar[CommandErrorType]
    CEType_PT_NoTemplateGroup: _ClassVar[CommandErrorType]
    PT_NoTemplate: _ClassVar[CommandErrorType]
    CEType_PT_NoTemplate: _ClassVar[CommandErrorType]
    PT_SampleRateMismatch: _ClassVar[CommandErrorType]
    CEType_PT_SampleRateMismatch: _ClassVar[CommandErrorType]
    PT_NoVideoTrackFound: _ClassVar[CommandErrorType]
    CEType_PT_NoVideoTrackFound: _ClassVar[CommandErrorType]
    PT_NoTracksFound: _ClassVar[CommandErrorType]
    CEType_PT_NoTracksFound: _ClassVar[CommandErrorType]
    PT_NoOpenedSession: _ClassVar[CommandErrorType]
    CEType_PT_NoOpenedSession: _ClassVar[CommandErrorType]
    PT_NoTrackFound: _ClassVar[CommandErrorType]
    CEType_PT_NoTrackFound: _ClassVar[CommandErrorType]
    PT_NoClipsFound: _ClassVar[CommandErrorType]
    CEType_PT_NoClipsFound: _ClassVar[CommandErrorType]
    PT_NoSelection: _ClassVar[CommandErrorType]
    CEType_PT_NoSelection: _ClassVar[CommandErrorType]
    PT_RecordDrive: _ClassVar[CommandErrorType]
    CEType_PT_RecordDrive: _ClassVar[CommandErrorType]
    PT_NoPresetFound: _ClassVar[CommandErrorType]
    CEType_PT_NoPresetFound: _ClassVar[CommandErrorType]
    PT_FileTypeMXF: _ClassVar[CommandErrorType]
    CEType_PT_FileTypeMXF: _ClassVar[CommandErrorType]
    PT_CopyOptionCopy: _ClassVar[CommandErrorType]
    CEType_PT_CopyOptionCopy: _ClassVar[CommandErrorType]
    PT_CopyOptionLink: _ClassVar[CommandErrorType]
    CEType_PT_CopyOptionLink: _ClassVar[CommandErrorType]
    PT_QuantizeEdits: _ClassVar[CommandErrorType]
    CEType_PT_QuantizeEdits: _ClassVar[CommandErrorType]
    PT_ExportAsMultichannel: _ClassVar[CommandErrorType]
    CEType_PT_ExportAsMultichannel: _ClassVar[CommandErrorType]
    PT_IllegalCharactersComments: _ClassVar[CommandErrorType]
    CEType_PT_IllegalCharactersComments: _ClassVar[CommandErrorType]
    PT_IllegalCharactersSequenceName: _ClassVar[CommandErrorType]
    CEType_PT_IllegalCharactersSequenceName: _ClassVar[CommandErrorType]
    PT_MaxCharactersComments: _ClassVar[CommandErrorType]
    CEType_PT_MaxCharactersComments: _ClassVar[CommandErrorType]
    PT_MaxCharactersSequenceName: _ClassVar[CommandErrorType]
    CEType_PT_MaxCharactersSequenceName: _ClassVar[CommandErrorType]
    PT_NoSequenceName: _ClassVar[CommandErrorType]
    CEType_PT_NoSequenceName: _ClassVar[CommandErrorType]
    PT_InvalidTask: _ClassVar[CommandErrorType]
    CEType_PT_InvalidTask: _ClassVar[CommandErrorType]
    PT_FileNotFound: _ClassVar[CommandErrorType]
    CEType_PT_FileNotFound: _ClassVar[CommandErrorType]
    PT_InvalidSelection: _ClassVar[CommandErrorType]
    CEType_PT_InvalidSelection: _ClassVar[CommandErrorType]
    PT_ReadOnlySession: _ClassVar[CommandErrorType]
    CEType_PT_ReadOnlySession: _ClassVar[CommandErrorType]
    PT_InvalidParameter: _ClassVar[CommandErrorType]
    CEType_PT_InvalidParameter: _ClassVar[CommandErrorType]
    PT_Forbidden: _ClassVar[CommandErrorType]
    CEType_PT_Forbidden: _ClassVar[CommandErrorType]
    PT_NoTimelineFound: _ClassVar[CommandErrorType]
    CEType_PT_NoTimelineFound: _ClassVar[CommandErrorType]
    PT_ArgumentOutOfRange: _ClassVar[CommandErrorType]
    CEType_PT_ArgumentOutOfRange: _ClassVar[CommandErrorType]
    PT_ForbiddenTrackType: _ClassVar[CommandErrorType]
    CEType_PT_ForbiddenTrackType: _ClassVar[CommandErrorType]
    PT_NoVideoEngineFound: _ClassVar[CommandErrorType]
    CEType_PT_NoVideoEngineFound: _ClassVar[CommandErrorType]
    PT_NoDspHardwareFound: _ClassVar[CommandErrorType]
    CEType_PT_NoDspHardwareFound: _ClassVar[CommandErrorType]
    PT_UnsupportedCommand: _ClassVar[CommandErrorType]
    CEType_PT_UnsupportedCommand: _ClassVar[CommandErrorType]
    PT_HostNotReady: _ClassVar[CommandErrorType]
    CEType_PT_HostNotReady: _ClassVar[CommandErrorType]
    PT_CannotBeDone: _ClassVar[CommandErrorType]
    CEType_PT_CannotBeDone: _ClassVar[CommandErrorType]
    PT_ResponseLengthExceeded: _ClassVar[CommandErrorType]
    CEType_PT_ResponseLengthExceeded: _ClassVar[CommandErrorType]
    PT_CommandTimeout: _ClassVar[CommandErrorType]
    CEType_PT_CommandTimeout: _ClassVar[CommandErrorType]
    PT_HostIsBusy: _ClassVar[CommandErrorType]
    CEType_PT_HostIsBusy: _ClassVar[CommandErrorType]
    CEType_PT_DeprecatedParameter: _ClassVar[CommandErrorType]
    CEType_PT_DeprecatedParameterValue: _ClassVar[CommandErrorType]
    PT_Info: _ClassVar[CommandErrorType]
    CEType_PT_Info: _ClassVar[CommandErrorType]
    SDK_VersionMismatch: _ClassVar[CommandErrorType]
    CEType_SDK_VersionMismatch: _ClassVar[CommandErrorType]
    SDK_NotImplemented: _ClassVar[CommandErrorType]
    CEType_SDK_NotImplemented: _ClassVar[CommandErrorType]
    SDK_SessionIdParseError: _ClassVar[CommandErrorType]
    CEType_SDK_SessionIdParseError: _ClassVar[CommandErrorType]
    SDK_GrpcGeneric: _ClassVar[CommandErrorType]
    CEType_SDK_GrpcGeneric: _ClassVar[CommandErrorType]

class TrackType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    Unknown: _ClassVar[TrackType]
    TT_Unknown: _ClassVar[TrackType]
    TType_Unknown: _ClassVar[TrackType]
    Midi: _ClassVar[TrackType]
    TT_Midi: _ClassVar[TrackType]
    TType_Midi: _ClassVar[TrackType]
    AudioTrack: _ClassVar[TrackType]
    TT_Audio: _ClassVar[TrackType]
    TType_Audio: _ClassVar[TrackType]
    Aux: _ClassVar[TrackType]
    TT_Aux: _ClassVar[TrackType]
    TType_Aux: _ClassVar[TrackType]
    VideoTrack: _ClassVar[TrackType]
    TT_Video: _ClassVar[TrackType]
    TType_Video: _ClassVar[TrackType]
    Vca: _ClassVar[TrackType]
    TT_Vca: _ClassVar[TrackType]
    TType_Vca: _ClassVar[TrackType]
    Tempo: _ClassVar[TrackType]
    TT_Tempo: _ClassVar[TrackType]
    TType_Tempo: _ClassVar[TrackType]
    Markers: _ClassVar[TrackType]
    TT_Markers: _ClassVar[TrackType]
    TType_Markers: _ClassVar[TrackType]
    Meter: _ClassVar[TrackType]
    TT_Meter: _ClassVar[TrackType]
    TType_Meter: _ClassVar[TrackType]
    KeySignature: _ClassVar[TrackType]
    TT_KeySignature: _ClassVar[TrackType]
    TType_KeySignature: _ClassVar[TrackType]
    ChordSymbols: _ClassVar[TrackType]
    TT_ChordSymbols: _ClassVar[TrackType]
    TType_ChordSymbols: _ClassVar[TrackType]
    Instrument: _ClassVar[TrackType]
    TT_Instrument: _ClassVar[TrackType]
    TType_Instrument: _ClassVar[TrackType]
    Master: _ClassVar[TrackType]
    TT_Master: _ClassVar[TrackType]
    TType_Master: _ClassVar[TrackType]
    Heat: _ClassVar[TrackType]
    TT_Heat: _ClassVar[TrackType]
    TType_Heat: _ClassVar[TrackType]
    BasicFolder: _ClassVar[TrackType]
    TT_BasicFolder: _ClassVar[TrackType]
    TType_BasicFolder: _ClassVar[TrackType]
    RoutingFolder: _ClassVar[TrackType]
    TT_RoutingFolder: _ClassVar[TrackType]
    TType_RoutingFolder: _ClassVar[TrackType]
    CompLane: _ClassVar[TrackType]
    TT_CompLane: _ClassVar[TrackType]
    TType_CompLane: _ClassVar[TrackType]

class TrackFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TF_Unknown: _ClassVar[TrackFormat]
    TFormat_Unknown: _ClassVar[TrackFormat]
    TF_Mono: _ClassVar[TrackFormat]
    TFormat_Mono: _ClassVar[TrackFormat]
    TF_Stereo: _ClassVar[TrackFormat]
    TFormat_Stereo: _ClassVar[TrackFormat]
    TF_LCR: _ClassVar[TrackFormat]
    TFormat_LCR: _ClassVar[TrackFormat]
    TF_LCRS: _ClassVar[TrackFormat]
    TFormat_LCRS: _ClassVar[TrackFormat]
    TF_Quad: _ClassVar[TrackFormat]
    TFormat_Quad: _ClassVar[TrackFormat]
    TF_5_0: _ClassVar[TrackFormat]
    TFormat_5_0: _ClassVar[TrackFormat]
    TF_5_1: _ClassVar[TrackFormat]
    TFormat_5_1: _ClassVar[TrackFormat]
    TF_5_0_2: _ClassVar[TrackFormat]
    TFormat_5_0_2: _ClassVar[TrackFormat]
    TF_5_1_2: _ClassVar[TrackFormat]
    TFormat_5_1_2: _ClassVar[TrackFormat]
    TF_5_0_4: _ClassVar[TrackFormat]
    TFormat_5_0_4: _ClassVar[TrackFormat]
    TF_5_1_4: _ClassVar[TrackFormat]
    TFormat_5_1_4: _ClassVar[TrackFormat]
    TF_6_0: _ClassVar[TrackFormat]
    TFormat_6_0: _ClassVar[TrackFormat]
    TF_6_1: _ClassVar[TrackFormat]
    TFormat_6_1: _ClassVar[TrackFormat]
    TF_7_0: _ClassVar[TrackFormat]
    TFormat_7_0: _ClassVar[TrackFormat]
    TF_7_1: _ClassVar[TrackFormat]
    TFormat_7_1: _ClassVar[TrackFormat]
    TF_7_0_SDDS: _ClassVar[TrackFormat]
    TFormat_7_0_SDDS: _ClassVar[TrackFormat]
    TF_7_1_SDDS: _ClassVar[TrackFormat]
    TFormat_7_1_SDDS: _ClassVar[TrackFormat]
    TF_7_0_2: _ClassVar[TrackFormat]
    TFormat_7_0_2: _ClassVar[TrackFormat]
    TF_7_1_2: _ClassVar[TrackFormat]
    TFormat_7_1_2: _ClassVar[TrackFormat]
    TF_7_0_4: _ClassVar[TrackFormat]
    TFormat_7_0_4: _ClassVar[TrackFormat]
    TF_7_1_4: _ClassVar[TrackFormat]
    TFormat_7_1_4: _ClassVar[TrackFormat]
    TF_7_0_6: _ClassVar[TrackFormat]
    TFormat_7_0_6: _ClassVar[TrackFormat]
    TF_7_1_6: _ClassVar[TrackFormat]
    TFormat_7_1_6: _ClassVar[TrackFormat]
    TF_9_0_4: _ClassVar[TrackFormat]
    TFormat_9_0_4: _ClassVar[TrackFormat]
    TF_9_1_4: _ClassVar[TrackFormat]
    TFormat_9_1_4: _ClassVar[TrackFormat]
    TF_9_0_6: _ClassVar[TrackFormat]
    TFormat_9_0_6: _ClassVar[TrackFormat]
    TF_9_1_6: _ClassVar[TrackFormat]
    TFormat_9_1_6: _ClassVar[TrackFormat]
    TF_1stOrderAmbisonics: _ClassVar[TrackFormat]
    TFormat_1stOrderAmbisonics: _ClassVar[TrackFormat]
    TF_2ndOrderAmbisonics: _ClassVar[TrackFormat]
    TFormat_2ndOrderAmbisonics: _ClassVar[TrackFormat]
    TF_3rdOrderAmbisonics: _ClassVar[TrackFormat]
    TFormat_3rdOrderAmbisonics: _ClassVar[TrackFormat]
    TF_4thOrderAmbisonics: _ClassVar[TrackFormat]
    TFormat_4thOrderAmbisonics: _ClassVar[TrackFormat]
    TF_5thOrderAmbisonics: _ClassVar[TrackFormat]
    TFormat_5thOrderAmbisonics: _ClassVar[TrackFormat]
    TF_6thOrderAmbisonics: _ClassVar[TrackFormat]
    TFormat_6thOrderAmbisonics: _ClassVar[TrackFormat]
    TF_7thOrderAmbisonics: _ClassVar[TrackFormat]
    TFormat_7thOrderAmbisonics: _ClassVar[TrackFormat]
    TF_None: _ClassVar[TrackFormat]
    TFormat_None: _ClassVar[TrackFormat]
    TF_2_1: _ClassVar[TrackFormat]
    TFormat_2_1: _ClassVar[TrackFormat]
    TF_Overhead: _ClassVar[TrackFormat]
    TFormat_Overhead: _ClassVar[TrackFormat]

class TrackTimebase(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TTB_Unknown: _ClassVar[TrackTimebase]
    TTimebase_Unknown: _ClassVar[TrackTimebase]
    TTB_Samples: _ClassVar[TrackTimebase]
    TTimebase_Samples: _ClassVar[TrackTimebase]
    TTB_Ticks: _ClassVar[TrackTimebase]
    TTimebase_Ticks: _ClassVar[TrackTimebase]
    TTB_None: _ClassVar[TrackTimebase]
    TTimebase_None: _ClassVar[TrackTimebase]

class TrackAttributeState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TAState_Unknown: _ClassVar[TrackAttributeState]
    None: _ClassVar[TrackAttributeState]
    TAState_None: _ClassVar[TrackAttributeState]
    SetExplicitly: _ClassVar[TrackAttributeState]
    TAState_SetExplicitly: _ClassVar[TrackAttributeState]
    SetImplicitly: _ClassVar[TrackAttributeState]
    TAState_SetImplicitly: _ClassVar[TrackAttributeState]
    SetExplicitlyAndImplicitly: _ClassVar[TrackAttributeState]
    TAState_SetExplicitlyAndImplicitly: _ClassVar[TrackAttributeState]

class FileType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FType_Unknown: _ClassVar[FileType]
    FT_WAVE: _ClassVar[FileType]
    FType_WAVE: _ClassVar[FileType]
    FT_AIFF: _ClassVar[FileType]
    FType_AIFF: _ClassVar[FileType]
    FT_AAF: _ClassVar[FileType]
    FType_AAF: _ClassVar[FileType]
    FT_OMF: _ClassVar[FileType]
    FType_OMF: _ClassVar[FileType]
    FType_MXF: _ClassVar[FileType]

class IOSettings(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    IOSettings_Unknown: _ClassVar[IOSettings]
    IO_None: _ClassVar[IOSettings]
    IOSettings_None: _ClassVar[IOSettings]
    IO_Last: _ClassVar[IOSettings]
    IOSettings_Last: _ClassVar[IOSettings]
    IO_StereoMix: _ClassVar[IOSettings]
    IOSettings_StereoMix: _ClassVar[IOSettings]
    IO_51FilmMix: _ClassVar[IOSettings]
    IOSettings_51FilmMix: _ClassVar[IOSettings]
    IO_51SMPTEMix: _ClassVar[IOSettings]
    IOSettings_51SMPTEMix: _ClassVar[IOSettings]
    IO_51DTSMix: _ClassVar[IOSettings]
    IOSettings_51DTSMix: _ClassVar[IOSettings]
    IO_UserDefined: _ClassVar[IOSettings]
    IOSettings_UserDefined: _ClassVar[IOSettings]

class ImportType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    IType_Unknown: _ClassVar[ImportType]
    Session: _ClassVar[ImportType]
    IType_Session: _ClassVar[ImportType]
    Audio: _ClassVar[ImportType]
    IType_Audio: _ClassVar[ImportType]

class AudioMediaOptions(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AMOptions_Unknown: _ClassVar[AudioMediaOptions]
    LinkToSourceAudio: _ClassVar[AudioMediaOptions]
    AMOptions_LinkToSourceAudio: _ClassVar[AudioMediaOptions]
    CopyFromSourceAudio: _ClassVar[AudioMediaOptions]
    AMOptions_CopyFromSourceAudio: _ClassVar[AudioMediaOptions]
    ConsolidateFromSourceAudio: _ClassVar[AudioMediaOptions]
    AMOptions_ConsolidateFromSourceAudio: _ClassVar[AudioMediaOptions]
    ForceToTargetSessionFormat: _ClassVar[AudioMediaOptions]
    AMOptions_ForceToTargetSessionFormat: _ClassVar[AudioMediaOptions]

class VideoMediaOptions(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    VMOptions_Unknown: _ClassVar[VideoMediaOptions]
    LinkToSourceVideo: _ClassVar[VideoMediaOptions]
    VMOptions_LinkToSourceVideo: _ClassVar[VideoMediaOptions]
    CopyFromSourceVideo: _ClassVar[VideoMediaOptions]
    VMOptions_CopyFromSourceVideo: _ClassVar[VideoMediaOptions]
    ImportAsOfflineSatelliteMedia: _ClassVar[VideoMediaOptions]

class MatchTrackOptions(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MTOptions_Unknown: _ClassVar[MatchTrackOptions]
    MT_None: _ClassVar[MatchTrackOptions]
    MTOptions_None: _ClassVar[MatchTrackOptions]
    MT_MatchTracks: _ClassVar[MatchTrackOptions]
    MTOptions_MatchTracks: _ClassVar[MatchTrackOptions]
    MT_ImportAsNewTrack: _ClassVar[MatchTrackOptions]
    MTOptions_ImportAsNewTrack: _ClassVar[MatchTrackOptions]

class TimeCodeMappingOptions(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TCMOptions_Unknown: _ClassVar[TimeCodeMappingOptions]
    MaintainAbsoluteTimeCodeValues: _ClassVar[TimeCodeMappingOptions]
    TCMOptions_MaintainAbsoluteTimeCodeValues: _ClassVar[TimeCodeMappingOptions]
    MaintainRelativeTimeCodeValues: _ClassVar[TimeCodeMappingOptions]
    TCMOptions_MaintainRelativeTimeCodeValues: _ClassVar[TimeCodeMappingOptions]
    MapStartTimeCodeTo: _ClassVar[TimeCodeMappingOptions]
    TCMOptions_MapStartTimeCodeTo: _ClassVar[TimeCodeMappingOptions]

class TrackOffsetOptions(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TOOptions_Unknown: _ClassVar[TrackOffsetOptions]
    BarsBeats: _ClassVar[TrackOffsetOptions]
    TOOptions_BarsBeats: _ClassVar[TrackOffsetOptions]
    MinSecs: _ClassVar[TrackOffsetOptions]
    TOOptions_MinSecs: _ClassVar[TrackOffsetOptions]
    TimeCode: _ClassVar[TrackOffsetOptions]
    TOOptions_TimeCode: _ClassVar[TrackOffsetOptions]
    FeetFrames: _ClassVar[TrackOffsetOptions]
    TOOptions_FeetFrames: _ClassVar[TrackOffsetOptions]
    Samples: _ClassVar[TrackOffsetOptions]
    TOOptions_Samples: _ClassVar[TrackOffsetOptions]

class ConversionQuality(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CQuality_Unknown: _ClassVar[ConversionQuality]
    Low: _ClassVar[ConversionQuality]
    CQuality_Low: _ClassVar[ConversionQuality]
    Good: _ClassVar[ConversionQuality]
    CQuality_Good: _ClassVar[ConversionQuality]
    Better: _ClassVar[ConversionQuality]
    CQuality_Better: _ClassVar[ConversionQuality]
    Best: _ClassVar[ConversionQuality]
    CQuality_Best: _ClassVar[ConversionQuality]
    TweakHead: _ClassVar[ConversionQuality]
    CQuality_TweakHead: _ClassVar[ConversionQuality]

class MainPlaylistOptions(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MPOptions_Unknown: _ClassVar[MainPlaylistOptions]
    ImportReplaceExistingPlaylists: _ClassVar[MainPlaylistOptions]
    MPOptions_ImportReplaceExistingPlaylists: _ClassVar[MainPlaylistOptions]
    ImportOverlayNewOnExistingPlaylists: _ClassVar[MainPlaylistOptions]
    MPOptions_ImportOverlayNewOnExistingPlaylists: _ClassVar[MainPlaylistOptions]
    DoNotImport: _ClassVar[MainPlaylistOptions]
    MPOptions_DoNotImport: _ClassVar[MainPlaylistOptions]

class AudioOperations(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AOperations_Unknown: _ClassVar[AudioOperations]
    AddAudio: _ClassVar[AudioOperations]
    AOperations_AddAudio: _ClassVar[AudioOperations]
    CopyAudio: _ClassVar[AudioOperations]
    AOperations_CopyAudio: _ClassVar[AudioOperations]
    ConvertAudio: _ClassVar[AudioOperations]
    AOperations_ConvertAudio: _ClassVar[AudioOperations]
    Default: _ClassVar[AudioOperations]
    AOperations_Default: _ClassVar[AudioOperations]

class MediaDestination(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MDestination_Unknown: _ClassVar[MediaDestination]
    MD_None: _ClassVar[MediaDestination]
    MDestination_None: _ClassVar[MediaDestination]
    MD_MainVideoTrack: _ClassVar[MediaDestination]
    MDestination_MainVideoTrack: _ClassVar[MediaDestination]
    MD_NewTrack: _ClassVar[MediaDestination]
    MDestination_NewTrack: _ClassVar[MediaDestination]
    MD_ClipList: _ClassVar[MediaDestination]
    MDestination_ClipList: _ClassVar[MediaDestination]

class MediaLocation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MLocation_Unknown: _ClassVar[MediaLocation]
    ML_None: _ClassVar[MediaLocation]
    MLocation_None: _ClassVar[MediaLocation]
    ML_SessionStart: _ClassVar[MediaLocation]
    MLocation_SessionStart: _ClassVar[MediaLocation]
    ML_SongStart: _ClassVar[MediaLocation]
    MLocation_SongStart: _ClassVar[MediaLocation]
    ML_Selection: _ClassVar[MediaLocation]
    MLocation_Selection: _ClassVar[MediaLocation]
    ML_Spot: _ClassVar[MediaLocation]
    MLocation_Spot: _ClassVar[MediaLocation]

class TrackListFilter(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TLFilter_Unknown: _ClassVar[TrackListFilter]
    All: _ClassVar[TrackListFilter]
    TLFilter_All: _ClassVar[TrackListFilter]
    Selected: _ClassVar[TrackListFilter]
    TLFilter_Selected: _ClassVar[TrackListFilter]
    SelectedExplicitly: _ClassVar[TrackListFilter]
    TLFilter_SelectedExplicitly: _ClassVar[TrackListFilter]
    SelectedImplicitly: _ClassVar[TrackListFilter]
    TLFilter_SelectedImplicitly: _ClassVar[TrackListFilter]
    WithClipsOnMainPlaylist: _ClassVar[TrackListFilter]
    TLFilter_WithClipsOnMainPlaylist: _ClassVar[TrackListFilter]
    WithAutomationOnMainPlaylist: _ClassVar[TrackListFilter]
    TLFilter_WithAutomationOnMainPlaylist: _ClassVar[TrackListFilter]
    Inactive: _ClassVar[TrackListFilter]
    TLFilter_Inactive: _ClassVar[TrackListFilter]
    InactiveExplicitly: _ClassVar[TrackListFilter]
    TLFilter_InactiveExplicitly: _ClassVar[TrackListFilter]
    InactiveImplicitly: _ClassVar[TrackListFilter]
    TLFilter_InactiveImplicitly: _ClassVar[TrackListFilter]
    Hidden: _ClassVar[TrackListFilter]
    TLFilter_Hidden: _ClassVar[TrackListFilter]
    HiddenExplicitly: _ClassVar[TrackListFilter]
    TLFilter_HiddenExplicitly: _ClassVar[TrackListFilter]
    HiddenImplicitly: _ClassVar[TrackListFilter]
    TLFilter_HiddenImplicitly: _ClassVar[TrackListFilter]
    Locked: _ClassVar[TrackListFilter]
    TLFilter_Locked: _ClassVar[TrackListFilter]
    Muted: _ClassVar[TrackListFilter]
    TLFilter_Muted: _ClassVar[TrackListFilter]
    Frozen: _ClassVar[TrackListFilter]
    TLFilter_Frozen: _ClassVar[TrackListFilter]
    Open: _ClassVar[TrackListFilter]
    TLFilter_Open: _ClassVar[TrackListFilter]
    Online: _ClassVar[TrackListFilter]
    TLFilter_Online: _ClassVar[TrackListFilter]
    TLFilter_HasEditSelection: _ClassVar[TrackListFilter]
    TLFilter_HasEditSelectionExplicitly: _ClassVar[TrackListFilter]
    TLFilter_HasEditSelectionImplicitly: _ClassVar[TrackListFilter]

class SpotLocationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SLType_Unknown: _ClassVar[SpotLocationType]
    Start: _ClassVar[SpotLocationType]
    SLType_Start: _ClassVar[SpotLocationType]
    SyncPoint: _ClassVar[SpotLocationType]
    SLType_SyncPoint: _ClassVar[SpotLocationType]
    End: _ClassVar[SpotLocationType]
    SLType_End: _ClassVar[SpotLocationType]

class ExportFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EFormat_Unknown: _ClassVar[ExportFormat]
    EF_None: _ClassVar[ExportFormat]
    EFormat_None: _ClassVar[ExportFormat]
    EF_Mono: _ClassVar[ExportFormat]
    EFormat_Mono: _ClassVar[ExportFormat]
    EF_MultipleMono: _ClassVar[ExportFormat]
    EFormat_MultipleMono: _ClassVar[ExportFormat]
    EF_Interleaved: _ClassVar[ExportFormat]
    EFormat_Interleaved: _ClassVar[ExportFormat]

class ExportFileType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EFType_Unknown: _ClassVar[ExportFileType]
    WAV: _ClassVar[ExportFileType]
    EFType_WAV: _ClassVar[ExportFileType]
    AIFF: _ClassVar[ExportFileType]
    EFType_AIFF: _ClassVar[ExportFileType]
    MXF: _ClassVar[ExportFileType]
    EFType_MXF: _ClassVar[ExportFileType]
    MP3: _ClassVar[ExportFileType]
    EFType_MP3: _ClassVar[ExportFileType]
    QuickTime: _ClassVar[ExportFileType]
    EFType_QuickTime: _ClassVar[ExportFileType]

class BitDepth(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BDepth_Unknown: _ClassVar[BitDepth]
    Bit_None: _ClassVar[BitDepth]
    BDepth_None: _ClassVar[BitDepth]
    Bit16: _ClassVar[BitDepth]
    BDepth_16: _ClassVar[BitDepth]
    Bit24: _ClassVar[BitDepth]
    BDepth_24: _ClassVar[BitDepth]
    Bit32Float: _ClassVar[BitDepth]
    BDepth_32Float: _ClassVar[BitDepth]

class ResolveDuplicateNamesBy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RDNBy_Unknown: _ClassVar[ResolveDuplicateNamesBy]
    AutoRenaming: _ClassVar[ResolveDuplicateNamesBy]
    RDNBy_AutoRenaming: _ClassVar[ResolveDuplicateNamesBy]
    ReplacingWithNewFiles: _ClassVar[ResolveDuplicateNamesBy]
    RDNBy_ReplacingWithNewFiles: _ClassVar[ResolveDuplicateNamesBy]

class ExportAsAAFFileType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EAAFFType_Unknown: _ClassVar[ExportAsAAFFileType]
    EAAFFType_None: _ClassVar[ExportAsAAFFileType]
    AAF_WAV: _ClassVar[ExportAsAAFFileType]
    EAAFFType_WAV: _ClassVar[ExportAsAAFFileType]
    AAF_AIFF: _ClassVar[ExportAsAAFFileType]
    EAAFFType_AIFF: _ClassVar[ExportAsAAFFileType]
    AAF_MXF: _ClassVar[ExportAsAAFFileType]
    EAAFFType_MXF: _ClassVar[ExportAsAAFFileType]
    AAF_Embedded: _ClassVar[ExportAsAAFFileType]
    EAAFFType_Embedded: _ClassVar[ExportAsAAFFileType]

class AAFFileBitDepth(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AAFFBDepth_Unknown: _ClassVar[AAFFileBitDepth]
    AAFFBDepth_None: _ClassVar[AAFFileBitDepth]
    AAF_Bit16: _ClassVar[AAFFileBitDepth]
    AAFFBDepth_Bit16: _ClassVar[AAFFileBitDepth]
    AAF_Bit24: _ClassVar[AAFFileBitDepth]
    AAFFBDepth_Bit24: _ClassVar[AAFFileBitDepth]

class CopyOption(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    COption_Unknown: _ClassVar[CopyOption]
    ConsolidateFromSourceMedia: _ClassVar[CopyOption]
    COption_ConsolidateFromSourceMedia: _ClassVar[CopyOption]
    CopyFromSourceMedia: _ClassVar[CopyOption]
    COption_CopyFromSourceMedia: _ClassVar[CopyOption]
    LinkFromSourceMedia: _ClassVar[CopyOption]
    COption_LinkFromSourceMedia: _ClassVar[CopyOption]

class FileLocationTypeFilter(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FLTFilter_Unknown: _ClassVar[FileLocationTypeFilter]
    All_Files: _ClassVar[FileLocationTypeFilter]
    FLTFilter_AllFiles: _ClassVar[FileLocationTypeFilter]
    OnTimeline_Files: _ClassVar[FileLocationTypeFilter]
    FLTFilter_OnTimelineFiles: _ClassVar[FileLocationTypeFilter]
    NotOnTimeline_Files: _ClassVar[FileLocationTypeFilter]
    FLTFilter_NotOnTimelineFiles: _ClassVar[FileLocationTypeFilter]
    Online_Files: _ClassVar[FileLocationTypeFilter]
    FLTFilter_OnlineFiles: _ClassVar[FileLocationTypeFilter]
    Offline_Files: _ClassVar[FileLocationTypeFilter]
    FLTFilter_OfflineFiles: _ClassVar[FileLocationTypeFilter]
    Audio_Files: _ClassVar[FileLocationTypeFilter]
    FLTFilter_AudioFiles: _ClassVar[FileLocationTypeFilter]
    Video_Files: _ClassVar[FileLocationTypeFilter]
    FLTFilter_VideoFiles: _ClassVar[FileLocationTypeFilter]
    Rendered_Files: _ClassVar[FileLocationTypeFilter]
    FLTFilter_RenderedFiles: _ClassVar[FileLocationTypeFilter]
    SelectedClipsTimeline: _ClassVar[FileLocationTypeFilter]
    FLTFilter_SelectedClipsTimeline: _ClassVar[FileLocationTypeFilter]
    SelectedClipsClipsList: _ClassVar[FileLocationTypeFilter]
    FLTFilter_SelectedClipsClipsList: _ClassVar[FileLocationTypeFilter]

class AutomationDataOptions(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ADOptions_Unknown: _ClassVar[AutomationDataOptions]
    All_Automation: _ClassVar[AutomationDataOptions]
    ADOptions_AllAutomation: _ClassVar[AutomationDataOptions]
    Pan_Automation: _ClassVar[AutomationDataOptions]
    ADOptions_PanAutomation: _ClassVar[AutomationDataOptions]
    PlugIn_Automation: _ClassVar[AutomationDataOptions]
    ADOptions_PlugInAutomation: _ClassVar[AutomationDataOptions]
    Clip_Gain: _ClassVar[AutomationDataOptions]
    ADOptions_ClipGain: _ClassVar[AutomationDataOptions]
    Clip_Effects: _ClassVar[AutomationDataOptions]
    ADOptions_ClipEffects: _ClassVar[AutomationDataOptions]

class PasteSpecialOptions(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PSOptions_Unknown: _ClassVar[PasteSpecialOptions]
    Merge: _ClassVar[PasteSpecialOptions]
    MergeMidi: _ClassVar[PasteSpecialOptions]
    PSOptions_MergeMidi: _ClassVar[PasteSpecialOptions]
    Repeat_To_Fill_Selection: _ClassVar[PasteSpecialOptions]
    PSOptions_RepeatToFillSelection: _ClassVar[PasteSpecialOptions]
    To_Current_Automation_Type: _ClassVar[PasteSpecialOptions]
    PSOptions_ToCurrentAutomationType: _ClassVar[PasteSpecialOptions]
    MergeMarkers: _ClassVar[PasteSpecialOptions]
    PSOptions_MergeMarkers: _ClassVar[PasteSpecialOptions]

class TripleBool(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TBool_Unknown: _ClassVar[TripleBool]
    TB_None: _ClassVar[TripleBool]
    TBool_None: _ClassVar[TripleBool]
    TB_False: _ClassVar[TripleBool]
    TBool_False: _ClassVar[TripleBool]
    TB_True: _ClassVar[TripleBool]
    TBool_True: _ClassVar[TripleBool]

class EM_SourceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EMSType_Unknown: _ClassVar[EM_SourceType]
    PhysicalOut: _ClassVar[EM_SourceType]
    EMSType_PhysicalOut: _ClassVar[EM_SourceType]
    Bus: _ClassVar[EM_SourceType]
    EMSType_Bus: _ClassVar[EM_SourceType]
    Output: _ClassVar[EM_SourceType]
    EMSType_Output: _ClassVar[EM_SourceType]

class CompressionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CType_Unknown: _ClassVar[CompressionType]
    CT_None: _ClassVar[CompressionType]
    CType_None: _ClassVar[CompressionType]
    CT_PCM: _ClassVar[CompressionType]
    CType_PCM: _ClassVar[CompressionType]

class SampleRate(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SRate_Unknown: _ClassVar[SampleRate]
    SR_None: _ClassVar[SampleRate]
    SRate_None: _ClassVar[SampleRate]
    SR_44100: _ClassVar[SampleRate]
    SRate_44100: _ClassVar[SampleRate]
    SR_48000: _ClassVar[SampleRate]
    SRate_48000: _ClassVar[SampleRate]
    SR_88200: _ClassVar[SampleRate]
    SRate_88200: _ClassVar[SampleRate]
    SR_96000: _ClassVar[SampleRate]
    SRate_96000: _ClassVar[SampleRate]
    SR_176400: _ClassVar[SampleRate]
    SRate_176400: _ClassVar[SampleRate]
    SR_192000: _ClassVar[SampleRate]
    SRate_192000: _ClassVar[SampleRate]

class EM_VideoExportOptions(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EMVEOptions_Unknown: _ClassVar[EM_VideoExportOptions]
    VE_None: _ClassVar[EM_VideoExportOptions]
    EMVEOptions_None: _ClassVar[EM_VideoExportOptions]
    VE_SameAsSource: _ClassVar[EM_VideoExportOptions]
    EMVEOptions_SameAsSource: _ClassVar[EM_VideoExportOptions]
    VE_Transcode: _ClassVar[EM_VideoExportOptions]
    EMVEOptions_Transcode: _ClassVar[EM_VideoExportOptions]

class EM_FileType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EMFType_Unknown: _ClassVar[EM_FileType]
    EM_None: _ClassVar[EM_FileType]
    EMFType_None: _ClassVar[EM_FileType]
    EM_MOV: _ClassVar[EM_FileType]
    EMFType_MOV: _ClassVar[EM_FileType]
    EM_WAV: _ClassVar[EM_FileType]
    EMFType_WAV: _ClassVar[EM_FileType]
    EM_AIFF: _ClassVar[EM_FileType]
    EMFType_AIFF: _ClassVar[EM_FileType]
    EM_MP3: _ClassVar[EM_FileType]
    EMFType_MP3: _ClassVar[EM_FileType]
    EM_MXFOPAtom: _ClassVar[EM_FileType]
    EMFType_MXFOPAtom: _ClassVar[EM_FileType]
    EM_WAVADM: _ClassVar[EM_FileType]
    EMFType_WAVADM: _ClassVar[EM_FileType]
    EMFType_M4A: _ClassVar[EM_FileType]

class EM_FileDestination(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EMFDestination_Unknown: _ClassVar[EM_FileDestination]
    EM_FD_None: _ClassVar[EM_FileDestination]
    EMFDestination_None: _ClassVar[EM_FileDestination]
    EM_FD_SessionFolder: _ClassVar[EM_FileDestination]
    EMFDestination_SessionFolder: _ClassVar[EM_FileDestination]
    EM_FD_Directory: _ClassVar[EM_FileDestination]
    EMFDestination_Directory: _ClassVar[EM_FileDestination]

class EM_DeliveryFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EMDFormat_Unknown: _ClassVar[EM_DeliveryFormat]
    EM_DF_None: _ClassVar[EM_DeliveryFormat]
    EMDFormat_None: _ClassVar[EM_DeliveryFormat]
    EM_DF_FilePerMixSource: _ClassVar[EM_DeliveryFormat]
    EMDFormat_FilePerMixSource: _ClassVar[EM_DeliveryFormat]
    EM_DF_SingleFile: _ClassVar[EM_DeliveryFormat]
    EMDFormat_SingleFile: _ClassVar[EM_DeliveryFormat]

class MP3EncodingOptionsConstantBitRate(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MP3EOCBRate_Unknown: _ClassVar[MP3EncodingOptionsConstantBitRate]
    MP3EOCBRate_320kbps: _ClassVar[MP3EncodingOptionsConstantBitRate]
    MP3EOCBRate_256kbps: _ClassVar[MP3EncodingOptionsConstantBitRate]
    MP3EOCBRate_224kbps: _ClassVar[MP3EncodingOptionsConstantBitRate]
    MP3EOCBRate_192kbps: _ClassVar[MP3EncodingOptionsConstantBitRate]
    MP3EOCBRate_160kbps: _ClassVar[MP3EncodingOptionsConstantBitRate]
    MP3EOCBRate_128kbps: _ClassVar[MP3EncodingOptionsConstantBitRate]
    MP3EOCBRate_112kbps: _ClassVar[MP3EncodingOptionsConstantBitRate]
    MP3EOCBRate_96kbps: _ClassVar[MP3EncodingOptionsConstantBitRate]
    MP3EOCBRate_80kbps: _ClassVar[MP3EncodingOptionsConstantBitRate]
    MP3EOCBRate_64kbps: _ClassVar[MP3EncodingOptionsConstantBitRate]
    MP3EOCBRate_56kbps: _ClassVar[MP3EncodingOptionsConstantBitRate]
    MP3EOCBRate_48kbps: _ClassVar[MP3EncodingOptionsConstantBitRate]
    MP3EOCBRate_40kbps: _ClassVar[MP3EncodingOptionsConstantBitRate]
    MP3EOCBRate_32kbps: _ClassVar[MP3EncodingOptionsConstantBitRate]
    MP3EOCBRate_24kbps: _ClassVar[MP3EncodingOptionsConstantBitRate]
    MP3EOCBRate_20kbps: _ClassVar[MP3EncodingOptionsConstantBitRate]
    MP3EOCBRate_18kbps: _ClassVar[MP3EncodingOptionsConstantBitRate]
    MP3EOCBRate_16kbps: _ClassVar[MP3EncodingOptionsConstantBitRate]

class MP3EncodingOptionsQuality(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MP3EOQuality_Unknown: _ClassVar[MP3EncodingOptionsQuality]
    MP3EOQuality_Low: _ClassVar[MP3EncodingOptionsQuality]
    MP3EOQuality_Highest: _ClassVar[MP3EncodingOptionsQuality]

class DP_ValueTypes(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DPVTypes_Unknown: _ClassVar[DP_ValueTypes]
    DP_VT_double: _ClassVar[DP_ValueTypes]
    DPVTypes_Double: _ClassVar[DP_ValueTypes]
    DP_VT_float: _ClassVar[DP_ValueTypes]
    DPVTypes_Float: _ClassVar[DP_ValueTypes]
    DP_VT_int32: _ClassVar[DP_ValueTypes]
    DPVTypes_Int32: _ClassVar[DP_ValueTypes]
    DP_VT_int64: _ClassVar[DP_ValueTypes]
    DPVTypes_Int64: _ClassVar[DP_ValueTypes]
    DP_VT_uint32: _ClassVar[DP_ValueTypes]
    DPVTypes_Uint32: _ClassVar[DP_ValueTypes]
    DP_VT_uint64: _ClassVar[DP_ValueTypes]
    DPVTypes_Uint64: _ClassVar[DP_ValueTypes]
    DP_VT_sint32: _ClassVar[DP_ValueTypes]
    DPVTypes_Sint32: _ClassVar[DP_ValueTypes]
    DP_VT_sint64: _ClassVar[DP_ValueTypes]
    DPVTypes_Sint64: _ClassVar[DP_ValueTypes]
    DP_VT_fixed32: _ClassVar[DP_ValueTypes]
    DPVTypes_Fixed32: _ClassVar[DP_ValueTypes]
    DP_VT_fixed64: _ClassVar[DP_ValueTypes]
    DPVTypes_Fixed64: _ClassVar[DP_ValueTypes]
    DP_VT_sfixed32: _ClassVar[DP_ValueTypes]
    DPVTypes_Sfixed32: _ClassVar[DP_ValueTypes]
    DP_VT_sfixed64: _ClassVar[DP_ValueTypes]
    DPVTypes_Sfixed64: _ClassVar[DP_ValueTypes]
    DP_VT_bool: _ClassVar[DP_ValueTypes]
    DPVTypes_Bool: _ClassVar[DP_ValueTypes]
    DP_VT_string: _ClassVar[DP_ValueTypes]
    DPVTypes_String: _ClassVar[DP_ValueTypes]
    DP_VT_bytes: _ClassVar[DP_ValueTypes]
    DPVTypes_Bytes: _ClassVar[DP_ValueTypes]
    DP_VT_enum: _ClassVar[DP_ValueTypes]
    DPVTypes_Enum: _ClassVar[DP_ValueTypes]
    DP_VT_object: _ClassVar[DP_ValueTypes]
    DPVTypes_Object: _ClassVar[DP_ValueTypes]

class DynamicPropertyType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DPType_Unknown: _ClassVar[DynamicPropertyType]
    DP_EM_CodecInfo: _ClassVar[DynamicPropertyType]
    DPType_CodecInfo: _ClassVar[DynamicPropertyType]
    DP_EM_DolbyAtmosInfo: _ClassVar[DynamicPropertyType]
    DPType_DolbyAtmosInfo: _ClassVar[DynamicPropertyType]

class TrackListType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TListType_Unknown: _ClassVar[TrackListType]
    AllTracks: _ClassVar[TrackListType]
    TListType_AllTracks: _ClassVar[TrackListType]
    SelectedTracksOnly: _ClassVar[TrackListType]
    TListType_SelectedTracksOnly: _ClassVar[TrackListType]

class FadeHandlingType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FHType_Unknown: _ClassVar[FadeHandlingType]
    ShowCrossfades: _ClassVar[FadeHandlingType]
    FHType_ShowCrossfades: _ClassVar[FadeHandlingType]
    DontShowCrossfades: _ClassVar[FadeHandlingType]
    FHType_DontShowCrossfades: _ClassVar[FadeHandlingType]
    CombineCrossfadedClips: _ClassVar[FadeHandlingType]
    FHType_CombineCrossfadedClips: _ClassVar[FadeHandlingType]

class TextAsFileFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TFFormat_Unknown: _ClassVar[TextAsFileFormat]
    TextEdit: _ClassVar[TextAsFileFormat]
    TFFormat_TextEdit: _ClassVar[TextAsFileFormat]
    UTF8: _ClassVar[TextAsFileFormat]
    TFFormat_UTF8: _ClassVar[TextAsFileFormat]

class ESI_OutputType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ESI_Unknown: _ClassVar[ESI_OutputType]
    ESIOType_Unknown: _ClassVar[ESI_OutputType]
    ESI_File: _ClassVar[ESI_OutputType]
    ESIOType_File: _ClassVar[ESI_OutputType]
    ESI_String: _ClassVar[ESI_OutputType]
    ESIOType_String: _ClassVar[ESI_OutputType]

class PlaybackMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PMode_Unknown: _ClassVar[PlaybackMode]
    PM_Normal: _ClassVar[PlaybackMode]
    PMode_Normal: _ClassVar[PlaybackMode]
    PM_Loop: _ClassVar[PlaybackMode]
    PMode_Loop: _ClassVar[PlaybackMode]
    PM_DynamicTransport: _ClassVar[PlaybackMode]
    PMode_DynamicTransport: _ClassVar[PlaybackMode]

class RecordMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RMode_Unknown: _ClassVar[RecordMode]
    RM_Normal: _ClassVar[RecordMode]
    RMode_Normal: _ClassVar[RecordMode]
    RM_Loop: _ClassVar[RecordMode]
    RMode_Loop: _ClassVar[RecordMode]
    RM_Destructive: _ClassVar[RecordMode]
    RMode_Destructive: _ClassVar[RecordMode]
    RM_QuickPunch: _ClassVar[RecordMode]
    RMode_QuickPunch: _ClassVar[RecordMode]
    RM_TrackPunch: _ClassVar[RecordMode]
    RMode_TrackPunch: _ClassVar[RecordMode]
    RM_DestructivePunch: _ClassVar[RecordMode]
    RMode_DestructivePunch: _ClassVar[RecordMode]

class SessionAudioFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SAFormat_Unknown: _ClassVar[SessionAudioFormat]
    SAF_WAVE: _ClassVar[SessionAudioFormat]
    SAFormat_WAVE: _ClassVar[SessionAudioFormat]
    SAF_AIFF: _ClassVar[SessionAudioFormat]
    SAFormat_AIFF: _ClassVar[SessionAudioFormat]

class SessionTimeCodeRate(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    STCRate_Unknown: _ClassVar[SessionTimeCodeRate]
    STCR_Fps23976: _ClassVar[SessionTimeCodeRate]
    STCRate_Fps23976: _ClassVar[SessionTimeCodeRate]
    STCR_Fps24: _ClassVar[SessionTimeCodeRate]
    STCRate_Fps24: _ClassVar[SessionTimeCodeRate]
    STCR_Fps25: _ClassVar[SessionTimeCodeRate]
    STCRate_Fps25: _ClassVar[SessionTimeCodeRate]
    STCR_Fps2997: _ClassVar[SessionTimeCodeRate]
    STCRate_Fps2997: _ClassVar[SessionTimeCodeRate]
    STCR_Fps2997Drop: _ClassVar[SessionTimeCodeRate]
    SSTCRate_Fps2997Drop: _ClassVar[SessionTimeCodeRate]
    STCR_Fps30: _ClassVar[SessionTimeCodeRate]
    STCRate_Fps30: _ClassVar[SessionTimeCodeRate]
    STCR_Fps30Drop: _ClassVar[SessionTimeCodeRate]
    STCRate_Fps30Drop: _ClassVar[SessionTimeCodeRate]
    STCR_Fps47952: _ClassVar[SessionTimeCodeRate]
    STCRate_Fps47952: _ClassVar[SessionTimeCodeRate]
    STCR_Fps48: _ClassVar[SessionTimeCodeRate]
    STCRate_Fps48: _ClassVar[SessionTimeCodeRate]
    STCR_Fps50: _ClassVar[SessionTimeCodeRate]
    STCRate_Fps50: _ClassVar[SessionTimeCodeRate]
    STCR_Fps5994: _ClassVar[SessionTimeCodeRate]
    STCRate_Fps5994: _ClassVar[SessionTimeCodeRate]
    STCR_Fps5994Drop: _ClassVar[SessionTimeCodeRate]
    STCRate_Fps5994Drop: _ClassVar[SessionTimeCodeRate]
    STCR_Fps60: _ClassVar[SessionTimeCodeRate]
    STCRate_Fps60: _ClassVar[SessionTimeCodeRate]
    STCR_Fps60Drop: _ClassVar[SessionTimeCodeRate]
    STCRate_Fps60Drop: _ClassVar[SessionTimeCodeRate]
    STCR_Fps100: _ClassVar[SessionTimeCodeRate]
    STCRate_Fps100: _ClassVar[SessionTimeCodeRate]
    STCR_Fps11988: _ClassVar[SessionTimeCodeRate]
    STCRate_Fps11988: _ClassVar[SessionTimeCodeRate]
    STCR_Fps11988Drop: _ClassVar[SessionTimeCodeRate]
    STCRate_Fps11988Drop: _ClassVar[SessionTimeCodeRate]
    STCR_Fps120: _ClassVar[SessionTimeCodeRate]
    STCRate_Fps120: _ClassVar[SessionTimeCodeRate]
    STCR_Fps120Drop: _ClassVar[SessionTimeCodeRate]
    STCRate_Fps120Drop: _ClassVar[SessionTimeCodeRate]

class SessionFeetFramesRate(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SFFRate_Unknown: _ClassVar[SessionFeetFramesRate]
    SFFR_Fps23976: _ClassVar[SessionFeetFramesRate]
    SFFRate_Fps23976: _ClassVar[SessionFeetFramesRate]
    SFFR_Fps24: _ClassVar[SessionFeetFramesRate]
    SFFRate_Fps24: _ClassVar[SessionFeetFramesRate]
    SFFR_Fps25: _ClassVar[SessionFeetFramesRate]
    SFFRate_Fps25: _ClassVar[SessionFeetFramesRate]

class SessionRatePull(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SRPull_Unknown: _ClassVar[SessionRatePull]
    SRP_None: _ClassVar[SessionRatePull]
    SRPull_None: _ClassVar[SessionRatePull]
    SRP_Up01: _ClassVar[SessionRatePull]
    SRPull_Up01: _ClassVar[SessionRatePull]
    SRP_Down01: _ClassVar[SessionRatePull]
    SRPull_Down01: _ClassVar[SessionRatePull]
    SRP_Up4: _ClassVar[SessionRatePull]
    SRPull_Up4: _ClassVar[SessionRatePull]
    SRP_Up4Up01: _ClassVar[SessionRatePull]
    SRPull_Up4Up01: _ClassVar[SessionRatePull]
    SRP_Up4Down01: _ClassVar[SessionRatePull]
    SRPull_Up4Down01: _ClassVar[SessionRatePull]
    SRP_Down4: _ClassVar[SessionRatePull]
    SRPull_Down4: _ClassVar[SessionRatePull]
    SRP_Down4Up01: _ClassVar[SessionRatePull]
    SRPull_Down4Up01: _ClassVar[SessionRatePull]
    SRP_Down4Down01: _ClassVar[SessionRatePull]
    SRPull_Down4Down01: _ClassVar[SessionRatePull]

class TransportState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TState_Unknown: _ClassVar[TransportState]
    TS_TransportPlaying: _ClassVar[TransportState]
    TState_TransportPlaying: _ClassVar[TransportState]
    TS_TransportStopped: _ClassVar[TransportState]
    TState_TransportStopped: _ClassVar[TransportState]
    TS_TransportRecording: _ClassVar[TransportState]
    TState_TransportRecording: _ClassVar[TransportState]
    TS_TransportPlayingHalfSpeed: _ClassVar[TransportState]
    TState_TransportPlayingHalfSpeed: _ClassVar[TransportState]
    TS_TransportRecordingHalfSpeed: _ClassVar[TransportState]
    TState_TransportRecordingHalfSpeed: _ClassVar[TransportState]
    TS_TransportFastForward: _ClassVar[TransportState]
    TState_TransportFastForward: _ClassVar[TransportState]
    TS_TransportRewind: _ClassVar[TransportState]
    TState_TransportRewind: _ClassVar[TransportState]
    TS_TransportScrub: _ClassVar[TransportState]
    TState_TransportScrub: _ClassVar[TransportState]
    TS_TransportShuttle: _ClassVar[TransportState]
    TState_TransportShuttle: _ClassVar[TransportState]
    TS_TransportPrimed: _ClassVar[TransportState]
    TState_TransportPrimed: _ClassVar[TransportState]
    TS_TransportIsCueing: _ClassVar[TransportState]
    TState_TransportIsCueing: _ClassVar[TransportState]
    TS_TransportIsCued: _ClassVar[TransportState]
    TState_TransportIsCued: _ClassVar[TransportState]
    TS_TransportIsCuedForPreview: _ClassVar[TransportState]
    TState_TransportIsCuedForPreview: _ClassVar[TransportState]
    TS_TransportIsStopping: _ClassVar[TransportState]
    TState_TransportIsStopping: _ClassVar[TransportState]
    TS_TransportIsPreviewing: _ClassVar[TransportState]
    TState_TransportIsPreviewing: _ClassVar[TransportState]

class ClipLocation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CLocation_Unknown: _ClassVar[ClipLocation]
    CL_ClipsList: _ClassVar[ClipLocation]
    CLocation_ClipsList: _ClassVar[ClipLocation]
    CL_Timeline: _ClassVar[ClipLocation]
    CLocation_Timeline: _ClassVar[ClipLocation]

class TimeProperties(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TProperties_Unknown: _ClassVar[TimeProperties]
    TP_Marker: _ClassVar[TimeProperties]
    TProperties_Marker: _ClassVar[TimeProperties]
    TP_Selection: _ClassVar[TimeProperties]
    TProperties_Selection: _ClassVar[TimeProperties]
    TP_None: _ClassVar[TimeProperties]
    TProperties_None: _ClassVar[TimeProperties]

class MemoryLocationReference(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MLReference_Unknown: _ClassVar[MemoryLocationReference]
    MLR_BarBeat: _ClassVar[MemoryLocationReference]
    MLReference_BarBeat: _ClassVar[MemoryLocationReference]
    MLR_Absolute: _ClassVar[MemoryLocationReference]
    MLReference_Absolute: _ClassVar[MemoryLocationReference]
    MLR_FollowTrackTimebase: _ClassVar[MemoryLocationReference]
    MLReference_FollowTrackTimebase: _ClassVar[MemoryLocationReference]

class MarkerLocation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MLC_Unknown: _ClassVar[MarkerLocation]
    MarkerLocation_Unknown: _ClassVar[MarkerLocation]
    MLC_MainRuler: _ClassVar[MarkerLocation]
    MarkerLocation_MainRuler: _ClassVar[MarkerLocation]
    MLC_Track: _ClassVar[MarkerLocation]
    MarkerLocation_Track: _ClassVar[MarkerLocation]
    MarkerLocation_NamedRuler: _ClassVar[MarkerLocation]

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
    EMode_Unknown: _ClassVar[EditMode]
    EMO_Shuffle: _ClassVar[EditMode]
    EMode_Shuffle: _ClassVar[EditMode]
    EMO_Slip: _ClassVar[EditMode]
    EMode_Slip: _ClassVar[EditMode]
    EMO_Spot: _ClassVar[EditMode]
    EMode_Spot: _ClassVar[EditMode]
    EMO_GridAbsolute: _ClassVar[EditMode]
    EMode_GridAbsolute: _ClassVar[EditMode]
    EMO_GridRelative: _ClassVar[EditMode]
    EMode_GridRelative: _ClassVar[EditMode]
    EMO_ShuffleSnapToGridAbsolute: _ClassVar[EditMode]
    EMode_ShuffleSnapToGridAbsolute: _ClassVar[EditMode]
    EMO_SlipSnapToGridAbsolute: _ClassVar[EditMode]
    EMode_SlipSnapToGridAbsolute: _ClassVar[EditMode]
    EMO_SpotSnapToGridAbsolute: _ClassVar[EditMode]
    EMode_SpotSnapToGridAbsolute: _ClassVar[EditMode]
    EMO_ShuffleSnapToGridRelative: _ClassVar[EditMode]
    EMode_ShuffleSnapToGridRelative: _ClassVar[EditMode]
    EMO_SlipSnapToGridRelative: _ClassVar[EditMode]
    EMode_SlipSnapToGridRelative: _ClassVar[EditMode]
    EMO_SpotSnapToGridRelative: _ClassVar[EditMode]
    EMode_SpotSnapToGridRelative: _ClassVar[EditMode]

class EditTool(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ET_Unknown: _ClassVar[EditTool]
    ETool_Unknown: _ClassVar[EditTool]
    ET_ZoomNormal: _ClassVar[EditTool]
    ETool_ZoomNormal: _ClassVar[EditTool]
    ET_ZoomSingle: _ClassVar[EditTool]
    ETool_ZoomSingle: _ClassVar[EditTool]
    ET_TrimStandard: _ClassVar[EditTool]
    ETool_TrimStandard: _ClassVar[EditTool]
    ET_TrimTce: _ClassVar[EditTool]
    ETool_TrimTce: _ClassVar[EditTool]
    ET_TrimScrub: _ClassVar[EditTool]
    ETool_TrimScrub: _ClassVar[EditTool]
    ET_TrimLoop: _ClassVar[EditTool]
    ETool_TrimLoop: _ClassVar[EditTool]
    ET_Selector: _ClassVar[EditTool]
    ETool_Selector: _ClassVar[EditTool]
    ET_GrabberTime: _ClassVar[EditTool]
    ETool_GrabberTime: _ClassVar[EditTool]
    ET_GrabberSeparation: _ClassVar[EditTool]
    ETool_GrabberSeparation: _ClassVar[EditTool]
    ET_GrabberObject: _ClassVar[EditTool]
    ETool_GrabberObject: _ClassVar[EditTool]
    ET_SmartTool: _ClassVar[EditTool]
    ETool_SmartTool: _ClassVar[EditTool]
    ET_Scrubber: _ClassVar[EditTool]
    ETool_Scrubber: _ClassVar[EditTool]
    ET_PencilFreeHand: _ClassVar[EditTool]
    ETool_PencilFreeHand: _ClassVar[EditTool]
    ET_PencilLine: _ClassVar[EditTool]
    ETool_PencilLine: _ClassVar[EditTool]
    ET_PencilTriangle: _ClassVar[EditTool]
    ETool_PencilTriangle: _ClassVar[EditTool]
    ET_PencilSquare: _ClassVar[EditTool]
    ETool_PencilSquare: _ClassVar[EditTool]
    ET_PencilRandom: _ClassVar[EditTool]
    ETool_PencilRandom: _ClassVar[EditTool]
    ET_PencilParabolic: _ClassVar[EditTool]
    ETool_PencilParabolic: _ClassVar[EditTool]
    ET_PencilSCurve: _ClassVar[EditTool]
    ETool_PencilSCurve: _ClassVar[EditTool]

class TimelineUpdateVideo(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TUV_Unknown: _ClassVar[TimelineUpdateVideo]
    TUVideo_Unknown: _ClassVar[TimelineUpdateVideo]
    TUV_None: _ClassVar[TimelineUpdateVideo]
    TUVideo_None: _ClassVar[TimelineUpdateVideo]
    TUV_In: _ClassVar[TimelineUpdateVideo]
    TUVideo_In: _ClassVar[TimelineUpdateVideo]
    TUV_Out: _ClassVar[TimelineUpdateVideo]
    TUVideo_Out: _ClassVar[TimelineUpdateVideo]

class SelectionMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SM_Unknown: _ClassVar[SelectionMode]
    SMode_Unknown: _ClassVar[SelectionMode]
    SM_Replace: _ClassVar[SelectionMode]
    SMode_Replace: _ClassVar[SelectionMode]
    SM_Add: _ClassVar[SelectionMode]
    SMode_Add: _ClassVar[SelectionMode]
    SM_Subtract: _ClassVar[SelectionMode]
    SMode_Subtract: _ClassVar[SelectionMode]

class TrackFromClipGroupExclusionReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TCGEReason_Unknown: _ClassVar[TrackFromClipGroupExclusionReason]
    TCGEReason_TrackTypeIsNotAllowed: _ClassVar[TrackFromClipGroupExclusionReason]
    TCGEReason_TrackIsFrozen: _ClassVar[TrackFromClipGroupExclusionReason]
    TCGEReason_TrackIsClosed: _ClassVar[TrackFromClipGroupExclusionReason]
    TCGEReason_TrackIsLocked: _ClassVar[TrackFromClipGroupExclusionReason]
    TCGEReason_TrackIsInPlaylistView: _ClassVar[TrackFromClipGroupExclusionReason]
    TCGEReason_TrackIsElasticAudioWithFades: _ClassVar[TrackFromClipGroupExclusionReason]

class TimelineLocationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TLType_Unknown: _ClassVar[TimelineLocationType]
    TLType_Samples: _ClassVar[TimelineLocationType]
    TLType_Ticks: _ClassVar[TimelineLocationType]
    TLType_Frames: _ClassVar[TimelineLocationType]
    TLType_MinSecs: _ClassVar[TimelineLocationType]
    TLType_TimeCode: _ClassVar[TimelineLocationType]
    TLType_BarsBeats: _ClassVar[TimelineLocationType]
    TLType_FeetFrames: _ClassVar[TimelineLocationType]
    TLType_Seconds: _ClassVar[TimelineLocationType]

class BasicTimeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BTType_Unknown: _ClassVar[BasicTimeType]
    BTType_Samples: _ClassVar[BasicTimeType]
    BTType_Ticks: _ClassVar[BasicTimeType]
    BTType_Frames: _ClassVar[BasicTimeType]

class ClipType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ClipType_Unknown: _ClassVar[ClipType]
    ClipType_Audio: _ClassVar[ClipType]
    ClipType_Midi: _ClassVar[ClipType]
    ClipType_Video: _ClassVar[ClipType]
    ClipType_AudioClipGroup: _ClassVar[ClipType]
    ClipType_MidiClipGroup: _ClassVar[ClipType]
    ClipType_VideoClipGroup: _ClassVar[ClipType]
    ClipType_MixedClipGroup: _ClassVar[ClipType]

class StemFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SFormat_Unknown: _ClassVar[StemFormat]
    SFormat_Mono: _ClassVar[StemFormat]
    SFormat_Stereo: _ClassVar[StemFormat]
    SFormat_LCR: _ClassVar[StemFormat]
    SFormat_LCRS: _ClassVar[StemFormat]
    SFormat_Quad: _ClassVar[StemFormat]
    SFormat_5_0: _ClassVar[StemFormat]
    SFormat_5_1: _ClassVar[StemFormat]
    SFormat_5_0_2: _ClassVar[StemFormat]
    SFormat_5_1_2: _ClassVar[StemFormat]
    SFormat_5_0_4: _ClassVar[StemFormat]
    SFormat_5_1_4: _ClassVar[StemFormat]
    SFormat_6_0: _ClassVar[StemFormat]
    SFormat_6_1: _ClassVar[StemFormat]
    SFormat_7_0: _ClassVar[StemFormat]
    SFormat_7_1: _ClassVar[StemFormat]
    SFormat_7_0_SDDS: _ClassVar[StemFormat]
    SFormat_7_1_SDDS: _ClassVar[StemFormat]
    SFormat_7_0_2: _ClassVar[StemFormat]
    SFormat_7_1_2: _ClassVar[StemFormat]
    SFormat_7_0_4: _ClassVar[StemFormat]
    SFormat_7_1_4: _ClassVar[StemFormat]
    SFormat_7_0_6: _ClassVar[StemFormat]
    SFormat_7_1_6: _ClassVar[StemFormat]
    SFormat_9_0_4: _ClassVar[StemFormat]
    SFormat_9_1_4: _ClassVar[StemFormat]
    SFormat_9_0_6: _ClassVar[StemFormat]
    SFormat_9_1_6: _ClassVar[StemFormat]
    SFormat_1stOrderAmbisonics: _ClassVar[StemFormat]
    SFormat_2ndOrderAmbisonics: _ClassVar[StemFormat]
    SFormat_3rdOrderAmbisonics: _ClassVar[StemFormat]
    SFormat_4thOrderAmbisonics: _ClassVar[StemFormat]
    SFormat_5thOrderAmbisonics: _ClassVar[StemFormat]
    SFormat_6thOrderAmbisonics: _ClassVar[StemFormat]
    SFormat_7thOrderAmbisonics: _ClassVar[StemFormat]
    SFormat_None: _ClassVar[StemFormat]
    SFormat_2_1: _ClassVar[StemFormat]
    SFormat_Overhead: _ClassVar[StemFormat]

class StemChannel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SChannel_Unknown: _ClassVar[StemChannel]
    SChannel_Mono: _ClassVar[StemChannel]
    SChannel_Left: _ClassVar[StemChannel]
    SChannel_Right: _ClassVar[StemChannel]
    SChannel_Center: _ClassVar[StemChannel]
    SChannel_LeftSurround: _ClassVar[StemChannel]
    SChannel_CenterSurround: _ClassVar[StemChannel]
    SChannel_RightSurround: _ClassVar[StemChannel]
    SChannel_Surround: _ClassVar[StemChannel]
    SChannel_LeftCenter: _ClassVar[StemChannel]
    SChannel_RightCenter: _ClassVar[StemChannel]
    SChannel_LeftSide: _ClassVar[StemChannel]
    SChannel_RightSide: _ClassVar[StemChannel]
    SChannel_LeftFrontHeight: _ClassVar[StemChannel]
    SChannel_RightFrontHeight: _ClassVar[StemChannel]
    SChannel_LeftTopMiddle: _ClassVar[StemChannel]
    SChannel_RightTopMiddle: _ClassVar[StemChannel]
    SChannel_LeftTopFront: _ClassVar[StemChannel]
    SChannel_RightTopFront: _ClassVar[StemChannel]
    SChannel_LeftTopRear: _ClassVar[StemChannel]
    SChannel_RightTopRear: _ClassVar[StemChannel]
    SChannel_LeftWide: _ClassVar[StemChannel]
    SChannel_RightWide: _ClassVar[StemChannel]
    SChannel_LFE: _ClassVar[StemChannel]
    SChannel_0: _ClassVar[StemChannel]
    SChannel_1: _ClassVar[StemChannel]
    SChannel_2: _ClassVar[StemChannel]
    SChannel_3: _ClassVar[StemChannel]
    SChannel_4: _ClassVar[StemChannel]
    SChannel_5: _ClassVar[StemChannel]
    SChannel_6: _ClassVar[StemChannel]
    SChannel_7: _ClassVar[StemChannel]
    SChannel_8: _ClassVar[StemChannel]
    SChannel_9: _ClassVar[StemChannel]
    SChannel_10: _ClassVar[StemChannel]
    SChannel_11: _ClassVar[StemChannel]
    SChannel_12: _ClassVar[StemChannel]
    SChannel_13: _ClassVar[StemChannel]
    SChannel_14: _ClassVar[StemChannel]
    SChannel_15: _ClassVar[StemChannel]
    SChannel_16: _ClassVar[StemChannel]
    SChannel_17: _ClassVar[StemChannel]
    SChannel_18: _ClassVar[StemChannel]
    SChannel_19: _ClassVar[StemChannel]
    SChannel_20: _ClassVar[StemChannel]
    SChannel_21: _ClassVar[StemChannel]
    SChannel_22: _ClassVar[StemChannel]
    SChannel_23: _ClassVar[StemChannel]
    SChannel_24: _ClassVar[StemChannel]
    SChannel_25: _ClassVar[StemChannel]
    SChannel_26: _ClassVar[StemChannel]
    SChannel_27: _ClassVar[StemChannel]
    SChannel_28: _ClassVar[StemChannel]
    SChannel_29: _ClassVar[StemChannel]
    SChannel_30: _ClassVar[StemChannel]
    SChannel_31: _ClassVar[StemChannel]
    SChannel_32: _ClassVar[StemChannel]
    SChannel_33: _ClassVar[StemChannel]
    SChannel_34: _ClassVar[StemChannel]
    SChannel_35: _ClassVar[StemChannel]
    SChannel_36: _ClassVar[StemChannel]
    SChannel_37: _ClassVar[StemChannel]
    SChannel_38: _ClassVar[StemChannel]
    SChannel_39: _ClassVar[StemChannel]
    SChannel_40: _ClassVar[StemChannel]
    SChannel_41: _ClassVar[StemChannel]
    SChannel_42: _ClassVar[StemChannel]
    SChannel_43: _ClassVar[StemChannel]
    SChannel_44: _ClassVar[StemChannel]
    SChannel_45: _ClassVar[StemChannel]
    SChannel_46: _ClassVar[StemChannel]
    SChannel_47: _ClassVar[StemChannel]
    SChannel_48: _ClassVar[StemChannel]
    SChannel_49: _ClassVar[StemChannel]
    SChannel_50: _ClassVar[StemChannel]
    SChannel_51: _ClassVar[StemChannel]
    SChannel_52: _ClassVar[StemChannel]
    SChannel_53: _ClassVar[StemChannel]
    SChannel_54: _ClassVar[StemChannel]
    SChannel_55: _ClassVar[StemChannel]
    SChannel_56: _ClassVar[StemChannel]
    SChannel_57: _ClassVar[StemChannel]
    SChannel_58: _ClassVar[StemChannel]
    SChannel_59: _ClassVar[StemChannel]
    SChannel_60: _ClassVar[StemChannel]
    SChannel_61: _ClassVar[StemChannel]
    SChannel_62: _ClassVar[StemChannel]
    SChannel_63: _ClassVar[StemChannel]

class BatchJobStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BatchJobStatus_Unknown: _ClassVar[BatchJobStatus]
    BatchJobStatus_Pending: _ClassVar[BatchJobStatus]
    BatchJobStatus_Running: _ClassVar[BatchJobStatus]
    BatchJobStatus_Completed: _ClassVar[BatchJobStatus]
    BatchJobStatus_TimedOut: _ClassVar[BatchJobStatus]
    BatchJobStatus_Failed: _ClassVar[BatchJobStatus]
    BatchJobStatus_Canceled: _ClassVar[BatchJobStatus]
CreateSession: CommandId
CId_CreateSession: CommandId
OpenSession: CommandId
CId_OpenSession: CommandId
Import: CommandId
CId_Import: CommandId
GetTrackList: CommandId
CId_GetTrackList: CommandId
SelectAllClipsOnTrack: CommandId
CId_SelectAllClipsOnTrack: CommandId
ExtendSelectionToTargetTracks: CommandId
CId_ExtendSelectionToTargetTracks: CommandId
TrimToSelection: CommandId
CId_TrimToSelection: CommandId
CreateFadesBasedOnPreset: CommandId
CId_CreateFadesBasedOnPreset: CommandId
RenameTargetTrack: CommandId
CId_RenameTargetTrack: CommandId
ConsolidateClip: CommandId
CId_ConsolidateClip: CommandId
ExportClipsAsFiles: CommandId
CId_ExportClipsAsFiles: CommandId
ExportSelectedTracksAsAAFOMF: CommandId
CId_ExportSelectedTracksAsAAFOMF: CommandId
GetTaskStatus: CommandId
CId_GetTaskStatus: CommandId
HostReadyCheck: CommandId
CId_HostReadyCheck: CommandId
RefreshTargetAudioFiles: CommandId
CId_RefreshTargetAudioFiles: CommandId
RefreshAllModifiedAudioFiles: CommandId
CId_RefreshAllModifiedAudioFiles: CommandId
GetFileLocation: CommandId
CId_GetFileLocation: CommandId
CloseSession: CommandId
CId_CloseSession: CommandId
SaveSession: CommandId
CId_SaveSession: CommandId
SaveSessionAs: CommandId
CId_SaveSessionAs: CommandId
Cut: CommandId
CId_Cut: CommandId
Copy: CommandId
CId_Copy: CommandId
Paste: CommandId
CId_Paste: CommandId
Clear: CommandId
CId_Clear: CommandId
CutSpecial: CommandId
CId_CutSpecial: CommandId
CopySpecial: CommandId
CId_CopySpecial: CommandId
ClearSpecial: CommandId
CId_ClearSpecial: CommandId
PasteSpecial: CommandId
CId_PasteSpecial: CommandId
ExportMix: CommandId
CId_ExportMix: CommandId
Spot: CommandId
CId_Spot: CommandId
ExportSessionInfoAsText: CommandId
CId_ExportSessionInfoAsText: CommandId
GetDynamicProperties: CommandId
CId_GetDynamicProperties: CommandId
SetPlaybackMode: CommandId
CId_SetPlaybackMode: CommandId
SetRecordMode: CommandId
CId_SetRecordMode: CommandId
GetSessionAudioFormat: CommandId
CId_GetSessionAudioFormat: CommandId
GetSessionSampleRate: CommandId
CId_GetSessionSampleRate: CommandId
GetSessionBitDepth: CommandId
CId_GetSessionBitDepth: CommandId
GetSessionInterleavedState: CommandId
CId_GetSessionInterleavedState: CommandId
GetSessionTimeCodeRate: CommandId
CId_GetSessionTimeCodeRate: CommandId
GetSessionFeetFramesRate: CommandId
CId_GetSessionFeetFramesRate: CommandId
GetSessionAudioRatePullSettings: CommandId
CId_GetSessionAudioRatePullSettings: CommandId
GetSessionVideoRatePullSettings: CommandId
CId_GetSessionVideoRatePullSettings: CommandId
GetSessionName: CommandId
CId_GetSessionName: CommandId
GetSessionPath: CommandId
CId_GetSessionPath: CommandId
GetSessionStartTime: CommandId
CId_GetSessionStartTime: CommandId
GetSessionLength: CommandId
CId_GetSessionLength: CommandId
SetSessionAudioFormat: CommandId
CId_SetSessionAudioFormat: CommandId
SetSessionBitDepth: CommandId
CId_SetSessionBitDepth: CommandId
SetSessionInterleavedState: CommandId
CId_SetSessionInterleavedState: CommandId
SetSessionTimeCodeRate: CommandId
CId_SetSessionTimeCodeRate: CommandId
SetSessionFeetFramesRate: CommandId
CId_SetSessionFeetFramesRate: CommandId
SetSessionAudioRatePullSettings: CommandId
CId_SetSessionAudioRatePullSettings: CommandId
SetSessionVideoRatePullSettings: CommandId
CId_SetSessionVideoRatePullSettings: CommandId
SetSessionStartTime: CommandId
CId_SetSessionStartTime: CommandId
SetSessionLength: CommandId
CId_SetSessionLength: CommandId
GetPTSLVersion: CommandId
CId_GetPTSLVersion: CommandId
GetPlaybackMode: CommandId
CId_GetPlaybackMode: CommandId
GetRecordMode: CommandId
CId_GetRecordMode: CommandId
GetTransportArmed: CommandId
CId_GetTransportArmed: CommandId
GetTransportState: CommandId
CId_GetTransportState: CommandId
ClearMemoryLocation: CommandId
CId_ClearMemoryLocation: CommandId
RenameSelectedClip: CommandId
CId_RenameSelectedClip: CommandId
RenameTargetClip: CommandId
CId_RenameTargetClip: CommandId
TogglePlayState: CommandId
CId_TogglePlayState: CommandId
ToggleRecordEnable: CommandId
CId_ToggleRecordEnable: CommandId
PlayHalfSpeed: CommandId
CId_PlayHalfSpeed: CommandId
RecordHalfSpeed: CommandId
CId_RecordHalfSpeed: CommandId
EditMemoryLocation: CommandId
CId_EditMemoryLocation: CommandId
GetMemoryLocations: CommandId
CId_GetMemoryLocations: CommandId
RegisterConnection: CommandId
CId_RegisterConnection: CommandId
CreateMemoryLocation: CommandId
CId_CreateMemoryLocation: CommandId
CreateNewTracks: CommandId
CId_CreateNewTracks: CommandId
SelectTracksByName: CommandId
CId_SelectTracksByName: CommandId
GetEditMode: CommandId
CId_GetEditMode: CommandId
SetEditMode: CommandId
CId_SetEditMode: CommandId
GetEditTool: CommandId
CId_GetEditTool: CommandId
SetEditTool: CommandId
CId_SetEditTool: CommandId
RecallZoomPreset: CommandId
CId_RecallZoomPreset: CommandId
GetEditModeOptions: CommandId
CId_GetEditModeOptions: CommandId
SetEditModeOptions: CommandId
CId_SetEditModeOptions: CommandId
SetTimelineSelection: CommandId
CId_SetTimelineSelection: CommandId
GetTimelineSelection: CommandId
CId_GetTimelineSelection: CommandId
ImportVideo: CommandId
CId_ImportVideo: CommandId
SelectMemoryLocation: CommandId
CId_SelectMemoryLocation: CommandId
SetTrackMuteState: CommandId
CId_SetTrackMuteState: CommandId
SetTrackSoloState: CommandId
CId_SetTrackSoloState: CommandId
SetTrackSoloSafeState: CommandId
CId_SetTrackSoloSafeState: CommandId
SetTrackRecordEnableState: CommandId
CId_SetTrackRecordEnableState: CommandId
SetTrackRecordSafeEnableState: CommandId
CId_SetTrackRecordSafeEnableState: CommandId
SetTrackInputMonitorState: CommandId
CId_SetTrackInputMonitorState: CommandId
SetTrackSmartDspState: CommandId
CId_SetTrackSmartDspState: CommandId
SetTrackHiddenState: CommandId
CId_SetTrackHiddenState: CommandId
SetTrackInactiveState: CommandId
CId_SetTrackInactiveState: CommandId
SetTrackFrozenState: CommandId
CId_SetTrackFrozenState: CommandId
SetTrackOnlineState: CommandId
CId_SetTrackOnlineState: CommandId
SetTrackOpenState: CommandId
CId_SetTrackOpenState: CommandId
GetSessionIDs: CommandId
CId_GetSessionIDs: CommandId
GetMemoryLocationsManageMode: CommandId
CId_GetMemoryLocationsManageMode: CommandId
SetMemoryLocationsManageMode: CommandId
CId_SetMemoryLocationsManageMode: CommandId
SetMainCounterFormat: CommandId
CId_SetMainCounterFormat: CommandId
SetSubCounterFormat: CommandId
CId_SetSubCounterFormat: CommandId
GetMainCounterFormat: CommandId
CId_GetMainCounterFormat: CommandId
GetSubCounterFormat: CommandId
CId_GetSubCounterFormat: CommandId
Undo: CommandId
CId_Undo: CommandId
Redo: CommandId
CId_Redo: CommandId
UndoAll: CommandId
CId_UndoAll: CommandId
RedoAll: CommandId
CId_RedoAll: CommandId
ClearUndoQueue: CommandId
CId_ClearUndoQueue: CommandId
SetTrackDSPModeSafeState: CommandId
CId_SetTrackDSPModeSafeState: CommandId
GetSessionSystemDelayInfo: CommandId
CId_GetSessionSystemDelayInfo: CommandId
GroupClips: CommandId
CId_GroupClips: CommandId
UngroupClips: CommandId
CId_UngroupClips: CommandId
UngroupAllClips: CommandId
CId_UngroupAllClips: CommandId
RegroupClips: CommandId
CId_RegroupClips: CommandId
RepeatSelection: CommandId
CId_RepeatSelection: CommandId
DuplicateSelection: CommandId
CId_DuplicateSelection: CommandId
ClearAllMemoryLocations: CommandId
CId_ClearAllMemoryLocations: CommandId
CId_GetTimeAsType: CommandId
CId_SubtractLocations: CommandId
CId_AddLengthToLocation: CommandId
CId_SubtractPositions: CommandId
CId_AddLengthToPosition: CommandId
CId_ImportAudioToClipList: CommandId
CId_SpotClipsByID: CommandId
CId_GetClipList: CommandId
CId_GetMediaFileInfo: CommandId
CId_CreateAudioClips: CommandId
CId_GetExportMixSourceList: CommandId
CId_CreateBatchJob: CommandId
CId_GetMonitorOutputPath: CommandId
CId_GetEditSelection: CommandId
CId_SubscribeToEvents: CommandId
CId_GetBatchJobStatus: CommandId
CId_BounceTrack: CommandId
CId_PollEvents: CommandId
CId_UnsubscribeFromEvents: CommandId
CId_CompleteBatchJob: CommandId
CId_CancelBatchJob: CommandId
CId_BeginScrub: CommandId
CId_EndScrub: CommandId
CId_ContinueScrub: CommandId
CId_EnableCueProVideoPlugIn: CommandId
CId_UpdateVideo: CommandId
CId_EnableAPI: CommandId
CId_ExchangePublicKeys: CommandId
EId_Unknown: EventId
EId_SessionOpened: EventId
EId_SessionCreated: EventId
EId_SessionClosed: EventId
Queued: TaskStatus
TStatus_Queued: TaskStatus
Pending: TaskStatus
TStatus_Pending: TaskStatus
InProgress: TaskStatus
TStatus_InProgress: TaskStatus
Completed: TaskStatus
TStatus_Completed: TaskStatus
Failed: TaskStatus
TStatus_Failed: TaskStatus
WaitingForUserInput: TaskStatus
TStatus_WaitingForUserInput: TaskStatus
CompletedWithBadResponse: TaskStatus
TStatus_CompletedWithBadResponse: TaskStatus
FailedWithBadErrorResponse: TaskStatus
TStatus_FailedWithBadErrorResponse: TaskStatus
OS_WritePermissions: CommandErrorType
CEType_OS_WritePermissions: CommandErrorType
OS_ErrorCode: CommandErrorType
CEType_OS_ErrorCode: CommandErrorType
OS_NoLocationFound: CommandErrorType
CEType_OS_NoLocationFound: CommandErrorType
OS_NoSessionFound: CommandErrorType
CEType_OS_NoSessionFound: CommandErrorType
OS_FilePathLocation: CommandErrorType
OS_ReadError: CommandErrorType
CEType_OS_ReadError: CommandErrorType
OS_DiskSpace: CommandErrorType
CEType_OS_DiskSpace: CommandErrorType
OS_DuplicateName: CommandErrorType
CEType_OS_DuplicateName: CommandErrorType
OS_IllegalCharacters: CommandErrorType
CEType_OS_IllegalCharacters: CommandErrorType
OS_CharactersLimit: CommandErrorType
CEType_OS_CharactersLimit: CommandErrorType
OS_ProToolsIsNotAvailable: CommandErrorType
CEType_OS_ProToolsIsNotAvailable: CommandErrorType
OS_NoFilePathFound: CommandErrorType
CEType_OS_NoFilePathFound: CommandErrorType
PT_UnknownError: CommandErrorType
CEType_PT_UnknownError: CommandErrorType
PT_NoTemplateGroup: CommandErrorType
CEType_PT_NoTemplateGroup: CommandErrorType
PT_NoTemplate: CommandErrorType
CEType_PT_NoTemplate: CommandErrorType
PT_SampleRateMismatch: CommandErrorType
CEType_PT_SampleRateMismatch: CommandErrorType
PT_NoVideoTrackFound: CommandErrorType
CEType_PT_NoVideoTrackFound: CommandErrorType
PT_NoTracksFound: CommandErrorType
CEType_PT_NoTracksFound: CommandErrorType
PT_NoOpenedSession: CommandErrorType
CEType_PT_NoOpenedSession: CommandErrorType
PT_NoTrackFound: CommandErrorType
CEType_PT_NoTrackFound: CommandErrorType
PT_NoClipsFound: CommandErrorType
CEType_PT_NoClipsFound: CommandErrorType
PT_NoSelection: CommandErrorType
CEType_PT_NoSelection: CommandErrorType
PT_RecordDrive: CommandErrorType
CEType_PT_RecordDrive: CommandErrorType
PT_NoPresetFound: CommandErrorType
CEType_PT_NoPresetFound: CommandErrorType
PT_FileTypeMXF: CommandErrorType
CEType_PT_FileTypeMXF: CommandErrorType
PT_CopyOptionCopy: CommandErrorType
CEType_PT_CopyOptionCopy: CommandErrorType
PT_CopyOptionLink: CommandErrorType
CEType_PT_CopyOptionLink: CommandErrorType
PT_QuantizeEdits: CommandErrorType
CEType_PT_QuantizeEdits: CommandErrorType
PT_ExportAsMultichannel: CommandErrorType
CEType_PT_ExportAsMultichannel: CommandErrorType
PT_IllegalCharactersComments: CommandErrorType
CEType_PT_IllegalCharactersComments: CommandErrorType
PT_IllegalCharactersSequenceName: CommandErrorType
CEType_PT_IllegalCharactersSequenceName: CommandErrorType
PT_MaxCharactersComments: CommandErrorType
CEType_PT_MaxCharactersComments: CommandErrorType
PT_MaxCharactersSequenceName: CommandErrorType
CEType_PT_MaxCharactersSequenceName: CommandErrorType
PT_NoSequenceName: CommandErrorType
CEType_PT_NoSequenceName: CommandErrorType
PT_InvalidTask: CommandErrorType
CEType_PT_InvalidTask: CommandErrorType
PT_FileNotFound: CommandErrorType
CEType_PT_FileNotFound: CommandErrorType
PT_InvalidSelection: CommandErrorType
CEType_PT_InvalidSelection: CommandErrorType
PT_ReadOnlySession: CommandErrorType
CEType_PT_ReadOnlySession: CommandErrorType
PT_InvalidParameter: CommandErrorType
CEType_PT_InvalidParameter: CommandErrorType
PT_Forbidden: CommandErrorType
CEType_PT_Forbidden: CommandErrorType
PT_NoTimelineFound: CommandErrorType
CEType_PT_NoTimelineFound: CommandErrorType
PT_ArgumentOutOfRange: CommandErrorType
CEType_PT_ArgumentOutOfRange: CommandErrorType
PT_ForbiddenTrackType: CommandErrorType
CEType_PT_ForbiddenTrackType: CommandErrorType
PT_NoVideoEngineFound: CommandErrorType
CEType_PT_NoVideoEngineFound: CommandErrorType
PT_NoDspHardwareFound: CommandErrorType
CEType_PT_NoDspHardwareFound: CommandErrorType
PT_UnsupportedCommand: CommandErrorType
CEType_PT_UnsupportedCommand: CommandErrorType
PT_HostNotReady: CommandErrorType
CEType_PT_HostNotReady: CommandErrorType
PT_CannotBeDone: CommandErrorType
CEType_PT_CannotBeDone: CommandErrorType
PT_ResponseLengthExceeded: CommandErrorType
CEType_PT_ResponseLengthExceeded: CommandErrorType
PT_CommandTimeout: CommandErrorType
CEType_PT_CommandTimeout: CommandErrorType
PT_HostIsBusy: CommandErrorType
CEType_PT_HostIsBusy: CommandErrorType
CEType_PT_DeprecatedParameter: CommandErrorType
CEType_PT_DeprecatedParameterValue: CommandErrorType
PT_Info: CommandErrorType
CEType_PT_Info: CommandErrorType
SDK_VersionMismatch: CommandErrorType
CEType_SDK_VersionMismatch: CommandErrorType
SDK_NotImplemented: CommandErrorType
CEType_SDK_NotImplemented: CommandErrorType
SDK_SessionIdParseError: CommandErrorType
CEType_SDK_SessionIdParseError: CommandErrorType
SDK_GrpcGeneric: CommandErrorType
CEType_SDK_GrpcGeneric: CommandErrorType
Unknown: TrackType
TT_Unknown: TrackType
TType_Unknown: TrackType
Midi: TrackType
TT_Midi: TrackType
TType_Midi: TrackType
AudioTrack: TrackType
TT_Audio: TrackType
TType_Audio: TrackType
Aux: TrackType
TT_Aux: TrackType
TType_Aux: TrackType
VideoTrack: TrackType
TT_Video: TrackType
TType_Video: TrackType
Vca: TrackType
TT_Vca: TrackType
TType_Vca: TrackType
Tempo: TrackType
TT_Tempo: TrackType
TType_Tempo: TrackType
Markers: TrackType
TT_Markers: TrackType
TType_Markers: TrackType
Meter: TrackType
TT_Meter: TrackType
TType_Meter: TrackType
KeySignature: TrackType
TT_KeySignature: TrackType
TType_KeySignature: TrackType
ChordSymbols: TrackType
TT_ChordSymbols: TrackType
TType_ChordSymbols: TrackType
Instrument: TrackType
TT_Instrument: TrackType
TType_Instrument: TrackType
Master: TrackType
TT_Master: TrackType
TType_Master: TrackType
Heat: TrackType
TT_Heat: TrackType
TType_Heat: TrackType
BasicFolder: TrackType
TT_BasicFolder: TrackType
TType_BasicFolder: TrackType
RoutingFolder: TrackType
TT_RoutingFolder: TrackType
TType_RoutingFolder: TrackType
CompLane: TrackType
TT_CompLane: TrackType
TType_CompLane: TrackType
TF_Unknown: TrackFormat
TFormat_Unknown: TrackFormat
TF_Mono: TrackFormat
TFormat_Mono: TrackFormat
TF_Stereo: TrackFormat
TFormat_Stereo: TrackFormat
TF_LCR: TrackFormat
TFormat_LCR: TrackFormat
TF_LCRS: TrackFormat
TFormat_LCRS: TrackFormat
TF_Quad: TrackFormat
TFormat_Quad: TrackFormat
TF_5_0: TrackFormat
TFormat_5_0: TrackFormat
TF_5_1: TrackFormat
TFormat_5_1: TrackFormat
TF_5_0_2: TrackFormat
TFormat_5_0_2: TrackFormat
TF_5_1_2: TrackFormat
TFormat_5_1_2: TrackFormat
TF_5_0_4: TrackFormat
TFormat_5_0_4: TrackFormat
TF_5_1_4: TrackFormat
TFormat_5_1_4: TrackFormat
TF_6_0: TrackFormat
TFormat_6_0: TrackFormat
TF_6_1: TrackFormat
TFormat_6_1: TrackFormat
TF_7_0: TrackFormat
TFormat_7_0: TrackFormat
TF_7_1: TrackFormat
TFormat_7_1: TrackFormat
TF_7_0_SDDS: TrackFormat
TFormat_7_0_SDDS: TrackFormat
TF_7_1_SDDS: TrackFormat
TFormat_7_1_SDDS: TrackFormat
TF_7_0_2: TrackFormat
TFormat_7_0_2: TrackFormat
TF_7_1_2: TrackFormat
TFormat_7_1_2: TrackFormat
TF_7_0_4: TrackFormat
TFormat_7_0_4: TrackFormat
TF_7_1_4: TrackFormat
TFormat_7_1_4: TrackFormat
TF_7_0_6: TrackFormat
TFormat_7_0_6: TrackFormat
TF_7_1_6: TrackFormat
TFormat_7_1_6: TrackFormat
TF_9_0_4: TrackFormat
TFormat_9_0_4: TrackFormat
TF_9_1_4: TrackFormat
TFormat_9_1_4: TrackFormat
TF_9_0_6: TrackFormat
TFormat_9_0_6: TrackFormat
TF_9_1_6: TrackFormat
TFormat_9_1_6: TrackFormat
TF_1stOrderAmbisonics: TrackFormat
TFormat_1stOrderAmbisonics: TrackFormat
TF_2ndOrderAmbisonics: TrackFormat
TFormat_2ndOrderAmbisonics: TrackFormat
TF_3rdOrderAmbisonics: TrackFormat
TFormat_3rdOrderAmbisonics: TrackFormat
TF_4thOrderAmbisonics: TrackFormat
TFormat_4thOrderAmbisonics: TrackFormat
TF_5thOrderAmbisonics: TrackFormat
TFormat_5thOrderAmbisonics: TrackFormat
TF_6thOrderAmbisonics: TrackFormat
TFormat_6thOrderAmbisonics: TrackFormat
TF_7thOrderAmbisonics: TrackFormat
TFormat_7thOrderAmbisonics: TrackFormat
TF_None: TrackFormat
TFormat_None: TrackFormat
TF_2_1: TrackFormat
TFormat_2_1: TrackFormat
TF_Overhead: TrackFormat
TFormat_Overhead: TrackFormat
TTB_Unknown: TrackTimebase
TTimebase_Unknown: TrackTimebase
TTB_Samples: TrackTimebase
TTimebase_Samples: TrackTimebase
TTB_Ticks: TrackTimebase
TTimebase_Ticks: TrackTimebase
TTB_None: TrackTimebase
TTimebase_None: TrackTimebase
TAState_Unknown: TrackAttributeState
None: TrackAttributeState
TAState_None: TrackAttributeState
SetExplicitly: TrackAttributeState
TAState_SetExplicitly: TrackAttributeState
SetImplicitly: TrackAttributeState
TAState_SetImplicitly: TrackAttributeState
SetExplicitlyAndImplicitly: TrackAttributeState
TAState_SetExplicitlyAndImplicitly: TrackAttributeState
FType_Unknown: FileType
FT_WAVE: FileType
FType_WAVE: FileType
FT_AIFF: FileType
FType_AIFF: FileType
FT_AAF: FileType
FType_AAF: FileType
FT_OMF: FileType
FType_OMF: FileType
FType_MXF: FileType
IOSettings_Unknown: IOSettings
IO_None: IOSettings
IOSettings_None: IOSettings
IO_Last: IOSettings
IOSettings_Last: IOSettings
IO_StereoMix: IOSettings
IOSettings_StereoMix: IOSettings
IO_51FilmMix: IOSettings
IOSettings_51FilmMix: IOSettings
IO_51SMPTEMix: IOSettings
IOSettings_51SMPTEMix: IOSettings
IO_51DTSMix: IOSettings
IOSettings_51DTSMix: IOSettings
IO_UserDefined: IOSettings
IOSettings_UserDefined: IOSettings
IType_Unknown: ImportType
Session: ImportType
IType_Session: ImportType
Audio: ImportType
IType_Audio: ImportType
AMOptions_Unknown: AudioMediaOptions
LinkToSourceAudio: AudioMediaOptions
AMOptions_LinkToSourceAudio: AudioMediaOptions
CopyFromSourceAudio: AudioMediaOptions
AMOptions_CopyFromSourceAudio: AudioMediaOptions
ConsolidateFromSourceAudio: AudioMediaOptions
AMOptions_ConsolidateFromSourceAudio: AudioMediaOptions
ForceToTargetSessionFormat: AudioMediaOptions
AMOptions_ForceToTargetSessionFormat: AudioMediaOptions
VMOptions_Unknown: VideoMediaOptions
LinkToSourceVideo: VideoMediaOptions
VMOptions_LinkToSourceVideo: VideoMediaOptions
CopyFromSourceVideo: VideoMediaOptions
VMOptions_CopyFromSourceVideo: VideoMediaOptions
ImportAsOfflineSatelliteMedia: VideoMediaOptions
MTOptions_Unknown: MatchTrackOptions
MT_None: MatchTrackOptions
MTOptions_None: MatchTrackOptions
MT_MatchTracks: MatchTrackOptions
MTOptions_MatchTracks: MatchTrackOptions
MT_ImportAsNewTrack: MatchTrackOptions
MTOptions_ImportAsNewTrack: MatchTrackOptions
TCMOptions_Unknown: TimeCodeMappingOptions
MaintainAbsoluteTimeCodeValues: TimeCodeMappingOptions
TCMOptions_MaintainAbsoluteTimeCodeValues: TimeCodeMappingOptions
MaintainRelativeTimeCodeValues: TimeCodeMappingOptions
TCMOptions_MaintainRelativeTimeCodeValues: TimeCodeMappingOptions
MapStartTimeCodeTo: TimeCodeMappingOptions
TCMOptions_MapStartTimeCodeTo: TimeCodeMappingOptions
TOOptions_Unknown: TrackOffsetOptions
BarsBeats: TrackOffsetOptions
TOOptions_BarsBeats: TrackOffsetOptions
MinSecs: TrackOffsetOptions
TOOptions_MinSecs: TrackOffsetOptions
TimeCode: TrackOffsetOptions
TOOptions_TimeCode: TrackOffsetOptions
FeetFrames: TrackOffsetOptions
TOOptions_FeetFrames: TrackOffsetOptions
Samples: TrackOffsetOptions
TOOptions_Samples: TrackOffsetOptions
CQuality_Unknown: ConversionQuality
Low: ConversionQuality
CQuality_Low: ConversionQuality
Good: ConversionQuality
CQuality_Good: ConversionQuality
Better: ConversionQuality
CQuality_Better: ConversionQuality
Best: ConversionQuality
CQuality_Best: ConversionQuality
TweakHead: ConversionQuality
CQuality_TweakHead: ConversionQuality
MPOptions_Unknown: MainPlaylistOptions
ImportReplaceExistingPlaylists: MainPlaylistOptions
MPOptions_ImportReplaceExistingPlaylists: MainPlaylistOptions
ImportOverlayNewOnExistingPlaylists: MainPlaylistOptions
MPOptions_ImportOverlayNewOnExistingPlaylists: MainPlaylistOptions
DoNotImport: MainPlaylistOptions
MPOptions_DoNotImport: MainPlaylistOptions
AOperations_Unknown: AudioOperations
AddAudio: AudioOperations
AOperations_AddAudio: AudioOperations
CopyAudio: AudioOperations
AOperations_CopyAudio: AudioOperations
ConvertAudio: AudioOperations
AOperations_ConvertAudio: AudioOperations
Default: AudioOperations
AOperations_Default: AudioOperations
MDestination_Unknown: MediaDestination
MD_None: MediaDestination
MDestination_None: MediaDestination
MD_MainVideoTrack: MediaDestination
MDestination_MainVideoTrack: MediaDestination
MD_NewTrack: MediaDestination
MDestination_NewTrack: MediaDestination
MD_ClipList: MediaDestination
MDestination_ClipList: MediaDestination
MLocation_Unknown: MediaLocation
ML_None: MediaLocation
MLocation_None: MediaLocation
ML_SessionStart: MediaLocation
MLocation_SessionStart: MediaLocation
ML_SongStart: MediaLocation
MLocation_SongStart: MediaLocation
ML_Selection: MediaLocation
MLocation_Selection: MediaLocation
ML_Spot: MediaLocation
MLocation_Spot: MediaLocation
TLFilter_Unknown: TrackListFilter
All: TrackListFilter
TLFilter_All: TrackListFilter
Selected: TrackListFilter
TLFilter_Selected: TrackListFilter
SelectedExplicitly: TrackListFilter
TLFilter_SelectedExplicitly: TrackListFilter
SelectedImplicitly: TrackListFilter
TLFilter_SelectedImplicitly: TrackListFilter
WithClipsOnMainPlaylist: TrackListFilter
TLFilter_WithClipsOnMainPlaylist: TrackListFilter
WithAutomationOnMainPlaylist: TrackListFilter
TLFilter_WithAutomationOnMainPlaylist: TrackListFilter
Inactive: TrackListFilter
TLFilter_Inactive: TrackListFilter
InactiveExplicitly: TrackListFilter
TLFilter_InactiveExplicitly: TrackListFilter
InactiveImplicitly: TrackListFilter
TLFilter_InactiveImplicitly: TrackListFilter
Hidden: TrackListFilter
TLFilter_Hidden: TrackListFilter
HiddenExplicitly: TrackListFilter
TLFilter_HiddenExplicitly: TrackListFilter
HiddenImplicitly: TrackListFilter
TLFilter_HiddenImplicitly: TrackListFilter
Locked: TrackListFilter
TLFilter_Locked: TrackListFilter
Muted: TrackListFilter
TLFilter_Muted: TrackListFilter
Frozen: TrackListFilter
TLFilter_Frozen: TrackListFilter
Open: TrackListFilter
TLFilter_Open: TrackListFilter
Online: TrackListFilter
TLFilter_Online: TrackListFilter
TLFilter_HasEditSelection: TrackListFilter
TLFilter_HasEditSelectionExplicitly: TrackListFilter
TLFilter_HasEditSelectionImplicitly: TrackListFilter
SLType_Unknown: SpotLocationType
Start: SpotLocationType
SLType_Start: SpotLocationType
SyncPoint: SpotLocationType
SLType_SyncPoint: SpotLocationType
End: SpotLocationType
SLType_End: SpotLocationType
EFormat_Unknown: ExportFormat
EF_None: ExportFormat
EFormat_None: ExportFormat
EF_Mono: ExportFormat
EFormat_Mono: ExportFormat
EF_MultipleMono: ExportFormat
EFormat_MultipleMono: ExportFormat
EF_Interleaved: ExportFormat
EFormat_Interleaved: ExportFormat
EFType_Unknown: ExportFileType
WAV: ExportFileType
EFType_WAV: ExportFileType
AIFF: ExportFileType
EFType_AIFF: ExportFileType
MXF: ExportFileType
EFType_MXF: ExportFileType
MP3: ExportFileType
EFType_MP3: ExportFileType
QuickTime: ExportFileType
EFType_QuickTime: ExportFileType
BDepth_Unknown: BitDepth
Bit_None: BitDepth
BDepth_None: BitDepth
Bit16: BitDepth
BDepth_16: BitDepth
Bit24: BitDepth
BDepth_24: BitDepth
Bit32Float: BitDepth
BDepth_32Float: BitDepth
RDNBy_Unknown: ResolveDuplicateNamesBy
AutoRenaming: ResolveDuplicateNamesBy
RDNBy_AutoRenaming: ResolveDuplicateNamesBy
ReplacingWithNewFiles: ResolveDuplicateNamesBy
RDNBy_ReplacingWithNewFiles: ResolveDuplicateNamesBy
EAAFFType_Unknown: ExportAsAAFFileType
EAAFFType_None: ExportAsAAFFileType
AAF_WAV: ExportAsAAFFileType
EAAFFType_WAV: ExportAsAAFFileType
AAF_AIFF: ExportAsAAFFileType
EAAFFType_AIFF: ExportAsAAFFileType
AAF_MXF: ExportAsAAFFileType
EAAFFType_MXF: ExportAsAAFFileType
AAF_Embedded: ExportAsAAFFileType
EAAFFType_Embedded: ExportAsAAFFileType
AAFFBDepth_Unknown: AAFFileBitDepth
AAFFBDepth_None: AAFFileBitDepth
AAF_Bit16: AAFFileBitDepth
AAFFBDepth_Bit16: AAFFileBitDepth
AAF_Bit24: AAFFileBitDepth
AAFFBDepth_Bit24: AAFFileBitDepth
COption_Unknown: CopyOption
ConsolidateFromSourceMedia: CopyOption
COption_ConsolidateFromSourceMedia: CopyOption
CopyFromSourceMedia: CopyOption
COption_CopyFromSourceMedia: CopyOption
LinkFromSourceMedia: CopyOption
COption_LinkFromSourceMedia: CopyOption
FLTFilter_Unknown: FileLocationTypeFilter
All_Files: FileLocationTypeFilter
FLTFilter_AllFiles: FileLocationTypeFilter
OnTimeline_Files: FileLocationTypeFilter
FLTFilter_OnTimelineFiles: FileLocationTypeFilter
NotOnTimeline_Files: FileLocationTypeFilter
FLTFilter_NotOnTimelineFiles: FileLocationTypeFilter
Online_Files: FileLocationTypeFilter
FLTFilter_OnlineFiles: FileLocationTypeFilter
Offline_Files: FileLocationTypeFilter
FLTFilter_OfflineFiles: FileLocationTypeFilter
Audio_Files: FileLocationTypeFilter
FLTFilter_AudioFiles: FileLocationTypeFilter
Video_Files: FileLocationTypeFilter
FLTFilter_VideoFiles: FileLocationTypeFilter
Rendered_Files: FileLocationTypeFilter
FLTFilter_RenderedFiles: FileLocationTypeFilter
SelectedClipsTimeline: FileLocationTypeFilter
FLTFilter_SelectedClipsTimeline: FileLocationTypeFilter
SelectedClipsClipsList: FileLocationTypeFilter
FLTFilter_SelectedClipsClipsList: FileLocationTypeFilter
ADOptions_Unknown: AutomationDataOptions
All_Automation: AutomationDataOptions
ADOptions_AllAutomation: AutomationDataOptions
Pan_Automation: AutomationDataOptions
ADOptions_PanAutomation: AutomationDataOptions
PlugIn_Automation: AutomationDataOptions
ADOptions_PlugInAutomation: AutomationDataOptions
Clip_Gain: AutomationDataOptions
ADOptions_ClipGain: AutomationDataOptions
Clip_Effects: AutomationDataOptions
ADOptions_ClipEffects: AutomationDataOptions
PSOptions_Unknown: PasteSpecialOptions
Merge: PasteSpecialOptions
MergeMidi: PasteSpecialOptions
PSOptions_MergeMidi: PasteSpecialOptions
Repeat_To_Fill_Selection: PasteSpecialOptions
PSOptions_RepeatToFillSelection: PasteSpecialOptions
To_Current_Automation_Type: PasteSpecialOptions
PSOptions_ToCurrentAutomationType: PasteSpecialOptions
MergeMarkers: PasteSpecialOptions
PSOptions_MergeMarkers: PasteSpecialOptions
TBool_Unknown: TripleBool
TB_None: TripleBool
TBool_None: TripleBool
TB_False: TripleBool
TBool_False: TripleBool
TB_True: TripleBool
TBool_True: TripleBool
EMSType_Unknown: EM_SourceType
PhysicalOut: EM_SourceType
EMSType_PhysicalOut: EM_SourceType
Bus: EM_SourceType
EMSType_Bus: EM_SourceType
Output: EM_SourceType
EMSType_Output: EM_SourceType
CType_Unknown: CompressionType
CT_None: CompressionType
CType_None: CompressionType
CT_PCM: CompressionType
CType_PCM: CompressionType
SRate_Unknown: SampleRate
SR_None: SampleRate
SRate_None: SampleRate
SR_44100: SampleRate
SRate_44100: SampleRate
SR_48000: SampleRate
SRate_48000: SampleRate
SR_88200: SampleRate
SRate_88200: SampleRate
SR_96000: SampleRate
SRate_96000: SampleRate
SR_176400: SampleRate
SRate_176400: SampleRate
SR_192000: SampleRate
SRate_192000: SampleRate
EMVEOptions_Unknown: EM_VideoExportOptions
VE_None: EM_VideoExportOptions
EMVEOptions_None: EM_VideoExportOptions
VE_SameAsSource: EM_VideoExportOptions
EMVEOptions_SameAsSource: EM_VideoExportOptions
VE_Transcode: EM_VideoExportOptions
EMVEOptions_Transcode: EM_VideoExportOptions
EMFType_Unknown: EM_FileType
EM_None: EM_FileType
EMFType_None: EM_FileType
EM_MOV: EM_FileType
EMFType_MOV: EM_FileType
EM_WAV: EM_FileType
EMFType_WAV: EM_FileType
EM_AIFF: EM_FileType
EMFType_AIFF: EM_FileType
EM_MP3: EM_FileType
EMFType_MP3: EM_FileType
EM_MXFOPAtom: EM_FileType
EMFType_MXFOPAtom: EM_FileType
EM_WAVADM: EM_FileType
EMFType_WAVADM: EM_FileType
EMFType_M4A: EM_FileType
EMFDestination_Unknown: EM_FileDestination
EM_FD_None: EM_FileDestination
EMFDestination_None: EM_FileDestination
EM_FD_SessionFolder: EM_FileDestination
EMFDestination_SessionFolder: EM_FileDestination
EM_FD_Directory: EM_FileDestination
EMFDestination_Directory: EM_FileDestination
EMDFormat_Unknown: EM_DeliveryFormat
EM_DF_None: EM_DeliveryFormat
EMDFormat_None: EM_DeliveryFormat
EM_DF_FilePerMixSource: EM_DeliveryFormat
EMDFormat_FilePerMixSource: EM_DeliveryFormat
EM_DF_SingleFile: EM_DeliveryFormat
EMDFormat_SingleFile: EM_DeliveryFormat
MP3EOCBRate_Unknown: MP3EncodingOptionsConstantBitRate
MP3EOCBRate_320kbps: MP3EncodingOptionsConstantBitRate
MP3EOCBRate_256kbps: MP3EncodingOptionsConstantBitRate
MP3EOCBRate_224kbps: MP3EncodingOptionsConstantBitRate
MP3EOCBRate_192kbps: MP3EncodingOptionsConstantBitRate
MP3EOCBRate_160kbps: MP3EncodingOptionsConstantBitRate
MP3EOCBRate_128kbps: MP3EncodingOptionsConstantBitRate
MP3EOCBRate_112kbps: MP3EncodingOptionsConstantBitRate
MP3EOCBRate_96kbps: MP3EncodingOptionsConstantBitRate
MP3EOCBRate_80kbps: MP3EncodingOptionsConstantBitRate
MP3EOCBRate_64kbps: MP3EncodingOptionsConstantBitRate
MP3EOCBRate_56kbps: MP3EncodingOptionsConstantBitRate
MP3EOCBRate_48kbps: MP3EncodingOptionsConstantBitRate
MP3EOCBRate_40kbps: MP3EncodingOptionsConstantBitRate
MP3EOCBRate_32kbps: MP3EncodingOptionsConstantBitRate
MP3EOCBRate_24kbps: MP3EncodingOptionsConstantBitRate
MP3EOCBRate_20kbps: MP3EncodingOptionsConstantBitRate
MP3EOCBRate_18kbps: MP3EncodingOptionsConstantBitRate
MP3EOCBRate_16kbps: MP3EncodingOptionsConstantBitRate
MP3EOQuality_Unknown: MP3EncodingOptionsQuality
MP3EOQuality_Low: MP3EncodingOptionsQuality
MP3EOQuality_Highest: MP3EncodingOptionsQuality
DPVTypes_Unknown: DP_ValueTypes
DP_VT_double: DP_ValueTypes
DPVTypes_Double: DP_ValueTypes
DP_VT_float: DP_ValueTypes
DPVTypes_Float: DP_ValueTypes
DP_VT_int32: DP_ValueTypes
DPVTypes_Int32: DP_ValueTypes
DP_VT_int64: DP_ValueTypes
DPVTypes_Int64: DP_ValueTypes
DP_VT_uint32: DP_ValueTypes
DPVTypes_Uint32: DP_ValueTypes
DP_VT_uint64: DP_ValueTypes
DPVTypes_Uint64: DP_ValueTypes
DP_VT_sint32: DP_ValueTypes
DPVTypes_Sint32: DP_ValueTypes
DP_VT_sint64: DP_ValueTypes
DPVTypes_Sint64: DP_ValueTypes
DP_VT_fixed32: DP_ValueTypes
DPVTypes_Fixed32: DP_ValueTypes
DP_VT_fixed64: DP_ValueTypes
DPVTypes_Fixed64: DP_ValueTypes
DP_VT_sfixed32: DP_ValueTypes
DPVTypes_Sfixed32: DP_ValueTypes
DP_VT_sfixed64: DP_ValueTypes
DPVTypes_Sfixed64: DP_ValueTypes
DP_VT_bool: DP_ValueTypes
DPVTypes_Bool: DP_ValueTypes
DP_VT_string: DP_ValueTypes
DPVTypes_String: DP_ValueTypes
DP_VT_bytes: DP_ValueTypes
DPVTypes_Bytes: DP_ValueTypes
DP_VT_enum: DP_ValueTypes
DPVTypes_Enum: DP_ValueTypes
DP_VT_object: DP_ValueTypes
DPVTypes_Object: DP_ValueTypes
DPType_Unknown: DynamicPropertyType
DP_EM_CodecInfo: DynamicPropertyType
DPType_CodecInfo: DynamicPropertyType
DP_EM_DolbyAtmosInfo: DynamicPropertyType
DPType_DolbyAtmosInfo: DynamicPropertyType
TListType_Unknown: TrackListType
AllTracks: TrackListType
TListType_AllTracks: TrackListType
SelectedTracksOnly: TrackListType
TListType_SelectedTracksOnly: TrackListType
FHType_Unknown: FadeHandlingType
ShowCrossfades: FadeHandlingType
FHType_ShowCrossfades: FadeHandlingType
DontShowCrossfades: FadeHandlingType
FHType_DontShowCrossfades: FadeHandlingType
CombineCrossfadedClips: FadeHandlingType
FHType_CombineCrossfadedClips: FadeHandlingType
TFFormat_Unknown: TextAsFileFormat
TextEdit: TextAsFileFormat
TFFormat_TextEdit: TextAsFileFormat
UTF8: TextAsFileFormat
TFFormat_UTF8: TextAsFileFormat
ESI_Unknown: ESI_OutputType
ESIOType_Unknown: ESI_OutputType
ESI_File: ESI_OutputType
ESIOType_File: ESI_OutputType
ESI_String: ESI_OutputType
ESIOType_String: ESI_OutputType
PMode_Unknown: PlaybackMode
PM_Normal: PlaybackMode
PMode_Normal: PlaybackMode
PM_Loop: PlaybackMode
PMode_Loop: PlaybackMode
PM_DynamicTransport: PlaybackMode
PMode_DynamicTransport: PlaybackMode
RMode_Unknown: RecordMode
RM_Normal: RecordMode
RMode_Normal: RecordMode
RM_Loop: RecordMode
RMode_Loop: RecordMode
RM_Destructive: RecordMode
RMode_Destructive: RecordMode
RM_QuickPunch: RecordMode
RMode_QuickPunch: RecordMode
RM_TrackPunch: RecordMode
RMode_TrackPunch: RecordMode
RM_DestructivePunch: RecordMode
RMode_DestructivePunch: RecordMode
SAFormat_Unknown: SessionAudioFormat
SAF_WAVE: SessionAudioFormat
SAFormat_WAVE: SessionAudioFormat
SAF_AIFF: SessionAudioFormat
SAFormat_AIFF: SessionAudioFormat
STCRate_Unknown: SessionTimeCodeRate
STCR_Fps23976: SessionTimeCodeRate
STCRate_Fps23976: SessionTimeCodeRate
STCR_Fps24: SessionTimeCodeRate
STCRate_Fps24: SessionTimeCodeRate
STCR_Fps25: SessionTimeCodeRate
STCRate_Fps25: SessionTimeCodeRate
STCR_Fps2997: SessionTimeCodeRate
STCRate_Fps2997: SessionTimeCodeRate
STCR_Fps2997Drop: SessionTimeCodeRate
SSTCRate_Fps2997Drop: SessionTimeCodeRate
STCR_Fps30: SessionTimeCodeRate
STCRate_Fps30: SessionTimeCodeRate
STCR_Fps30Drop: SessionTimeCodeRate
STCRate_Fps30Drop: SessionTimeCodeRate
STCR_Fps47952: SessionTimeCodeRate
STCRate_Fps47952: SessionTimeCodeRate
STCR_Fps48: SessionTimeCodeRate
STCRate_Fps48: SessionTimeCodeRate
STCR_Fps50: SessionTimeCodeRate
STCRate_Fps50: SessionTimeCodeRate
STCR_Fps5994: SessionTimeCodeRate
STCRate_Fps5994: SessionTimeCodeRate
STCR_Fps5994Drop: SessionTimeCodeRate
STCRate_Fps5994Drop: SessionTimeCodeRate
STCR_Fps60: SessionTimeCodeRate
STCRate_Fps60: SessionTimeCodeRate
STCR_Fps60Drop: SessionTimeCodeRate
STCRate_Fps60Drop: SessionTimeCodeRate
STCR_Fps100: SessionTimeCodeRate
STCRate_Fps100: SessionTimeCodeRate
STCR_Fps11988: SessionTimeCodeRate
STCRate_Fps11988: SessionTimeCodeRate
STCR_Fps11988Drop: SessionTimeCodeRate
STCRate_Fps11988Drop: SessionTimeCodeRate
STCR_Fps120: SessionTimeCodeRate
STCRate_Fps120: SessionTimeCodeRate
STCR_Fps120Drop: SessionTimeCodeRate
STCRate_Fps120Drop: SessionTimeCodeRate
SFFRate_Unknown: SessionFeetFramesRate
SFFR_Fps23976: SessionFeetFramesRate
SFFRate_Fps23976: SessionFeetFramesRate
SFFR_Fps24: SessionFeetFramesRate
SFFRate_Fps24: SessionFeetFramesRate
SFFR_Fps25: SessionFeetFramesRate
SFFRate_Fps25: SessionFeetFramesRate
SRPull_Unknown: SessionRatePull
SRP_None: SessionRatePull
SRPull_None: SessionRatePull
SRP_Up01: SessionRatePull
SRPull_Up01: SessionRatePull
SRP_Down01: SessionRatePull
SRPull_Down01: SessionRatePull
SRP_Up4: SessionRatePull
SRPull_Up4: SessionRatePull
SRP_Up4Up01: SessionRatePull
SRPull_Up4Up01: SessionRatePull
SRP_Up4Down01: SessionRatePull
SRPull_Up4Down01: SessionRatePull
SRP_Down4: SessionRatePull
SRPull_Down4: SessionRatePull
SRP_Down4Up01: SessionRatePull
SRPull_Down4Up01: SessionRatePull
SRP_Down4Down01: SessionRatePull
SRPull_Down4Down01: SessionRatePull
TState_Unknown: TransportState
TS_TransportPlaying: TransportState
TState_TransportPlaying: TransportState
TS_TransportStopped: TransportState
TState_TransportStopped: TransportState
TS_TransportRecording: TransportState
TState_TransportRecording: TransportState
TS_TransportPlayingHalfSpeed: TransportState
TState_TransportPlayingHalfSpeed: TransportState
TS_TransportRecordingHalfSpeed: TransportState
TState_TransportRecordingHalfSpeed: TransportState
TS_TransportFastForward: TransportState
TState_TransportFastForward: TransportState
TS_TransportRewind: TransportState
TState_TransportRewind: TransportState
TS_TransportScrub: TransportState
TState_TransportScrub: TransportState
TS_TransportShuttle: TransportState
TState_TransportShuttle: TransportState
TS_TransportPrimed: TransportState
TState_TransportPrimed: TransportState
TS_TransportIsCueing: TransportState
TState_TransportIsCueing: TransportState
TS_TransportIsCued: TransportState
TState_TransportIsCued: TransportState
TS_TransportIsCuedForPreview: TransportState
TState_TransportIsCuedForPreview: TransportState
TS_TransportIsStopping: TransportState
TState_TransportIsStopping: TransportState
TS_TransportIsPreviewing: TransportState
TState_TransportIsPreviewing: TransportState
CLocation_Unknown: ClipLocation
CL_ClipsList: ClipLocation
CLocation_ClipsList: ClipLocation
CL_Timeline: ClipLocation
CLocation_Timeline: ClipLocation
TProperties_Unknown: TimeProperties
TP_Marker: TimeProperties
TProperties_Marker: TimeProperties
TP_Selection: TimeProperties
TProperties_Selection: TimeProperties
TP_None: TimeProperties
TProperties_None: TimeProperties
MLReference_Unknown: MemoryLocationReference
MLR_BarBeat: MemoryLocationReference
MLReference_BarBeat: MemoryLocationReference
MLR_Absolute: MemoryLocationReference
MLReference_Absolute: MemoryLocationReference
MLR_FollowTrackTimebase: MemoryLocationReference
MLReference_FollowTrackTimebase: MemoryLocationReference
MLC_Unknown: MarkerLocation
MarkerLocation_Unknown: MarkerLocation
MLC_MainRuler: MarkerLocation
MarkerLocation_MainRuler: MarkerLocation
MLC_Track: MarkerLocation
MarkerLocation_Track: MarkerLocation
MarkerLocation_NamedRuler: MarkerLocation
TIPoint_Unknown: TrackInsertionPoint
TIPoint_Before: TrackInsertionPoint
TIPoint_After: TrackInsertionPoint
TIPoint_First: TrackInsertionPoint
TIPoint_Last: TrackInsertionPoint
EMO_Unknown: EditMode
EMode_Unknown: EditMode
EMO_Shuffle: EditMode
EMode_Shuffle: EditMode
EMO_Slip: EditMode
EMode_Slip: EditMode
EMO_Spot: EditMode
EMode_Spot: EditMode
EMO_GridAbsolute: EditMode
EMode_GridAbsolute: EditMode
EMO_GridRelative: EditMode
EMode_GridRelative: EditMode
EMO_ShuffleSnapToGridAbsolute: EditMode
EMode_ShuffleSnapToGridAbsolute: EditMode
EMO_SlipSnapToGridAbsolute: EditMode
EMode_SlipSnapToGridAbsolute: EditMode
EMO_SpotSnapToGridAbsolute: EditMode
EMode_SpotSnapToGridAbsolute: EditMode
EMO_ShuffleSnapToGridRelative: EditMode
EMode_ShuffleSnapToGridRelative: EditMode
EMO_SlipSnapToGridRelative: EditMode
EMode_SlipSnapToGridRelative: EditMode
EMO_SpotSnapToGridRelative: EditMode
EMode_SpotSnapToGridRelative: EditMode
ET_Unknown: EditTool
ETool_Unknown: EditTool
ET_ZoomNormal: EditTool
ETool_ZoomNormal: EditTool
ET_ZoomSingle: EditTool
ETool_ZoomSingle: EditTool
ET_TrimStandard: EditTool
ETool_TrimStandard: EditTool
ET_TrimTce: EditTool
ETool_TrimTce: EditTool
ET_TrimScrub: EditTool
ETool_TrimScrub: EditTool
ET_TrimLoop: EditTool
ETool_TrimLoop: EditTool
ET_Selector: EditTool
ETool_Selector: EditTool
ET_GrabberTime: EditTool
ETool_GrabberTime: EditTool
ET_GrabberSeparation: EditTool
ETool_GrabberSeparation: EditTool
ET_GrabberObject: EditTool
ETool_GrabberObject: EditTool
ET_SmartTool: EditTool
ETool_SmartTool: EditTool
ET_Scrubber: EditTool
ETool_Scrubber: EditTool
ET_PencilFreeHand: EditTool
ETool_PencilFreeHand: EditTool
ET_PencilLine: EditTool
ETool_PencilLine: EditTool
ET_PencilTriangle: EditTool
ETool_PencilTriangle: EditTool
ET_PencilSquare: EditTool
ETool_PencilSquare: EditTool
ET_PencilRandom: EditTool
ETool_PencilRandom: EditTool
ET_PencilParabolic: EditTool
ETool_PencilParabolic: EditTool
ET_PencilSCurve: EditTool
ETool_PencilSCurve: EditTool
TUV_Unknown: TimelineUpdateVideo
TUVideo_Unknown: TimelineUpdateVideo
TUV_None: TimelineUpdateVideo
TUVideo_None: TimelineUpdateVideo
TUV_In: TimelineUpdateVideo
TUVideo_In: TimelineUpdateVideo
TUV_Out: TimelineUpdateVideo
TUVideo_Out: TimelineUpdateVideo
SM_Unknown: SelectionMode
SMode_Unknown: SelectionMode
SM_Replace: SelectionMode
SMode_Replace: SelectionMode
SM_Add: SelectionMode
SMode_Add: SelectionMode
SM_Subtract: SelectionMode
SMode_Subtract: SelectionMode
TCGEReason_Unknown: TrackFromClipGroupExclusionReason
TCGEReason_TrackTypeIsNotAllowed: TrackFromClipGroupExclusionReason
TCGEReason_TrackIsFrozen: TrackFromClipGroupExclusionReason
TCGEReason_TrackIsClosed: TrackFromClipGroupExclusionReason
TCGEReason_TrackIsLocked: TrackFromClipGroupExclusionReason
TCGEReason_TrackIsInPlaylistView: TrackFromClipGroupExclusionReason
TCGEReason_TrackIsElasticAudioWithFades: TrackFromClipGroupExclusionReason
TLType_Unknown: TimelineLocationType
TLType_Samples: TimelineLocationType
TLType_Ticks: TimelineLocationType
TLType_Frames: TimelineLocationType
TLType_MinSecs: TimelineLocationType
TLType_TimeCode: TimelineLocationType
TLType_BarsBeats: TimelineLocationType
TLType_FeetFrames: TimelineLocationType
TLType_Seconds: TimelineLocationType
BTType_Unknown: BasicTimeType
BTType_Samples: BasicTimeType
BTType_Ticks: BasicTimeType
BTType_Frames: BasicTimeType
ClipType_Unknown: ClipType
ClipType_Audio: ClipType
ClipType_Midi: ClipType
ClipType_Video: ClipType
ClipType_AudioClipGroup: ClipType
ClipType_MidiClipGroup: ClipType
ClipType_VideoClipGroup: ClipType
ClipType_MixedClipGroup: ClipType
SFormat_Unknown: StemFormat
SFormat_Mono: StemFormat
SFormat_Stereo: StemFormat
SFormat_LCR: StemFormat
SFormat_LCRS: StemFormat
SFormat_Quad: StemFormat
SFormat_5_0: StemFormat
SFormat_5_1: StemFormat
SFormat_5_0_2: StemFormat
SFormat_5_1_2: StemFormat
SFormat_5_0_4: StemFormat
SFormat_5_1_4: StemFormat
SFormat_6_0: StemFormat
SFormat_6_1: StemFormat
SFormat_7_0: StemFormat
SFormat_7_1: StemFormat
SFormat_7_0_SDDS: StemFormat
SFormat_7_1_SDDS: StemFormat
SFormat_7_0_2: StemFormat
SFormat_7_1_2: StemFormat
SFormat_7_0_4: StemFormat
SFormat_7_1_4: StemFormat
SFormat_7_0_6: StemFormat
SFormat_7_1_6: StemFormat
SFormat_9_0_4: StemFormat
SFormat_9_1_4: StemFormat
SFormat_9_0_6: StemFormat
SFormat_9_1_6: StemFormat
SFormat_1stOrderAmbisonics: StemFormat
SFormat_2ndOrderAmbisonics: StemFormat
SFormat_3rdOrderAmbisonics: StemFormat
SFormat_4thOrderAmbisonics: StemFormat
SFormat_5thOrderAmbisonics: StemFormat
SFormat_6thOrderAmbisonics: StemFormat
SFormat_7thOrderAmbisonics: StemFormat
SFormat_None: StemFormat
SFormat_2_1: StemFormat
SFormat_Overhead: StemFormat
SChannel_Unknown: StemChannel
SChannel_Mono: StemChannel
SChannel_Left: StemChannel
SChannel_Right: StemChannel
SChannel_Center: StemChannel
SChannel_LeftSurround: StemChannel
SChannel_CenterSurround: StemChannel
SChannel_RightSurround: StemChannel
SChannel_Surround: StemChannel
SChannel_LeftCenter: StemChannel
SChannel_RightCenter: StemChannel
SChannel_LeftSide: StemChannel
SChannel_RightSide: StemChannel
SChannel_LeftFrontHeight: StemChannel
SChannel_RightFrontHeight: StemChannel
SChannel_LeftTopMiddle: StemChannel
SChannel_RightTopMiddle: StemChannel
SChannel_LeftTopFront: StemChannel
SChannel_RightTopFront: StemChannel
SChannel_LeftTopRear: StemChannel
SChannel_RightTopRear: StemChannel
SChannel_LeftWide: StemChannel
SChannel_RightWide: StemChannel
SChannel_LFE: StemChannel
SChannel_0: StemChannel
SChannel_1: StemChannel
SChannel_2: StemChannel
SChannel_3: StemChannel
SChannel_4: StemChannel
SChannel_5: StemChannel
SChannel_6: StemChannel
SChannel_7: StemChannel
SChannel_8: StemChannel
SChannel_9: StemChannel
SChannel_10: StemChannel
SChannel_11: StemChannel
SChannel_12: StemChannel
SChannel_13: StemChannel
SChannel_14: StemChannel
SChannel_15: StemChannel
SChannel_16: StemChannel
SChannel_17: StemChannel
SChannel_18: StemChannel
SChannel_19: StemChannel
SChannel_20: StemChannel
SChannel_21: StemChannel
SChannel_22: StemChannel
SChannel_23: StemChannel
SChannel_24: StemChannel
SChannel_25: StemChannel
SChannel_26: StemChannel
SChannel_27: StemChannel
SChannel_28: StemChannel
SChannel_29: StemChannel
SChannel_30: StemChannel
SChannel_31: StemChannel
SChannel_32: StemChannel
SChannel_33: StemChannel
SChannel_34: StemChannel
SChannel_35: StemChannel
SChannel_36: StemChannel
SChannel_37: StemChannel
SChannel_38: StemChannel
SChannel_39: StemChannel
SChannel_40: StemChannel
SChannel_41: StemChannel
SChannel_42: StemChannel
SChannel_43: StemChannel
SChannel_44: StemChannel
SChannel_45: StemChannel
SChannel_46: StemChannel
SChannel_47: StemChannel
SChannel_48: StemChannel
SChannel_49: StemChannel
SChannel_50: StemChannel
SChannel_51: StemChannel
SChannel_52: StemChannel
SChannel_53: StemChannel
SChannel_54: StemChannel
SChannel_55: StemChannel
SChannel_56: StemChannel
SChannel_57: StemChannel
SChannel_58: StemChannel
SChannel_59: StemChannel
SChannel_60: StemChannel
SChannel_61: StemChannel
SChannel_62: StemChannel
SChannel_63: StemChannel
BatchJobStatus_Unknown: BatchJobStatus
BatchJobStatus_Pending: BatchJobStatus
BatchJobStatus_Running: BatchJobStatus
BatchJobStatus_Completed: BatchJobStatus
BatchJobStatus_TimedOut: BatchJobStatus
BatchJobStatus_Failed: BatchJobStatus
BatchJobStatus_Canceled: BatchJobStatus

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
    __slots__ = ("task_id", "command", "version", "session_id", "version_minor", "version_revision", "versioned_request_header_json")
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_MINOR_FIELD_NUMBER: _ClassVar[int]
    VERSION_REVISION_FIELD_NUMBER: _ClassVar[int]
    VERSIONED_REQUEST_HEADER_JSON_FIELD_NUMBER: _ClassVar[int]
    task_id: str
    command: CommandId
    version: int
    session_id: str
    version_minor: int
    version_revision: int
    versioned_request_header_json: str
    def __init__(self, task_id: _Optional[str] = ..., command: _Optional[_Union[CommandId, str]] = ..., version: _Optional[int] = ..., session_id: _Optional[str] = ..., version_minor: _Optional[int] = ..., version_revision: _Optional[int] = ..., versioned_request_header_json: _Optional[str] = ...) -> None: ...

class VersionedRequestHeader(_message.Message):
    __slots__ = ("batch_job_header",)
    BATCH_JOB_HEADER_FIELD_NUMBER: _ClassVar[int]
    batch_job_header: BatchJobRequestHeaderData
    def __init__(self, batch_job_header: _Optional[_Union[BatchJobRequestHeaderData, _Mapping]] = ...) -> None: ...

class Request(_message.Message):
    __slots__ = ("header", "request_body_json")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    REQUEST_BODY_JSON_FIELD_NUMBER: _ClassVar[int]
    header: RequestHeader
    request_body_json: str
    def __init__(self, header: _Optional[_Union[RequestHeader, _Mapping]] = ..., request_body_json: _Optional[str] = ...) -> None: ...

class ResponseHeader(_message.Message):
    __slots__ = ("task_id", "command", "status", "progress", "version", "version_minor", "version_revision", "versioned_response_header_json")
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    VERSION_MINOR_FIELD_NUMBER: _ClassVar[int]
    VERSION_REVISION_FIELD_NUMBER: _ClassVar[int]
    VERSIONED_RESPONSE_HEADER_JSON_FIELD_NUMBER: _ClassVar[int]
    task_id: str
    command: CommandId
    status: TaskStatus
    progress: int
    version: int
    version_minor: int
    version_revision: int
    versioned_response_header_json: str
    def __init__(self, task_id: _Optional[str] = ..., command: _Optional[_Union[CommandId, str]] = ..., status: _Optional[_Union[TaskStatus, str]] = ..., progress: _Optional[int] = ..., version: _Optional[int] = ..., version_minor: _Optional[int] = ..., version_revision: _Optional[int] = ..., versioned_response_header_json: _Optional[str] = ...) -> None: ...

class VersionedResponseHeader(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Response(_message.Message):
    __slots__ = ("header", "response_body_json", "response_error_json")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_BODY_JSON_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_ERROR_JSON_FIELD_NUMBER: _ClassVar[int]
    header: ResponseHeader
    response_body_json: str
    response_error_json: str
    def __init__(self, header: _Optional[_Union[ResponseHeader, _Mapping]] = ..., response_body_json: _Optional[str] = ..., response_error_json: _Optional[str] = ...) -> None: ...

class EventRequestData(_message.Message):
    __slots__ = ("event_id", "event_data_json")
    EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    EVENT_DATA_JSON_FIELD_NUMBER: _ClassVar[int]
    event_id: EventId
    event_data_json: str
    def __init__(self, event_id: _Optional[_Union[EventId, str]] = ..., event_data_json: _Optional[str] = ...) -> None: ...

class EventResponseData(_message.Message):
    __slots__ = ("event_id", "event_data_json")
    EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    EVENT_DATA_JSON_FIELD_NUMBER: _ClassVar[int]
    event_id: EventId
    event_data_json: str
    def __init__(self, event_id: _Optional[_Union[EventId, str]] = ..., event_data_json: _Optional[str] = ...) -> None: ...

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
    __slots__ = ("is_inactive", "is_hidden", "is_selected", "contains_clips", "contains_automation", "is_soloed", "is_record_enabled", "is_input_monitoring_on", "is_smart_dsp_on", "is_locked", "is_muted", "is_frozen", "is_open", "is_online", "is_record_enabled_safe", "is_smart_dsp_on_safe", "is_soloed_safe", "has_edit_selection")
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
    HAS_EDIT_SELECTION_FIELD_NUMBER: _ClassVar[int]
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
    has_edit_selection: TrackAttributeState
    def __init__(self, is_inactive: _Optional[_Union[TrackAttributeState, str]] = ..., is_hidden: _Optional[_Union[TrackAttributeState, str]] = ..., is_selected: _Optional[_Union[TrackAttributeState, str]] = ..., contains_clips: bool = ..., contains_automation: bool = ..., is_soloed: bool = ..., is_record_enabled: bool = ..., is_input_monitoring_on: _Optional[_Union[TrackAttributeState, str]] = ..., is_smart_dsp_on: bool = ..., is_locked: bool = ..., is_muted: bool = ..., is_frozen: bool = ..., is_open: bool = ..., is_online: bool = ..., is_record_enabled_safe: bool = ..., is_smart_dsp_on_safe: bool = ..., is_soloed_safe: bool = ..., has_edit_selection: _Optional[_Union[TrackAttributeState, str]] = ...) -> None: ...

class Track(_message.Message):
    __slots__ = ("name", "type", "id", "index", "color", "track_attributes", "id_compressed", "format", "timebase", "parent_folder_name", "parent_folder_id")
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    TRACK_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    ID_COMPRESSED_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    TIMEBASE_FIELD_NUMBER: _ClassVar[int]
    PARENT_FOLDER_NAME_FIELD_NUMBER: _ClassVar[int]
    PARENT_FOLDER_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    type: TrackType
    id: str
    index: int
    color: str
    track_attributes: TrackAttributes
    id_compressed: str
    format: TrackFormat
    timebase: TrackTimebase
    parent_folder_name: str
    parent_folder_id: str
    def __init__(self, name: _Optional[str] = ..., type: _Optional[_Union[TrackType, str]] = ..., id: _Optional[str] = ..., index: _Optional[int] = ..., color: _Optional[str] = ..., track_attributes: _Optional[_Union[TrackAttributes, _Mapping]] = ..., id_compressed: _Optional[str] = ..., format: _Optional[_Union[TrackFormat, str]] = ..., timebase: _Optional[_Union[TrackTimebase, str]] = ..., parent_folder_name: _Optional[str] = ..., parent_folder_id: _Optional[str] = ...) -> None: ...

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

class OpenSessionBehaviorOptions(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class OpenSessionRequestBody(_message.Message):
    __slots__ = ("session_path", "behavior_options")
    SESSION_PATH_FIELD_NUMBER: _ClassVar[int]
    BEHAVIOR_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    session_path: str
    behavior_options: OpenSessionBehaviorOptions
    def __init__(self, session_path: _Optional[str] = ..., behavior_options: _Optional[_Union[OpenSessionBehaviorOptions, _Mapping]] = ...) -> None: ...

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
    __slots__ = ("location_type", "location_value", "location_options", "location")
    LOCATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    LOCATION_VALUE_FIELD_NUMBER: _ClassVar[int]
    LOCATION_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    location_type: SpotLocationType
    location_value: str
    location_options: TrackOffsetOptions
    location: TimelineLocation
    def __init__(self, location_type: _Optional[_Union[SpotLocationType, str]] = ..., location_value: _Optional[str] = ..., location_options: _Optional[_Union[TrackOffsetOptions, str]] = ..., location: _Optional[_Union[TimelineLocation, _Mapping]] = ...) -> None: ...

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
    __slots__ = ("path", "info", "file_id")
    PATH_FIELD_NUMBER: _ClassVar[int]
    INFO_FIELD_NUMBER: _ClassVar[int]
    FILE_ID_FIELD_NUMBER: _ClassVar[int]
    path: str
    info: FileLocationInfo
    file_id: str
    def __init__(self, path: _Optional[str] = ..., info: _Optional[_Union[FileLocationInfo, _Mapping]] = ..., file_id: _Optional[str] = ...) -> None: ...

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

class MP3EncodingOptions(_message.Message):
    __slots__ = ("bit_rate", "quality")
    BIT_RATE_FIELD_NUMBER: _ClassVar[int]
    QUALITY_FIELD_NUMBER: _ClassVar[int]
    bit_rate: MP3EncodingOptionsConstantBitRate
    quality: MP3EncodingOptionsQuality
    def __init__(self, bit_rate: _Optional[_Union[MP3EncodingOptionsConstantBitRate, str]] = ..., quality: _Optional[_Union[MP3EncodingOptionsQuality, str]] = ...) -> None: ...

class AudioEncodingOptions(_message.Message):
    __slots__ = ("encoding_options_mp3",)
    ENCODING_OPTIONS_MP3_FIELD_NUMBER: _ClassVar[int]
    encoding_options_mp3: MP3EncodingOptions
    def __init__(self, encoding_options_mp3: _Optional[_Union[MP3EncodingOptions, _Mapping]] = ...) -> None: ...

class ExportMixRequestBody(_message.Message):
    __slots__ = ("preset_path", "file_name", "file_type", "files_list", "audio_info", "video_info", "location_info", "dolby_atmos_info", "offline_bounce", "mix_source_list", "audio_encoding_options", "start_time", "end_time")
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
    AUDIO_ENCODING_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
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
    audio_encoding_options: AudioEncodingOptions
    start_time: TimelineLocation
    end_time: TimelineLocation
    def __init__(self, preset_path: _Optional[str] = ..., file_name: _Optional[str] = ..., file_type: _Optional[_Union[EM_FileType, str]] = ..., files_list: _Optional[_Iterable[_Union[EM_SourceInfo, _Mapping]]] = ..., audio_info: _Optional[_Union[EM_AudioInfo, _Mapping]] = ..., video_info: _Optional[_Union[EM_VideoInfo, _Mapping]] = ..., location_info: _Optional[_Union[EM_LocationInfo, _Mapping]] = ..., dolby_atmos_info: _Optional[_Union[EM_DolbyAtmosInfo, _Mapping]] = ..., offline_bounce: _Optional[_Union[TripleBool, str]] = ..., mix_source_list: _Optional[_Iterable[_Union[EM_SourceInfo, _Mapping]]] = ..., audio_encoding_options: _Optional[_Union[AudioEncodingOptions, _Mapping]] = ..., start_time: _Optional[_Union[TimelineLocation, _Mapping]] = ..., end_time: _Optional[_Union[TimelineLocation, _Mapping]] = ...) -> None: ...

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
    __slots__ = ("include_file_list", "include_clip_list", "include_markers", "include_plugin_list", "include_track_edls", "show_sub_frames", "include_user_timestamps", "track_list_type", "fade_handling_type", "track_offset_options", "text_as_file_format", "output_type", "output_path", "location_type")
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
    LOCATION_TYPE_FIELD_NUMBER: _ClassVar[int]
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
    location_type: TimelineLocationType
    def __init__(self, include_file_list: bool = ..., include_clip_list: bool = ..., include_markers: bool = ..., include_plugin_list: bool = ..., include_track_edls: bool = ..., show_sub_frames: bool = ..., include_user_timestamps: bool = ..., track_list_type: _Optional[_Union[TrackListType, str]] = ..., fade_handling_type: _Optional[_Union[FadeHandlingType, str]] = ..., track_offset_options: _Optional[_Union[TrackOffsetOptions, str]] = ..., text_as_file_format: _Optional[_Union[TextAsFileFormat, str]] = ..., output_type: _Optional[_Union[ESI_OutputType, str]] = ..., output_path: _Optional[str] = ..., location_type: _Optional[_Union[TimelineLocationType, str]] = ...) -> None: ...

class ExportSessionInfoAsTextResponseBody(_message.Message):
    __slots__ = ("session_info",)
    SESSION_INFO_FIELD_NUMBER: _ClassVar[int]
    session_info: str
    def __init__(self, session_info: _Optional[str] = ...) -> None: ...

class SetPlaybackModeRequestBody(_message.Message):
    __slots__ = ("playback_mode",)
    PLAYBACK_MODE_FIELD_NUMBER: _ClassVar[int]
    playback_mode: PlaybackMode
    def __init__(self, playback_mode: _Optional[_Union[PlaybackMode, str]] = ...) -> None: ...

class SetPlaybackModeResponseBody(_message.Message):
    __slots__ = ("current_playback_mode", "playback_mode_list")
    CURRENT_PLAYBACK_MODE_FIELD_NUMBER: _ClassVar[int]
    PLAYBACK_MODE_LIST_FIELD_NUMBER: _ClassVar[int]
    current_playback_mode: PlaybackMode
    playback_mode_list: _containers.RepeatedScalarFieldContainer[PlaybackMode]
    def __init__(self, current_playback_mode: _Optional[_Union[PlaybackMode, str]] = ..., playback_mode_list: _Optional[_Iterable[_Union[PlaybackMode, str]]] = ...) -> None: ...

class SetRecordModeRequestBody(_message.Message):
    __slots__ = ("record_mode", "record_arm_transport")
    RECORD_MODE_FIELD_NUMBER: _ClassVar[int]
    RECORD_ARM_TRANSPORT_FIELD_NUMBER: _ClassVar[int]
    record_mode: RecordMode
    record_arm_transport: bool
    def __init__(self, record_mode: _Optional[_Union[RecordMode, str]] = ..., record_arm_transport: bool = ...) -> None: ...

class SetRecordModeResponseBody(_message.Message):
    __slots__ = ("current_record_mode", "record_mode_list")
    CURRENT_RECORD_MODE_FIELD_NUMBER: _ClassVar[int]
    RECORD_MODE_LIST_FIELD_NUMBER: _ClassVar[int]
    current_record_mode: RecordMode
    record_mode_list: _containers.RepeatedScalarFieldContainer[RecordMode]
    def __init__(self, current_record_mode: _Optional[_Union[RecordMode, str]] = ..., record_mode_list: _Optional[_Iterable[_Union[RecordMode, str]]] = ...) -> None: ...

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
    __slots__ = ("session_start_time", "track_offset_opts", "maintain_relative_position", "location")
    SESSION_START_TIME_FIELD_NUMBER: _ClassVar[int]
    TRACK_OFFSET_OPTS_FIELD_NUMBER: _ClassVar[int]
    MAINTAIN_RELATIVE_POSITION_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    session_start_time: str
    track_offset_opts: TrackOffsetOptions
    maintain_relative_position: bool
    location: TimelineLocation
    def __init__(self, session_start_time: _Optional[str] = ..., track_offset_opts: _Optional[_Union[TrackOffsetOptions, str]] = ..., maintain_relative_position: bool = ..., location: _Optional[_Union[TimelineLocation, _Mapping]] = ...) -> None: ...

class SetSessionLengthRequestBody(_message.Message):
    __slots__ = ("session_length",)
    SESSION_LENGTH_FIELD_NUMBER: _ClassVar[int]
    session_length: str
    def __init__(self, session_length: _Optional[str] = ...) -> None: ...

class GetPTSLVersionResponseBody(_message.Message):
    __slots__ = ("version", "version_minor", "version_revision")
    VERSION_FIELD_NUMBER: _ClassVar[int]
    VERSION_MINOR_FIELD_NUMBER: _ClassVar[int]
    VERSION_REVISION_FIELD_NUMBER: _ClassVar[int]
    version: int
    version_minor: int
    version_revision: int
    def __init__(self, version: _Optional[int] = ..., version_minor: _Optional[int] = ..., version_revision: _Optional[int] = ...) -> None: ...

class GetPlaybackModeResponseBody(_message.Message):
    __slots__ = ("current_settings", "possible_settings")
    CURRENT_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    POSSIBLE_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    current_settings: _containers.RepeatedScalarFieldContainer[PlaybackMode]
    possible_settings: _containers.RepeatedScalarFieldContainer[PlaybackMode]
    def __init__(self, current_settings: _Optional[_Iterable[_Union[PlaybackMode, str]]] = ..., possible_settings: _Optional[_Iterable[_Union[PlaybackMode, str]]] = ...) -> None: ...

class GetRecordModeResponseBody(_message.Message):
    __slots__ = ("current_setting", "possible_settings")
    CURRENT_SETTING_FIELD_NUMBER: _ClassVar[int]
    POSSIBLE_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    current_setting: RecordMode
    possible_settings: _containers.RepeatedScalarFieldContainer[RecordMode]
    def __init__(self, current_setting: _Optional[_Union[RecordMode, str]] = ..., possible_settings: _Optional[_Iterable[_Union[RecordMode, str]]] = ...) -> None: ...

class GetTransportStateResponseBody(_message.Message):
    __slots__ = ("current_setting", "possible_settings")
    CURRENT_SETTING_FIELD_NUMBER: _ClassVar[int]
    POSSIBLE_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    current_setting: TransportState
    possible_settings: _containers.RepeatedScalarFieldContainer[TransportState]
    def __init__(self, current_setting: _Optional[_Union[TransportState, str]] = ..., possible_settings: _Optional[_Iterable[_Union[TransportState, str]]] = ...) -> None: ...

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
    clip_location: ClipLocation
    new_name: str
    rename_file: bool
    def __init__(self, clip_location: _Optional[_Union[ClipLocation, str]] = ..., new_name: _Optional[str] = ..., rename_file: bool = ...) -> None: ...

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
    __slots__ = ("number_of_tracks", "created_track_names", "pagination_response", "created_track_ids")
    NUMBER_OF_TRACKS_FIELD_NUMBER: _ClassVar[int]
    CREATED_TRACK_NAMES_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    CREATED_TRACK_IDS_FIELD_NUMBER: _ClassVar[int]
    number_of_tracks: int
    created_track_names: _containers.RepeatedScalarFieldContainer[str]
    pagination_response: PaginationResponse
    created_track_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, number_of_tracks: _Optional[int] = ..., created_track_names: _Optional[_Iterable[str]] = ..., pagination_response: _Optional[_Union[PaginationResponse, _Mapping]] = ..., created_track_ids: _Optional[_Iterable[str]] = ...) -> None: ...

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
    __slots__ = ("play_start_marker_time", "in_time", "out_time", "pre_roll_start_time", "post_roll_stop_time", "pre_roll_enabled", "post_roll_enabled", "update_video_to", "propagate_to_satellites", "location_type")
    PLAY_START_MARKER_TIME_FIELD_NUMBER: _ClassVar[int]
    IN_TIME_FIELD_NUMBER: _ClassVar[int]
    OUT_TIME_FIELD_NUMBER: _ClassVar[int]
    PRE_ROLL_START_TIME_FIELD_NUMBER: _ClassVar[int]
    POST_ROLL_STOP_TIME_FIELD_NUMBER: _ClassVar[int]
    PRE_ROLL_ENABLED_FIELD_NUMBER: _ClassVar[int]
    POST_ROLL_ENABLED_FIELD_NUMBER: _ClassVar[int]
    UPDATE_VIDEO_TO_FIELD_NUMBER: _ClassVar[int]
    PROPAGATE_TO_SATELLITES_FIELD_NUMBER: _ClassVar[int]
    LOCATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    play_start_marker_time: str
    in_time: str
    out_time: str
    pre_roll_start_time: str
    post_roll_stop_time: str
    pre_roll_enabled: TripleBool
    post_roll_enabled: TripleBool
    update_video_to: TimelineUpdateVideo
    propagate_to_satellites: TripleBool
    location_type: TimelineLocationType
    def __init__(self, play_start_marker_time: _Optional[str] = ..., in_time: _Optional[str] = ..., out_time: _Optional[str] = ..., pre_roll_start_time: _Optional[str] = ..., post_roll_stop_time: _Optional[str] = ..., pre_roll_enabled: _Optional[_Union[TripleBool, str]] = ..., post_roll_enabled: _Optional[_Union[TripleBool, str]] = ..., update_video_to: _Optional[_Union[TimelineUpdateVideo, str]] = ..., propagate_to_satellites: _Optional[_Union[TripleBool, str]] = ..., location_type: _Optional[_Union[TimelineLocationType, str]] = ...) -> None: ...

class GetTimelineSelectionRequestBody(_message.Message):
    __slots__ = ("time_scale", "location_type")
    TIME_SCALE_FIELD_NUMBER: _ClassVar[int]
    LOCATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    time_scale: TrackOffsetOptions
    location_type: TimelineLocationType
    def __init__(self, time_scale: _Optional[_Union[TrackOffsetOptions, str]] = ..., location_type: _Optional[_Union[TimelineLocationType, str]] = ...) -> None: ...

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
    __slots__ = ("time_scale", "location_type")
    TIME_SCALE_FIELD_NUMBER: _ClassVar[int]
    LOCATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    time_scale: TrackOffsetOptions
    location_type: TimelineLocationType
    def __init__(self, time_scale: _Optional[_Union[TrackOffsetOptions, str]] = ..., location_type: _Optional[_Union[TimelineLocationType, str]] = ...) -> None: ...

class SetSubCounterFormatRequestBody(_message.Message):
    __slots__ = ("time_scale", "location_type")
    TIME_SCALE_FIELD_NUMBER: _ClassVar[int]
    LOCATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    time_scale: TrackOffsetOptions
    location_type: TimelineLocationType
    def __init__(self, time_scale: _Optional[_Union[TrackOffsetOptions, str]] = ..., location_type: _Optional[_Union[TimelineLocationType, str]] = ...) -> None: ...

class GetMainCounterFormatResponseBody(_message.Message):
    __slots__ = ("current_setting", "possible_settings", "current_type", "possible_types")
    CURRENT_SETTING_FIELD_NUMBER: _ClassVar[int]
    POSSIBLE_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    CURRENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    POSSIBLE_TYPES_FIELD_NUMBER: _ClassVar[int]
    current_setting: TrackOffsetOptions
    possible_settings: _containers.RepeatedScalarFieldContainer[TrackOffsetOptions]
    current_type: TimelineLocationType
    possible_types: _containers.RepeatedScalarFieldContainer[TimelineLocationType]
    def __init__(self, current_setting: _Optional[_Union[TrackOffsetOptions, str]] = ..., possible_settings: _Optional[_Iterable[_Union[TrackOffsetOptions, str]]] = ..., current_type: _Optional[_Union[TimelineLocationType, str]] = ..., possible_types: _Optional[_Iterable[_Union[TimelineLocationType, str]]] = ...) -> None: ...

class GetSubCounterFormatResponseBody(_message.Message):
    __slots__ = ("current_setting", "possible_settings", "current_type", "possible_types")
    CURRENT_SETTING_FIELD_NUMBER: _ClassVar[int]
    POSSIBLE_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    CURRENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    POSSIBLE_TYPES_FIELD_NUMBER: _ClassVar[int]
    current_setting: TrackOffsetOptions
    possible_settings: _containers.RepeatedScalarFieldContainer[TrackOffsetOptions]
    current_type: TimelineLocationType
    possible_types: _containers.RepeatedScalarFieldContainer[TimelineLocationType]
    def __init__(self, current_setting: _Optional[_Union[TrackOffsetOptions, str]] = ..., possible_settings: _Optional[_Iterable[_Union[TrackOffsetOptions, str]]] = ..., current_type: _Optional[_Union[TimelineLocationType, str]] = ..., possible_types: _Optional[_Iterable[_Union[TimelineLocationType, str]]] = ...) -> None: ...

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

class TimelineLocation(_message.Message):
    __slots__ = ("location", "time_type")
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    TIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    location: str
    time_type: TimelineLocationType
    def __init__(self, location: _Optional[str] = ..., time_type: _Optional[_Union[TimelineLocationType, str]] = ...) -> None: ...

class MediaTimePosition(_message.Message):
    __slots__ = ("position", "time_type")
    POSITION_FIELD_NUMBER: _ClassVar[int]
    TIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    position: int
    time_type: BasicTimeType
    def __init__(self, position: _Optional[int] = ..., time_type: _Optional[_Union[BasicTimeType, str]] = ...) -> None: ...

class TimeLength(_message.Message):
    __slots__ = ("length", "time_type")
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    TIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    length: int
    time_type: BasicTimeType
    def __init__(self, length: _Optional[int] = ..., time_type: _Optional[_Union[BasicTimeType, str]] = ...) -> None: ...

class ClearAllMemoryLocationsResponseBody(_message.Message):
    __slots__ = ("success_count", "failure_count", "failure_list")
    SUCCESS_COUNT_FIELD_NUMBER: _ClassVar[int]
    FAILURE_COUNT_FIELD_NUMBER: _ClassVar[int]
    FAILURE_LIST_FIELD_NUMBER: _ClassVar[int]
    success_count: int
    failure_count: int
    failure_list: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, success_count: _Optional[int] = ..., failure_count: _Optional[int] = ..., failure_list: _Optional[_Iterable[int]] = ...) -> None: ...

class GetTimeAsTypeRequestBody(_message.Message):
    __slots__ = ("location", "time_type")
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    TIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    location: TimelineLocation
    time_type: TimelineLocationType
    def __init__(self, location: _Optional[_Union[TimelineLocation, _Mapping]] = ..., time_type: _Optional[_Union[TimelineLocationType, str]] = ...) -> None: ...

class GetTimeAsTypeResponseBody(_message.Message):
    __slots__ = ("converted_location",)
    CONVERTED_LOCATION_FIELD_NUMBER: _ClassVar[int]
    converted_location: TimelineLocation
    def __init__(self, converted_location: _Optional[_Union[TimelineLocation, _Mapping]] = ...) -> None: ...

class SubtractLocationsRequestBody(_message.Message):
    __slots__ = ("first_location", "second_location", "desired_length_type")
    FIRST_LOCATION_FIELD_NUMBER: _ClassVar[int]
    SECOND_LOCATION_FIELD_NUMBER: _ClassVar[int]
    DESIRED_LENGTH_TYPE_FIELD_NUMBER: _ClassVar[int]
    first_location: TimelineLocation
    second_location: TimelineLocation
    desired_length_type: BasicTimeType
    def __init__(self, first_location: _Optional[_Union[TimelineLocation, _Mapping]] = ..., second_location: _Optional[_Union[TimelineLocation, _Mapping]] = ..., desired_length_type: _Optional[_Union[BasicTimeType, str]] = ...) -> None: ...

class SubtractLocationsResponseBody(_message.Message):
    __slots__ = ("length",)
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    length: TimeLength
    def __init__(self, length: _Optional[_Union[TimeLength, _Mapping]] = ...) -> None: ...

class AddLengthToLocationRequestBody(_message.Message):
    __slots__ = ("location", "length")
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    location: TimelineLocation
    length: TimeLength
    def __init__(self, location: _Optional[_Union[TimelineLocation, _Mapping]] = ..., length: _Optional[_Union[TimeLength, _Mapping]] = ...) -> None: ...

class AddLengthToLocationResponseBody(_message.Message):
    __slots__ = ("result_location",)
    RESULT_LOCATION_FIELD_NUMBER: _ClassVar[int]
    result_location: TimelineLocation
    def __init__(self, result_location: _Optional[_Union[TimelineLocation, _Mapping]] = ...) -> None: ...

class SubtractPositionsRequestBody(_message.Message):
    __slots__ = ("first_position", "second_position")
    FIRST_POSITION_FIELD_NUMBER: _ClassVar[int]
    SECOND_POSITION_FIELD_NUMBER: _ClassVar[int]
    first_position: MediaTimePosition
    second_position: MediaTimePosition
    def __init__(self, first_position: _Optional[_Union[MediaTimePosition, _Mapping]] = ..., second_position: _Optional[_Union[MediaTimePosition, _Mapping]] = ...) -> None: ...

class SubtractPositionsResponseBody(_message.Message):
    __slots__ = ("length",)
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    length: TimeLength
    def __init__(self, length: _Optional[_Union[TimeLength, _Mapping]] = ...) -> None: ...

class AddLengthToPositionRequestBody(_message.Message):
    __slots__ = ("position", "length")
    POSITION_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    position: MediaTimePosition
    length: TimeLength
    def __init__(self, position: _Optional[_Union[MediaTimePosition, _Mapping]] = ..., length: _Optional[_Union[TimeLength, _Mapping]] = ...) -> None: ...

class AddLengthToPositionResponseBody(_message.Message):
    __slots__ = ("result_position",)
    RESULT_POSITION_FIELD_NUMBER: _ClassVar[int]
    result_position: MediaTimePosition
    def __init__(self, result_position: _Optional[_Union[MediaTimePosition, _Mapping]] = ...) -> None: ...

class ImportAudioToClipListResponseEntry(_message.Message):
    __slots__ = ("original_input_path", "destination_file_list")
    ORIGINAL_INPUT_PATH_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_FILE_LIST_FIELD_NUMBER: _ClassVar[int]
    original_input_path: str
    destination_file_list: _containers.RepeatedCompositeFieldContainer[ImportAudioToClipListResponseEntryFile]
    def __init__(self, original_input_path: _Optional[str] = ..., destination_file_list: _Optional[_Iterable[_Union[ImportAudioToClipListResponseEntryFile, _Mapping]]] = ...) -> None: ...

class ImportAudioToClipListResponseEntryFile(_message.Message):
    __slots__ = ("file_id", "file_path", "clip_id_list")
    FILE_ID_FIELD_NUMBER: _ClassVar[int]
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    CLIP_ID_LIST_FIELD_NUMBER: _ClassVar[int]
    file_id: str
    file_path: str
    clip_id_list: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, file_id: _Optional[str] = ..., file_path: _Optional[str] = ..., clip_id_list: _Optional[_Iterable[str]] = ...) -> None: ...

class ImportAudioToClipListRequestBody(_message.Message):
    __slots__ = ("file_list", "audio_operations", "destination_path")
    FILE_LIST_FIELD_NUMBER: _ClassVar[int]
    AUDIO_OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_PATH_FIELD_NUMBER: _ClassVar[int]
    file_list: _containers.RepeatedScalarFieldContainer[str]
    audio_operations: AudioOperations
    destination_path: str
    def __init__(self, file_list: _Optional[_Iterable[str]] = ..., audio_operations: _Optional[_Union[AudioOperations, str]] = ..., destination_path: _Optional[str] = ...) -> None: ...

class ImportAudioToClipListResponseBody(_message.Message):
    __slots__ = ("file_list", "failure_list")
    FILE_LIST_FIELD_NUMBER: _ClassVar[int]
    FAILURE_LIST_FIELD_NUMBER: _ClassVar[int]
    file_list: _containers.RepeatedCompositeFieldContainer[ImportAudioToClipListResponseEntry]
    failure_list: _containers.RepeatedCompositeFieldContainer[ImportFailureInfo]
    def __init__(self, file_list: _Optional[_Iterable[_Union[ImportAudioToClipListResponseEntry, _Mapping]]] = ..., failure_list: _Optional[_Iterable[_Union[ImportFailureInfo, _Mapping]]] = ...) -> None: ...

class ClipInstanceAttributes(_message.Message):
    __slots__ = ("color_index",)
    COLOR_INDEX_FIELD_NUMBER: _ClassVar[int]
    color_index: int
    def __init__(self, color_index: _Optional[int] = ...) -> None: ...

class SpotClipsByIDRequestBody(_message.Message):
    __slots__ = ("src_clips", "dst_track_id", "dst_track_name", "dst_location_data", "clip_instance_attributes")
    SRC_CLIPS_FIELD_NUMBER: _ClassVar[int]
    DST_TRACK_ID_FIELD_NUMBER: _ClassVar[int]
    DST_TRACK_NAME_FIELD_NUMBER: _ClassVar[int]
    DST_LOCATION_DATA_FIELD_NUMBER: _ClassVar[int]
    CLIP_INSTANCE_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    src_clips: _containers.RepeatedScalarFieldContainer[str]
    dst_track_id: str
    dst_track_name: str
    dst_location_data: SpotLocationData
    clip_instance_attributes: ClipInstanceAttributes
    def __init__(self, src_clips: _Optional[_Iterable[str]] = ..., dst_track_id: _Optional[str] = ..., dst_track_name: _Optional[str] = ..., dst_location_data: _Optional[_Union[SpotLocationData, _Mapping]] = ..., clip_instance_attributes: _Optional[_Union[ClipInstanceAttributes, _Mapping]] = ...) -> None: ...

class Clip(_message.Message):
    __slots__ = ("file_id", "clip_id", "clip_full_name", "clip_root_name", "clip_type", "start_point", "end_point", "sync_point", "group_name", "src_start_point", "src_end_point", "transpose_semitones", "transpose_cents")
    FILE_ID_FIELD_NUMBER: _ClassVar[int]
    CLIP_ID_FIELD_NUMBER: _ClassVar[int]
    CLIP_FULL_NAME_FIELD_NUMBER: _ClassVar[int]
    CLIP_ROOT_NAME_FIELD_NUMBER: _ClassVar[int]
    CLIP_TYPE_FIELD_NUMBER: _ClassVar[int]
    START_POINT_FIELD_NUMBER: _ClassVar[int]
    END_POINT_FIELD_NUMBER: _ClassVar[int]
    SYNC_POINT_FIELD_NUMBER: _ClassVar[int]
    GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    SRC_START_POINT_FIELD_NUMBER: _ClassVar[int]
    SRC_END_POINT_FIELD_NUMBER: _ClassVar[int]
    TRANSPOSE_SEMITONES_FIELD_NUMBER: _ClassVar[int]
    TRANSPOSE_CENTS_FIELD_NUMBER: _ClassVar[int]
    file_id: str
    clip_id: str
    clip_full_name: str
    clip_root_name: str
    clip_type: ClipType
    start_point: MediaTimePosition
    end_point: MediaTimePosition
    sync_point: MediaTimePosition
    group_name: str
    src_start_point: MediaTimePosition
    src_end_point: MediaTimePosition
    transpose_semitones: int
    transpose_cents: int
    def __init__(self, file_id: _Optional[str] = ..., clip_id: _Optional[str] = ..., clip_full_name: _Optional[str] = ..., clip_root_name: _Optional[str] = ..., clip_type: _Optional[_Union[ClipType, str]] = ..., start_point: _Optional[_Union[MediaTimePosition, _Mapping]] = ..., end_point: _Optional[_Union[MediaTimePosition, _Mapping]] = ..., sync_point: _Optional[_Union[MediaTimePosition, _Mapping]] = ..., group_name: _Optional[str] = ..., src_start_point: _Optional[_Union[MediaTimePosition, _Mapping]] = ..., src_end_point: _Optional[_Union[MediaTimePosition, _Mapping]] = ..., transpose_semitones: _Optional[int] = ..., transpose_cents: _Optional[int] = ...) -> None: ...

class GetClipListRequestBody(_message.Message):
    __slots__ = ("pagination_request",)
    PAGINATION_REQUEST_FIELD_NUMBER: _ClassVar[int]
    pagination_request: PaginationRequest
    def __init__(self, pagination_request: _Optional[_Union[PaginationRequest, _Mapping]] = ...) -> None: ...

class GetClipListResponseBody(_message.Message):
    __slots__ = ("clips", "pagination_response")
    CLIPS_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    clips: _containers.RepeatedCompositeFieldContainer[Clip]
    pagination_response: PaginationResponse
    def __init__(self, clips: _Optional[_Iterable[_Union[Clip, _Mapping]]] = ..., pagination_response: _Optional[_Union[PaginationResponse, _Mapping]] = ...) -> None: ...

class AudioFileInfo(_message.Message):
    __slots__ = ("file_id", "num_channels", "sample_rate", "encoding", "file_type", "smpte_uid", "protools_umid", "original_timestamp", "user_timestamp", "length", "stem_format")
    FILE_ID_FIELD_NUMBER: _ClassVar[int]
    NUM_CHANNELS_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_RATE_FIELD_NUMBER: _ClassVar[int]
    ENCODING_FIELD_NUMBER: _ClassVar[int]
    FILE_TYPE_FIELD_NUMBER: _ClassVar[int]
    SMPTE_UID_FIELD_NUMBER: _ClassVar[int]
    PROTOOLS_UMID_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    USER_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    STEM_FORMAT_FIELD_NUMBER: _ClassVar[int]
    file_id: str
    num_channels: int
    sample_rate: SampleRate
    encoding: BitDepth
    file_type: FileType
    smpte_uid: str
    protools_umid: str
    original_timestamp: TimelineLocation
    user_timestamp: TimelineLocation
    length: TimeLength
    stem_format: StemFormat
    def __init__(self, file_id: _Optional[str] = ..., num_channels: _Optional[int] = ..., sample_rate: _Optional[_Union[SampleRate, str]] = ..., encoding: _Optional[_Union[BitDepth, str]] = ..., file_type: _Optional[_Union[FileType, str]] = ..., smpte_uid: _Optional[str] = ..., protools_umid: _Optional[str] = ..., original_timestamp: _Optional[_Union[TimelineLocation, _Mapping]] = ..., user_timestamp: _Optional[_Union[TimelineLocation, _Mapping]] = ..., length: _Optional[_Union[TimeLength, _Mapping]] = ..., stem_format: _Optional[_Union[StemFormat, str]] = ...) -> None: ...

class GetMediaFileInfoRequestBody(_message.Message):
    __slots__ = ("file_id",)
    FILE_ID_FIELD_NUMBER: _ClassVar[int]
    file_id: str
    def __init__(self, file_id: _Optional[str] = ...) -> None: ...

class GetMediaFileInfoResponseBody(_message.Message):
    __slots__ = ("audio_file_info",)
    AUDIO_FILE_INFO_FIELD_NUMBER: _ClassVar[int]
    audio_file_info: AudioFileInfo
    def __init__(self, audio_file_info: _Optional[_Union[AudioFileInfo, _Mapping]] = ...) -> None: ...

class StemChannelId(_message.Message):
    __slots__ = ("name", "index")
    NAME_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    name: StemChannel
    index: int
    def __init__(self, name: _Optional[_Union[StemChannel, str]] = ..., index: _Optional[int] = ...) -> None: ...

class CreateAudioClipRequestEntry(_message.Message):
    __slots__ = ("name", "channel_format", "original_timestamp", "user_timestamp", "clip_info")
    NAME_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_FORMAT_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    USER_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    CLIP_INFO_FIELD_NUMBER: _ClassVar[int]
    name: str
    channel_format: StemFormat
    original_timestamp: TimelineLocation
    user_timestamp: TimelineLocation
    clip_info: _containers.RepeatedCompositeFieldContainer[CreateAudioClipRequestEntryClipInfo]
    def __init__(self, name: _Optional[str] = ..., channel_format: _Optional[_Union[StemFormat, str]] = ..., original_timestamp: _Optional[_Union[TimelineLocation, _Mapping]] = ..., user_timestamp: _Optional[_Union[TimelineLocation, _Mapping]] = ..., clip_info: _Optional[_Iterable[_Union[CreateAudioClipRequestEntryClipInfo, _Mapping]]] = ...) -> None: ...

class CreateAudioClipResponseEntry(_message.Message):
    __slots__ = ("clip_ids",)
    CLIP_IDS_FIELD_NUMBER: _ClassVar[int]
    clip_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, clip_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class CreateAudioClipRequestEntryClipInfo(_message.Message):
    __slots__ = ("file_id", "src_start_point", "src_end_point", "src_sync_point", "src_channel", "dst_channel", "start_point", "end_point", "transpose_semitones", "transpose_cents")
    FILE_ID_FIELD_NUMBER: _ClassVar[int]
    SRC_START_POINT_FIELD_NUMBER: _ClassVar[int]
    SRC_END_POINT_FIELD_NUMBER: _ClassVar[int]
    SRC_SYNC_POINT_FIELD_NUMBER: _ClassVar[int]
    SRC_CHANNEL_FIELD_NUMBER: _ClassVar[int]
    DST_CHANNEL_FIELD_NUMBER: _ClassVar[int]
    START_POINT_FIELD_NUMBER: _ClassVar[int]
    END_POINT_FIELD_NUMBER: _ClassVar[int]
    TRANSPOSE_SEMITONES_FIELD_NUMBER: _ClassVar[int]
    TRANSPOSE_CENTS_FIELD_NUMBER: _ClassVar[int]
    file_id: str
    src_start_point: MediaTimePosition
    src_end_point: MediaTimePosition
    src_sync_point: MediaTimePosition
    src_channel: StemChannelId
    dst_channel: StemChannelId
    start_point: MediaTimePosition
    end_point: MediaTimePosition
    transpose_semitones: int
    transpose_cents: int
    def __init__(self, file_id: _Optional[str] = ..., src_start_point: _Optional[_Union[MediaTimePosition, _Mapping]] = ..., src_end_point: _Optional[_Union[MediaTimePosition, _Mapping]] = ..., src_sync_point: _Optional[_Union[MediaTimePosition, _Mapping]] = ..., src_channel: _Optional[_Union[StemChannelId, _Mapping]] = ..., dst_channel: _Optional[_Union[StemChannelId, _Mapping]] = ..., start_point: _Optional[_Union[MediaTimePosition, _Mapping]] = ..., end_point: _Optional[_Union[MediaTimePosition, _Mapping]] = ..., transpose_semitones: _Optional[int] = ..., transpose_cents: _Optional[int] = ...) -> None: ...

class CreateAudioClipsRequestBody(_message.Message):
    __slots__ = ("clip_list",)
    CLIP_LIST_FIELD_NUMBER: _ClassVar[int]
    clip_list: _containers.RepeatedCompositeFieldContainer[CreateAudioClipRequestEntry]
    def __init__(self, clip_list: _Optional[_Iterable[_Union[CreateAudioClipRequestEntry, _Mapping]]] = ...) -> None: ...

class CreateAudioClipsResponseBody(_message.Message):
    __slots__ = ("clip_list",)
    CLIP_LIST_FIELD_NUMBER: _ClassVar[int]
    clip_list: _containers.RepeatedCompositeFieldContainer[CreateAudioClipResponseEntry]
    def __init__(self, clip_list: _Optional[_Iterable[_Union[CreateAudioClipResponseEntry, _Mapping]]] = ...) -> None: ...

class BatchJobRequestHeaderData(_message.Message):
    __slots__ = ("id", "progress")
    ID_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    id: str
    progress: int
    def __init__(self, id: _Optional[str] = ..., progress: _Optional[int] = ...) -> None: ...

class BatchJobDefinition(_message.Message):
    __slots__ = ("name", "description", "timeout", "is_cancelable", "cancel_on_failure")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    IS_CANCELABLE_FIELD_NUMBER: _ClassVar[int]
    CANCEL_ON_FAILURE_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    timeout: int
    is_cancelable: bool
    cancel_on_failure: bool
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., timeout: _Optional[int] = ..., is_cancelable: bool = ..., cancel_on_failure: bool = ...) -> None: ...

class CreateBatchJobRequestBody(_message.Message):
    __slots__ = ("job",)
    JOB_FIELD_NUMBER: _ClassVar[int]
    job: BatchJobDefinition
    def __init__(self, job: _Optional[_Union[BatchJobDefinition, _Mapping]] = ...) -> None: ...

class CreateBatchJobResponseBody(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetExportMixSourceListRequestBody(_message.Message):
    __slots__ = ("type",)
    TYPE_FIELD_NUMBER: _ClassVar[int]
    type: EM_SourceType
    def __init__(self, type: _Optional[_Union[EM_SourceType, str]] = ...) -> None: ...

class GetExportMixSourceListResponseBody(_message.Message):
    __slots__ = ("source_list",)
    SOURCE_LIST_FIELD_NUMBER: _ClassVar[int]
    source_list: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, source_list: _Optional[_Iterable[str]] = ...) -> None: ...

class BeginScrubRequestBody(_message.Message):
    __slots__ = ("start_position",)
    START_POSITION_FIELD_NUMBER: _ClassVar[int]
    start_position: int
    def __init__(self, start_position: _Optional[int] = ...) -> None: ...

class ContinueScrubRequestBody(_message.Message):
    __slots__ = ("velocity",)
    VELOCITY_FIELD_NUMBER: _ClassVar[int]
    velocity: int
    def __init__(self, velocity: _Optional[int] = ...) -> None: ...

class ContinueScrubResponseBody(_message.Message):
    __slots__ = ("timeline_position",)
    TIMELINE_POSITION_FIELD_NUMBER: _ClassVar[int]
    timeline_position: TimelineLocation
    def __init__(self, timeline_position: _Optional[_Union[TimelineLocation, _Mapping]] = ...) -> None: ...

class EnableCueProVideoPlugInRequestBody(_message.Message):
    __slots__ = ("enable",)
    ENABLE_FIELD_NUMBER: _ClassVar[int]
    enable: bool
    def __init__(self, enable: bool = ...) -> None: ...

class UpdateVideoRequestBody(_message.Message):
    __slots__ = ("frame_position",)
    FRAME_POSITION_FIELD_NUMBER: _ClassVar[int]
    frame_position: int
    def __init__(self, frame_position: _Optional[int] = ...) -> None: ...

class GetMonitorOutputPathResponseBody(_message.Message):
    __slots__ = ("monitor_path",)
    MONITOR_PATH_FIELD_NUMBER: _ClassVar[int]
    monitor_path: str
    def __init__(self, monitor_path: _Optional[str] = ...) -> None: ...

class GetEditSelectionRequestBody(_message.Message):
    __slots__ = ("location_type",)
    LOCATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    location_type: TimelineLocationType
    def __init__(self, location_type: _Optional[_Union[TimelineLocationType, str]] = ...) -> None: ...

class GetEditSelectionResponseBody(_message.Message):
    __slots__ = ("in_time", "out_time")
    IN_TIME_FIELD_NUMBER: _ClassVar[int]
    OUT_TIME_FIELD_NUMBER: _ClassVar[int]
    in_time: str
    out_time: str
    def __init__(self, in_time: _Optional[str] = ..., out_time: _Optional[str] = ...) -> None: ...

class SubscribeToEventsRequestBody(_message.Message):
    __slots__ = ("events",)
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    events: _containers.RepeatedCompositeFieldContainer[EventRequestData]
    def __init__(self, events: _Optional[_Iterable[_Union[EventRequestData, _Mapping]]] = ...) -> None: ...

class BatchJobStatusInfo(_message.Message):
    __slots__ = ("job_data", "id", "progress", "status")
    JOB_DATA_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    job_data: BatchJobDefinition
    id: str
    progress: int
    status: BatchJobStatus
    def __init__(self, job_data: _Optional[_Union[BatchJobDefinition, _Mapping]] = ..., id: _Optional[str] = ..., progress: _Optional[int] = ..., status: _Optional[_Union[BatchJobStatus, str]] = ...) -> None: ...

class GetBatchJobStatusRequestBody(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetBatchJobStatusResponseBody(_message.Message):
    __slots__ = ("job_info",)
    JOB_INFO_FIELD_NUMBER: _ClassVar[int]
    job_info: BatchJobStatusInfo
    def __init__(self, job_info: _Optional[_Union[BatchJobStatusInfo, _Mapping]] = ...) -> None: ...

class RenderAutomationOptions(_message.Message):
    __slots__ = ("render_volume_automation", "render_pan_automation")
    RENDER_VOLUME_AUTOMATION_FIELD_NUMBER: _ClassVar[int]
    RENDER_PAN_AUTOMATION_FIELD_NUMBER: _ClassVar[int]
    render_volume_automation: bool
    render_pan_automation: bool
    def __init__(self, render_volume_automation: bool = ..., render_pan_automation: bool = ...) -> None: ...

class BounceTrackRequestBody(_message.Message):
    __slots__ = ("preset_path", "file_name_prefix", "file_type", "audio_info", "location_info", "offline_bounce", "audio_encoding_options", "src_track_id", "in_location", "out_location", "automation_options")
    PRESET_PATH_FIELD_NUMBER: _ClassVar[int]
    FILE_NAME_PREFIX_FIELD_NUMBER: _ClassVar[int]
    FILE_TYPE_FIELD_NUMBER: _ClassVar[int]
    AUDIO_INFO_FIELD_NUMBER: _ClassVar[int]
    LOCATION_INFO_FIELD_NUMBER: _ClassVar[int]
    OFFLINE_BOUNCE_FIELD_NUMBER: _ClassVar[int]
    AUDIO_ENCODING_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    SRC_TRACK_ID_FIELD_NUMBER: _ClassVar[int]
    IN_LOCATION_FIELD_NUMBER: _ClassVar[int]
    OUT_LOCATION_FIELD_NUMBER: _ClassVar[int]
    AUTOMATION_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    preset_path: str
    file_name_prefix: str
    file_type: EM_FileType
    audio_info: EM_AudioInfo
    location_info: EM_LocationInfo
    offline_bounce: TripleBool
    audio_encoding_options: AudioEncodingOptions
    src_track_id: str
    in_location: TimelineLocation
    out_location: TimelineLocation
    automation_options: RenderAutomationOptions
    def __init__(self, preset_path: _Optional[str] = ..., file_name_prefix: _Optional[str] = ..., file_type: _Optional[_Union[EM_FileType, str]] = ..., audio_info: _Optional[_Union[EM_AudioInfo, _Mapping]] = ..., location_info: _Optional[_Union[EM_LocationInfo, _Mapping]] = ..., offline_bounce: _Optional[_Union[TripleBool, str]] = ..., audio_encoding_options: _Optional[_Union[AudioEncodingOptions, _Mapping]] = ..., src_track_id: _Optional[str] = ..., in_location: _Optional[_Union[TimelineLocation, _Mapping]] = ..., out_location: _Optional[_Union[TimelineLocation, _Mapping]] = ..., automation_options: _Optional[_Union[RenderAutomationOptions, _Mapping]] = ...) -> None: ...

class BounceTrackResponseBody(_message.Message):
    __slots__ = ("file_paths",)
    FILE_PATHS_FIELD_NUMBER: _ClassVar[int]
    file_paths: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, file_paths: _Optional[_Iterable[str]] = ...) -> None: ...

class PollEventsResponseBody(_message.Message):
    __slots__ = ("event",)
    EVENT_FIELD_NUMBER: _ClassVar[int]
    event: EventResponseData
    def __init__(self, event: _Optional[_Union[EventResponseData, _Mapping]] = ...) -> None: ...

class UnsubscribeFromEventsRequestBody(_message.Message):
    __slots__ = ("events",)
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    events: _containers.RepeatedCompositeFieldContainer[EventRequestData]
    def __init__(self, events: _Optional[_Iterable[_Union[EventRequestData, _Mapping]]] = ...) -> None: ...

class CompleteBatchJobRequestBody(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class CancelBatchJobRequestBody(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class EnableAPIRequestBody(_message.Message):
    __slots__ = ("client_key_string",)
    CLIENT_KEY_STRING_FIELD_NUMBER: _ClassVar[int]
    client_key_string: str
    def __init__(self, client_key_string: _Optional[str] = ...) -> None: ...

class EnableAPIResponseBody(_message.Message):
    __slots__ = ("success",)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: bool = ...) -> None: ...

class ExchangePublicKeysRequestBody(_message.Message):
    __slots__ = ("client_key_string",)
    CLIENT_KEY_STRING_FIELD_NUMBER: _ClassVar[int]
    client_key_string: str
    def __init__(self, client_key_string: _Optional[str] = ...) -> None: ...

class ExchangePublicKeysResponseBody(_message.Message):
    __slots__ = ("pt_key_string",)
    PT_KEY_STRING_FIELD_NUMBER: _ClassVar[int]
    pt_key_string: str
    def __init__(self, pt_key_string: _Optional[str] = ...) -> None: ...

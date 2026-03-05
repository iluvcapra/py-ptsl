"""
Operations classes.
"""

from typing import Any

from .operation import Operation

# Implemented by Pro Tools 2022.12

from .get_ptsl_version import CId_GetPTSLVersion
from .get_session_sample_rate import CId_GetSessionSampleRate
from .get_session_name import CId_GetSessionName
from .get_session_path import CId_GetSessionPath
from .get_session_audio_format import CId_GetSessionAudioFormat
from .get_session_bit_depth import CId_GetSessionBitDepth
from .get_session_start_time import CId_GetSessionStartTime
from .get_session_time_code_rate import CId_GetSessionTimeCodeRate
from .get_session_feet_frames_rate import CId_GetSessionFeetFramesRate
from .get_session_interleaved_state import CId_GetSessionInterleavedState
from .get_session_audio_rate_pull_settings import \
    CId_GetSessionAudioRatePullSettings
from .get_session_video_rate_pull_settings import \
    CId_GetSessionVideoRatePullSettings
from .get_session_length import CId_GetSessionLength
from .get_playback_mode import CId_GetPlaybackMode
from .get_transport_state import CId_GetTransportState
from .get_transport_armed import CId_GetTransportArmed
from .get_record_mode import CId_GetRecordMode
from .get_track_list import CId_GetTrackList
from .create_session import CId_CreateSession
from .open_session import CId_OpenSession
from .export_session_info_as_text import CId_ExportSessionInfoAsText
from .select_all_clips_on_track import CId_SelectAllClipsOnTrack
from .extend_selection_to_target_tracks \
    import (CId_ExtendSelectionToTargetTracks)
from .create_fades_based_on_preset import CId_CreateFadesBasedOnPreset
from .cut import CId_Cut
from .copy import CId_Copy
from .paste import CId_Paste
from .clear import CId_Clear
from .save_session import CId_SaveSession
from .close_session import CId_CloseSession
from .trim_to_selection import CId_TrimToSelection
from .consolidate_clip import CId_ConsolidateClip
from .import_command import CId_Import
from .clear_special import CId_ClearSpecial
from .copy_special import CId_CopySpecial
from .cut_special import CId_CutSpecial
from .export_clips_as_files import CId_ExportClipsAsFiles
from .export_selected_tracks_as_aaf_omf import CId_ExportSelectedTracksAsAAFOMF
from .export_mix import CId_ExportMix
from .get_dynamic_properties import CId_GetDynamicProperties
from .get_file_location import CId_GetFileLocation
from .get_task_status import CId_GetTaskStatus
from .host_ready_check import CId_HostReadyCheck
from .paste_special import CId_PasteSpecial
from .refresh_all_modified_audio_files import CId_RefreshAllModifiedAudioFiles
from .refresh_target_audio_files import CId_RefreshTargetAudioFiles
from .rename_target_track import CId_RenameTargetTrack
from .save_session_as import CId_SaveSessionAs
from .set_playback_mode import CId_SetPlaybackMode
from .set_record_mode import CId_SetRecordMode
from .spot import CId_Spot
from .authorize_connection import AuthorizeConnection
from .set_session_audio_format import CId_SetSessionAudioFormat
from .set_session_audio_rate_pull_settings import \
    CId_SetSessionAudioRatePullSettings
from .set_session_bit_depth import CId_SetSessionBitDepth
from .set_session_feet_frames_rate import CId_SetSessionFeetFramesRate
from .set_session_interleaved_state import CId_SetSessionInterleavedState
from .set_session_length import CId_SetSessionLength
from .set_session_start_time import CId_SetSessionStartTime
from .set_session_time_code_rate import CId_SetSessionTimeCodeRate
from .set_session_video_rate_pull_settings import \
    CId_SetSessionVideoRatePullSettings


# Pro Tools 2023.3

from .register_connection import CId_RegisterConnection
from .rename_selected_clip import CId_RenameSelectedClip
from .rename_target_clip import CId_RenameTargetClip
from .toggle_play_state import \
    CId_TogglePlayState, CId_ToggleRecordEnable, \
    CId_PlayHalfSpeed, CId_RecordHalfSpeed

from .memory_locations import CId_EditMemoryLocation, \
    CId_GetMemoryLocations, CId_CreateMemoryLocation

# Pro Tools 2023.9

from .create_new_tracks import CId_CreateNewTracks
from .select_tracks import CId_SelectTracksByName
from .zoom_preset import CId_RecallZoomPreset
from .timeline_selection import \
    CId_SetTimelineSelection, CId_GetTimelineSelection
from .set_edit_mode import CId_SetEditMode
from .get_edit_mode import CId_GetEditMode
from .set_edit_tool import CId_SetEditTool
from .get_edit_tool import CId_GetEditTool
from .get_edit_mode_options import CId_GetEditModeOptions
from .set_edit_mode_options import CId_SetEditModeOptions


# Pro Tools 2023.12

from .select_memory_location import CId_SelectMemoryLocation
from .set_track_mute_state import CId_SetTrackMuteState
from .set_track_solo_state import CId_SetTrackSoloState
from .set_track_solo_safe_state import CId_SetTrackSoloSafeState
from .set_track_record_safe_enable_state \
    import CId_SetTrackRecordSafeEnableState
from .set_track_input_monitor_state import CId_SetTrackInputMonitorState
from .set_track_smart_dsp_state import CId_SetTrackSmartDspState
from .set_track_hidden_state import CId_SetTrackHiddenState
from .set_track_inactive_state import CId_SetTrackInactiveState
from .set_track_frozen_state import CId_SetTrackFrozenState
from .set_track_online_state import CId_SetTrackOnlineState
from .set_track_open_state import CId_SetTrackOpenState

# Pro Tools 2024.6
from .get_memory_locations_manage_mode import CId_GetMemoryLocationsManageMode
from .set_memory_locations_manage_mode import CId_SetMemoryLocationsManageMode
from .set_main_counter_format import CId_SetMainCounterFormat
from .set_sub_counter_format import CId_SetSubCounterFormat
from .get_main_counter_format import CId_GetMainCounterFormat
from .get_sub_counter_format import CId_GetSubCounterFormat
from .undo import CId_Undo
from .redo import CId_Redo
from .undoall import CId_UndoAll
from .redoall import CId_RedoAll
from .clear_undo_queue import CId_ClearUndoQueue
from .set_track_DSP_mode_safe_state import CId_SetTrackDSPModeSafeState
from .get_system_session_delay_info import CId_GetSessionSystemDelayInfo
from .group_clips import CId_GroupClips
from .ungroup_clips import CId_UngroupClips
from .ungroup_all_clips import CId_UngroupAllClips
from .regroup_clips import CId_RegroupClips
from .repeat_selection import CId_RepeatSelection
from .duplicate_selection import CId_DuplicateSelection

# Pro Tools 2024.10

from .clear_all_memory_locations import CId_ClearAllMemoryLocations

# Pro Tools 2024.3

from .get_session_ids import CId_GetSessionsIDs

# Pro Tools 2025.6

from .get_edit_selection import CId_GetEditSelection
from .get_monitor_output_path import CId_GetMonitorOutputPath

# Pro Tools 2025.10

from .set_track_record_enable_state import CId_SetTrackRecordEnableState

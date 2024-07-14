"""
Operations classes.
"""

from typing import Any

from .operation import Operation

# Implemented by Pro Tools 2022.12

from .get_ptsl_version import GetPTSLVersion
from .get_session_sample_rate import GetSessionSampleRate
from .get_session_name import GetSessionName
from .get_session_path import GetSessionPath
from .get_session_audio_format import GetSessionAudioFormat
from .get_session_bit_depth import GetSessionBitDepth
from .get_session_start_time import GetSessionStartTime
from .get_session_time_code_rate import GetSessionTimeCodeRate
from .get_session_feet_frames_rate import GetSessionFeetFramesRate
from .get_session_interleaved_state import GetSessionInterleavedState
from .get_session_audio_rate_pull_settings import \
    GetSessionAudioRatePullSettings
from .get_session_video_rate_pull_settings import \
    GetSessionVideoRatePullSettings
from .get_session_length import GetSessionLength
from .get_playback_mode import GetPlaybackMode
from .get_transport_state import GetTransportState
from .get_transport_armed import GetTransportArmed
from .get_record_mode import GetRecordMode
from .get_track_list import GetTrackList
from .create_session import CreateSession
from .open_session import OpenSession
from .export_session_info_as_text import ExportSessionInfoAsText
from .select_all_clips_on_track import SelectAllClipsOnTrack
from .extend_selection_to_target_tracks import ExtendSelectionToTargetTracks
from .create_fades_based_on_preset import CreateFadesBasedOnPreset
from .cut import Cut
from .copy import Copy
from .paste import Paste
from .clear import Clear
from .save_session import SaveSession
from .close_session import CloseSession
from .trim_to_selection import TrimToSelection
from .consolidate_clip import ConsolidateClip
from .import_command import Import
from .clear_special import ClearSpecial
from .copy_special import CopySpecial
from .cut_special import CutSpecial
from .export_clips_as_files import ExportClipsAsFiles
from .export_selected_tracks_as_aaf_omf import ExportSelectedTracksAsAAFOMF
from .export_mix import ExportMix
from .get_dyamic_properties import GetDynamicProperties
from .get_file_location import GetFileLocation
from .get_task_status import GetTaskStatus
from .host_ready_check import HostReadyCheck
from .paste_special import PasteSpecial
from .refresh_all_modified_audio_files import RefreshAllModifiedAudioFiles
from .refresh_target_audio_files import RefreshTargetAudioFiles
from .rename_target_track import RenameTargetTrack
from .save_session_as import SaveSessionAs
from .set_playback_mode import SetPlaybackMode
from .set_record_mode import SetRecordMode
from .spot import Spot
from .authorize_connection import AuthorizeConnection
from .set_session_audio_format import SetSessionAudioFormat
from .set_session_audio_rate_pull_settings import \
    SetSessionAudioRatePullSettings
from .set_session_bit_depth import SetSessionBitDepth
from .set_session_feet_frames_rate import SetSessionFeetFramesRate
from .set_session_interleaved_state import SetSessionInterleavedState
from .set_session_length import SetSessionLength
from .set_session_start_time import SetSessionStartTime
from .set_session_time_code_rate import SetSessionTimeCodeRate
from .set_session_video_rate_pull_settings import \
    SetSessionVideoRatePullSettings


# Pro Tools 2023.3

from .register_connection import RegisterConnection
from .rename_selected_clip import RenameSelectedClip
from .rename_target_clip import RenameTargetClip
from .toggle_play_state import \
    TogglePlayState, ToggleRecordEnable, \
    PlayHalfSpeed, RecordHalfSpeed

from .memory_locations import EditMemoryLocation, \
    GetMemoryLocations, CreateMemoryLocation

# Pro Tools 2023.9

from .create_new_tracks import CreateNewTracks
from .select_tracks import SelectTracksByName
from .edit_mode import GetEditMode, SetEditMode, GetEditModeOptions, \
        SetEditModeOptions
from .edit_tool import GetEditTool, SetEditTool
from .zoom_preset import RecallZoomPreset
from .timeline_selection import SetTimelineSelection, GetTimelineSelection

from .pt_202406_additions import GetSessionSystemDelayInfo

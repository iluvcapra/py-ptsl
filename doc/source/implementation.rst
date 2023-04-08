Command Implementations in `Engine`
===================================

PTSL Version 1
--------------

===================================   =========   =============================================================
Command                               Version     :class:`~ptsl.Engine` method                                                                                 
===================================   =========   =============================================================
CreateSession                         >=2022.12   :meth:`~ptsl.Engine.create_session`
OpenSession                           >=2022.12   :meth:`~ptsl.Engine.open_session`
Import                                >=2022.12   :meth:`~ptsl.Engine.import_data`
GetTrackList                          >=2022.12   :meth:`~ptsl.Engine.track_list`                        
SelectAllClipsOnTrack                 >=2022.12   :meth:`~ptsl.Engine.select_all_clips_on_track`
ExtendSelectionToTargetTracks         >=2022.12   :meth:`~ptsl.Engine.extend_selection_to_target_tracks`
TrimToSelection                       >=2022.12   :meth:`~ptsl.Engine.trim_to_selection` 
CreateFadesBasedOnPreset              >=2022.12   :meth:`~ptsl.Engine.create_batch_fades`
RenameTargetTrack                     >=2022.12   :meth:`~ptsl.Engine.rename_target_track`
ConsolidateClip                       >=2022.12   :meth:`~ptsl.Engine.consolidate_clip`
ExportClipsAsFiles                    >=2022.12   :meth:`~ptsl.Engine.export_clips_as_files`
ExportSelectedTracksAsAAFOMF          >=2022.12
GetTaskStatus                         >=2022.12
HostReadyCheck                        >=2022.12   :meth:`~ptsl.Engine.host_ready_check`
RefreshTargetAudioFiles               >=2022.12
RefreshAllModifiedAudioFiles          >=2022.12
GetFileLocation                       >=2022.12   :meth:`~ptsl.Engine.get_file_location`
CloseSession                          >=2022.12   :meth:`~ptsl.Engine.close_session`
SaveSession                           >=2022.12   :meth:`~ptsl.Engine.save_session`
SaveSessionAs                         >=2022.12   :meth:`~ptsl.Engine.save_session_as`
Cut                                   >=2022.12   :meth:`~ptsl.Engine.cut`
Copy                                  >=2022.12   :meth:`~ptsl.Engine.copy`
Paste                                 >=2022.12   :meth:`~ptsl.Engine.paste`
Clear                                 >=2022.12   :meth:`~ptsl.Engine.clear`
CutSpecial                            >=2022.12   :meth:`~ptsl.Engine.cut`
CopySpecial                           >=2022.12   :meth:`~ptsl.Engine.copy`
ClearSpecial                          >=2022.12   :meth:`~ptsl.Engine.clear`
PasteSpecial                          >=2022.12   :meth:`~ptsl.Engine.paste`
ExportMix                             >=2022.12   :meth:`~ptsl.Engine.export_mix`
Spot                                  >=2022.12
ExportSessionInfoAsText               >=2022.12
GetDynamicProperties                  >=2022.12
SetPlaybackMode                       >=2022.12   :meth:`~ptsl.Engine.set_playback_mode`
SetRecordMode                         >=2022.12   :meth:`~ptsl.Engine.set_record_mode`
GetSessionAudioFormat                 >=2022.12   :meth:`~ptsl.Engine.session_audio_format`
GetSessionSampleRate                  >=2022.12   :meth:`~ptsl.Engine.session_sample_rate`
GetSessionBitDepth                    >=2022.12   :meth:`~ptsl.Engine.session_bit_depth`    
GetSessionInterleavedState            >=2022.12   :meth:`~ptsl.Engine.session_interleaved_state`
GetSessionTimeCodeRate                >=2022.12   :meth:`~ptsl.Engine.session_timecode_rate`
GetSessionFeetFramesRate              >=2022.12   :meth:`~ptsl.Engine.session_feet_frames_rate`
GetSessionAudioRatePullSettings       >=2022.12   :meth:`~ptsl.Engine.session_audio_rate_pull`
GetSessionVideoRatePullSettings       >=2022.12   :meth:`~ptsl.Engine.session_video_rate_pull`
GetSessionName                        >=2022.12   :meth:`~ptsl.Engine.session_name`
GetSessionPath                        >=2022.12   :meth:`~ptsl.Engine.session_path`
GetSessionStartTime                   >=2022.12   :meth:`~ptsl.Engine.session_start_time`
GetSessionLength                      >=2022.12   :meth:`~ptsl.Engine.session_length`
SetSessionAudioFormat                 >=2022.12   :meth:`~ptsl.Engine.set_session_audio_format`
SetSessionBitDepth                    >=2022.12   :meth:`~ptsl.Engine.set_session_bit_depth`
SetSessionInterleavedState            >=2022.12   :meth:`~ptsl.Engine.set_session_interleaved_state`
SetSessionTimeCodeRate                >=2022.12   :meth:`~ptsl.Engine.set_session_time_code_rate`
SetSessionFeetFramesRate              >=2022.12   :meth:`~ptsl.Engine.set_session_feet_frames_rate`
SetSessionAudioRatePullSettings       >=2022.12   :meth:`~ptsl.Engine.set_session_audio_rate_pull`
SetSessionVideoRatePullSettings       >=2022.12   :meth:`~ptsl.Engine.set_session_video_rate_pull`
SetSessionStartTime                   >=2022.12   :meth:`~ptsl.Engine.set_session_start_time`
SetSessionLength                      >=2022.12   :meth:`~ptsl.Engine.set_session_length`
GetPTSLVersion                        >=2022.12   :meth:`~ptsl.Engine.ptsl_version`
GetPlaybackMode                       >=2022.12   :meth:`~ptsl.Engine.playback_modes`
GetRecordMode                         >=2022.12   :meth:`~ptsl.Engine.record_mode`
GetTransportArmed                     >=2022.12   :meth:`~ptsl.Engine.transport_armed`
GetTransportState                     >=2022.12   :meth:`~ptsl.Engine.transport_state`
AuthorizeConnection                   ==2022.12  
RenameSelectedClip                    >=2023.3    :meth:`~ptsl.Engine.rename_selected_clip`
RenameTargetClip                      >=2023.3    :meth:`~ptsl.Engine.rename_target_clip`
TogglePlayState                       >=2023.3    :meth:`~ptsl.Engine.toggle_play_state`
ToggleRecordEnable                    >=2023.3    :meth:`~ptsl.Engine.toggle_record_enable`
PlayHalfSpeed                         >=2023.3    :meth:`~ptsl.Engine.play_half_speed`
RecordHalfSpeed                       >=2023.3    :meth:`~ptsl.Engine.record_half_speed`
EditMemoryLocation                    >=2023.3    :meth:`~ptsl.Engine.edit_memory_location`
GetMemoryLocations                    >=2023.3    :meth:`~ptsl.Engine.get_memory_locations`
RegisterConnection                    >=2023.3    Implicit in :meth:`~ptsl.Client.__init__`
===================================   =========   =============================================================

Command Implementations in `Engine`
===================================


===================================   =============================================================
Command                               `Engine` method
===================================   =============================================================
CreateSession                         :meth:`ptsl.Engine.create_session`
OpenSession							  :meth:`ptsl.Engine.open_session`
Import								  :meth:`ptsl.Engine.import_data`
GetTrackList                          :meth:`ptsl.Engine.track_list`                        
SelectAllClipsOnTrack   			  :meth:`ptsl.Engine.select_all_clips_on_track`
ExtendSelectionToTargetTracks		  :meth:`ptsl.Engine.extend_selection_to_target_tracks`
TrimToSelection
CreateFadesBasedOnPreset			  :meth:`ptsl.Engine.create_batch_fades`
RenameTargetTrack					  :meth:`ptsl.Engine.rename_target_track`
ConsolidateClip
ExportClipsAsFiles
ExportSelectedTracksAsAAFOMF
GetTaskStatus
HostReadyCheck
RefreshTargetAudioFiles
RefreshAllModifiedAudioFiles
GetFileLocation						  :meth:`ptsl.Engine.get_file_location`
CloseSession						  :meth:`ptsl.Engine.close_session`
SaveSession							  :meth:`ptsl.Engine.save_session`
SaveSessionAs						  :meth:`ptsl.Engine.save_session_as`
Cut                                   :meth:`ptsl.Engine.cut`
Copy                                  :meth:`ptsl.Engine.copy`
Paste                                 :meth:`ptsl.Engine.paste`
Clear                                 :meth:`ptsl.Engine.clear`
CutSpecial                            :meth:`ptsl.Engine.cut`
CopySpecial                           :meth:`ptsl.Engine.copy`
ClearSpecial                          :meth:`ptsl.Engine.clear`
PasteSpecial                          :meth:`ptsl.Engine.paste`
ExportMix							  :meth:`ptsl.Engine.export_mix`
Spot
ExportSessionInfoAsText
GetDynamicProperties
SetPlaybackMode                       :meth:`ptsl.Engine.set_playback_mode`
SetRecordMode                         :meth:`ptsl.Engine.set_record_mode`
GetSessionAudioFormat                 :meth:`ptsl.Engine.session_audio_format`
GetSessionSampleRate                  :meth:`ptsl.Engine.session_sample_rate`
GetSessionBitDepth					  :meth:`ptsl.Engine.session_bit_depth`	
GetSessionInterleavedState            :meth:`ptsl.Engine.session_interleaved_state`
GetSessionTimeCodeRate                :meth:`ptsl.Engine.session_timecode_rate`
GetSessionFeetFramesRate              :meth:`ptsl.Engine.session_feet_frames_rate`
GetSessionAudioRatePullSettings       :meth:`ptsl.Engine.session_audio_rate_pull`
GetSessionVideoRatePullSettings       :meth:`ptsl.Engine.session_video_rate_pull`
GetSessionName                        :meth:`ptsl.Engine.session_name`
GetSessionPath                        :meth:`ptsl.Engine.session_path`
GetSessionStartTime                   :meth:`ptsl.Engine.session_start_time`
GetSessionLength                      :meth:`ptsl.Engine.session_length`
SetSessionAudioFormat                 :meth:`ptsl.Engine.set_session_audio_format`
SetSessionBitDepth                    :meth:`ptsl.Engine.set_session_bit_depth`
SetSessionInterleavedState            :meth:`ptsl.Engine.set_session_interleaved_state`
SetSessionTimeCodeRate				  :meth:`ptsl.Engine.set_session_time_code_rate`
SetSessionFeetFramesRate			  :meth:`ptsl.Engine.set_session_feet_frames_rate`
SetSessionAudioRatePullSettings		  :meth:`ptsl.Engine.set_session_audio_rate_pull`
SetSessionVideoRatePullSettings		  :meth:`ptsl.Engine.set_session_video_rate_pull`
SetSessionStartTime                   :meth:`ptsl.Engine.set_session_start_time`
SetSessionLength                      :meth:`ptsl.Engine.set_session_length`
GetPTSLVersion                        :meth:`ptsl.Engine.ptsl_version`
GetPlaybackMode                       :meth:`ptsl.Engine.playback_modes`
GetRecordMode                         :meth:`ptsl.Engine.record_mode`
GetTransportArmed                     :meth:`ptsl.Engine.transport_armed`
GetTransportState                     :meth:`ptsl.Engine.transport_state`
AuthorizeConnection
===================================   =============================================================

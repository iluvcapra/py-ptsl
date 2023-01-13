.. table:: Engine Implementation
    :widths: auto

    =================================   =============================
    Command                             `Engine` method
    =================================   =============================
    CreateSession                       create_session
	OpenSession
	Import
	GetTrackList                        track_list                        
	SelectAllClipsOnTrack   
	ExtendSelectionToTargetTracks
	TrimToSelection
	CreateFadesBasedOnPreset
	RenameTargetTrack
	ConsolidateClip
	ExportClipsAsFiles
	ExportSelectedTracksAsAAFOMF
	GetTaskStatus
	HostReadyCheck
	RefreshTargetAudioFiles
	RefreshAllModifiedAudioFiles
	GetFileLocation
	CloseSession
	SaveSession
	SaveSessionAs
	Cut                                 cut
	Copy                                copy
	Paste                               paste
	Clear                               clear
	CutSpecial                          cut
	CopySpecial                         copy
	ClearSpecial                        clear
	PasteSpecial                        paste
	ExportMix
	Spot
	ExportSessionInfoAsText
	GetDynamicProperties
	SetPlaybackMode                     set_playback_mode
	SetRecordMode                       set_record_mode
	GetSessionAudioFormat               session_audio_format
	GetSessionSampleRate                session_sample_rate
	GetSessionBitDepth					session_bit_depth	
	GetSessionInterleavedState          session_interleaved_state
	GetSessionTimeCodeRate              session_timecode_rate
	GetSessionFeetFramesRate            session_feet_frames_rate
	GetSessionAudioRatePullSettings     session_audio_pull
	GetSessionVideoRatePullSettings     session_video_pull
	GetSessionName                      session_name
	GetSessionPath                      session_path
	GetSessionStartTime                 session_start_time
	GetSessionLength                    session_length
	SetSessionAudioFormat               set_session_audio_format
	SetSessionBitDepth                  set_session_bit_depth
	SetSessionInterleavedState          set_session_interleaved_state
	SetSessionTimeCodeRate				set_session_time_code_rate
	SetSessionFeetFramesRate			set_session_feet_frames_rate
	SetSessionAudioRatePullSettings		set_session_audio_rate_pull
	SetSessionVideoRatePullSettings		set_session_video_rate_pull
	SetSessionStartTime                 set_session_start_time
	SetSessionLength                    set_session_length
	GetPTSLVersion                      ptsl_version
	GetPlaybackMode                     playback_modes
	GetRecordMode                       record_mode
	GetTransportArmed                   transport_armed
	GetTransportState                   transport_state
	AuthorizeConnection
    =================================   =============================

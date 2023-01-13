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
	GetSessionBitDepth
	GetSessionInterleavedState          session_interleaved_state
	GetSessionTimeCodeRate              session_timecode_rate
	GetSessionFeetFramesRate            session_feet_frames_rate
	GetSessionAudioRatePullSettings     session_audio_pull
	GetSessionVideoRatePullSettings     session_video_pull
	GetSessionName                      session_name
	GetSessionPath                      session_path
	GetSessionStartTime                 session_start_time
	GetSessionLength                    session_length
	SetSessionAudioFormat               set_audio_format
	SetSessionBitDepth                  set_bit_depth
	SetSessionInterleavedState          
	SetSessionTimeCodeRate
	SetSessionFeetFramesRate
	SetSessionAudioRatePullSettings
	SetSessionVideoRatePullSettings
	SetSessionStartTime                 set_session_start_time
	SetSessionLength                    set_session_length
	GetPTSLVersion                      ptsl_version
	GetPlaybackMode                     playback_modes
	GetRecordMode                       record_mode
	GetTransportArmed                   transport_armed
	GetTransportState                   transport_state
	AuthorizeConnection
    =================================   =============================

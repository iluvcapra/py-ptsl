Types and Enumerations
======================

.. py:currentmodule:: ptsl.PTSL_pb2


These are some of the protobuf-generated enumerations used by 
the :class:`Engine` class for method arguments or return values.


.. note:: A side project might be writing a Sphinx extension
	for autogenerating this from the .proto file.


Common Settings and Value Types 
-------------------------------

.. py:class:: TripleBool

	A three-valued logic type.

	.. py:attribute:: TB_None
		:value: 0
	.. py:attribute:: TB_False
		:value: 1
	.. py:attribute:: TB_True
		:value: 2


.. py:class:: MediaDestination

	Used by the import methods.

	.. attribute:: MD_None
		:value: 0
	.. attribute:: MD_MainVideoTrack
		:value: 1
	.. attribute:: MD_NewTrack
		:value: 2
	.. attribute:: MD_ClipList
		:value: 3


.. py:class:: MediaLocation

	Used by the import methods.

	.. attribute:: ML_None
		:value: 0
	.. attribute:: ML_SessionStart
		:value: 1
	.. attribute:: ML_SongStart
		:value: 2
	.. attribute:: ML_Selection
		:value: 3
	.. attribute:: ML_Spot
		:value: 4


.. py:class:: SessionAudioFormat
	
	Used to represent a session's audio recording format. This is a 
	parameter to :py:meth:`ptsl.Engine.create_session` (and its friends) as well as 
	:py:meth:`~ptsl.Engine.set_session_audio_format`.
	
	.. py:attribute:: SAF_WAVE
		:value: 0

	.. py:attribute:: SAF_AIFF
		:value: 1


.. py:class:: SessionTimeCodeRate

	.. attribute:: STCR_Fps23976
		:value: 0
	.. attribute:: STCR_Fps24
		:value: 1
	.. attribute:: STCR_Fps25
		:value: 2
	.. attribute:: STCR_Fps2997
		:value: 3
	.. attribute:: STCR_Fps2997Drop
		:value: 4
	.. attribute:: STCR_Fps30
		:value: 5
	.. attribute:: STCR_Fps30Drop
		:value: 6
	.. attribute:: STCR_Fps47952
		:value: 7
	.. attribute:: STCR_Fps48
		:value: 8
	.. attribute:: STCR_Fps50
		:value: 9
	.. attribute:: STCR_Fps5994
		:value: 10
	.. attribute:: STCR_Fps5994Drop
		:value: 11
	.. attribute:: STCR_Fps60
		:value: 12
	.. attribute:: STCR_Fps60Drop
		:value: 13
	.. attribute:: STCR_Fps100
		:value: 14
	.. attribute:: STCR_Fps11988
		:value: 15
	.. attribute:: STCR_Fps11988Drop
		:value: 16
	.. attribute:: STCR_Fps120
		:value: 17
	.. attribute:: STCR_Fps120Drop
		:value: 18


.. class:: TrackOffsetOptions

	Used by various methods to describe the string format of a 
	time reference.
	
	.. attribute:: BarsBeats
		:value: 0
	.. attribute:: MinSecs
		:value: 1
	.. attribute:: TimeCode
		:value: 2
	.. attribute:: FeetFrames
		:value: 3
	.. attribute:: Samples
		:value: 4

.. class:: SessionFeetFramesRate

	.. attribute:: SFFR_Fps23976
		:value: 0
	.. attribute:: SFFR_Fps24
		:value: 1
	.. attribute:: SFFR_Fps25
		:value: 2


.. class:: SessionRatePull

	.. attribute:: SRP_None
		:value: 0
	.. attribute:: SRP_Up01
		:value: 1
	.. attribute:: SRP_Down01
		:value: 2
	.. attribute:: SRP_Up4
		:value: 3
	.. attribute:: SRP_Up4Up01
		:value: 4
	.. attribute:: SRP_Up4Down01
		:value: 5
	.. attribute:: SRP_Down4
		:value: 6
	.. attribute:: SRP_Down4Up01
		:value: 7
	.. attribute:: SRP_Down4Down01
		:value: 8


Transport Modes
---------------

.. class:: RecordMode

    Renamed in PTSL 2025.6.0 from RM_RecordMode

	.. attribute:: RM_Normal
		:value: 0
	.. attribute:: RM_Loop
		:value: 1
	.. attribute:: RM_Destructive
		:value: 2
	.. attribute:: RM_QuickPunch
		:value: 3
	.. attribute:: RM_TrackPunch
		:value: 4
	.. attribute:: RM_DestructivePunch
		:value: 5

.. class:: PlaybackMode

    Renamed in PTSL 2025.6.0 from PM_PlaybackMode

	.. py:attribute:: PM_Normal
		:value: 0

	.. py:attribute:: PM_Loop
		:value: 1

	.. py:attribute:: PM_DynamicTransport
		:value: 2


.. py:class:: SampleRate
    
    Base sample rates.

	.. attribute:: SR_None
		:value: 0

	.. attribute:: SR_44100
		:value: 1

	.. attribute:: SR_48000
		:value: 2

	.. attribute:: SR_96000
		:value: 3

	.. attribute:: SR_176400
		:value: 4

	.. attribute:: SR_192000
		:value: 5

    .. attribute:: SR_88200 
        :value: 6

        Not available in Pro Tools 2022.12.
        

.. py:class:: BitDepth

	.. attribute:: Bit_None
		:value: 0
	.. attribute:: Bit16
		:value: 1
	.. attribute:: Bit24
		:value: 2
	.. attribute:: Bit32Float
		:value: 3


Property Containers
-------------------

.. class:: PropertyContainer

	.. attribute:: container_name
		:type: str
	.. attribute:: type
		:type: DP_ValueTypes
	.. attribute:: value
		:type: str


.. class:: DP_ValueTypes

	.. attribute:: DP_VT_double
		:value: 0
	.. attribute:: DP_VT_float
		:value: 1
	.. attribute:: DP_VT_int32
		:value: 2
	.. attribute:: DP_VT_int64
		:value: 3
	.. attribute:: DP_VT_uint32
		:value: 4
	.. attribute:: DP_VT_uint64
		:value: 5
	.. attribute:: DP_VT_sint32
		:value: 6
	.. attribute:: DP_VT_sint64
		:value: 7
	.. attribute:: DP_VT_fixed32
		:value: 8
	.. attribute:: DP_VT_fixed64
		:value: 9
	.. attribute:: DP_VT_sfixed32
		:value: 10
	.. attribute:: DP_VT_sfixed64
		:value: 11
	.. attribute:: DP_VT_bool
		:value: 12
	.. attribute:: DP_VT_string
		:value: 13
	.. attribute:: DP_VT_bytes
		:value: 14
	.. attribute:: DP_VT_enum
		:value: 15
	.. attribute:: DP_VT_object
		:value: 16

New Session Settings
--------------------

.. py:class:: IOSettings

	Used by :py:meth:`~ptsl.Engine.create_session` to set the
	initial IO setup of a new session.

	.. attribute:: IO_None
		:value: 0
	.. attribute:: IO_Last
		:value: 1
	.. attribute:: IO_StereoMix
		:value: 2
	.. attribute:: IO_51FilmMix
		:value: 3
	.. attribute:: IO_51SMPTEMix
		:value: 4
	.. attribute:: IO_51DTSMix
		:value: 5
	.. attribute:: IO_UserDefined
		:value: 6


Importing
---------

.. py:class:: ImportType

	Used by :py:meth:`~ptsl.Engine.import_data`, 
	according to talk on the DUC only the "Session"
	value is currently operative.

	.. attribute:: Session
		:value: 0
	.. attribute:: Audio
		:value: 1
	.. attribute:: Video
		:value: 2
	.. attribute:: MIDI
		:value: 3
	.. attribute:: ClipGroups
		:value: 4

.. py:class:: SessionData

	Used by :py:meth:`~ptsl.Engine.import_data`

	.. attribute:: audio_options
		:type: AudioMediaOptions

	.. attribute:: audio_handle_size
		:type: int

		Handle size in milliseconds. Only applies if :py:attr:`~ptsl.SessionData.audio_options`
		is :py:attr:`~ptsl.AudioMediaOptions.ConsolidateFromSourceAudio`

	.. attribute:: video_options
		:type: VideoMediaOptions

	.. attribute:: match_options
		:type: MatchTrackOptions

	.. attribute:: playlist_options
		:type: MainPlaylistOptions

	.. attribute:: track_data_to_import
		:type: TrackDataToImport

	.. attribute:: timecode_mapping_units
		:type: TimeCodeMappingOptions

	.. attribute:: adjust_session_start_time_to_match_source
		:type: bool


.. class:: MatchTrackOptions

	.. attribute:: MT_None
		:value: 0
	.. attribute:: MT_MatchTracks
		:value: 1
	.. attribute:: MT_ImportAsNewTrack
		:value: 2


.. class:: MainPlaylistOptions

	.. attribute:: ImportReplaceExistingPlaylists
		:value: 0
	.. attribute:: ImportOverlayNewOnExistingPlaylists
		:value: 1
	.. attribute:: DoNotImport
		:value: 2


.. class:: TrackDataToImport

	.. attribute:: track_data_preset_path
		:type: str
	.. attribute:: clip_gain
		:type: bool
	.. attribute:: clips_and_media
		:type: bool
	.. attribute:: volume_automation
		:type: bool


.. class:: TimeCodeMappingOptions

	.. attribute:: MaintainAbsoluteTimeCodeValues
		:value: 0
	.. attribute:: MaintainRelativeTimeCodeValues
		:value: 1
	.. attribute:: MapStartTimeCodeTo
		:value: 2


.. py:class:: AudioMediaOptions

	.. attribute:: LinkToSourceAudio
		:value: 0
	.. attribute:: CopyFromSourceAudio
		:value: 1
	.. attribute:: ConsolidateFromSourceAudio
		:value: 2
	.. attribute:: ForceToTargetSessionFormat
		:value: 3  

.. py:class:: VideoMediaOptions

	.. attribute:: LinkToSourceVideo
		:value: 0
	.. attribute:: CopyFromSourceVideo
		:value: 1
	.. attribute:: ImportAsOfflineSatelliteMedia
		:value: 2

		A note in the proto here says "will not support"


.. py:class:: AudioData

	.. attribute:: file_list
		:type: List[str]
	.. attribute:: audio_operations
		:type: AudioOperations
	.. attribute:: destination_path
		:type: str
	.. attribute:: destination
		:type: MediaDestination
	.. attribute:: location
		:type: MediaLocation


.. py:class:: AudioOperations

	.. attribute:: AddAudio
		:value: 0
	.. attribute:: CopyAudio
		:value: 1
	.. attribute:: ConvertAudio
		:value: 2
	.. attribute:: Default
		:value: 3



File Locations
--------------

.. class:: FileLocationTypeFilter

	Defines a set of predicates for use with the :py:meth:`~ptsl.Engine.get_file_location`
	method.

	.. attribute:: All_Files
		:value: 0
	.. attribute:: OnTimeline_Files
		:value: 1
	.. attribute:: NotOnTimeline_Files
		:value: 2
	.. attribute:: Online_Files
		:value: 3
	.. attribute:: Offline_Files
		:value: 4
	.. attribute:: Audio_Files
		:value: 5
	.. attribute:: Video_Files
		:value: 6
	.. attribute:: Rendered_Files
		:value: 7
	.. attribute:: SelectedClipsTimeline
		:value: 101
	.. attribute:: SelectedClipsClipsList
		:value: 102


.. class:: FileLocation

	.. attribute:: path
		:type: str
	.. attribute:: info
		:type: FileLocationInfo


.. class:: FileLocationInfo

	.. attribute:: is_online
		:type: bool


Exporting Clips and Mixes
-------------------------

.. class:: ExportFileType

	.. attribute:: WAV
		:value: 0
		
	.. attribute:: AIFF
		:value: 1
		
	.. attribute:: MXF
		:value: 2

		can't be selected unless 'Enforce Avid Compatibility is ON

	.. attribute:: MP3
		:value: 3

		is not supported

	.. attribute:: QuickTime
		:value: 4

		is not supported


.. class:: ResolveDuplicateNamesBy

	.. attribute:: AutoRenaming
		:value: 0

		default

	.. attribute:: ReplacingWithNewFiles
		:value: 1


.. class:: EM_FileType

	.. attribute:: EM_None
		:value: 0
	.. attribute:: EM_MOV
		:value: 1
	.. attribute:: EM_WAV
		:value: 2
	.. attribute:: EM_AIFF
		:value: 3
	.. attribute:: EM_MP3
		:value: 4
	.. attribute:: EM_MXFOPAtom
		:value: 5
	.. attribute:: EM_WAVADM
		:value: 6


.. class:: EM_SourceInfo

	An individual bounce source in an :py:meth:`~ptsl.Engine.export_mix`
	command.

	.. attribute:: source_type
		:type: EM_SourceType
	.. attribute:: name
		:type: str


.. class:: EM_SourceType

	.. attribute:: PhysicalOut
		:value: 0
	.. attribute:: Bus
		:value: 1
	.. attribute:: Output
		:value: 2

.. class:: EM_FileDestination

	.. attribute:: EM_FD_None
		:value: 0
	.. attribute:: EM_FD_SessionFolder
		:value: 1
	.. attribute:: EM_FD_Directory
		:value: 2


.. class:: EM_AudioInfo

	.. attribute:: compression_type
		:type: CompressionType
	.. attribute:: export_format
		:type: ExportFormat
	.. attribute:: bit_depth
		:type: BitDepth
	.. attribute:: sample_rate
		:type: SampleRate
	.. attribute:: pad_to_frame_boundary
		:type: TripleBool
	.. attribute:: delivery_format
		:type: EM_DeliveryFormat


.. class:: EM_VideoInfo

	.. attribute:: include_video
		:type: TripleBool
	.. attribute:: export_option
		:type: EM_VideoExportOptions
	.. attribute:: replace_timecode_track
		:type: TripleBool
	.. attribute:: codec_info
		:type: EM_CodecInfo


.. class:: EM_LocationInfo

	.. attribute:: import_after_bounce
		:type: TripleBool
	.. attribute:: import_options
		:type: EM_ImportOptions
	.. attribute:: file_destination
		:type: EM_FileDestination
	.. attribute:: directory
		:type: str


.. class:: EM_DolbyAtmosInfo

	.. attribute:: add_first_frame_of_action
		:type: TripleBool
	.. attribute:: timecode_value
		:type: str
	.. attribute:: frame_rate
		:type: int
	.. attribute:: property_list
		:type: List[PropertyContainer]


.. class:: CompressionType

	.. attribute:: CT_None
		:value: 0
	.. attribute:: CT_PCM
		:value: 1


.. class:: ExportFormat

	.. attribute:: EF_None
		:value: 0

	.. attribute:: EF_Mono
		:value: 1
	
	.. attribute:: EF_MultipleMono
		:value: 2
		
	.. attribute:: EF_Interleaved
		:value: 3

		default


.. class:: EM_DeliveryFormat

	.. attribute:: EM_DF_None
		:value: 0
	.. attribute:: EM_DF_FilePerMixSource
		:value: 1
	.. attribute:: EM_DF_SingleFile
		:value: 2


.. class:: EM_VideoExportOptions

	.. attribute:: VE_None
		:value: 0
	.. attribute:: VE_SameAsSource
		:value: 1
	.. attribute:: VE_Transcode
		:value: 2


.. class:: EM_ImportOptions

	.. attribute:: import_destination
		:type: MediaDestination
	.. attribute:: import_location
		:type: MediaLocation


.. class:: EM_CodecInfo

	.. attribute:: codec_name
		:type: str
	.. attribute:: property_list
		:type: List[PropertyContainer]


Working With Clips
------------------

.. class:: ClipLocation

    Renamed in PTSL 2025.6.0 from CL_ClipLocation
    
    Describes a named clip's location.


Working With Tracks
-------------------

.. class:: Track

	Contains information for a single track, returned 
	by :meth:`~ptsl.Engine.track_list`.

	.. attribute:: name
		:type: str
	.. attribute:: type
		:type: TrackType
	.. attribute:: id
		:type: str

		A UUID, in the format *{00000000-2a000000-f404e1df-f298fd4b}*.

	.. attribute:: index
		:type: int
		
		1-based track index.

	.. attribute:: color
		:type: str
	.. attribute:: track_attributes
		:type: TrackAttributes
	.. attribute:: id_compressed
		:type: str


.. class:: TrackType

	.. attribute:: Unknown
		:value: 0
	.. attribute:: Midi
		:value: 1
	.. attribute:: AudioTrack
		:value: 2
	.. attribute:: Aux
		:value: 3
	.. attribute:: VideoTrack
		:value: 4
	.. attribute:: Vca
		:value: 5
	.. attribute:: Tempo
		:value: 6
	.. attribute:: Markers
		:value: 7
	.. attribute:: Meter
		:value: 8
	.. attribute:: KeySignature
		:value: 9
	.. attribute:: ChordSymbols
		:value: 10
	.. attribute:: Instrument
		:value: 11
	.. attribute:: Master
		:value: 12
	.. attribute:: Heat
		:value: 13
	.. attribute:: BasicFolder
		:value: 14
	.. attribute:: RoutingFolder
		:value: 15
	.. attribute:: CompLane
		:value: 16


.. class:: TrackAttributes

	A list of these objects are returned by :py:meth:`~ptsl.Engine.track_list`.

	.. attribute:: is_inactive
		:type: TrackAttributeState
	.. attribute:: is_hidden
		:type: TrackAttributeState
	.. attribute:: is_selected
		:type: TrackAttributeState
	.. attribute:: contains_clips
		:type: bool
	.. attribute:: contains_automation
		:type: bool
	.. attribute:: is_soloed
		:type: bool
	.. attribute:: is_record_enabled
		:type: bool
	.. attribute:: is_input_monitoring_on
		:type: TrackAttributeState
	.. attribute:: is_smart_dsp_on
		:type: bool
	.. attribute:: is_locked
		:type: bool
	.. attribute:: is_muted
		:type: bool
	.. attribute:: is_frozen
		:type: bool
	.. attribute:: is_open
		:type: bool
	.. attribute:: is_online
		:type: bool


.. class:: TrackAttributeState

	.. attribute:: None
		:value: 0
	.. attribute:: SetExplicitly
		:value: 1
	.. attribute:: SetImplicitly
		:value: 2
	.. attribute:: SetExplicitlyAndImplicitly
		:value: 3


.. class:: TrackListInvertibleFilter

	A list of these objects is used as arguments to 
	:py:meth:`~ptsl.Engine.track_list` as predicates
	for a track search.

	.. attribute:: filter
		:type: TrackListFilter
	.. attribute:: is_inverted
		:type: bool

.. class:: TrackListFilter

	.. attribute:: All
		:value: 0
	.. attribute:: Selected
		:value: 1
	.. attribute:: SelectedExplicitly
		:value: 2
	.. attribute:: SelectedImplicitly
		:value: 3
	.. attribute:: WithClipsOnMainPlaylist
		:value: 4
	.. attribute:: WithAutomationOnMainPlaylist
		:value: 5
	.. attribute:: Inactive
		:value: 6
	.. attribute:: InactiveExplicitly
		:value: 7
	.. attribute:: InactiveImplicitly
		:value: 8
	.. attribute:: Hidden
		:value: 9
	.. attribute:: HiddenExplicitly
		:value: 10
	.. attribute:: HiddenImplicitly
		:value: 11
	.. attribute:: Locked
		:value: 12
	.. attribute:: Muted
		:value: 13
	.. attribute:: Frozen
		:value: 14
	.. attribute:: Open
		:value: 15
	.. attribute:: Online
		:value: 16

Working with Memory Locations
-----------------------------

.. class:: MemoryLocation

    Data structure for a single memory location.

    .. attribute:: name
        :type: str
    .. attribute:: number
        :type: int
    .. attribute:: reference
        :type: MemoryLocationReference 
    .. attribute:: start_time
        :type: str
    .. attribute:: end_time
        :type: str
    .. attribute:: time_properties
        :type: TimeProperties
    .. attribute:: general_properties
        :type: MemoryLocationProperties
    .. attribute:: comments
        :type: str


.. class:: MemoryLocationProperties

    .. attribute:: zoom_settings
        :type: bool
    .. attribute:: pre_post_roll_times
        :type: bool
    .. attribute:: track_visibility
        :type: bool
    .. attribute:: track_heights
        :type: bool
    .. attribute:: group_enables
        :type: bool
    .. attribute:: window_configuration
        :type: bool
    .. attribute:: window_configuration_index
        :type: int
    .. attribute:: window_configuration_name
        :type: str
    

.. class:: MemoryLocationReference
    
    .. attribute:: MLR_BarBeat
        :value: 0
    .. attribute:: MLR_Absolute
        :value: 1

.. class:: TimeProperties
    
    .. attribute:: TP_Marker
        :value: 0
    .. attribute:: TP_Selection
        :value: 1
    .. attribute:: TP_None
        :value: 2


Editing Modifiers
-----------------


.. class:: AutomationDataOptions

	Used by the :meth:`~ptsl.Engine.cut`, :meth:`~ptsl.Engine.copy` and 
	:meth:`~ptsl.Engine.clear` methods.

	.. attribute:: All_Automation
		:value: 0
	.. attribute:: Pan_Automation
		:value: 1
	.. attribute:: PlugIn_Automation
		:value: 2
	.. attribute:: Clip_Gain
		:value: 3
	.. attribute:: Clip_Effects
		:value: 4

.. class:: PasteSpecialOptions

	.. attribute:: Merge
		:value: 0
	.. attribute:: Repeat_To_Fill_Selection
		:value: 1
	.. attribute:: To_Current_Automation_Type
		:value: 2

Errors
------

.. class:: CommandErrorType

	Error enumeration.

	.. attribute:: OS_WritePermissions
		:value: 0

		command hits write permissions

	.. attribute:: OS_ErrorCode
		:value: 1

		other OS error

	.. attribute:: OS_NoLocationFound
		:value: 2

		the specified location does not exist

	.. attribute:: OS_NoSessionFound
		:value: 3

		the specified session does not exist
	.. attribute:: OS_FilePathLocation
		:value: 4

		the specified file path could not be found

	.. attribute:: OS_ReadError
		:value: 5

		command hits read permissions or can not read specified file

	.. attribute:: OS_DiskSpace
		:value: 6

		not enough free space on disk 

	.. attribute:: OS_DuplicateName
		:value: 7

		the session name to be created is a duplicate of some existing

	.. attribute:: OS_IllegalCharacters
		:value: 8

		the session name contains illegal characters/symbols

	.. attribute:: OS_CharactersLimit
		:value: 9

		the session/track name is too long (250 characters allowed)

	.. attribute:: OS_ProToolsIsNotAvailable
		:value: 10

		ProTools is not responding during a specified timeout

	.. attribute:: PT_UnknownError
		:value: 100

		an unspecified error occurred during execution of a command
	.. attribute:: PT_NoTemplateGroup
		:value: 101

		template group does not exist

	.. attribute:: PT_NoTemplate
		:value: 102

		template name does not exist
	.. attribute:: PT_SampleRateMismatch
		:value: 103

		cannot copy/link source media because SRC is on and sample rates don't match

	.. attribute:: PT_NoVideoTrackFound
		:value: 104

		cannot copy/link source media because no video track found in the session

	.. attribute:: PT_NoTracksFound
		:value: 105

		warning. no tracks matched because no tracks exist in source

	.. attribute:: PT_NoOpenedSession
		:value: 106

		session is not open

	.. attribute:: PT_NoTrackFound
		:value: 107

		specified track(s) not found

	.. attribute:: PT_NoClipsFound
		:value: 108

		specified track contains no clips

	.. attribute:: PT_NoSelection
		:value: 109

		no selection was found

	.. attribute:: PT_RecordDrive
		:value: 110

		the volume is not designated as a record drive

	.. attribute:: PT_NoPresetFound
		:value: 111

		preset does not exist in the specified location

	.. attribute:: PT_FileTypeMXF
		:value: 112

		MXF is only available when 'Enforce Media Composer compatibility' is on

	.. attribute:: PT_CopyOptionCopy
		:value: 113

		copy option are unavailable if 'Quantize Edits to Frame Boundaries' is checked

	.. attribute:: PT_CopyOptionLink
		:value: 114

		link option are unavailable if 'Quantize Edits to Frame Boundaries' is checked

	.. attribute:: PT_QuantizeEdits
		:value: 115

		Quantize Edits to Frame Boundaries' can't be false if 'Enforce Media Composer compatibility' is true

	.. attribute:: PT_ExportAsMultichannel
		:value: 116

		warning. 'Export Stereo, 5.1 and 7.1 Tracks as Multichannel' is not applicable because no tracks of that format are contained within the export selection

	.. attribute:: PT_IllegalCharactersComments
		:value: 117

		comments contain illegal characters

	.. attribute:: PT_IllegalCharactersSequenceName
		:value: 118

		sequence name contains illegal characters

	.. attribute:: PT_MaxCharactersComments
		:value: 119

		comments exceed the maximum character limit

	.. attribute:: PT_MaxCharactersSequenceName
		:value: 120

		sequence name exceeds the maximum character limit

	.. attribute:: PT_NoSequenceName
		:value: 121

		sequence name can't be empty

	.. attribute:: PT_InvalidTask
		:value: 122

		the specified task does not exist

	.. attribute:: PT_FileNotFound
		:value: 123

		specified files were not found

	.. attribute:: PT_InvalidSelection
		:value: 124

		unable to perform action because of invalid selection SDK errors

    .. attribute:: PT_ReadOnlySession
        :value: 125

        the session is located on a read-only drive and cannot be saved 
        without user intervention

    .. attribute:: PT_InvalidParameter
        :value: 126

        One or more parameters are invalid

	.. attribute:: SDK_Version_Mismatch
		:value: 401

		Versions of PTSL Host and PTSL Client are mismatched

    .. attribute:: sdk_notimplemented
        :value: 402

        Some PTSL functional is not implemented at the PT side


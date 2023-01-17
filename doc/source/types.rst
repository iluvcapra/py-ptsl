Types and Enumerations
======================

.. py:currentmodule:: ptsl.PTSL_pb2

These are some of the protobuf-generated enumerations 
used by the :class:`Engine` class for method arguments 
or return values.

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


.. py:class:: SampleRate

    .. py:attribute:: SR_None
        :value: 0
    .. py:attribute:: SR_44100
        :value: 1
    .. py:attribute:: SR_48000
        :value: 2
    .. py:attribute:: SR_96000
        :value: 3
    .. py:attribute:: SR_176400
        :value: 4
    .. py:attribute:: SR_192000
        :value: 5


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


Exporting Mixes
---------------

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

Getting Tracks
--------------

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

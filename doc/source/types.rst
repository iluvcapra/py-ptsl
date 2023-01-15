Types and Enumerations
======================

.. py:currentmodule:: ptsl

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

    Used by import methods.

    .. attribute:: MD_None
    .. attribute:: MD_MainVideoTrack
    .. attribute:: MD_NewTrack
    .. attribute:: MD_ClipList


.. py:class:: MediaLocation

    .. attribute:: ML_None
    .. attribute:: ML_SessionStart
    .. attribute:: ML_SongStart
    .. attribute:: ML_Selection
    .. attribute:: ML_Spot


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

    .. py:attribute:: Bit_None
    .. py:attribute:: Bit16
    .. py:attribute:: Bit24
    .. py:attribute:: Bit32Float


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

    .. py:attribute:: IO_None
    .. py:attribute:: IO_Last
    .. py:attribute:: IO_StereoMix
    .. py:attribute:: IO_51FilmMix
    .. py:attribute:: IO_51SMPTEMix
    .. py:attribute:: IO_51DTSMix
    .. py:attribute:: IO_UserDefined


Importing
---------

.. py:class:: ImportType

    Used by :py:meth:`~ptsl.Engine.import_data`, 
    according to talk on the DUC only the "Session"
    value is currently operative.

    .. attribute:: Session
    .. attribute:: Audio
    .. attribute:: Video
    .. attribute:: MIDI
    .. attribute:: ClipGroup


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


.. py:class:: AudioMediaOptions

    .. attribute:: LinkToSourceAudio
    .. attribute:: CopyFromSourceAudio
    .. attribute:: ConsolidateFromSourceAudio
    .. attribute:: ForceToTargetSessionFormat

.. py:class:: VideoMediaOptions

    .. attribute:: LinkToSourceVideo

    .. attribute:: CopyFromSourceVideo

    .. attribute:: ImportAsOfflineSatelliteMedia

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

    .. attribute:: CopyAudio

    .. attribute:: ConvertAudio

    .. attribute:: Default



File Locations
--------------

.. class:: FileLocationTypeFilter

    Defines a set of predicates for use with the :py:meth:`~ptsl.Engine.get_file_location`
    method.

    .. attribute:: All_Files
    .. attribute:: OnTimeline_Files
    .. attribute:: NotOnTimeline_Files
    .. attribute:: Online_File
    .. attribute:: Offline_Files
    .. attribute:: Audio_Files
    .. attribute:: Video_Files
    .. attribute:: Rendered_Files

    .. attribute:: SelecteClipsTimeline
    .. attribute:: SelectedClipsClipsList


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
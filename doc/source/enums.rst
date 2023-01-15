Enumerations
============

.. py:currentmodule:: ptsl

These are some of the protobuf-generated enumerations 
used by the :class:`Engine` class for method arguments 
or return values.

.. note:: A side project might be writing a Sphinx extension
    for autogenerating this from the .proto file.

Basic Settings and Values 
-------------------------

.. py:class:: TripleBool

    A three-valued logic type.

    .. py:attribute:: TB_None
        :value: 0
    .. py:attribute:: TB_False
        :value: 1
    .. py:attribute:: TB_True
        :value: 2


.. class:: PropertyContainer


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


.. class:: CompressionType


.. class:: ExportFormat


.. class:: EM_DeliveryFormat


.. class:: EM_VideoExportOptions


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
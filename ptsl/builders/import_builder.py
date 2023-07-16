from ptsl import ops
from ptsl.PTSL_pb2 import SessionData, AudioData, \
    Session, \
    LinkToSourceAudio, CopyFromSourceAudio, ConsolidateFromSourceAudio, \
    ForceToTargetSessionFormat, \
    LinkToSourceVideo, CopyFromSourceVideo, \
    AddAudio, CopyAudio, ConvertAudio, Default, \
    MT_None, MT_MatchTracks, MT_ImportASNewTrack, \
    ImportReplaceExistingPlaylists, ImportOverlayNewOnExistingPlaylists, \
    DoNotImport, \
    TrackDataToImport, \
    MaintainAbsoluteTimeCodeValues, MaintainRelativeTimeCodeValues, \
    MapStartTimeCodeTo


    # AudioOperations, MediaDestination, MediaLocation


class ImportSessionDataBuilder:
    
    def __init__(self, engine, session_path: str):
        self._engine = engine
        self._session_path = session_path
        self._import_type = Session # the only type supported at present
        self._audio_media_option = LinkToSourceAudio
        self._video_media_option = LinkToSourceVideo
        self._handles_ms = 1000

        self._match_track_option = MT_None
        self._playlist_option = DoNotImport
        self._timecode_mapping_option = MaintainAbsoluteTimeCodeValues
        self._timecode_mapping_start_time = ""
        self._adjust_session_start = False

    def import_data(self): 
        import_type = self._import_type
        
        track_data_import = TrackDataToImport(
            track_data_preset_path="",
            clip_gain=True,
            clips_and_media=True,
            volume_automation=True
        )

        session_data = SessionData(
            audio_options=self._audio_media_option, 
            audio_handle_size=self._handles_ms,
            video_options=self._video_media_option,
            match_options=self._match_track_option, 
            playlist_options=self._playlist_option, 
            track_data_to_import=track_data_import, 
            timecode_mapping_units=self._timecode_mapping_option, 
            timecode_mapping_start_time=self._timecode_mapping_start_time,
            adjust_session_start_time_to_match_source=self._adjust_session_start
        )
        
        audio_data = AudioData(
            file_list=None,
            audio_operations=None,
            destination_path=None,
            destination=None,
            location=None
        )

        op = ops.Import(
            session_path=self._session_path,
            import_type=import_type,
            session_data=session_data,
            audio_data=audio_data
        )

        self._engine.client.run(op)

from ptsl import ops
from ptsl.PTSL_pb2 import SessionData, AudioData, \
    Session, \
    LinkToSourceAudio, CopyFromSourceAudio, ConsolidateFromSourceAudio, \
    ForceToTargetSessionFormat, \
    LinkToSourceVideo, CopyFromSourceVideo, \
    MT_None, MT_MatchTracks, MT_ImportAsNewTrack, \
    ImportReplaceExistingPlaylists, ImportOverlayNewOnExistingPlaylists, \
    DoNotImport, \
    TrackDataToImport, \
    MaintainAbsoluteTimeCodeValues, MaintainRelativeTimeCodeValues, \
    MapStartTimeCodeTo
# AddAudio, CopyAudio, ConvertAudio, Default, \

# AudioOperations, MediaDestination, MediaLocation


class ImportSessionDataBuilder:

    def __init__(self, engine, session_path: str):
        self._engine = engine
        self._session_path = session_path
        self._import_type = Session  # the only type supported at present
        self._audio_media_option = LinkToSourceAudio
        self._video_media_option = LinkToSourceVideo
        self._handles_ms = 1000

        self._match_track_option = MT_None
        self._playlist_option = DoNotImport
        self._track_data_preset = None
        self._import_clip_gain = False
        self._import_clips_and_media = False
        self._import_volume_automation = False

        self._timecode_mapping_option = MaintainAbsoluteTimeCodeValues
        self._timecode_mapping_start_time = ""
        self._adjust_session_start = False

    def link_to_source_audio(self):
        self._audio_media_option = LinkToSourceAudio

    def copy_from_source_audio(self):
        self._audio_media_option = CopyFromSourceAudio

    def consolidate_from_source_audio(self, handles_ms: int = 1000):
        self._audio_media_option = ConsolidateFromSourceAudio
        self._handles_ms = handles_ms

    def force_audio_to_session_format(self):
        self._audio_media_option = ForceToTargetSessionFormat

    def link_to_source_video(self):
        self._video_media_option = LinkToSourceVideo

    def copy_from_source_video(self):
        self._video_media_option = CopyFromSourceVideo

    def match_tracks(self):
        self._match_track_option = MT_MatchTracks

    def import_as_new_tracks(self):
        self._match_track_option = MT_ImportAsNewTrack

    def replace_playlists(self):
        self._playlist_option = ImportReplaceExistingPlaylists

    def overlay_playlists(self):
        self._playlist_option = ImportOverlayNewOnExistingPlaylists

    def use_track_data_preset(self, preset_path: str):
        self._track_data_preset = preset_path

    def import_clip_gain(self):
        self._import_clip_gain = True

    def import_clips_and_media(self):
        self._import_clips_and_media = True

    def import_volume_automation(self):
        self._import_volume_automation = True

    def maintain_absolute_timecode(self):
        self._timecode_mapping_option = MaintainAbsoluteTimeCodeValues

    def maintain_relative_timecode(self):
        self._timecode_mapping_option = MaintainRelativeTimeCodeValues

    def map_start_timecode(self, to_time: str):
        self._timecode_mapping_option = MapStartTimeCodeTo
        self._timecode_mapping_start_time = to_time

    def adjust_start_timecode_to_match_source(self):
        self._adjust_session_start = True

    def import_data(self):
        import_type = self._import_type

        track_data_import = TrackDataToImport(
            track_data_preset_path=self._track_data_preset,
            clip_gain=self._import_clip_gain,
            clips_and_media=self._import_clips_and_media,
            volume_automation=self._import_volume_automation
        )

        adj = self._adjust_session_start
        session_data = SessionData(
            audio_options=self._audio_media_option,
            audio_handle_size=self._handles_ms,
            video_options=self._video_media_option,
            match_options=self._match_track_option,
            playlist_options=self._playlist_option,
            track_data_to_import=track_data_import,
            timecode_mapping_units=self._timecode_mapping_option,
            timecode_mapping_start_time=self._timecode_mapping_start_time,
            adjust_session_start_time_to_match_source=adj,
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

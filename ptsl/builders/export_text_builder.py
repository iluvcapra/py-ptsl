from ptsl.PTSL_pb2 import DontShowCrossfades, ShowCrossfades, \
    CombineCrossfadedClips, BarsBeats, MinSecs, TimeCode, \
    FeetFrames, Samples, UTF8, TextEdit, ESI_String, ESI_File, \
    AllTracks, SelectedTracksOnly

import ptsl
from ptsl import ops


class ExportSessionTextBuilder:

    def __init__(self, engine: 'ptsl.Engine'):
        self._engine = engine
        self._include_clip_list = False
        self._include_file_list = False
        self._include_markers = False
        self._include_plugin_list = False
        self._include_track_edls = False
        self._show_sub_frames = False
        self._track_list_type = None
        self._include_user_timestamps = False
        self._fade_handling_type = DontShowCrossfades
        self._track_offset_options = TimeCode
        self._encoding = UTF8
        self._output_type = ESI_String
        self._output_path = None

    def include_clip_list(self):
        self._include_clip_list = True

    def include_file_list(self):
        self._include_file_list = True

    def include_markers(self):
        self._include_markers = True

    def include_plugin_list(self):
        self._include_plugin_list = True

    def include_track_edls(self):
        self._include_track_edls = True
        self._track_list_type = AllTracks

    def show_sub_frames(self):
        self._show_sub_frames = True

    def all_tracks(self):
        self._track_list_type = AllTracks

    def selected_tracks_only(self):
        self._track_list_type = SelectedTracksOnly

    def dont_show_crossfades(self):
        self._fade_handling_type = DontShowCrossfades

    def show_crossfades(self):
        self._fade_handling_type = ShowCrossfades

    def combine_crossfaded_clips(self):
        self._fade_handling_type = CombineCrossfadedClips

    def time_type(self, value: str):
        """
        Set the time type.

        :param value: A string indicating the time format. Can
            be "tc", "timecode", "bars+beats", "min:sec",
            "feet+frames". Any otrher value will set the time
            type to Samples.
        """
        if value in ["tc", "timecode"]:
            self._track_offset_options = TimeCode
        elif value == "bars+beats":
            self._track_offset_options = BarsBeats
        elif value == "min:sec":
            self._track_offset_options = MinSecs
        elif value == "feet+frames":
            self._track_offset_options = FeetFrames
        else:
            self._track_offset_options = Samples

    def utf8_encoding(self):
        self._encoding = UTF8

    def textedit_encoding(self):
        self._encoding = TextEdit

    def export_file(self, path: str) -> None:
        op = ops.ExportSessionInfoAsText(
            include_clip_list=self._include_clip_list,
            include_file_list=self._include_file_list,
            include_markers=self._include_markers,
            include_plugin_list=self._include_plugin_list,
            include_track_edls=self._include_track_edls,
            show_sub_frames=self._show_sub_frames,
            track_list_type=self._track_list_type,
            include_user_timestamps=self._include_user_timestamps,
            fade_handling_type=self._fade_handling_type,
            track_offset_options=self._track_offset_options,
            text_as_file_format=self._encoding,
            output_type=ESI_File,
            output_path=path)

        self._engine.client.run(op)

    def export_string(self) -> str:
        op = ops.ExportSessionInfoAsText(
            include_clip_list=self._include_clip_list,
            include_file_list=self._include_file_list,
            include_markers=self._include_markers,
            include_plugin_list=self._include_plugin_list,
            include_track_edls=self._include_track_edls,
            show_sub_frames=self._show_sub_frames,
            track_list_type=self._track_list_type,
            include_user_timestamps=self._include_user_timestamps,
            fade_handling_type=self._fade_handling_type,
            track_offset_options=self._track_offset_options,
            text_as_file_format=self._encoding,
            output_type=ESI_String,
            output_path=None)

        self._engine.client.run(op)
        return op.response.session_info

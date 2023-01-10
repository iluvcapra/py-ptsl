import json

from ptsl import PTSL_pb2 as pt

from ptsl.ops import Operation

class GetPlaybackMode(Operation):

    @staticmethod
    def request_body():
        return None

    @staticmethod
    def response_body():
        return pt.GetPlaybackModeResponseBody

    @staticmethod
    def command_id():
        return pt.GetPlaybackMode

    def __init__(self, *args, **kwargs) -> None:
        self.playback_modes = None
        super().__init__(*args, **kwargs)

    # FIXME: This is a bug that needs to be reported, the protobuf says this should
    # be integers from an enum but the server is returning string values
    def json_cleanup(self, in_json: str, ptsl_version) -> str:

        def xform(x):
            return pt.PM_PlaybackMode.Value(x)

        decoder = json.JSONDecoder()
        decoded = decoder.decode(in_json)
        decoded['current_settings'] = [xform(x) for x in decoded['current_settings']]
        decoded['possible_settings'] = [xform(x) for x in decoded['possible_settings']]
        encoder = json.JSONEncoder()
        encoded = encoder.encode(decoded)
        #print("Fixed playback mode:" + encoded)
        return encoded 


    def on_response_body(self, body: pt.GetPlaybackModeResponseBody):
        self.playback_modes = body.current_settings





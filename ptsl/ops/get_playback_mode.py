import json

from ptsl import PTSL_pb2 as pt

from ptsl.ops import Operation

class GetPlaybackMode(Operation):

    REQUEST_BODY=None
    RESPONSE_BODY=pt.GetPlaybackModeResponseBody
    COMMAND_ID=pt.GetPlaybackMode

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

        return encoded 




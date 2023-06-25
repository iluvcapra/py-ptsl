import json

from ptsl import PTSL_pb2 as pt

from ptsl.ops import Operation


class GetPlaybackMode(Operation):
    pass

    def json_cleanup(self, in_json: str) -> str:

        def xform(x):
            return pt.PM_PlaybackMode.Value(x)

        decoder = json.JSONDecoder()
        decoded = decoder.decode(in_json)
        if isinstance(['possible_settings'][0], str):
            decoded['current_settings'] = [
                xform(x) for x in decoded['current_settings']]
            decoded['possible_settings'] = [
                xform(x) for x in decoded['possible_settings']]
        encoder = json.JSONEncoder()
        encoded = encoder.encode(decoded)

        return encoded

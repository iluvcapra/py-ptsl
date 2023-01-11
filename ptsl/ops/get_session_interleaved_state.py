import json

from ptsl import PTSL_pb2 as pt

from ptsl.ops import Operation


class GetSessionInterleavedState(Operation):

    # Reported https://duc.avid.com/showthread.php?t=423087
    def json_cleanup(self, in_json: str, ptsl_version) -> str:
        decoder = json.decoder.JSONDecoder()
        parsed = decoder.decode(in_json)
        parsed["possible_settings"] = [True, False]
        encoder = json.encoder.JSONEncoder()
        return encoder.encode(parsed)


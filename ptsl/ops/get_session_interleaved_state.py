from typing import Optional
import json

from ptsl import PTSL_pb2 as pt

from ptsl.ops import Operation


class GetSessionInterleavedState(Operation):

    REQUEST_BODY=None
    RESPONSE_BODY=pt.GetSessionInterleavedStateResponseBody
    COMMAND_ID=pt.GetSessionInterleavedState

    # Reported https://duc.avid.com/showthread.php?t=423087
    def json_cleanup(self, in_json: str, ptsl_version) -> str:
        decoder = json.decoder.JSONDecoder()
        parsed = decoder.decode(in_json)
        parsed["possible_settings"] = [True, False]
        encoder = json.encoder.JSONEncoder()
        return encoder.encode(parsed)


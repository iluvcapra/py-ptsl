from typing import Optional
import json

from ptsl import PTSL_pb2 as pt

from ptsl.ops import Operation


class GetSessionInterleavedState(Operation):

    @staticmethod
    def request_body():
        return None

    @staticmethod
    def response_body():
        return pt.GetSessionInterleavedStateResponseBody

    @staticmethod
    def command_id():
        return pt.GetSessionInterleavedState

    def __init__(self) -> None:
        self.request = None
        self.interleaved = None

    # Reported https://duc.avid.com/showthread.php?t=423087
    def json_cleanup(self, in_json: str, ptsl_version) -> str:
        decoder = json.decoder.JSONDecoder()
        parsed = decoder.decode(in_json)
        parsed["possible_settings"] = [True, False]
        encoder = json.encoder.JSONEncoder()
        return encoder.encode(parsed)

    def on_response_body(self, body):
        self.interleaved = body.current_setting



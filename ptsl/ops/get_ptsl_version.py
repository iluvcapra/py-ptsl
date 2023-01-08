from typing import Optional

from ptsl import PTSL_pb2 as pt

from ptsl.ops import Operation

class GetPTSLVersion(Operation):

    request: None
    version: int

    def __init__(self) -> None:
        self.request = None
        self.version = None

    def command_id(self):
        return pt.GetPTSLVersion

    def response_body_prototype(self):
        return pt.GetPTSLVersionResponseBody()

    def on_empty_response_body(self):
        pass

    def on_response_body(self, body):
        self.version = body.version

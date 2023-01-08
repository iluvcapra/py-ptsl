from typing import Optional

from ptsl import PTSL_pb2 as pt

from ptsl.ops import Operation

class GetSessionName(Operation):

    request: None
    session_name: str

    def __init__(self) -> None:
        self.request = None
        self.session_name = None

    def command_id(self):
        return pt.GetSessionName

    def response_body_prototype(self):
        return pt.GetSessionNameResponseBody()

    def on_empty_response_body(self):
        pass

    def on_response_body(self, body):
        body: pt.GetSessionNameResponseBody
        self.session_name = body.session_name





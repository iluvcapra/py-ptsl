from typing import Optional

from ptsl import PTSL_pb2 as pt

from ptsl.ops import Operation

class GetSessionLength(Operation):

    request: None
    session_length: str

    def __init__(self) -> None:
        self.session_length = None
        super().__init__()

    def command_id(self):
        return pt.GetSessionLength

    def response_body_prototype(self):
        return pt.GetSessionLengthResponseBody()

    def on_response_body(self, body: pt.GetSessionLengthResponseBody):
        self.session_length = body.session_length





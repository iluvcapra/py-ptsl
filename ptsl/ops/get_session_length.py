from typing import Optional

from ptsl import PTSL_pb2 as pt

from ptsl.ops import Operation

class GetSessionLength(Operation):

    @staticmethod
    def request_body():
        return None

    @staticmethod
    def response_body():
        return pt.GetSessionLengthResponseBody

    @staticmethod
    def command_id():
        return pt.GetSessionLength

    def __init__(self) -> None:
        self.session_length = None
        super().__init__()

    def on_response_body(self, body: pt.GetSessionLengthResponseBody):
        self.session_length = body.session_length





from typing import Optional

from ptsl import PTSL_pb2 as pt

from ptsl.ops import Operation

class GetSessionName(Operation):

    @staticmethod
    def request_body():
        return None

    @staticmethod
    def response_body():
        return pt.GetSessionNameResponseBody

    @staticmethod
    def command_id():
        return pt.GetSessionName

    def __init__(self, *args, **kwargs) -> None:
        self.session_name = None
        super().__init__(*args, **kwargs)

    def on_response_body(self, body):
        body: pt.GetSessionNameResponseBody
        self.session_name = body.session_name





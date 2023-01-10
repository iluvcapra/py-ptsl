from typing import Optional

from ptsl import PTSL_pb2 as pt

from ptsl.ops import Operation

class GetSessionStartTime(Operation):

    @staticmethod
    def request_body():
        return None

    @staticmethod
    def response_body():
        return pt.GetSessionStartTimeResponseBody

    @staticmethod
    def command_id():
        return pt.GetSessionStartTime

    def __init__(self) -> None:
        self.start_time = None
        super().__init__()

    def on_response_body(self, body):
        self.start_time = body.session_start_time





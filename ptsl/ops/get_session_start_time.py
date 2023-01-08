from typing import Optional

from ptsl import PTSL_pb2 as pt

from ptsl.ops import Operation

class GetSessionStartTime(Operation):

    request: None
    start_time: str

    def __init__(self) -> None:
        self.audio_format = None
        super().__init__()

    def command_id(self):
        return pt.GetSessionStartTime

    def response_body_prototype(self):
        return pt.GetSessionStartTimeResponseBody()

    def on_response_body(self, body):
        self.start_time = body.session_start_time





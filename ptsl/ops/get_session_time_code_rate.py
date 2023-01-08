from typing import Optional

from ptsl import PTSL_pb2 as pt

from ptsl.ops import Operation

class GetSessionTimeCodeRate(Operation):

    request: None
    rate: pt.SessionTimeCodeRate

    def __init__(self) -> None:
        self.rate = None
        super().__init__()

    def command_id(self):
        return pt.GetSessionTimeCodeRate

    def response_body_prototype(self):
        return pt.GetSessionTimeCodeRateResponseBody()

    def on_empty_response_body(self):
        pass

    def on_response_body(self, body):
        self.rate = body.current_setting





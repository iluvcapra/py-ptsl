from typing import Optional

from ptsl import PTSL_pb2 as pt

from ptsl.ops import Operation

class GetSessionTimeCodeRate(Operation):

    @staticmethod
    def request_body():
        return None

    @staticmethod
    def response_body():
        return pt.GetSessionTimeCodeRateResponseBody

    @staticmethod
    def command_id():
        return pt.GetSessionTimeCodeRate

    def __init__(self) -> None:
        self.rate = None
        super().__init__()

    def on_empty_response_body(self):
        pass

    def on_response_body(self, body):
        self.rate = body.current_setting





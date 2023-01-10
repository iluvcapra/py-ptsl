from typing import Optional

from ptsl import PTSL_pb2 as pt

from ptsl.ops import Operation

class GetSessionFeetFramesRate(Operation):

    @staticmethod
    def request_body():
        return None

    @staticmethod
    def response_body():
        return pt.GetSessionFeetFramesRateResponseBody

    @staticmethod
    def command_id():
        return pt.GetSessionFeetFramesRate

    def __init__(self, *args, **kwargs) -> None:
        self.rate = None
        super().__init__(*args, **kwargs)

    def response_body_prototype(self):
        return pt.GetSessionFeetFramesRateResponseBody()

    def on_empty_response_body(self):
        pass

    def on_response_body(self, body):
        self.rate = body.current_setting





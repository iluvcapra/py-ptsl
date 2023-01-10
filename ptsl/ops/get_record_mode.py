from typing import Optional

from ptsl import PTSL_pb2 as pt

from ptsl.ops import Operation

class GetRecordMode(Operation):

    @staticmethod
    def request_body():
        return None

    @staticmethod
    def response_body():
        return pt.GetRecordModeResponseBody

    @staticmethod
    def command_id():
        return pt.GetRecordMode

    def __init__(self, **kwargs) -> None:
        self.record_state = None
        super().__init__(**kwargs)

    def on_empty_response_body(self):
        pass

    def on_response_body(self, body: pt.GetRecordModeResponseBody):
        self.record_state = body.current_setting

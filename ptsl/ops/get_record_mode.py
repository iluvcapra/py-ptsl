from typing import Optional

from ptsl import PTSL_pb2 as pt

from ptsl.ops import Operation

class GetRecordMode(Operation):

    request: None
    record_state: pt.RM_RecordMode

    def __init__(self) -> None:
        self.request = None
        self.record_state = None

    def command_id(self):
        return pt.GetRecordMode

    def response_body_prototype(self):
        return pt.GetRecordModeResponseBody()

    def on_empty_response_body(self):
        pass

    def on_response_body(self, body: pt.GetRecordModeResponseBody):
        self.record_state = body.current_setting

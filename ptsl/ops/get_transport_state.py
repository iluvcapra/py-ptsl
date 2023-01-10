from typing import Optional

from ptsl import PTSL_pb2 as pt

from ptsl.ops import Operation

class GetTransportState(Operation):

    @staticmethod
    def request_body():
        return None

    @staticmethod
    def response_body():
        return pt.GetTransportStateResponseBody

    @staticmethod
    def command_id():
        return pt.GetTransportState

    def __init__(self) -> None:
        self.request = None
        self.transport_state = None

    def on_response_body(self, body: pt.GetTransportStateResponseBody):
        self.transport_state = body.current_setting





from typing import Optional

from ptsl import PTSL_pb2 as pt

from ptsl.ops import Operation

class GetTransportState(Operation):

    request: None
    transport_state: pt.TS_TransportState

    def __init__(self) -> None:
        self.request = None
        self.transport_state = None

    def command_id(self):
        return pt.GetTransportState

    def response_body_prototype(self):
        return pt.GetTransportStateResponseBody()

    def on_empty_response_body(self):
        pass

    def on_response_body(self, body: pt.GetTransportStateResponseBody):
        self.transport_state = body.current_setting





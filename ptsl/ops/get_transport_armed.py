from typing import Optional
import json

from ptsl import PTSL_pb2 as pt

from ptsl.ops import Operation


class GetTransportArmed(Operation):

    request: None
    is_transport_armed: bool

    def __init__(self) -> None:
        self.request = None
        self.is_transport_armed = None

    def command_id(self):
        return pt.GetTransportArmed

    def response_body_prototype(self):
        return pt.GetTransportArmedResponseBody()

    def on_empty_response_body(self):
        pass

    def on_response_body(self, body: pt.GetTransportArmedResponseBody):
        self.is_transport_armed = body.is_transport_armed



from typing import Optional
import json

from ptsl import PTSL_pb2 as pt

from ptsl.ops import Operation


class GetTransportArmed(Operation):

    @staticmethod
    def request_body():
        return None

    @staticmethod
    def response_body():
        return pt.GetTransportArmedResponseBody

    @staticmethod
    def command_id():
        return pt.GetTransportArmed

    def __init__(self) -> None:
        self.request = None
        self.is_transport_armed = None

    def on_response_body(self, body: pt.GetTransportArmedResponseBody):
        self.is_transport_armed = body.is_transport_armed



import json

from ptsl import PTSL_pb2 as pt

from ptsl.ops import Operation


class CreateSession(Operation):

    request: pt.CreateSessionRequestBody

    def __init__(self, *args, **kwargs) -> None:
        self.request = pt.CreateSessionRequestBody(**kwargs)

    def command_id(self):
        return pt.CreateSession

    def on_empty_response_body(self):
        pass

    def on_response_body(self, _body):
        pass

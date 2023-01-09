import json

from ptsl import PTSL_pb2 as pt

from ptsl.ops import Operation


class ExportMix(Operation):

    request: pt.ExportMixRequestBody

    # FIXME: This does not fail if you ask it to create a new session on top 
    # of an old one
    def __init__(self, *args, **kwargs) -> None:
        self.request = pt.ExportMixRequestBody(**kwargs)

    def command_id(self):
        return pt.ExportMix

    def on_empty_response_body(self):
        pass

    def on_response_body(self, _body):
        pass

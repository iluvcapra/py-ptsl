from typing import Optional

from ptsl import PTSL_pb2 as pt

from ptsl.ops import Operation

class GetPTSLVersion(Operation):

    @staticmethod
    def request_body():
        return None

    @staticmethod
    def response_body():
        return pt.GetPTSLVersionResponseBody

    @staticmethod
    def command_id():
        return pt.GetPTSLVersion

    def __init__(self, *args, **kwargs) -> None:
        self.version = None
        super().__init__(*args, **kwargs)

    def on_empty_response_body(self):
        pass

    def on_response_body(self, body):
        self.version = body.version

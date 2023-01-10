from typing import Optional

from ptsl import PTSL_pb2 as pt

from ptsl.ops import Operation

class GetSessionPath(Operation):

    @staticmethod
    def request_body():
        return None

    @staticmethod
    def response_body():
        return pt.GetSessionPathResponseBody

    @staticmethod
    def command_id():
        return pt.GetSessionPath

    def __init__(self, *args, **kwargs) -> None:
        self.session_path = None
        self.is_online = None
        super().__init__(*args, **kwargs)

    def on_response_body(self, body: pt.GetSessionPathResponseBody):
        self.session_path = body.session_path.path
        self.is_online = body.session_path.info.is_online





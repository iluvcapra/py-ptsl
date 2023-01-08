from typing import Optional

from ptsl import PTSL_pb2 as pt

from ptsl.ops import Operation

class GetSessionPath(Operation):

    request: None
    session_path: str

    def __init__(self) -> None:
        self.request = None
        self.session_name = None

    def command_id(self):
        return pt.GetSessionPath

    def response_body_prototype(self):
        return pt.GetSessionPathResponseBody()

    def on_empty_response_body(self):
        pass

    def on_response_body(self, body):
        self.session_path = body.session_path.path
        self.is_online = body.session_path.info.is_online





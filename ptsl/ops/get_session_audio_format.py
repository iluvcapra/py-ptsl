from typing import Optional

from ptsl import PTSL_pb2 as pt

from ptsl.ops import Operation

class GetSessionAudioFormat(Operation):

    request: None
    audio_format: pt.FileType

    def __init__(self) -> None:
        self.audio_format = None
        super().__init__()

    def command_id(self):
        return pt.GetSessionAudioFormat

    def response_body_prototype(self):
        return pt.GetSessionAudioFormatResponseBody()

    def on_empty_response_body(self):
        pass

    def on_response_body(self, body):
        self.audio_format = body.current_setting





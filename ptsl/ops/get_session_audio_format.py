from typing import Optional

from ptsl import PTSL_pb2 as pt

from ptsl.ops import Operation

class GetSessionAudioFormat(Operation):

    @staticmethod
    def request_body():
        return None

    @staticmethod
    def response_body():
        return pt.GetSessionAudioFormatResponseBody

    @staticmethod
    def command_id():
        return pt.GetSessionAudioFormat

    def __init__(self, **kwargs) -> None:
        self.audio_format = None
        super().__init__(**kwargs)

    def on_empty_response_body(self):
        pass

    def on_response_body(self, body):
        self.audio_format = body.current_setting





from typing import Optional

from ptsl import PTSL_pb2 as pt

from ptsl.ops import Operation

class GetSessionAudioPullSettings(Operation):

    @staticmethod
    def request_body():
        return None

    @staticmethod
    def response_body():
        return pt.GetSessionAudioRatePullSettingsResponseBody

    @staticmethod
    def command_id():
        return pt.GetSessionAudioRatePullSettings

    def __init__(self, **kwargs) -> None:
        self.request = None
        self.pull_rate = None
        super().__init__(**kwargs)

    def on_empty_response_body(self):
        pass

    def on_response_body(self, body):
        self.pull_rate = body.current_setting





from typing import Optional

from ptsl import PTSL_pb2 as pt

from ptsl.ops import Operation

class GetSessionAudioPullSettings(Operation):

    request: None
    pull_rate: pt.SessionRatePull

    def __init__(self) -> None:
        self.request = None
        self.session_name = None

    def command_id(self):
        return pt.GetSessionAudioRatePullSettings

    def response_body_prototype(self):
        return pt.GetSessionAudioRatePullSettingsResponseBody()

    def on_empty_response_body(self):
        pass

    def on_response_body(self, body):
        self.pull_rate = body.current_setting





from typing import Optional

from ptsl import PTSL_pb2 as pt

from ptsl.ops import Operation

class GetSessionVideoPullSettings(Operation):

    request: None
    pull_rate: pt.SessionRatePull

    def __init__(self) -> None:
        self.request = None
        self.pull_rate = None

    def command_id(self):
        return pt.GetSessionVideoRatePullSettings

    def response_body_prototype(self):
        return pt.GetSessionVideoRatePullSettingsResponseBody()

    def on_empty_response_body(self):
        pass

    def on_response_body(self, body):
        self.pull_rate = body.current_setting

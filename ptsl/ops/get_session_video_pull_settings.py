from typing import Optional

from ptsl import PTSL_pb2 as pt

from ptsl.ops import Operation

class GetSessionVideoPullSettings(Operation):

    @staticmethod
    def request_body():
        return None

    @staticmethod
    def response_body():
        return pt.GetSessionVideoRatePullSettingsResponseBody

    @staticmethod
    def command_id():
        return pt.GetSessionVideoRatePullSettings

    def __init__(self) -> None:
        self.request = None
        self.pull_rate = None

    def on_response_body(self, body):
        self.pull_rate = body.current_setting

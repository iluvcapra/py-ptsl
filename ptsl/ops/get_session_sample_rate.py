from typing import Optional

from ptsl import PTSL_pb2 as pt

from ptsl.ops import Operation

class GetSessionSampleRate(Operation):

    @staticmethod
    def request_body():
        return None

    @staticmethod
    def response_body():
        return pt.GetSessionSampleRateResponseBody

    @staticmethod
    def command_id():
        return pt.GetSessionSampleRate
    
    def __init__(self, *args, **kwargs) -> None:
        self.request = None
        self.sample_rate_raw = None
        super().__init__(*args, **kwargs)

    def on_empty_response_body(self):
        pass

    def sample_rate(self) -> Optional[float]:
        if self.sample_rate_raw == pt.SR_192000:
            return 192000.0
        elif self.sample_rate_raw == pt.SR_176400:
            return 176400.0
        elif self.sample_rate_raw == pt.SR_96000:
            return 96000.0
        elif self.sample_rate_raw == pt.SR_48000:
            return 48000.0
        elif self.sample_rate_raw == pt.SR_44100:
            return 44100.0
        elif self.sample_rate_raw == pt.SR_None:
            return None

    def on_response_body(self, body):
        body: pt.GetSessionSampleRateResponseBody
        self.sample_rate_raw = body.sample_rate





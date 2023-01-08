from typing import Optional

from ptsl import PTSL_pb2 as pt

from ptsl.ops import Operation

class GetSessionSampleRate(Operation):

    request: None
    sample_rate_raw: pt.SampleRate

    def __init__(self) -> None:
        self.request = None
        self.sample_rate_raw = None

    def command_id(self):
        return pt.GetSessionSampleRate

    def response_body_prototype(self):
        return pt.GetSessionSampleRateResponseBody()

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





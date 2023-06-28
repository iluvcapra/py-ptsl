from typing import Optional

from ptsl import PTSL_pb2 as pt

from ptsl.ops import Operation


class GetSessionSampleRate(Operation):

    def sample_rate(self) -> Optional[float]:
        if self.response.sample_rate == pt.SR_192000:
            return 192000.0
        elif self.response.sample_rate == pt.SR_176400:
            return 176400.0
        elif self.response.sample_rate == pt.SR_96000:
            return 96000.0
        elif self.response.sample_rate == pt.SR_48000:
            return 48000.0
        elif self.response.sample_rate == pt.SR_44100:
            return 44100.0
        else:
            return None

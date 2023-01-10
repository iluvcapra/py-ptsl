from typing import Optional

from ptsl import PTSL_pb2 as pt

from ptsl.ops import Operation

class GetSessionTimeCodeRate(Operation):

    REQUEST_BODY=None
    RESPONSE_BODY=pt.GetSessionTimeCodeRateResponseBody
    COMMAND_ID=pt.GetSessionTimeCodeRate





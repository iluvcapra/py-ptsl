from typing import Optional

from ptsl import PTSL_pb2 as pt

from ptsl.ops import Operation

class GetSessionFeetFramesRate(Operation):

    REQUEST_BODY=None
    RESPONSE_BODY=pt.GetSessionFeetFramesRateResponseBody
    COMMAND_ID=pt.GetSessionFeetFramesRate






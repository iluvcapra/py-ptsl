from typing import Optional

from ptsl import PTSL_pb2 as pt

from ptsl.ops import Operation

class GetSessionStartTime(Operation):

    REQUEST_BODY=None
    RESPONSE_BODY=pt.GetSessionStartTimeResponseBody
    COMMAND_ID=pt.GetSessionStartTime





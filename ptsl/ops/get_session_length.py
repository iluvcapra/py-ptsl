from typing import Optional

from ptsl import PTSL_pb2 as pt

from ptsl.ops import Operation

class GetSessionLength(Operation):

    REQUEST_BODY=None
    RESPONSE_BODY=pt.GetSessionLengthResponseBody
    COMMAND_ID=pt.GetSessionLength





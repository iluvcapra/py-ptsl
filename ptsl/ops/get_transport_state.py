from typing import Optional

from ptsl import PTSL_pb2 as pt

from ptsl.ops import Operation

class GetTransportState(Operation):

    REQUEST_BODY=None
    RESPONSE_BODY=pt.GetTransportStateResponseBody
    COMMAND_ID=pt.GetTransportState


from typing import Optional
import json

from ptsl import PTSL_pb2 as pt

from ptsl.ops import Operation


class GetTransportArmed(Operation):

    REQUEST_BODY=None
    RESPONSE_BODY=pt.GetTransportArmedResponseBody
    COMMAND_ID=pt.GetTransportArmed

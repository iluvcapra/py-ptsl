from typing import Optional

from ptsl import PTSL_pb2 as pt

from ptsl.ops import Operation

class GetSessionName(Operation):
    REQUEST_BODY = None
    RESPONSE_BODY = pt.GetSessionNameResponseBody
    COMMAND_ID = pt.GetSessionName





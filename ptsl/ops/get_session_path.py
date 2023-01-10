from typing import Optional

from ptsl import PTSL_pb2 as pt

from ptsl.ops import Operation

class GetSessionPath(Operation):
    REQUEST_BODY= None
    RESPONSE_BODY=pt.GetSessionPathResponseBody
    COMMAND_ID=pt.GetSessionPath



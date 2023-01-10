from ptsl import PTSL_pb2 as pt

from ptsl.ops import Operation

class CloseSession(Operation):
    REQUEST_BODY=pt.CloseSessionRequestBody
    COMMAND_ID=pt.CloseSession
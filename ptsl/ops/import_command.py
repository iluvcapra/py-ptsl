
from ptsl import PTSL_pb2 as pt

from .operation import Operation

class Import(Operation):
    REQUEST_BODY= pt.ImportRequestBody
    RESPONSE_BODY= pt.ImportResponseBody
    COMMAND_ID= pt.Import
from ptsl import PTSL_pb2 as pt

from ptsl.ops import Operation

class Cut(Operation):
    COMMAND_ID=pt.Cut
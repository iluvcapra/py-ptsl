from ptsl import PTSL_pb2 as pt

from ptsl.ops import Operation

class SaveSession(Operation):
    COMMAND_ID=pt.SaveSession
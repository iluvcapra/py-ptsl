from ptsl import PTSL_pb2 as pt

from ptsl.ops import Operation

class ConsolidateClip(Operation):
    COMMAND_ID=pt.ConsolidateClip
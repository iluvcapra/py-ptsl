from ptsl import PTSL_pb2 as pt

from ptsl.ops import Operation

class TrimToSelection(Operation):

    @staticmethod
    def command_id():
        return pt.TrimToSelection
from ptsl import PTSL_pb2 as pt

from ptsl.ops import Operation

class SaveSession(Operation):

    @staticmethod
    def command_id():
        return pt.SaveSession
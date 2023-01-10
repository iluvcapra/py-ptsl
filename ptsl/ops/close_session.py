from ptsl import PTSL_pb2 as pt

from ptsl.ops import Operation

class CloseSession(Operation):

    @staticmethod
    def request_body():
        return pt.CloseSessionRequestBody

    @staticmethod
    def command_id():
        return pt.CloseSession
import json

from ptsl import PTSL_pb2 as pt

from ptsl.ops import Operation


class ExportMix(Operation):

    @staticmethod
    def request_body():
        return pt.ExportMixRequestBody

    @staticmethod
    def response_body():
        return None

    @staticmethod
    def command_id():
        return pt.ExportMix


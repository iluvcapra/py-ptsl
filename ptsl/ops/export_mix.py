import json

from ptsl import PTSL_pb2 as pt

from ptsl.ops import Operation


class ExportMix(Operation):
    REQUEST_BODY=pt.ExportMixRequestBody
    COMMAND_ID=pt.ExportMix


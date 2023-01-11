from ptsl import PTSL_pb2 as pt

from .operation import Operation

class CreateFadesBasedOnPreset(Operation):
    REQUEST_BODY=pt.CreateFadesBasedOnPresetRequestBody
    RESPONSE_BODY=pt.CreateFadesBasedOnPresetResponseBody
    COMMAND_ID=pt.CreateFadesBasedOnPreset
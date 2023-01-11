from ptsl import PTSL_pb2 as pt

from .operation import Operation

class ExtendSelectionToTargetTracks(Operation):
    REQUEST_BODY=pt.ExtendSelectionToTargetTracksRequestBody
    RESPONSE_BODY=pt.ExtendSelectionToTargetTracksResponseBody
    COMMAND_ID=pt.ExtendSelectionToTargetTracks
    
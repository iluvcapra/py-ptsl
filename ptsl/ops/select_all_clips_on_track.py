
from ptsl import PTSL_pb2 as pt

from .operation import Operation

class SelectAllClipsOnTrack(Operation):
    REQUEST_BODY=pt.SelectAllClipsOnTrackRequestBody
    RESPONSE_BODY=pt.SelectAllClipsOnTrackResponseBody
    COMMAND_ID=pt.SelectAllClipsOnTrack
from typing import Optional

from ptsl import PTSL_pb2 as pt

from ptsl.ops import Operation

class GetSessionAudioFormat(Operation):

    REQUEST_BODY= None
    RESPONSE_BODY=pt.GetSessionAudioFormatResponseBody
    COMMAND_ID=pt.GetSessionAudioFormat

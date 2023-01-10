from typing import Optional

from ptsl import PTSL_pb2 as pt

from ptsl.ops import Operation

class GetSessionVideoPullSettings(Operation):

    REQUEST_BODY=None
    RESPONSE_BODY=pt.GetSessionVideoRatePullSettingsResponseBody
    COMMAND_ID=pt.GetSessionVideoRatePullSettings


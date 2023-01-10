from ptsl import PTSL_pb2 as pt

from ptsl.ops import Operation


# There is a documented bug with this, it won't return a string
# if you select ESI_string as the output_type
#
# https://duc.avid.com/showthread.php?t=422971
class ExportSessionInfoAsText(Operation):

    @staticmethod
    def request_body():
        return pt.ExportSessionInfoAsTextRequestBody

    @staticmethod
    def response_body():
        return pt.ExportSessionInfoAsTextResponseBody

    @staticmethod
    def command_id():
        return pt.ExportSessionInfoAsText

    def __init__(self, *args, **kwargs) -> None:
        self.session_info = None
        super().__init__(*args, **kwargs)

    def on_response_body(self, body: pt.ExportSessionInfoAsTextResponseBody):
        self.session_info = body.session_info

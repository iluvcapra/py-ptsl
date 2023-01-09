from ptsl import PTSL_pb2 as pt

from ptsl.ops import Operation


# There is a documented bug with this, it won't return a string
# if you select ESI_string as the output_type
#
# https://duc.avid.com/showthread.php?t=422971
class ExportSessionInfoAsText(Operation):

    request: pt.ExportMixRequestBody
    session_info: str

    def __init__(self, *args, **kwargs) -> None:
        self.session_info = ""
        self.request = pt.ExportSessionInfoAsTextRequestBody(**kwargs)

    def command_id(self):
        return pt.ExportSessionInfoAsText

    def response_body_prototype(self):
        return pt.ExportSessionInfoAsTextResponseBody()

    def on_empty_response_body(self):
        pass

    def on_response_body(self, body: pt.ExportSessionInfoAsTextResponseBody):
        self.session_info = body.session_info

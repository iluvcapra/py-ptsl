from ptsl import PTSL_pb2 as pt

from ptsl.ops import Operation


# There is a documented bug with this, it won't return a string
# if you select ESI_string as the output_type
#
# https://duc.avid.com/showthread.php?t=422971
class ExportSessionInfoAsText(Operation):

    #FIXME: Pro Tools doesn't seem to return a response body
    @classmethod
    def response_body(cls):
        return None

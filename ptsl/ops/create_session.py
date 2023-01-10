import json

from ptsl import PTSL_pb2 as pt

from ptsl.ops import Operation

# FIXME: This does not fail if you ask it to create a new session on top 
# of an old one
class CreateSession(Operation):

    @staticmethod
    def request_body():
        return pt.CreateSessionRequestBody

    @staticmethod
    def response_body():
        return None

    @staticmethod
    def command_id():
        return pt.CreateSession


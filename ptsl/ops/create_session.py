import json

from ptsl import PTSL_pb2 as pt

from ptsl.ops import Operation

# FIXME: This does not fail if you ask it to create a new session on top 
# of an old one
class CreateSession(Operation):
    REQUEST_BODY=pt.CreateSessionRequestBody
    COMMAND_ID=pt.CreateSession


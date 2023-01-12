# make_session.py
#
# This example demonstrates how to create a new file with the `Engine` class

import ptsl
from ptsl import PTSL_pb2 as pt
from ptsl import open_engine
import os
import sys

api_key = os.getenv('PTSL_KEY', default=None)

if len(sys.argv) < 3 or api_key is None:
    print("Usage: %s <path> <session-name>" % sys.argv[0])
    print("env vairable PTSL_KEY must be set to the path to your developer key")
    exit(-1)

with ptsl.open_engine(api_key) as e:
    e.create_session(name=sys.argv[2], path=sys.argv[1])

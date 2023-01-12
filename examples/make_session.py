import ptsl
from ptsl import PTSL_pb2 as pt
from ptsl import open_engine

import sys

if len(sys.argv) < 4:
    print("Usage: %s <json-dev-key> <path> <session-name>" % sys.argv[0])

with ptsl.open_engine(sys.argv[1]) as e:
    e.create_session(name=sys.argv[3], path=sys.argv[2])


    
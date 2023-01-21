# make_session.py
#
# This example demonstrates how to create a new file with the `ptsl.Engine` class

import ptsl
from ptsl import PTSL_pb2 as pt
from ptsl import open_engine
import os
import sys


if len(sys.argv) < 3:
    print("Usage: %s <path> <session-name>" % sys.argv[0])
    exit(-1)

with ptsl.open_engine() as e:
    e.create_session(name=sys.argv[2], path=sys.argv[1])

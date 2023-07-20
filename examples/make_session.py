# make_session.py
#
# This example demonstrates how to create a new file with the `
# ptsl.Engine` class

import sys
import ptsl

import os.path

with ptsl.open_engine(company_name="py-ptsl",
                      application_name=sys.argv[0]) as e:
    print("Creating new session:")
    path = input("Session path: ")
    name = input("Session name: ")
    builder = e.create_session(name=name, path=os.path.expanduser(path))
    builder.sample_rate(int(input("Sample rate: ")))
    builder.bit_depth(int(input("Bit Depth: ")))
    if input("WAVE or AIFF? ").startswith(("A","a")):
        builder.aiff_format()
    else:
        builder.wave_format()

    builder.create()




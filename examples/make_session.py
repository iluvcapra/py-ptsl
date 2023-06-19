# make_session.py
#
# This example demonstrates how to create a new file with the `
# ptsl.Engine` class

import sys
import ptsl


if len(sys.argv) < 3:
    print(f"Usage: {sys.argv[0]} <path> <session-name>")
    sys.exit(-1)

with ptsl.open_engine(company_name="py-ptsl",
                      application_name=sys.argv[0]) as e:
    e.create_session(name=sys.argv[2], path=sys.argv[1])

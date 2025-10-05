# py-ptsl main

import sys
from optparse import OptionParser
import json
from typing import Optional

from .client import Client
from .PTSL_pb2 import CommandId

def main(tool_name="ptsl"):
    oparse = OptionParser()
    oparse.usage= f"{tool_name} [-v] [-j JSON] COMMAND"
    oparse.add_option('-v','--verbose', action='store_true', 
                      help="Verbose output")
    oparse.add_option('-j','--json', action='store', 
                      help="Request JSON to pass (instead of stdin)")
    
    (options, args) = oparse.parse_args()

    assert len(args) == 1, ("Incorrect number of arguments, only one "
                             "commmand allowed")

    client = Client(company_name="py-ptsl", application_name="ptsl")

    if options.verbose:
        client.auditor.enabled = True
    
    request_json: Optional[str] = None
    if options.json:
        request_json = options.json
    else:
        request_json = sys.stdin.read()

    command_id: Optional[int] = None
    for command_name in CommandId.keys():
        if args[0] == command_name:
            command_id = CommandId.Value(args[0])

    assert command_id is not None, f"Command `{args[0]}` was not recognized"

    if request_json:
        request = json.loads(request_json)
        assert isinstance(request, dict), "Provided JSON must be an object"

    else:
        request = dict()

    response = client.run_command(command_id=command_id, request=request)

    print(response)

if __name__ == "__main__":
    main()

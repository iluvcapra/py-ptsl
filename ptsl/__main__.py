# py-ptsl main

import sys
from optparse import OptionParser
import json
from typing import Optional

from .client import Client
from .errors import CommandError
from .PTSL_pb2 import CommandId


def main(tool_name="ptsl"):
    oparse = OptionParser(usage=f"python3 -m {tool_name} [options] COMMAND")
    oparse.add_option('-v', '--verbose', action='store_true',
                      help="Verbose output")
    oparse.add_option('-f', '--file', action='store', metavar="FILE",
                      help="Get Request JSON from FILE instead of stdin")
    oparse.add_option('-n', '--no-input', action='store_true',
                      help="Request JSON should be empty, ignore stdin")
    oparse.add_option('--list', action='store_true',
                      help="Print all available commands and exit")

    (options, args) = oparse.parse_args()

    if options.list:
        for command_name in CommandId.keys():
            print(command_name)

        return

    assert len(args) > 0, ("Command not given")

    assert len(args) == 1, ("Incorrect number of arguments, only one "
                            "commmand allowed")

    request_json: Optional[str] = None
    if options.no_input:
        pass
    elif options.file:
        with open(options.file, 'r') as f:
            request_json = f.read()
    else:
        request_json = sys.stdin.read()

    command_id: Optional[int] = None
    for command_name in CommandId.keys():
        if args[0] == command_name:
            command_id = CommandId.Value(args[0])

    assert command_id is not None, f"Command `{args[0]}` was not recognized"

    if request_json:
        request = json.loads(request_json or "{}")
        assert isinstance(request, dict), "Provided JSON must be an object"

    else:
        request = dict()

    client = Client(company_name="py-ptsl", application_name="ptsl")

    if options.verbose:
        print("Verbose logging enabled", file=sys.stderr)
        client.auditor.enabled = True

    try:
        response = client.run_command(command_id=command_id, request=request)

        if response:
            response_json = json.dumps(response)
            print(response_json)

        else:
            print(">>> No Response", file=sys.stderr)

    except CommandError as e:
        print(e, file=sys.stderr)
        for response in e.error_responses:
            print(e, file=sys.stderr)


if __name__ == "__main__":
    main()

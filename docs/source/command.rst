Run py-ptsl from the Command Line 
===================================

``py-ptsl`` implements a main function and can be run from a shell directly.

.. code-block:: bash 

   bash$ poetry run python3 -m ptsl GetTrackList << JSON 
   {
   "pagination_request": {
     "limit": 100, "offset": 0
     },
   "track_filter_list": [
     {"filter": 0, "is_inverted": false}
     ]
   }
   JSON 

Usage 
~~~~~

**ptsl** *[options]* COMMAND 

**COMMAND**
  Name of the PTSL command to run.

The tool will read the command's Request JSON from stdin and if there is a 
Response from Pro tools, it will emit the JSON to stdout. 

If the command has no Response, nothing will be written to stdout and the 
message ``< No Response >`` will be printed to stderr.

.. note::
  For command names and documentation of the Command Request and Response forms
  refer to Avid's PTSL documentation.


Options 
~~~~~~~

-v, --verbose   Verbose output

-f FILE, --file=FILE    Get Request JSON from ``FILE`` instead of stdin

-n, --no-input   Request JSON is empty, ignore stdin

--list    Print all available commands and exit

--help    Print help summary and exit


Exit Status
~~~~~~~~~~~

0
  Success

1
  Internal failures, gRPC failure, failed assertions, bad arguments 

2
  PTSL error response




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

COMMAND
  Name of the PTSL command to run

Options 
~~~~~~~

-v, --verbose   Verbose output

-f FILE, --file FILE    Get Request JSON from FILE instead of stdin

-n, --no-input   Request JSON is iempty, ignore stdin

--list    Print all available commands and exit

--help  Print help summary and exit

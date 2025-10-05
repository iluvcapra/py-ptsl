#!/usr/bin/env bash

poetry run python3 -m ptsl CreateSession <<JSON 
{"session_name": "Test Session", 
"session_location": "/Users/j/Desktop",
"file_type": "FT_WAVE",
"sample_rate": "SR_48000",
"bit_depth": "Bit24",
"input_output_settings": "IO_Last",
"is_interleaved": true,
"is_cloud_project": false,
"create_from_template": false,
"template_group": "",
"template_name": ""
}
JSON

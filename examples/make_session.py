import sys

import ptsl
from ptsl import PTSL_pb2 as pt
from ptsl.ops import *

with ptsl.open_client(sys.argv[1]) as client:
    op = CreateSession(
        session_name="New Session",
        create_from_template=False,
        template_group=None,
        template_name=None,
        file_type=pt.FT_WAVE,
        sample_rate=pt.SR_48000,
        input_output_settings=pt.IO_Last,
        is_interleaved=True,
        session_location="Macintosh HD:Users:jamie:",
        is_cloud_project=False, 
        create_from_aaf=False,
        path_to_aaf=None,
        bit_depth=pt.Bit24   
    )

    client.run(op)

    
import ptsl
from ptsl import PTSL_pb2 as pt
from ptsl.ops import *

import sys

with ptsl.open_client(sys.argv[1]) as client:
    op = ExportSessionInfoAsText(
        include_file_list = False,
        include_clip_list = False,
        include_markers = True,
        include_track_edls = False,
        show_sub_frames = False,
        include_user_timestamps = False,
        text_as_file_format=pt.UTF8,
        output_type=pt.ESI_String,
        output_path="Macintosh HD:Users:jamie:Output.txt"
    )

    client.run(op)

    print(op.session_info)

    
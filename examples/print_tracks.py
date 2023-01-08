import sys
import os.path

import ptsl
from ptsl import PTSL_pb2 as pt
from ptsl.ops import *

print("#: %5s : %-13s : %-32s : %9s : %s" % ("ATTRS", "TYPE","NAME","COLOR","ID"))

with ptsl.open_client(sys.argv[1]) as client:
    tracks_op = GetTrackList(
        page_limit=1000, 
        track_filter_list=[pt.TrackListInvertibleFilter(filter=pt.AllTracks, is_inverted=False)]
        )

    client.run(tracks_op)

    for track in tracks_op.track_list:
        mode = list("     ")
        if track.track_attributes.is_selected:
            mode[0] = "*"
        if track.track_attributes.is_soloed:
            mode[1] = "S"
        if track.track_attributes.is_muted:
            mode[2] = "M"
        if track.track_attributes.is_hidden:
            mode[3] = "H"
        if track.track_attributes.is_inactive:
            mode[4] = "X"

        mode = ''.join(mode)

        print("%i: %5s : %-13s : %-32s : %9s : %s" % (track.index, mode, pt.TrackType.Name(track.type), track.name[0:32], track.color , track.id))

    # for track in tracks_op.track_list:
    #     print(track)
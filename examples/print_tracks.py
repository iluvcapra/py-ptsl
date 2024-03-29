# print_tracks.py
#
# This example demonstrates getting a list of tracks.
#
# ```sh
# $  python3 examples/print_tracks.py
# #: ATTRS : TYPE          : NAME
# 1: *     : RoutingFolder : Folder 2
# 2: *S    : AudioTrack    : A1
# 3: *     : AudioTrack    : A2
# 4:       : BasicFolder   : Folder 1
# 5:  SM   : Vca           : VCA 1
# 6:       : Vca           : VCA 2
# 7:       : AudioTrack    : B1
# 8:    HX : AudioTrack    : B2
# ```

import sys

from ptsl import open_engine
from ptsl import PTSL_pb2 as pt

print("#: %5s : %-13s : %-32s : %9s : %s" %
      ("ATTRS", "TYPE", "NAME", "COLOR", "ID"))

with open_engine(company_name="py-ptsl",
                 application_name=sys.argv[0]) as engine:

    track_list = engine.track_list()

    for track in track_list:
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

        print("%i: %5s : %-13s : %-32s : %9s : %s" %
              (track.index, mode, pt.TrackType.Name(track.type),
               track.name[0:32], track.color, track.id))

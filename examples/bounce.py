# bounce.py
#
# This is Jamie taking a look at the streaming RPC. At this time the "progress"
# field in GetTaskStatus is not being updated by Pro Tools so I don't see any 
# reason to continue to develop this feature at this time. 
#
# I've posted about this bug at https://duc.avid.com/showthread.php?p=2658650#post2658650

import os

from ptsl import open_engine, CommandError
from ptsl import PTSL_pb2 as pt
from ptsl.ops import ExportMix, GetTaskStatus

with open_engine(os.getenv('PTSL_KEY')) as engine:
    client = engine.client

    op = ExportMix(
        file_name="test.wav",
        file_type=pt.EM_WAV,
        files_list=[pt.EM_SourceInfo(source_type=pt.Bus, name="FX 1")],
        audio_info=pt.EM_AudioInfo(
            compression_type=pt.CT_None, 
            export_format=pt.EF_Interleaved,
            bit_depth=pt.Bit24,
            sample_rate=pt.SR_48000,
            pad_to_frame_boundary=False,
            delivery_format=pt.EM_DF_FilePerMixSource),
        location_info=pt.EM_LocationInfo(
            import_after_bounce=pt.TB_False,
            import_options=None,
            file_destination=pt.EM_FD_SessionFolder,
            directory=""
        ),
        offline_bounce=pt.TB_True
    )

    r = client.__launch_test(op)
    print(op)
    print(op.task_id)

    import time

    for _ in range(100):
        time.sleep(0.5)

        stat_op = GetTaskStatus(
            task_id = op.task_id
        )

        try:
            client.run(stat_op)
            print("Status: %s" % pt.TaskStatus.Name(stat_op.response.status))
            print("Progress: %i" % stat_op.response.progress)
        except CommandError as e:
            print(e.message)
            break



import sys
import os.path

import ptsl
from ptsl import PTSL_pb2 as pt
from ptsl.ops import *

with ptsl.open_client(sys.argv[1]) as client:
    
    try:
        get_ptsl_version_op = GetPTSLVersion()
        client.run(get_ptsl_version_op)
        print("PTSL Version: %i" % get_ptsl_version_op.version)

        get_session_name_op = GetSessionName()
        client.run(get_session_name_op)
        print("Session Name: %s" % get_session_name_op.session_name)

        get_session_path_op = GetSessionPath()
        client.run(get_session_path_op)
        print("Session Path: %s" % get_session_path_op.session_path)

        get_sample_rate_op = GetSessionSampleRate()
        client.run(get_sample_rate_op)
        sr = get_sample_rate_op.sample_rate_raw
        print("Session Sample Rate: %s" % pt.SampleRate.Name(sr))

        get_session_audio_format_op = GetSessionAudioFormat()
        client.run(get_session_audio_format_op)
        print("Session Audio Format: %s" % pt.FileType.Name(get_session_audio_format_op.audio_format))

        # Does not work, seems to be a bug in Pro Tools
        get_session_interleaved_state_op = GetSessionInterleavedState()
        client.run(get_session_interleaved_state_op)
        print("Session Interleaved: " + ("TRUE" if get_session_interleaved_state_op.interleaved else "FALSE"))

        get_session_tc_rate_op = GetSessionTimeCodeRate()
        client.run(get_session_tc_rate_op)
        print("Session Timecode Rate: %s" % pt.SessionTimeCodeRate.Name(get_session_tc_rate_op.rate))

        get_session_start_time_op = GetSessionStartTime()
        client.run(get_session_start_time_op)
        print("Session Start Time: %s" % get_session_start_time_op.start_time)

        get_session_ff_op = GetSessionFeetFramesRate()
        client.run(get_session_ff_op)
        print("Session Feet+Frames Rate: %s" % pt.SessionFeetFramesRate.Name(get_session_ff_op.rate))

    except ptsl.client.CommandError as e:
        print("Command Error:" + e)
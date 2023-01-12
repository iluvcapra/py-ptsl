import sys

from ptsl import open_engine, CommandError
from ptsl.PTSL_pb2 import PT_NoOpenedSession

with open_engine(api_key_path=sys.argv[1]) as engine:
    
    try:
        print("PTSL Version: %i" % engine.ptsl_version())
        print("Session Name: %s" % engine.session_name())
        print("Session Path: %s" % engine.session_path())
        print("Session Sample Rate: %i" % engine.session_sample_rate())
        print("Session Audio Format: %s" % engine.session_audio_format())
        print("Session Audio Interlaved: %s" % "TRUE" if engine.session_interleaved_state() else "FALSE")

        tc = engine.session_timecode_rate()
        print("Session Timecode Rate: %.03f %s" % (float(tc[0]) / float(tc[1]), "Drop" if tc[2] else "Non-Drop"))

        print("Session Start Time: %s" % engine.session_start_time())
        print("Session Length: %s" % engine.session_length())

        ff = engine.session_feet_frames_rate()
        print("Session feet+frames rate: %.03f" % (float(ff[0]) / float(ff[1])))

        # FIXME: print these out maybe
        ap = engine.session_audio_pull()
        vp = engine.session_video_pull()

        print("-------------------------------")
        print("Transport State: %s " % engine.transport_state())
        print("Transport Arm: %s" % ("ARMED" if engine.transport_armed() else "SAFE"))

        pbm = engine.playback_modes()
        pbms = []
        if pbm[0]: pbms.append("Normal")
        if pbm[1]: pbms.append("Loop")
        if pbm[2]: pbms.append("Dynamic Transport")
        print("Playback Modes: %s" % ", ".join(pbms))

        print("Record Mode: %s" % engine.record_mode())


    except CommandError as e:
        if e.error_response.command_error_type == PT_NoOpenedSession:
            print("No Opened Session, exiting!")
        else:
            print("Command Error, exiting")

# session_info.py
# 
# This example demonstrates various getter methods of the `ptsl.Engine`
# class.

import sys
import os

from ptsl import open_engine, CommandError
from ptsl.PTSL_pb2 import PT_NoOpenedSession
import ptsl.PTSL_pb2 as pt

key_path = os.getenv('PTSL_KEY')

with open_engine(api_key_path=key_path) as engine:
    
    try:
        print("PTSL Version: %i" % engine.ptsl_version())
        print("Session Name: %s" % engine.session_name())
        print("Session Path: %s" % engine.session_path())
        print("Session Sample Rate: %i" % engine.session_sample_rate())
        print("Session Audio Format: %s" % 
            pt.SessionAudioFormat.Name(engine.session_audio_format()))

        print("Session Bit Depth: %s" % 
            pt.BitDepth.Name(engine.session_bit_depth()))
            
        print("Session Audio Interlaved: %s" % "TRUE" if engine.session_interleaved_state() else "FALSE")

        tc = engine.session_timecode_rate()
        print("Session Timecode Rate: %s" % 
            pt.SessionTimeCodeRate.Name(engine.session_timecode_rate()))

        print("Session Start Time: %s" % engine.session_start_time())
        print("Session Length: %s" % engine.session_length())

        ff = engine.session_feet_frames_rate()
        print("Session feet+frames rate: %s" % 
        pt.SessionFeetFramesRate.Name(engine.session_feet_frames_rate()))

        print("Session Audio Rate Pull: %s" % 
            pt.SessionRatePull.Name(engine.session_audio_pull()))
        
        print("Session Video Rate Pull: %s" %
            pt.SessionRatePull.Name(engine.session_video_pull()))

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

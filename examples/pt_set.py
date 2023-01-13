# pt_set.py
# 
# This example demonstrates some of the set_* functions of the
# `ptsl.Engine`.

import optparse
from ptsl import open_engine, CommandError
import ptsl.PTSL_pb2 as pt

import os

def process_option(opts, name, tipo, set_method):
    val = getattr(opts, name)

    if val is None:
        return

    if tipo is str:
        set_method(val)
        return
    
    if tipo is bool:
        val = True if val.capitalize() == 'TRUE' else False
        set_method(val)
        return

    if val not in tipo.keys():
        print("%s: Unrecognized value '%s'" % (name, val))
        print("Allowed values: %s" % tipo.keys())
    else:
        set_method(getattr(pt, val))


p = optparse.OptionParser()
p.add_option("-K", nargs=1, help="Developer key file")
p.add_option("--playback-mode", nargs=1)
p.add_option("--record-mode", nargs=1)
p.add_option("--audio-format", nargs=1)
p.add_option("--bit-depth", nargs=1)
p.add_option("--interleaved-state", nargs=1)
p.add_option("--timecode-rate", nargs=1)
p.add_option("--feetframes-rate", nargs=1)
p.add_option("--audio-pull", nargs=1)
p.add_option("--video-pull", nargs=1)
p.add_option("--start-time", nargs=1)
p.add_option("--length", nargs=1)

(options, args) = p.parse_args()

api_key = options.K or os.getenv('PTSL_KEY', default=None)

assert api_key is not None, "No developer key file provided"

with open_engine(api_key_path=api_key) as e:
    try:
        process_option(options, 'playback_mode', pt.PM_PlaybackMode, e.set_playback_mode)
        process_option(options, 'record_mode', pt.RM_RecordMode, lambda x: e.set_record_mode(x, False))
        process_option(options, 'bit_depth', pt.BitDepth, e.set_session_bit_depth)
        process_option(options, 'audio_format', pt.SessionAudioFormat, e.set_session_audio_format)

        def simple_set_start(t):
            e.set_session_start_time(t, pt.TimeCode, True)

        process_option(options, 'start_time', str, simple_set_start)
        process_option(options, 'length', str, e.set_session_length)
        process_option(options, 'interleaved_state', bool, e.set_session_interleaved_state)
        process_option(options, 'timecode_rate', str, e.set_session_time_code_rate)
        process_option(options, 'feetframes_rate', str, e.set_session_feet_frames_rate)
        process_option(options, 'audio_pull', pt.SessionRatePull, e.set_session_audio_rate_pull)
        process_option(options, 'video_pull', pt.SessionRatePull, e.set_session_video_rate_pull)
    except CommandError as e:
        print(("WARNING %s:" if e.is_warning else "FAILURE: %s") % e.error_name)
        print(" %s" % e.message)
        exit(-1)
    


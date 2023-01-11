from typing import Optional, Tuple

from contextlib import contextmanager

import ptsl
import ptsl.ops as ops
import ptsl.PTSL_pb2 as pt


@contextmanager
def open_engine(**kwargs):
    engine = Engine(**kwargs)

    try:
        yield engine
    finally:
        engine.close()



class Engine:

    client: ptsl.client.Client

    def __init__(self, api_key_path: str, address='localhost:31416') -> None:
        self.client = ptsl.client.Client(api_key_path=api_key_path, address=address)

    def close(self):
        self.client.close()

    def ptsl_version(self) -> int:
        op = ops.GetPTSLVersion()
        self.client.run(op)
        return op.response.version


    def session_name(self) -> str:
        op = ops.GetSessionName()
        self.client.run(op)
        return op.response.session_name


    def session_path(self) -> str:
        op = ops.GetSessionPath()
        self.client.run(op)
        return op.response.session_path.path


    def session_sample_rate(self) -> Optional[int]:
        op = ops.GetSessionSampleRate()
        self.client.run(op)
        map_dict = {
            pt.SR_192000: 192000,
            pt.SR_176400: 176400,
            pt.SR_96000: 96000,
            pt.SR_48000: 48000,
            pt.SR_44100: 44100
        }
        return map_dict.get(op.response.sample_rate, None)


    def session_audio_format(self) -> Optional[str]:
        op = ops.GetSessionAudioFormat()
        self.client.run(op)
        map_dict = {
            pt.SAF_WAVE: 'WAVE',
            pt.SAF_AIFF: 'AIFF',
        }
        return map_dict[op.response.current_setting]


    def session_interleaved_state(self) -> bool:
        op = ops.GetSessionInterleavedState()
        self.client.run(op)
        return op.response.current_setting

    def session_timecode_rate(self) -> Tuple[int, int, bool]:
        """
        :returns: a Tuple of (`quanta_per_second`, `quanta_per_frame`, `is_drop_frame`)
        """
        op = ops.GetSessionTimeCodeRate()
        self.client.run(op)
        map_dict = {
            pt.STCR_Fps120: (120, 1, False),
            pt.STCR_Fps120Drop: (120, 1, True),
            pt.STCR_Fps11988: (120_000, 1001, False),
            pt.STCR_Fps11988Drop: (120_000, 1001, True),
            pt.STCR_Fps100: (100, 1, False),
            pt.STCR_Fps60: (60, 1, False),
            pt.STCR_Fps60Drop: (60, 1, True),
            pt.STCR_Fps5994: (60000, 1001, False),
            pt.STCR_Fps5994Drop: (60000, 1001, True),
            pt.STCR_Fps50: (50, 1, False),
            pt.STCR_Fps48: (48, 1, False),
            pt.STCR_Fps47952: (48000, 1001, False),
            pt.STCR_Fps30: (30, 1, False),
            pt.STCR_Fps30Drop: (30, 1, True),
            pt.STCR_Fps2997: (30000, 1001, False),
            pt.STCR_Fps2997Drop: (30000, 1001, True),
            pt.STCR_Fps25: (25, 1, False),
            pt.STCR_Fps24: (24, 1, False),
            pt.STCR_Fps23976: (24000, 1001, False)
        }
        return map_dict[op.response.current_setting]

    def session_start_time(self) -> str:
        op = ops.GetSessionStartTime()
        self.client.run(op)
        return op.response.session_start_time

    def session_length(self) -> str:
        op = ops.GetSessionLength()
        self.client.run(op)
        return op.response.session_length

    def session_feet_frames_rate(self) -> Tuple[int, int]:
        op = ops.GetSessionFeetFramesRate()
        self.client.run(op)
        map_dict = {
            pt.SFFR_Fps25: (25, 1),
            pt.SFFR_Fps24: (24, 1),
            pt.SFFR_Fps23976: (24000, 1001)
        }
        return map_dict[op.response.current_setting]

    PULL_DICT = {
        pt.SRP_None: (0,0),
        pt.SRP_Down01: (0,-1),
        pt.SRP_Down4: (-1,0),
        pt.SRP_Down4Down01: (-1,-1),
        pt.SRP_Down4Up01: (-1,1),
        pt.SRP_Up01: (0, 1),
        pt.SRP_Up4: (1, 0),
        pt.SRP_Up4Up01: (1, 1),
        pt.SRP_Up4Down01: (1, -1),
    }

    def session_audio_pull(self) -> Tuple[int, int]:
        """
        :returns: a Tuple of (`4pct_pull_factor`, `01pct_pull_factor`)
        """
        op = ops.GetSessionAudioRatePullSettings()
        self.client.run(op)
        return self.PULL_DICT[op.response.current_setting]

    def session_video_pull(self) -> Tuple[int, int]:
        """
        :returns: a Tuple of (`4pct_pull_factor`, `01pct_pull_factor`)
        """
        op = ops.GetSessionVideoRatePullSettings()
        self.client.run(op)
        self.PULL_DICT[op.response.current_setting]

    def transport_state(self) -> str:
        op = ops.GetTransportState()
        self.client.run(op)
        return pt.TS_TransportState.Name(op.response.current_setting)

    def transport_armed(self) -> bool:
        op = ops.GetTransportArmed()
        self.client.run(op)
        return op.response.is_transport_armed

    def playback_modes(self) -> Tuple[bool, bool, bool]:
        """
        :returns: A Tuple if (`is_normal`, `is_loop`, `is_dynamic_transport`)
        """
        op = ops.GetPlaybackMode()
        self.client.run(op)
        return (pt.PM_Normal in op.response.current_settings, 
                pt.PM_Loop in op.response.current_settings,
                pt.PM_DynamicTransport in op.response.current_settings)

    def record_mode(self) -> str:
        op = ops.GetRecordMode()
        self.client.run(op)
        return pt.RM_RecordMode.Name(op.response.current_setting)





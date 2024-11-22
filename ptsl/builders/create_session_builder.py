from ptsl.PTSL_pb2 import SAF_AIFF, SAF_WAVE, \
    SR_48000, Bit16, Bit24, Bit32Float, \
    IO_Last, IO_StereoMix, IO_51SMPTEMix

import ptsl
from ptsl import ops, util


class CreateSessionBuilder:
    def __init__(self, engine: 'ptsl.Engine', name: str, path: str):
        self._engine = engine
        self._session_name = name
        self._path = path
        self._audio_format = SAF_WAVE
        self._sample_rate = SR_48000
        self._bit_depth = Bit24
        self._io_settings = IO_Last
        self._is_interleaved = False

    def audio_format(self, value: str):
        """
        :param value: Audio format for the new session. Acceptable
            values are "wave" or "aiff".
        """
        if value == 'wave':
            self._audio_format = SAF_WAVE
        elif value == 'aiff':
            self._audio_format = SAF_AIFF
        else:
            assert False, f"Invalid audio_format value {value}"

    def wave_format(self):
        self.audio_format("wave")

    def aiff_format(self):
        self.audio_format("aiff")

    def sample_rate(self, value: int):
        self._sample_rate = util.sample_rate_enum(value)

    def bit_depth(self, value: int):
        """
        :param value: Bit depth for the new session. Acceptable
            values are `16`, `24` or `32`.
        """
        if value == 16:
            self._bit_depth = Bit16
        elif value == 24:
            self._bit_depth = Bit24
        elif value == 32:
            self._bit_depth = Bit32Float
        else:
            assert False, f"Invalid bit_depth value {value}"

    def stereo_io_settings(self):
        self._io_settings = IO_StereoMix

    def smpte51_io_settings(self):
        self._io_settings = IO_51SMPTEMix

    def interleaved(self, value: bool):
        self._is_interleaved = value

    def create(self) -> None:
        import pprint
        op = ops.CreateSession(
            session_name=self._session_name,
            file_type=self._audio_format,
            sample_rate=self._sample_rate,
            input_output_settings=self._io_settings,
            is_interleaved=self._is_interleaved,
            session_location=self._path,
            bit_depth=self._bit_depth,
            is_cloud_project=False,
            create_from_template=False,
        )
        print("------")
        pprint.pprint(op.request)
        self._engine.client.run(op)


class CreateSessionFromTemplateBuilder(CreateSessionBuilder):

    def __init__(self, engine: 'ptsl.Engine',
                 template_name: str,
                 template_group: str,
                 name: str,
                 path: str):
        self._template_name = template_name
        self._template_group = template_group
        super().__init__(engine, name, path)

    def create(self):
        op = ops.CreateSession(
            session_name=self._session_name,
            create_from_template=True,
            template_group=self._template_group,
            template_name=self._template_name,
            file_type=self._audio_format,
            sample_rate=self._sample_rate,
            input_output_settings=self._io_settings,
            is_interleaved=self._is_interleaved,
            session_location=self._path,
            bit_depth=self._bit_depth
        )

        self._engine.client.run(op)


class CreateSessionFromAAFBuilder(CreateSessionBuilder):

    def __init__(self, engine: 'ptsl.Engine',
                 aaf_path: str,
                 name: str,
                 path: str):
        self._aaf_path = aaf_path
        super().__init__(engine, name, path)

    def create(self):
        op = ops.CreateSession(
            session_name=self._session_name,
            file_type=self._audio_format,
            sample_rate=self._sample_rate,
            input_output_settings=self._io_settings,
            is_interleaved=self._is_interleaved,
            session_location=self._path,
            bit_depth=self._bit_depth,
            create_from_aaf=True,
            path_to_aaf=self._aaf_path
        )

        self._engine.client.run(op)

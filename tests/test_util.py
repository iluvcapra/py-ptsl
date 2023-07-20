from unittest import TestCase
from fractions import Fraction

from ptsl import util
from ptsl import PTSL_pb2 as pt


class UtilTest(TestCase):

    def test_timecodes(self):
        info = util.timecode_info(pt.STCR_Fps30)
        self.assertEqual(info[0], Fraction(30, 1))
        self.assertEqual(info[1], False)

    def test_feet_frames_info(self):
        info = util.feet_frames_info(pt.SFFR_Fps24)
        self.assertEqual(info, Fraction(24, 1))

    def test_sample_rate_enum(self):
        info = util.sample_rate_enum(44100)
        self.assertEqual(info, pt.SR_44100)
        info = util.sample_rate_enum(44144)
        self.assertEqual(info, pt.SR_None)

    def test_sample_rate_info(self):
        info = util.sample_rate_info(pt.SR_48000)
        self.assertEqual(info, 48000)

    def test_pull_rate_info(self):
        info = util.pull_rate_info(pt.SRP_Down01)
        self.assertEqual(info, (0, -1))

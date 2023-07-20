"""
ptsl Utilities - Utility functions for working with types
"""

from typing import Tuple, Optional, Dict
from fractions import Fraction

import ptsl.PTSL_pb2 as pt
from ptsl.PTSL_pb2 import SessionTimeCodeRate, SessionFeetFramesRate, \
    SessionRatePull, SampleRate


def timecode_info(
        session_rate: 'SessionTimeCodeRate'
) -> Tuple[Fraction, bool]:
    """
    For the given :class:`~ptsl.PTSL_pb2.SessionTimeCodeRate` enumeration
    value, returns a library-agnostic description that can be used for time
    arithmetic.

    The first element in the return :class:`tuple` is the duration of a frame
    in the given ``session_rate`` as a fractional number of seconds. The
    second element is a `bool` which is `True` if the ``session_rate`` is
    drop-frame.

    :param session_rate: The session rate value.
    :returns: a Tuple of (`frame duration`, `is drop frame`)
    """
    map_dict: Dict[pt.SessionTimeCodeRate, Tuple[int, int, bool]] = {
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
    assert session_rate in map_dict.keys(), \
        "session_rate (%i) not recognized" % session_rate

    val = map_dict[session_rate]
    return (Fraction(val[0], val[1]), val[2])


def feet_frames_info(feet_frames_rate: 'SessionFeetFramesRate') -> Fraction:
    """
    For the given :class:`~ptsl.PTSL_pb2.SessionFeetFramesRate` enumeration
    value, returns a library-agnostic description that can be used for time
    arithmetic.

    :param feet_frames_rate: The session feet+frames rate value.
    :returns: The duration of a frame in the given rate, as a fractional number
    of seconds.
    """
    map_dict = {
        pt.SFFR_Fps25: (25, 1),
        pt.SFFR_Fps24: (24, 1),
        pt.SFFR_Fps23976: (24000, 1001)
    }
    assert feet_frames_rate in map_dict.keys(), \
        "feet_frames_rate (%i) not recognized" % feet_frames_rate

    return Fraction(*map_dict.get(feet_frames_rate))


def sample_rate_enum(sample_rate: Optional[int]) -> 'SampleRate':
    """
    Get the symbolic sample rate from the `SampleRate` enum from
    an integer.

    .. note:: A `sample_rate` not in the enumeration will be returned
        as `SR_None`
    """
    map_dict = {
        192000: pt.SR_192000,
        176400: pt.SR_176400,
        96000: pt.SR_96000,
        88200: pt.SR_88200,
        48000: pt.SR_48000,
        44100: pt.SR_44100,
        None: pt.SR_None
    }
    return map_dict.get(sample_rate, pt.SR_None)


def sample_rate_info(sample_rate: 'SampleRate') -> Optional[int]:
    """
    Get the sample rate for a :class:`~ptsl.PTSL_pb2.SampleRate` as an
    integer.

    .. note:: The :attr:`~ptsl.PTSL_pb2.SampleRate.SR_None` value will be
        returned as a `None`
    """
    map_dict = {
        pt.SR_192000: 192000,
        pt.SR_176400: 176400,
        pt.SR_96000: 96000,
        pt.SR_88200: 88200,
        pt.SR_48000: 48000,
        pt.SR_44100: 44100,
        pt.SR_None: None
    }
    return map_dict[sample_rate]


def pull_rate_info(rate_pull: 'SessionRatePull') -> Tuple[int, int]:
    """
    For the given :class:`~ptsl.PTSL_pb2.SessionRatePull` enumeration value,
    returns a library-agnostic description that can be used for time
    arithmetic.

    Returns a Tuple where ``retval[0]`` can be multiplied by 4% to give the
    4% pull value (as when converting 24fps and 25fps playback), and
    ``retval[1]`` can be multiplied by 0.1% to give the 0.1% pull value (as
    when converting NTSC to integral frame rates).

    :param rate_pull: The rate pull.
    :returns: A Tuple of (:class:`int`, :class:`int`)
    """
    map_dict = {
        pt.SRP_None: (0, 0),
        pt.SRP_Down01: (0, -1),
        pt.SRP_Down4: (-1, 0),
        pt.SRP_Down4Down01: (-1, -1),
        pt.SRP_Down4Up01: (-1, 1),
        pt.SRP_Up01: (0, 1),
        pt.SRP_Up4: (1, 0),
        pt.SRP_Up4Up01: (1, 1),
        pt.SRP_Up4Down01: (1, -1),
    }
    assert rate_pull in map_dict.keys(), \
        "rate_pull (%i) not recgonized" % rate_pull

    return map_dict[rate_pull]

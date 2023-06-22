"""
Native Python PTSL (Pro Tools Scripting Library) RPC interface

This package (c) 2023 Jamie Hardt. All Rights Reserved.
Read the LICENSE file distributed with this package to learn about
your rights to use, modify and redistribute this software package.

This project is a work of Pro Tools enthusiasts and users and is not
affiliated with Avid.

For more information on this package see the github repository at
https://github.com/iluvcapra/py-ptsl/
"""

from .client import Client
from .engine import Engine, open_engine
from .errors import CommandError

__version__ = '0.0a2'

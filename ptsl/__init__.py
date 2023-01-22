"""
py-ptsl: Native Python client for the Pro Tools scripting RPC interface
"""

# flake8: noqa
from .client import Client
from .engine import Engine, open_engine
from .errors import CommandError

__version__ = '0.0.1'

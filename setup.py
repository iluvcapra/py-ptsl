#!/usr/bin/env python

from setuptools import setup
from ptsl import __VERSION__

setup(name='ptsl',
      version=__VERSION__,
      packages=['ptsl'],
      install_requires=[
            'grpcio >= 1.51.1', 
            'protobuf >= 4.21.12'
            ],
      package_data={},
      )
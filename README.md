[![Lint and Test](https://github.com/iluvcapra/py-ptsl/actions/workflows/lint_and_pytest.yml/badge.svg)](https://github.com/iluvcapra/py-ptsl/actions/workflows/lint_and_pytest.yml)
[![codecov](https://codecov.io/gh/iluvcapra/py-ptsl/branch/master/graph/badge.svg?token=PR6SUQJISZ)](https://codecov.io/gh/iluvcapra/py-ptsl)
[![Documentation Status](https://readthedocs.org/projects/py-ptsl/badge/?version=latest)](https://py-ptsl.readthedocs.io/en/latest/?badge=latest)
![GitHub last commit](https://img.shields.io/github/last-commit/iluvcapra/py-ptsl)

![](https://img.shields.io/pypi/pyversions/py-ptsl.svg) [![](https://img.shields.io/pypi/v/py-ptsl.svg)](https://pypi.org/project/py-ptsl/) ![](https://img.shields.io/pypi/wheel/py-ptsl.svg)

[![Pro Tools Version - 2024.10](https://img.shields.io/static/v1?label=Pro+Tools+Version&message=2024.10&color=8f228f)](https://github.com/iluvcapra/py-ptsl/blob/master/docs/source/ptsl_versions.rst)
[![PTSL Version - 5](https://img.shields.io/static/v1?label=PTSL+Version&message=5&color=0000ff)](https://github.com/iluvcapra/py-ptsl/blob/master/docs/source/ptsl_versions.rst)

# py-ptsl

Native Python PTSL (Pro Tools Scripting Library) RPC interface

## Important Notice! 

This software is developed by enthusiasts and is not a work of or supported by 
Avid. Developers who wish to contribute to this project should obtain the PTSL 
SDK [from Avid's Developer site](https://developer.avid.com) for the most 
current documentation and protobuf source files.

## Example

See the [examples directory](examples) for scripts demonstrating how to use the
client.

- [session_info.py](examples/session_info.py) - This example 
  prints a list of gettable properties from the currently-open
      session.
- [print_tracks.py](examples/print_tracks.py) - This example prints
  a list of every track in the currently-open session, including state
  information like selection, mute and solo state, track color and 
  track ID.
- [make_session.py](examples/make_session.py) - Creates a new
  session interactively from the terminal.
- [pt_set.py](examples/pt_set.py) - Allows several session setup
  options to be set from the terminal.
- [pt_pasteboard.py](examples/pt_pasteboard.py) - Demonstrates
  triggering cut/copy/paste actions.
- [toolshell.py](examples/toolshell.py) - Implements a command line 
  interface for Pro Tools.


### Sending Commands To Pro Tools with the `Engine` class

The `Engine` class exposes `ptsl` commands with a method call interface.

```python
from ptsl import open_engine

with open_engine(company_name="MY_COMPANY", application_name="MY_TOOL") as engine:
    session_name = engine.session_name()
```


"""
Native Python PTSL (Pro Tools Scripting Library) RPC interface

This package (c) 2023 Jamie Hardt. All Rights Reserved.
Read the LICENSE file distributed with this package to learn about
your rights to use, modify and redistribute this software package.

This project is a work of Pro Tools enthusiasts and users and is not
affiliated with Avid.

For more information on this package see the github repository at
https://github.com/iluvcapra/py-ptsl/

Note on Versions
----------------

The `__version__` property of this module uses semantic versioning of
a particular form.

- The first element of the version triple is the PTSL version as
  supported by the client * 100, plus the major version of this module.
- The second element increments with feature enhancements. Support for
  new versions of Pro Tools will always increment this value.
- The third element increments with bug fixes or modifcations to docs,
  build system, etc.

"""


from .client import Client
from .engine import Engine, open_engine
from .errors import CommandError

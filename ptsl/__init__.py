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
a particular form. Instead of the usual three elements, there are 
four.

- The first element of the version triple is the PTSL version as 
  supported by the client.
- The second element is the major version number of this module.

Changes in the first two elements of the version are breaking changes.
While the module remains in beta development, breaking changes may 
occur with any change in version.

- The third element increments with feature enhancements. Support for
  new versions of Pro Tools will always increment this value.
- The fourth element increments with bug fixes or modifcations to docs, 
  build system, etc.

Changes in the remaining final two elements of the version are 
guaranteed not to be breaking changes past X.1.0.0.

"""

from .client import Client
from .engine import Engine, open_engine
from .errors import CommandError

__version__ = '1.0.1.0'

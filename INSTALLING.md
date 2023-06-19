# Installing

## Minimum Requirements

`py-ptsl` requires Python 3.11.

## Steps

py-ptsl can be installed by cloning the repository from Github, and then 
installing the package with `pip`.

```sh
$ gh repo clone iluvcapra/py-ptsl
$ cd py-ptsl
$ python3 -m pip install .
```

Since this module is being actively developed and is not being distributed, I'd 
recommend installing it in a [virtualenv] and in [editable mode][em]. (Replace
the third line above with these:)

```sh
$ python3 -m venv venv
$ source venv/bin/activate
$ python3 -m pip install -e .
```

If you'd like to build the documentation, install the `doc` optional 
dependencies.

```sh
$ python3 -m pip install .[doc]
```

[virtualenv]: https://pypi.org/project/virtualenv/
[em]: https://pip.pypa.io/en/stable/cli/pip_install/#cmdoption-e

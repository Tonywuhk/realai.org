---
permalink: /course/pip/
title: Course | Pip
---
# Pip

[Pip](https://pypi.python.org/pypi/pip) is the PyPA recommended tool for installing ([pip install](https://pip.pypa.io/en/stable/reference/pip_install/)) Python packages. The [Python Package Index](https://pypi.python.org/pypi) (PyPI) is a repository of Python packages that can be installed using pip.

When both source distributions and wheels are available, pip [prefers](https://packaging.python.org/tutorials/installing-packages/#source-distributions-vs-wheels) to [install from wheels](https://pip.pypa.io/en/stable/user_guide/#installing-from-wheels).

## Requirement Specifiers

`pip` supports installing from a package index using a [requirement specifier](https://packaging.python.org/glossary/#term-requirement-specifier). For example, the following two lines install different versions of [html5lib](https://pypi.python.org/pypi/html5lib), a pure-python library for parsing HTML. The first line installs version 0.9999999 (seven 9's), the second line uninstalls this version, then installs version 0.99999999 (eight 9's):

``
sudo pip install html5lib==0.9999999
sudo pip install html5lib==0.99999999
``

Version numbers like this are very common, but can happen in practice. Other than referring to the package's homepage at PyPI, a quick way of checking available versions is

```
pip install html5lib==
```

It will show that `html5lib` has versions 0.9, 0.90, 0.99, 0.999, 0.9999, 0.99999, 0.999999, 0.9999999, 0.99999999, and 0.999999999, up to nine 9's. Installing the wrong version could cause other libraries to break.


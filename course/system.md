---
permalink: /course/system/
---
# System

The goal of this section is to set up productive environments for deep learning research.

## Basic Operations

* Virtual Machines: [Google Compute Engine](http://realai.org/course/GCE/)
* Operating System: [Ubuntu](https://www.ubuntu.com/) is a popular operating system that we will use during this course
* [Text processing](http://realai.org/course/text-processing/) with grep, sed, awk, and regular expressions
* Text editor: [Vim](http://realai.org/course/vim/) 
* Version control system: [Git](http://realai.org/course/git/)

## Installing Packages

### Ubuntu Packages

* Package management with [apt-get](https://help.ubuntu.com/community/AptGet/Howto)

### Python Packages

[Pip](https://pypi.python.org/pypi/pip) is the PyPA recommended tool for installing ([pip install](https://pip.pypa.io/en/stable/reference/pip_install/)) Python packages. The [Python Package Index](https://pypi.python.org/pypi) (PyPI) is a repository of Python packages that can be installed using `pip`.

When both source distributions and wheels are available, `pip` [prefers](https://packaging.python.org/tutorials/installing-packages/#source-distributions-vs-wheels) to [install from wheels](https://pip.pypa.io/en/stable/user_guide/#installing-from-wheels).

## Installing Libraries from Source

* [Bazel](https://bazel.build/) ([documentation](https://docs.bazel.build/)), a fast and scalable build system that only builds what is necessary

* [Wheel](https://pypi.python.org/pypi/wheel) ([documentation](http://wheel.rtfd.org/)) is a built-package format for Python with a specially formatted filename and the .whl extension.


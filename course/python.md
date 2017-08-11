---
permalink: /course/python/
title: Course | Python 3
---
# Python 3

[Python](https://www.python.org/) is a programming language that lets you work quickly and integrate systems more effectively. On a newly created Ubuntu 16.04 LTS VM on GCE, we can type `python3` to launch it. Beginners can take a short crash course at [Learn python3 in Y minutes](https://learnxinyminutes.com/docs/python3/).

Python can be launched from command line. Use `-c` to pass a program as string, for example, to check the version of TensorFlow installed in the system:

```bash
python3 -c "import tensorflow as tf; print(tf.__version__)"
```

Generally we should write Python code following [PEP 8 -- Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/), but we will be using 2 spaces because of [TensorFlow](https://www.tensorflow.org/community/style_guide).

## System

### Wheel

[Wheel](https://pypi.python.org/pypi/wheel) ([documentation](http://wheel.rtfd.org/)) is a built-package format for Python. Follwing [PEP 427](https://www.python.org/dev/peps/pep-0427/), its [file name convention](https://www.python.org/dev/peps/pep-0427/#file-name-convention) is `{distribution}-{version}(-{build tag})?-{python tag}-{abi tag}-{platform tag}.whl`, where ABI means [application binary interface](https://en.wikipedia.org/wiki/Application_binary_interface).


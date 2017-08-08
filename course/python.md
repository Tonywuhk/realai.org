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


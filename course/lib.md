---
permalink: /course/lib/
title: Libraries
---
# Deep Learning Libraries

## TensorFlow

* [TensorFlow](https://www.tensorflow.org/) ([Abadi et al., 2016](https://arxiv.org/abs/1605.08695)) is an open-source software library for machine intelligence.
* [Keras](https://keras.io/) ([Chollet 2015](https://github.com/fchollet/keras)) is a deep Learning library for Theano and TensorFlow.
* [Sonnet](https://github.com/deepmind/sonnet) is a library built on top of TensorFlow for building complex neural networks.

## PyTorch

* [PyTorch](http://pytorch.org/) is a deep learning framework that puts Python first. This [repository](https://github.com/yunjey/pytorch-tutorial) provides tutorial code.

## MXNet

[MXNet](http://mxnet.io/) is a flexible and efficient library for deep learning. [mxnet-the-straight-dope](https://github.com/zackchase/mxnet-the-straight-dope) is an [ambitious](https://twitter.com/zacharylipton/status/888096437187207168) roadmap to an interactive deep learning book.

## Remarks

TensorFlow is declarative, supposedly easier to optimize, but many programmers likely feel more comfortable with the imperative style of PyTorch, which may be a good fit if you want [better development and debugging experience](https://medium.com/@dubovikov.kirill/pytorch-vs-tensorflow-spotting-the-difference-25c75777377b). Windows support for PyTorch is an [outstanding issue since January 2017](https://github.com/pytorch/pytorch/issues/494). One main difference between TensorFlow and PyTorch is that the former uses static computation graphs whereas the latter supports dynamic computation graphs. It is further explained and demonstrated for conditional and loop structures on page 120-129 of the [slides](http://cs231n.stanford.edu/slides/2017/cs231n_2017_lecture8.pdf) used in a Stanford lecture.

## References

* 2016 May 27, Martín Abadi, Paul Barham, Jianmin Chen, Zhifeng Chen, Andy Davis, Jeffrey Dean, Matthieu Devin, Sanjay Ghemawat, Geoffrey Irving, Michael Isard, Manjunath Kudlur, Josh Levenberg, Rajat Monga, Sherry Moore, Derek G. Murray, Benoit Steiner, Paul Tucker, Vijay Vasudevan, Pete Warden, Martin Wicke, Yuan Yu, and Xiaoqiang Zheng. [TensorFlow: A system for large-scale machine learning](https://arxiv.org/abs/1605.08695). *arXiv:1605.08695*.
* 2015 March. François Chollet. [Keras](https://github.com/fchollet/keras). *GitHub*.

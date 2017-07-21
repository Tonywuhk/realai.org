---
permalink: /deep-learning-implementation/
title: Implementation
---
# Deep Learning Implementation

## System

A typical approach to address the computational requirements of large-scale neural networks is to use a heterogeneous distributed environment with a mixture of many CPUs and GPUs. [Mirhoseini & Pham et al. (2017)](https://arxiv.org/abs/1706.04972) use reinforcement learning to optimize device placement for TensorFlow computational graphs and ﬁnd non-trivial device placements for Inception-V3 and RNN LSTM.

## Software

* There are several widely used [deep learning libraries](http://realai.org/course/lib/).
* [rllab](https://github.com/openai/rllab) ([Duan et al., 2016](https://arxiv.org/abs/1604.06778)) is a framework for developing and evaluating reinforcement learning algorithms.

TensorFlow is declarative, supposedly easier to optimize, but many programmers likely feel more comfortable with the imperative style of PyTorch, which may be a good fit if you want [better development and debugging experience](https://medium.com/@dubovikov.kirill/pytorch-vs-tensorflow-spotting-the-difference-25c75777377b). Windows support for PyTorch is an [outstanding issue since January 2017](https://github.com/pytorch/pytorch/issues/494). One main difference between TensorFlow and PyTorch is that the former uses static computation graphs whereas the latter supports dynamic computation graphs. It is further explained and demonstrated for conditional and loop structures on page 120-129 of the [slides](http://cs231n.stanford.edu/slides/2017/cs231n_2017_lecture8.pdf) used in a Stanford lecture.

## Hardware

* 2017 April 5, Norm Jouppi. [Quantifying the performance of the TPU, our first machine learning chip](https://cloudplatform.googleblog.com/2017/04/quantifying-the-performance-of-the-TPU-our-first-machine-learning-chip.html). *Google Cloud Platform Blog*.

## References

* 2017 June 13, Azalia Mirhoseini, Hieu Pham, Quoc V. Le, Benoit Steiner, Rasmus Larsen, Yuefeng Zhou, Naveen Kumar, Mohammad Norouzi, Samy Bengio, and Jeff Dean. [Device Placement Optimization with Reinforcement Learning](https://arxiv.org/abs/1706.04972). *arXiv:1706.04972*.
* 2016 April 22, Yan Duan, Xi Chen, Rein Houthooft, John Schulman, and Pieter Abbeel. [Benchmarking Deep Reinforcement Learning for Continuous Control](https://arxiv.org/abs/1604.06778). *arXiv:1604.06778*.

---
permalink: /course/deep-learning/libraries/
redirect_from: /course/DL/libraries/
title: DL Libraries
---
# Deep Learning Libraries

[TensorFlow](https://www.tensorflow.org/) ([Abadi et al., 2016](https://arxiv.org/abs/1605.08695)) is an open-source software library for machine intelligence. It supports higher-level libraries such as [Keras](https://keras.io/) ([Chollet, 2015](https://github.com/fchollet/keras)) and [Sonnet](https://github.com/deepmind/sonnet) ([blog](https://deepmind.com/blog/open-sourcing-sonnet/)).

[PyTorch](http://pytorch.org/) is a deep learning framework that puts Python first. [The Incredible PyTorch](https://github.com/ritchieng/the-incredible-pytorch) is a curated list of tutorials, projects, libraries, videos, papers, books and anything related. As of September 2017, Windows support for PyTorch is still an [outstanding issue](https://github.com/pytorch/pytorch/issues/494). Libaries built on PyTorch include:

* [AllenNLP](http://allennlp.org/), an open-source NLP research library built on PyTorch, by the [Allen Institute for Artificial Intelligence](http://allenai.org/) in close collaboration with other researchers.
* [FAIR Sequence-to-Sequence Toolkit](https://github.com/facebookresearch/fairseq-py), a sequence-to-sequence learning toolkit from [Facebook AI Research](http://realai.org/research-groups/facebook-AI-research/).

[MXNet](http://mxnet.io/) is a flexible and efficient library for deep learning. [mxnet-the-straight-dope](https://github.com/zackchase/mxnet-the-straight-dope) is an [ambitious](https://twitter.com/zacharylipton/status/888096437187207168) roadmap to an interactive deep learning book.

[Caffe2](http://caffe2.ai/) is a new lightweight, modular, and scalable deep learning framework.

[Gluon](https://github.com/gluon-api/gluon-api/) is a clear, concise, simple yet powerful and efficient API for deep learning, announced in October 2017 by [AWS](https://aws.amazon.com/blogs/aws/introducing-gluon-a-new-library-for-machine-learning-from-aws-and-microsoft/) and Microsoft.

## Remarks

TensorFlow is declarative, supposedly easier to optimize, but many programmers likely feel more comfortable with the imperative style of PyTorch, which may be a good fit if you want [better development and debugging experience](https://medium.com/@dubovikov.kirill/pytorch-vs-tensorflow-spotting-the-difference-25c75777377b). Windows support for PyTorch is an [outstanding issue since January 2017](https://github.com/pytorch/pytorch/issues/494). One main difference between TensorFlow and PyTorch is that the former uses static computation graphs whereas the latter supports dynamic computation graphs. It is further explained and demonstrated for conditional and loop structures on page 120-129 of the [slides](http://cs231n.stanford.edu/slides/2017/cs231n_2017_lecture8.pdf) used in a Stanford lecture.

## References

* 2016 May 27, Martín Abadi, Paul Barham, Jianmin Chen, Zhifeng Chen, Andy Davis, Jeffrey Dean, Matthieu Devin, Sanjay Ghemawat, Geoffrey Irving, Michael Isard, Manjunath Kudlur, Josh Levenberg, Rajat Monga, Sherry Moore, Derek G. Murray, Benoit Steiner, Paul Tucker, Vijay Vasudevan, Pete Warden, Martin Wicke, Yuan Yu, and Xiaoqiang Zheng. [TensorFlow: A system for large-scale machine learning](https://arxiv.org/abs/1605.08695). *arXiv:1605.08695*.
* 2015 March. François Chollet. [Keras](https://github.com/fchollet/keras). *GitHub*.


---
permalink: /course/tensorflow/
redirect_from: /course/TF/
title: Course | TensorFlow
---
# TensorFlow

[TensorFlow](https://www.tensorflow.org/) is a technical term often mentioned in articles about artificial intelligence. It is the name of a software library that is designed for machine learning tasks. The objective of this course is to help readers with only everyday computer experience to grasp its basics as quickly as possible. In a few sessions, we hope that readers will attain the necessary background knowledge to access online content intended for TensorFlow practitioners, who are typically full-time developers with extensive programming experience.

To follow the main sequence, readers are advised to install the Chrome web browser and have a valid credit card that can be temporarily charged $1 in order to get a free Google cloud account.

## Contents

* Main Sequence
  * Session 1: [IT 101](#it-101)
  * Session 2. [Setting Up Your Computer](#setting-up-your-computer)
  * Session 3. [Classifying Handwritten Digits](#classifying-handwritten-digits)
  * Session 4. Deep Models
* [Further Reading](#further-reading)
* Topics
  * [Dynamic Batching](#dynamic-batching)
* [Resources](#resources)

## Main Sequence

### IT 101

TensorFlow is one of the most popular [deep learning libraries](http://realai.org/course/libraries/). It is Google’s second-generation machine learning system, specifically designed to correct the shortcomings of [DistBelief](https://research.google.com/pubs/pub40565.html), its predecessor. TensorFlow was [open sourced by Google](https://research.googleblog.com/2015/11/tensorflow-googles-latest-machine_9.html) on November 9, 2015. As is typical for most open-source projects, it is [hosted](https://github.com/tensorflow/tensorflow) on GitHub.

Within the scope of this sequence, TensorFlow can be viewed as an extension to the popular Python programming language. Readers can access both with Jupyter Notebook. Along with other concepts, they are illustrated in the diagram below:

![](http://realai.org/course/tensorflow/IT-101.png)

The actual architecture map is a lot more complex, for example, the part of TensorFlow we use in this sequence is only its Python API on the front end. As a deep learning library designed to be used for both research and production, TensorFlow connects all the way down to the drivers of the hardware components that form the physical cloud, and enables distributed execution on a range of devices such as CPU, GPU and mobile. It has APIs available in Python, C++, Java and Go. As of August 2017, the Python API is the most complete and the easiest to use. 

Fortunately we don’t need to know all these details to use TensorFlow, or to experiment on virtual machines in the cloud. Interested readers can follow the steps below to run a simple AI agent to StarCraft II on a remote desktop:

* [Running StarCraft II Learning Environment on Google Compute Engine](http://realai.org/course/lab/gce-sc2le/)

### Setting Up Your Computer

## Basics

Experiments in this section are conducted on an [n1-standard-1](https://cloud.google.com/compute/pricing#predefined_machine_types) instance on [Google Compute Engine](http://realai.org/course/google-compute-engine/). As of August 2017, the machine type costs less than $30 per month in [asia-east1](https://cloud.google.com/compute/docs/regions-zones/regions-zones#available). We use a Ubuntu 16.04 LTS boot image, with firewall rules that allow TCP access from ports 8888 and 6006 for Jupyter Notebook and TensorBoard, respectively. The environment can be set up by the following commands, explained in more details at [Running Jupyter on Google Compute Engine](http://realai.org/course/lab/gce-jupyter/):

```bash
curl https://bootstrap.pypa.io/get-pip.py | sudo python3 -
sudo pip3 install jupyter matplotlib tensorflow
echo >> .bashrc
echo "# Start Jupyter Notebook" >> .bashrc
echo "jupyter notebook --ip=0.0.0.0 &" >> .bashrc
source .bashrc
```

### Classifying Handwritten Digits

TensorFlow programs usually involve two phases: the construction phase of building a computation graph, and the execution phase of running that graph in a session.

## Further Reading

* [Effective TensorFlow](https://github.com/vahidk/EffectiveTensorflow) is [Vahid Kazemi](https://twitter.com/VahidK)’s attempt to write a series of articles on effective TensorFlow usage, and to keep the content up to date with the latest releases of TensorFlow API.
* 2017 January - June, Chip Huyen. [CS 20SI: Tensorflow for Deep Learning Research](http://web.stanford.edu/class/cs20si/). [GitHub](https://github.com/chiphuyen/stanford-tensorflow-tutorials). This Stanford University course covers the fundamentals and contemporary usage of the TensorFlow library for deep learning research.

## Topics

### Dynamic Batching

TensorFlow is designed to run static computation graphs in which the data flow for each input is the same. Multiple inputs can then be easily batched together to take advantage of modern parallel computing hardware. This is not enough for some research cases where each distinct input may have a different computation graph. To address this challenge, Google [released](https://research.googleblog.com/2017/02/announcing-tensorflow-fold-deep.html) in February 2017 [TensorFlow Fold](https://github.com/tensorflow/fold/), a new library built on top of TensorFlow. It builds a separate computation graph from each input, then automatically combines these graph for batching, both within and across inputs. This is well suited for [implementing](https://github.com/tensorflow/fold/blob/master/tensorflow_fold/g3doc/sentiment.ipynb) a Tree-LSTM ([Tai et al., 2015](https://arxiv.org/abs/1503.00075)) model, where a batch of inputs ([s-expressions](https://en.wikipedia.org/wiki/S-expression) encoded as strings) are transformed into multiple input graphs, which are treated by the dynamic batching algorithm ([Looks et al., 2017](https://arxiv.org/abs/1702.02181)) as a single disconnected graph for automatic batching. The requirement of a fixed computation graph as input limits the applicability of TensorFlow Fold. For example, in the SPINN architecture ([Bowman & Gauthier et al., 2016](https://arxiv.org/abs/1603.06021)), the computation graphs depend on the values of the input, and are not fixed at the time input examples are loaded. It is relatively straightforward to [implement](https://devblogs.nvidia.com/parallelforall/recursive-neural-networks-pytorch/) ([GitHub](https://github.com/jekbradbury/examples/tree/spinn/snli)) batching (and unbatching) in this case with PyTorch, which natively supports dynamic computation graph. As of August 2017, dynamic graph support is an [open issue](https://github.com/tensorflow/tensorflow/issues/12321) in TensorFlow.

#### References

* 2017 February 22, Moshe Looks, Marcello Herreshoff, DeLesley Hutchins, and Peter Norvig. [Deep Learning with Dynamic Computation Graphs](https://arxiv.org/abs/1702.02181). *arXiv:1702.02181*.
* 2016 July 30, Samuel R. Bowman, Jon Gauthier, Abhinav Rastogi, Raghav Gupta, Christopher D. Manning, and Christopher Potts. [A Fast Unified Model for Parsing and Sentence Understanding](https://arxiv.org/abs/1603.06021). *arXiv:1603.06021*. [blog](https://nlp.stanford.edu/blog/hybrid-tree-sequence-neural-networks-with-spinn/).
* 2015 May 30, Kai Sheng Tai, Richard Socher, and Christopher D. Manning. [Improved Semantic Representations From Tree-Structured Long Short-Term Memory Networks](https://arxiv.org/abs/1503.00075). *arXiv:1503.00075*. [code](https://github.com/stanfordnlp/treelstm).

## Resources

* Links: [Python API Documentation](https://www.tensorflow.org/api_docs/python/) \| [Releases](https://github.com/tensorflow/tensorflow/tags) \| [Official Twitter](https://twitter.com/tensorflow)
* Higher-Level Libraries: [TensorFlow Fold](https://github.com/tensorflow/fold) \| [Sonnet](https://github.com/deepmind/sonnet) \| [Tensor2Tensor](https://github.com/tensorflow/tensor2tensor) \| [Keras](https://keras.io/) \| [TFLearn](http://tflearn.org/)
* Related GitHub Repositories: [TensorBoard](https://github.com/tensorflow/tensorboard) \| [magenta](https://github.com/tensorflow/magenta) \| [Deepmath](https://github.com/tensorflow/deepmath)


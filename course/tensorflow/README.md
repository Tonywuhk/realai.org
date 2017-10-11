---
permalink: /course/tensorflow/
redirect_from: /course/TF/
title: Course | TensorFlow
mathjax: true
---
# TensorFlow

[TensorFlow](https://www.tensorflow.org/) is a technical term often mentioned by AI developers. It is the name of a software [library](https://en.wikipedia.org/wiki/Library_(computing)) that is designed for large-scale machine learning. The objective of this course is to help readers with only everyday computer experience to grasp its basics as quickly as possible. In a few sessions, we hope that readers will attain the necessary background knowledge to access online content intended for TensorFlow practitioners, who are typically full-time developers with extensive programming experience.

To follow the main sequence, readers are advised to install the [Chrome](https://www.google.com/chrome/) web browser and have a valid credit card that can be temporarily charged $1 in order to get a free [Google Cloud](https://cloud.google.com/) account.

## Contents

* Main Sequence
  * Session 1: [IT 101](#it-101)
  * Session 2: [TensorFlow Basics](#tensorflow-basics)
  * Session 3: [Classifying Handwritten Digits](#classifying-handwritten-digits)
  * Session 4: [Deep Models](#deep-models)
  * Session 5: [GPU](#gpu)
  * Session 6: [RNN](#rnn)
* [Further Reading](#further-reading)
* Topics
  * [Dynamic Batching](#dynamic-batching)
  * [Imperative Mode](#imperative-mode)
* [Resources](#resources)

## Main Sequence

### IT 101

TensorFlow is one of the most popular [deep learning libraries](http://realai.org/course/deep-learning/libraries/). It is Google’s second-generation machine learning system, specifically designed to correct the shortcomings of [DistBelief](https://research.google.com/pubs/pub40565.html), its predecessor. TensorFlow was [open sourced by Google](https://research.googleblog.com/2015/11/tensorflow-googles-latest-machine_9.html) on November 9, 2015. As is typical for open-source projects, it is [hosted](https://github.com/tensorflow/tensorflow) on [GitHub](https://github.com/), an Internet hosting service that is mostly used for code.

Within the scope of this sequence, we can think of TensorFlow as an extension to the popular [Python](http://realai.org/course/python/) programming language. In the [next session](#tensorflow-basics), we will set up a [virtual machine](https://en.wikipedia.org/wiki/Virtual_machine) (VM) on the [Google Cloud Platform](http://realai.org/course/google-cloud-platform/) running an [operating system](https://en.wikipedia.org/wiki/Operating_system) called [Ubuntu](http://realai.org/course/ubuntu/), install TensorFlow, and use [Jupyter Notebook](http://realai.org/course/jupyter/) for hands-on experiments. These concepts are illustrated in the diagram below:

![](http://realai.org/course/tensorflow/IT-101.png)

The actual architecture map is a lot more complex. For example, the part of TensorFlow we use in this sequence is only its Python [API](https://en.wikipedia.org/wiki/Application_programming_interface) on the front end. As a deep learning library designed to be used for both research and production, TensorFlow connects all the way down to the drivers of the hardware components that form the physical [cloud](https://en.wikipedia.org/wiki/Cloud_computing), and enables distributed execution on a range of devices such as CPU, GPU and [mobile](https://www.tensorflow.org/mobile/). It has APIs available in Python, C++, Java and Go. As of August 2017, the [Python API](https://www.tensorflow.org/api_docs/) is the most complete and the easiest to use.

Fortunately we don’t need to know all these details to use TensorFlow, or to experiment on virtual machines. Interested readers can optionally follow [these steps](http://realai.org/course/google-cloud-platform/gce-sc2le/) to run a simple AI agent that plays [StarCraft II](http://realai.org/environments/#starcraft-ii) on a remote desktop.

#### Setting Up Your Computer

Experiments in the next session will be conducted on an [n1-standard-1](https://cloud.google.com/compute/pricing#predefined_machine_types) instance on [Google Compute Engine](http://realai.org/course/google-cloud-platform/#google-compute-engine). As of August 2017, the machine type costs less than $30 per month in [asia-east1](https://cloud.google.com/compute/docs/regions-zones/regions-zones#available). We use a Ubuntu 16.04 LTS boot image, with firewall rules that allow TCP access from ports 8888 and 6006 for Jupyter Notebook and TensorBoard, respectively. The environment can be set up by the following commands:

```bash
curl https://bootstrap.pypa.io/get-pip.py | sudo python3 -
sudo pip install tensorflow jupyter matplotlib
echo >> .bashrc
echo "# Start Jupyter Notebook" >> .bashrc
echo "jupyter notebook --ip=0.0.0.0 &" >> .bashrc
```

For a step-by-step guide, see

* [Running TensorFlow in Jupyter on Google Compute Engine](http://realai.org/course/tensorflow/jupyter-gce/)

A known issue is that sometimes `tensorboard` reports an error message of `No module named 'html5lib.filters.base'`. It can be fixed by issuing an extra [`pip`](http://realai.org/course/pip/) command to reinstall `html5lib`:

```bash
sudo pip install html5lib==0.99999999
```

### TensorFlow Basics

TensorFlow contains a hierarchy of modules. Its public APIs are mostly under `tf.`, except [`tf.contrib`](https://www.tensorflow.org/api_docs/python/tf/contrib), which contains volatile or experimental code such as [Keras](https://www.tensorflow.org/api_docs/python/tf/contrib/keras) and [Learn](https://www.tensorflow.org/api_docs/python/tf/contrib/learn), as of August 2017. A practical difference between the public APIs and `tf.contrib` is that the latter is not covered by [TensorFlow Version Compatibility](https://www.tensorflow.org/programmers_guide/version_compat) in new [MINOR](http://semver.org/) releases.

#### Define and Run

TensorFlow programs usually involve two phases: the construction phase of building a computation graph, and the execution phase of running that graph in a session. For example, to calculate the gradient of

$$
  y = \frac{1}{6}( x_{00}^2 + x_{01}^2 + … + x_{22}^2 )
$$

with respect to \\(x\\), in the TensorFlow program below, we first define the computation graph from \\(x\\) to \\(y\\), then use [`tf.gradients`](https://www.tensorflow.org/api_docs/python/tf/gradients) to define the gradient step:

```python
import tensorflow as tf

x = tf.Variable(tf.ones([2, 3], tf.float32))
y = tf.reduce_mean(x ** 2)
x_grad = tf.gradients(y, x)

with tf.Session() as sess:
  sess.run(x.initializer)
  print(sess.run(x_grad))
```

The actual computations don’t happen until inside the [`tf.Session`](https://www.tensorflow.org/api_docs/python/tf/Session) and correctly produce the same derivatives for all components of \\(x\\).

```
[array([[ 0.33333334,  0.33333334,  0.33333334],
       [ 0.33333334,  0.33333334,  0.33333334]], dtype=float32)]
```

In a *define-by-run* framework like [PyTorch](http://pytorch.org/), there is no clear separation of building and computing a graph:

```python
import torch
from torch.autograd import Variable

x = Variable(torch.ones(2, 3), requires_grad=True)
y = (x ** 2).mean()
y.backward()

print(x.grad)
```

The derivatives are printed right after all computation steps are fully specified:

```
Variable containing:
 0.3333  0.3333  0.3333
 0.3333  0.3333  0.3333
[torch.FloatTensor of size 2x3]
```

#### Looking at Data 

The [MNIST database of handwritten digits](http://yann.lecun.com/exdb/mnist/) is a popular data set for basic machine learning exercises. The virtual machine set up earlier is well-equipped to handle MNIST tasks. Below we will show in Jupyter how to pass the data to TensorFlow, and take a look at a few images using [TensorBoard](https://www.tensorflow.org/get_started/summaries_and_tensorboard), a suite of visualization tools designed to work with TensorFlow:

* Jupyter Notebook: [MNIST Data](http://nbviewer.jupyter.org/url/realai.org/course/tensorflow/MNIST-data.ipynb) (hosted on nbviewer; [GitHub](https://github.com/real-ai/realai.org/blob/master/course/tensorflow/MNIST-data.ipynb); [source](http://realai.org/course/tensorflow/MNIST-data.ipynb))

### Classifying Handwritten Digits

To quickly build the working environment at the end of last session, first create an n1-standard-1 VM with tcp access to ports 6006 and 8888, then run the 5-line bash script at the beginning of [Setting Up Your Computer](#setting-up-your-computer), followed by

```bash
source .bashrc
wget http://realai.org/course/tensorflow/MNIST-data.ipynb
```

The notebook from last session should appear on a Jupyter Notebook that is accessible online.

In this session, we will build a [softmax regression](http://ufldl.stanford.edu/tutorial/supervised/SoftmaxRegression/) model in TensorFlow to classify handwritten digits:

* Jupyter Notebook: [MNIST Softmax Regression](http://nbviewer.jupyter.org/url/realai.org/course/tensorflow/MNIST-softmax-regression.ipynb) (hosted on nbviewer; [GitHub](https://github.com/real-ai/realai.org/blob/master/course/tensorflow/MNIST-softmax-regression.ipynb); [source](http://realai.org/course/tensorflow/MNIST-softmax-regression.ipynb))

The softmax regression model achieves a classification error of around 7%. Nowadays MNIST is considered such a simple problem that such a high error rate is unacceptable.

### Deep Models

In this session, we will build a [convolutional neural network](http://realai.org/course/deep-learning/convolutional-neural-network/) (CNN) for MNIST and achieve an error rate of around 1%:

* Jupyter Notebook: [Solving MNIST by Convolution](http://nbviewer.jupyter.org/url/realai.org/course/tensorflow/solving-MNIST-by-convolution.ipynb) (hosted on nbviewer; [GitHub](https://github.com/real-ai/realai.org/blob/master/course/tensorflow/solving-MNIST-by-convolution.ipynb); [source](http://realai.org/course/tensorflow/solving-MNIST-by-convolution.ipynb))

CNNs are directly applicable to more advanced or recent image classification tasks. The [CIFAR-10 and CIFAR-100](https://www.cs.toronto.edu/~kriz/cifar.html) data sets are images in 10 and 100 classes, respectively.

In August 2017, German commerce company [Zalando SE](http://www.zalando.com/) released [Fashion-MNIST](https://github.com/zalandoresearch/fashion-mnist), a data set of 60,000 training images and 10,000 test images in 28x28 grayscale, intended to serve as a direct drop-in replacement of the original MNIST dataset.

A simple model like the one we studied in this session is already close to adding value in the real world. In August 2016, it was reported that a Japanese farmer used a similar model to [sort cucumbers](https://cloud.google.com/blog/big-data/2016/08/how-a-japanese-cucumber-farmer-is-using-deep-learning-and-tensorflow).

### GPU

[Graphic Processing Unit](https://en.wikipedia.org/wiki/Graphics_processing_unit) (GPU) has become an indispensable device for large-scale deep learning projects today. A GPU has thousands of cores that can run in parallel, making it well-suited for the kind of numerical computations used in deep learning. A high-level library like TensorFlow goes through one or more intermediate layers to access a GPU. In a typical setup today with NVIDIA GPUs, a toolkit called [CUDA](http://www.nvidia.com/object/cuda_home_new.html) (Compute Unified Device Architecture) provides a development environment for high-performance GPU applications in general. A GPU-accelerated library [cuDNN](https://developer.nvidia.com/cudnn) provides highly-tuned building blocks specifically for deep learning, such as convolution, pooling, and normalization. These two components are major dependencies TensorFlow needs to run with GPU support. As of August 2017, TensorFlow 1.3.0 required CUDA 8.0 and cuDNN v6, and it was [anticipated](https://github.com/tensorflow/tensorflow/releases/tag/v1.3.0) that TensorFlow 1.4 would be released with cuDNN v7. The official TensorFlow installation page provides an up-to-date list of [NVIDIA requirements (Linux)](https://www.tensorflow.org/install/install_linux#nvidia_requirements_to_run_tensorflow_with_gpu_support). Following the steps below, we can build a VM on GCP with an [NVIDIA® Tesla® K80](http://www.nvidia.com/object/tesla-k80.html) GPU ([pricing](https://cloud.google.com/compute/pricing#gpus)). Running the machine translation experiment is optional:

* [Neural Machine Translation on Cloud GPU](http://realai.org/course/google-cloud-platform/gce-gpu-nmt/)

On our newly built VM, the CNN model in the previous session that took over 16 minutes to train on 8 vCPUs should now only take less than 2 minutes! With more computing power, let’s build a CNN with more convolutional layers for CIFAR-10:

* Jupyter Notebook: [Deep CNN for CIFAR-10](http://nbviewer.jupyter.org/url/realai.org/course/tensorflow/deep-cnn-for-CIFAR-10.ipynb) (hosted on nbviewer; [GitHub](https://github.com/real-ai/realai.org/blob/master/course/tensorflow/deep-cnn-for-CIFAR-10.ipynb); [source](http://realai.org/course/tensorflow/deep-cnn-for-CIFAR-10.ipynb))

### RNN

A [recurrent neural network](http://realai.org/course/deep-learning/recurrent-neural-network/) (RNN) is a class of neural networks that have been widely used in natural language tasks such as machine translation. They're very effective at generating sequences.

* Jupyter Notebook: [Character RNN](http://nbviewer.jupyter.org/url/realai.org/course/tensorflow/char-RNN.ipynb) (hosted on nbviewer; [GitHub](https://github.com/real-ai/realai.org/blob/master/course/tensorflow/char-RNN.ipynb); [source](http://realai.org/course/tensorflow/char-RNN.ipynb))

## Further Reading

* The official TensorFlow [Tutorials](https://www.tensorflow.org/tutorials/) contains demonstrations of how to do specific tasks.
* [TensorFlow Examples](https://github.com/aymericdamien/TensorFlow-Examples) is a tutorial designed for easily diving into TensorFlow, through examples. For readability, it includes both notebooks and source codes with explanation.
* [Effective TensorFlow](https://github.com/vahidk/EffectiveTensorflow) is [Vahid Kazemi](https://twitter.com/VahidK)’s attempt to write a series of articles on effective TensorFlow usage, and to keep the content up to date with the latest releases of TensorFlow API.
* 2017 January - June, Chip Huyen. [CS 20SI: Tensorflow for Deep Learning Research](http://web.stanford.edu/class/cs20si/). [GitHub](https://github.com/chiphuyen/stanford-tensorflow-tutorials). This Stanford University course covers the fundamentals and contemporary usage of the TensorFlow library for deep learning research.

### What's New

* 2017 September 12. [Introduction to TensorFlow Datasets and Estimators](https://developers.googleblog.com/2017/09/introducing-tensorflow-datasets.html). *Google Developers Blog*.

## Topics

### Dynamic Batching

TensorFlow is designed to run static computation graphs in which the data flow for each input is the same. Multiple inputs can then be easily batched together to take advantage of modern parallel computing hardware. This is not enough for some research cases where each distinct input may have a different computation graph. To address this challenge, Google [released](https://research.googleblog.com/2017/02/announcing-tensorflow-fold-deep.html) in February 2017 [TensorFlow Fold](https://github.com/tensorflow/fold/), a new library built on top of TensorFlow. It builds a separate computation graph from each input, then automatically combines these graph for batching, both within and across inputs. This is well suited for [implementing](https://github.com/tensorflow/fold/blob/master/tensorflow_fold/g3doc/sentiment.ipynb) a Tree-LSTM ([Tai et al., 2015](https://arxiv.org/abs/1503.00075)) model, where a batch of inputs ([s-expressions](https://en.wikipedia.org/wiki/S-expression) encoded as strings) are transformed into multiple input graphs, which are treated by the dynamic batching algorithm ([Looks et al., 2017](https://arxiv.org/abs/1702.02181)) as a single disconnected graph for automatic batching. The requirement of a fixed computation graph as input limits the applicability of TensorFlow Fold. For example, in the SPINN architecture ([Bowman & Gauthier et al., 2016](https://arxiv.org/abs/1603.06021)), the computation graphs depend on the values of the input, and are not fixed at the time input examples are loaded. It is relatively straightforward to [implement](https://devblogs.nvidia.com/parallelforall/recursive-neural-networks-pytorch/) ([GitHub](https://github.com/jekbradbury/examples/tree/spinn/snli)) batching (and unbatching) in this case with PyTorch, which natively supports dynamic computation graph. Static versus dynamic is one of the main differences between TensorFlow and PyTorch, and is further explained and demonstrated for conditional and loop structures on page 120-129 of the [slides](http://cs231n.stanford.edu/slides/2017/cs231n_2017_lecture8.pdf) used in a Stanford lecture. As of August 2017, dynamic graph support is an [open issue](https://github.com/tensorflow/tensorflow/issues/12321) in TensorFlow.

### Imperative Mode

TensorFlow's programming paradigm is [declarative](https://en.wikipedia.org/wiki/Declarative_programming): a dataflow graph is first defined, then sent to a session to run. Such a graph is supposedly easier to optimize. Long-time Python users, however, can experience difficulties adapting to TensorFlow if they're used to Python's [imperative](https://en.wikipedia.org/wiki/Imperative_programming) style, and some might prefer to use PyTorch, which has been claimed to be a good fit if you want [better development and debugging experience](https://medium.com/@dubovikov.kirill/pytorch-vs-tensorflow-spotting-the-difference-25c75777377b). [TensorFlow Eager](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/python/eager) is under active development as of September 2017, and could be a new imperative mode in TensorFlow, according to an [answer](https://stackoverflow.com/questions/45967895/what-is-tensorflow-eager-code-for) on Stack Overflow.

#### References

* 2017 February 22, Moshe Looks, Marcello Herreshoff, DeLesley Hutchins, and Peter Norvig. [Deep Learning with Dynamic Computation Graphs](https://arxiv.org/abs/1702.02181). *arXiv:1702.02181*.
* 2016 July 30, Samuel R. Bowman, Jon Gauthier, Abhinav Rastogi, Raghav Gupta, Christopher D. Manning, and Christopher Potts. [A Fast Unified Model for Parsing and Sentence Understanding](https://arxiv.org/abs/1603.06021). *arXiv:1603.06021*. [blog](https://nlp.stanford.edu/blog/hybrid-tree-sequence-neural-networks-with-spinn/).
* 2015 May 30, Kai Sheng Tai, Richard Socher, and Christopher D. Manning. [Improved Semantic Representations From Tree-Structured Long Short-Term Memory Networks](https://arxiv.org/abs/1503.00075). *arXiv:1503.00075*. [code](https://github.com/stanfordnlp/treelstm).

## Resources

* Links: [Python API Documentation](https://www.tensorflow.org/api_docs/python/) \| [Releases](https://github.com/tensorflow/tensorflow/tags) ([latest](https://github.com/tensorflow/tensorflow/blob/master/RELEASE.md)) \| [Official Twitter](https://twitter.com/tensorflow)
* Higher-Level Libraries: [TensorFlow Agents](https://github.com/tensorflow/agents) \| [TensorFlow Fold](https://github.com/tensorflow/fold) \| [Sonnet](https://github.com/deepmind/sonnet) \| [seq2seq](https://github.com/google/seq2seq) \| [Tensor2Tensor](https://github.com/tensorflow/tensor2tensor) \| [Keras](https://keras.io/) \| [TFLearn](http://tflearn.org/)
* Related GitHub Repositories: [TensorBoard](https://github.com/tensorflow/tensorboard) \| [magenta](https://github.com/tensorflow/magenta) \| [Deepmath](https://github.com/tensorflow/deepmath)


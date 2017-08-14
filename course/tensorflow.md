---
permalink: /course/tensorflow/
redirect_from: /course/TF/
title: Course | TensorFlow
---
# TensorFlow

[TensorFlow](https://www.tensorflow.org/) ([GitHub](https://github.com/tensorflow/tensorflow)) is one of the most popular [deep learning libraries](http://realai.org/course/libraries/) that we will use to implement projects. It is Google’s second-generation machine learning system, specifically designed to correct the shortcomings of [DistBelief](https://research.google.com/pubs/pub40565.html), its predecessor. TensorFlow was [open sourced by Google](https://research.googleblog.com/2015/11/tensorflow-googles-latest-machine_9.html) on November 9, 2015.

TensorFlow is designed to be used for both research and production. It enables distributed execution on a range of devices such as CPU, GPU and mobile. On the front end, it has APIs available in Python, C++, Java and Go. As of August 2017, the Python API is the most complete and the easiest to use. In version r1.2, higher-level APIs [tf.layers](https://www.tensorflow.org/api_docs/python/tf/layers) and [tf.estimator](https://www.tensorflow.org/api_docs/python/tf/estimator) are already in TensorFlow core. [Keras](https://www.tensorflow.org/api_docs/python/tf/contrib/keras) and [Learn](https://www.tensorflow.org/api_docs/python/tf/contrib/learn) are in [tf.contrib](https://www.tensorflow.org/api_docs/python/tf/contrib).

* Links: [Python API Documentation](https://www.tensorflow.org/api_docs/python/) \| [Releases](https://github.com/tensorflow/tensorflow/tags) \| [Official Twitter](https://twitter.com/tensorflow)
* Higher-Level Libraries: [TensorFlow Fold](https://github.com/tensorflow/fold) \| [Sonnet](https://github.com/deepmind/sonnet) \| [Tensor2Tensor](https://github.com/tensorflow/tensor2tensor) \| [Keras](https://keras.io/) \| [TFLearn](http://tflearn.org/)
* Related GitHub Repositories: [TensorBoard](https://github.com/tensorflow/tensorboard) \| [magenta](https://github.com/tensorflow/magenta) \| [Deepmath](https://github.com/tensorflow/deepmath)

## Basics

TensorFlow programs usually involve two phases: the construction phase of building a computation graph, and the execution phase of running that graph in a session.

Experiments in this section are conducted on an [n1-standard-1](https://cloud.google.com/compute/pricing#predefined_machine_types) instance on [Google Compute Engine](http://realai.org/course/google-compute-engine/). As of August 2017, the machine type costs less than $30 per month in [asia-east1](https://cloud.google.com/compute/docs/regions-zones/regions-zones#available). We use a Ubuntu 16.04 LTS boot image, with firewall rules that allow TCP access from ports 8888 and 6006 for Jupyter Notebook and TensorBoard, respectively. The environment can be set up by the following commands, explained in more details at [Running Jupyter on Google Compute Engine](http://realai.org/course/lab/gce-jupyter/):

```bash
curl https://bootstrap.pypa.io/get-pip.py | sudo python3 -
sudo pip3 install jupyter matplotlib tensorflow
echo >> .bashrc
echo "# Start Jupyter Notebook" >> .bashrc
echo "jupyter notebook --ip=0.0.0.0 &" >> .bashrc
source .bashrc
```


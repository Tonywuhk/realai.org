---
permalink: /course/deep-learning/convolutional-neural-network/
redirect_from:
  - /course/DL/CNN/
  - /course/DL/convolutional-neural-network/
  - /course/deep-learning/CNN/
---
# Convolutional Neural Network

A [convolutional neural network](https://en.wikipedia.org/wiki/Convolutional_neural_network) (CNN) is a neural network that makes substantial use of convolutions. To get started:

* 2016 July 20, Adit Deshpande. [A Beginner's Guide To Understanding Convolutional Neural Networks](https://adeshpande3.github.io/adeshpande3.github.io/A-Beginner%27s-Guide-To-Understanding-Convolutional-Neural-Networks/). *personal blog*.

Stanford University's master's level computer science course CS231n maintains [a more advanced overview of CNNs](http://cs231n.github.io/convolutional-networks/) on its course web site.

In the [Deep Models](http://realai.org/course/tensorflow/#deep-models) and [GPU](http://realai.org/course/tensorflow/#gpu) sessions of our [TensorFlow](http://realai.org/course/tensorflow/) course, we walk through the basic steps of building a deep CNN model for the [CIFAR-10](https://www.cs.toronto.edu/~kriz/cifar.html) dataset. The [TensorFlow Models](https://github.com/tensorflow/models) repository on GitHub contains many more models implemented in TensorFlow, including more sophisticated CNNs such as [Inception-v3](https://github.com/tensorflow/models/blob/master/inception/inception/slim/inception_model.py) and [ResNet](https://github.com/tensorflow/models/blob/master/resnet/resnet_model.py).

## Convolution

Other types of convolutions include dilated, transposed, and (spatial or depthwise) separable convolutions:

* 2017 July 23, Paul-Louis Pröve. [An Introduction to Different Types of Convolutions in Deep Learning](https://medium.com/towards-data-science/types-of-convolutions-in-deep-learning-717013397f4d). *Medium*.

## Applications

In November 2016, a group of Google researchers used a deep CNN to identify diabetic retinopathy ([Gulshan et al., 2016](https://research.google.com/pubs/pub45732.html)), a leading cause of blindness among adults. In January 2017, a group of researchers from Stanford University trained a single CNN to identify skin cancer ([Esteva et al., 2017](http://www.nature.com/nature/journal/v542/n7639/full/nature21056.html)).

### References

* 2016 November 29, Varun Gulshan, Lily Peng, Marc Coram, Martin Stumpe, Derek Wu, Arunachalam Narayanaswamy, Subhashini Venugopalan, Kasumi Widner, Tom Madams, Jorge Cuadros, Ramasamy Kim, Rajiv Raman, Philip Q Nelson, Jessica Mega, and Dale Webster. [Development and Validation of a Deep Learning Algorithm for Detection of Diabetic Retinopathy in Retinal Fundus Photographs](https://research.google.com/pubs/pub45732.html). *JAMA 2016*.
* 2017 January 25, Andre Esteva, Brett Kuprel, Roberto A. Novoa, Justin Ko, Susan M. Swetter, Helen M. Blau, and Sebastian Thrun. [Dermatologist-level classification of skin cancer with deep neural networks](http://www.nature.com/nature/journal/v542/n7639/full/nature21056.html). *Nature*, 542(7639):115-118.

## Further Reading

* 2017 April - June, Fei-Fei Li, Justin Johnson, and Serena Yeung. [CS 231N: Convolutional Neural Networks for Visual Recognition](http://cs231n.stanford.edu/). *Stanford University*.


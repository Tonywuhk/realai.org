---
permalink: /predictive-learning.html
---
# Predictive Learning

Predictive learning is machine learning with an objective of predicting future data. It is a commonly used intrinsic motivation that has a long root in neuroscience.

## Video Prediction

A general framework for video prediction is to learn a representation of an input video sequence, which can be transformed (or copied) into a new representation to be decoded into a future video sequence. [Srivastava et al. (2015)](https://arxiv.org/abs/1502.04681) used multilayer LSTM networks to predict future sequences of image patches and high-level “percepts” of video frames extracted using a pretrained convolutional net.

## References

* 2017 April 5, Alec Radford, Rafal Jozefowicz, and Ilya Sutskever. [Learning to Generate Reviews and Discovering Sentiment](https://arxiv.org/abs/1704.01444). *arXiv:1704.01444*.
* 2016 December 12, Mehdi Mirza, Aaron Courville, and Yoshua Bengio. [Generalizable Features From Unsupervised Learning](https://arxiv.org/abs/1612.03809). *arXiv:1612.03809*.
* 2016 November 6, Alexey Dosovitskiy and Vladlen Koltun. [Learning to Act by Predicting the Future](https://arxiv.org/abs/1611.01779). *arXiv:1611.01779*.
* 2016 August 19, Micah Richert, Dimitry Fisher, Filip Piekniewski, Eugene M. Izhikevich, and Todd L. Hylton. [Fundamental principles of cortical computation: unsupervised learning with prediction, compression and feedback](https://arxiv.org/abs/1608.06277). *arXiv:1608.06277*. [code](https://github.com/braincorp/ASC).
* 2016 July 22, Filip Piekniewski, Patryk Laurent, Csaba Petre, Micah Richert, Dimitry Fisher, and Todd Hylton. [Unsupervised Learning from Continuous Video in a Scalable Predictive Recurrent Network](https://arxiv.org/abs/1607.06854). *arXiv:1607.06854*. [code](https://github.com/braincorp/PVM).
* 2016 May 25, William Lotter, Gabriel Kreiman, and David Cox. [Deep Predictive Coding Networks for Video Prediction and Unsupervised Learning](https://arxiv.org/abs/1605.08104). *arXiv:1605.08104*.
* 2016 May 23, Chelsea Finn, Ian Goodfellow, and Sergey Levine. [Unsupervised Learning for Physical Interaction through Video Prediction](https://arxiv.org/abs/1605.07157). *arXiv:1605.07157*.
* 2015 February 16, Nitish Srivastava, Elman Mansimov, and Ruslan Salakhutdinov. [Unsupervised Learning of Video Representations using LSTMs](https://arxiv.org/abs/1502.04681). *arXiv:1502.04681*. [code](https://github.com/emansim/unsupervised-videos). [site](http://www.cs.toronto.edu/~nitish/unsupervised_video/).

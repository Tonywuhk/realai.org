---
permalink: /predictive-learning.html
---
# Predictive Learning

Predictive learning is machine learning with an objective of predicting future data. It is a commonly used intrinsic motivation that has a long root in neuroscience.

## Video Prediction

A general framework for video prediction is to learn a representation of an input video sequence, which can be transformed (or copied) into a new representation to be decoded into a future video sequence. [Srivastava et al. (2015)](https://arxiv.org/abs/1502.04681) used multilayer LSTM networks to predict future sequences of image patches and high-level “percepts” of video frames extracted using a pretrained convolutional net. [Oh et al. (2015)](https://arxiv.org/abs/1507.08750) allowed future video sequences to be conditioned on control inputs, and generated predictions of Atari game video frames that are both realistic and useful for control. [Mathieu et al. (2015)](https://arxiv.org/abs/1511.05440) proposed adversarial and image gradient difference losses, then used a multi-scale convolutional network to generate sharper future images. Inspired by the "predictive coding" concept from neuroscience, [Lotter et al. (2016)](https://arxiv.org/abs/1605.08104) built a multi-layer network where each layer made local predictions and only forwarded deviations from those predictions to subsequent layers.

## References

* 2017 April 5, Alec Radford, Rafal Jozefowicz, and Ilya Sutskever. [Learning to Generate Reviews and Discovering Sentiment](https://arxiv.org/abs/1704.01444). *arXiv:1704.01444*.
* 2016 December 12, Mehdi Mirza, Aaron Courville, and Yoshua Bengio. [Generalizable Features From Unsupervised Learning](https://arxiv.org/abs/1612.03809). *arXiv:1612.03809*.
* 2016 November 6, Alexey Dosovitskiy and Vladlen Koltun. [Learning to Act by Predicting the Future](https://arxiv.org/abs/1611.01779). *arXiv:1611.01779*.
* 2016 August 19, Micah Richert, Dimitry Fisher, Filip Piekniewski, Eugene M. Izhikevich, and Todd L. Hylton. [Fundamental principles of cortical computation: unsupervised learning with prediction, compression and feedback](https://arxiv.org/abs/1608.06277). *arXiv:1608.06277*. [code](https://github.com/braincorp/ASC).
* 2016 July 22, Filip Piekniewski, Patryk Laurent, Csaba Petre, Micah Richert, Dimitry Fisher, and Todd Hylton. [Unsupervised Learning from Continuous Video in a Scalable Predictive Recurrent Network](https://arxiv.org/abs/1607.06854). *arXiv:1607.06854*. [code](https://github.com/braincorp/PVM).
* 2016 May 25, William Lotter, Gabriel Kreiman, and David Cox. [Deep Predictive Coding Networks for Video Prediction and Unsupervised Learning](https://arxiv.org/abs/1605.08104). *arXiv:1605.08104*. [site](https://coxlab.github.io/prednet/).
* 2016 May 23, Chelsea Finn, Ian Goodfellow, and Sergey Levine. [Unsupervised Learning for Physical Interaction through Video Prediction](https://arxiv.org/abs/1605.07157). *arXiv:1605.07157*.
* 2015 November 17, Michael Mathieu, Camille Couprie, and Yann LeCun. [Deep multi-scale video prediction beyond mean square error](https://arxiv.org/abs/1511.05440). *arXiv:1511.05440*. [code](https://github.com/coupriec/VideoPredictionICLR2016). [site](http://cs.nyu.edu/~mathieu/iclr2016.html).
* 2015 July 31, Junhyuk Oh, Xiaoxiao Guo, Honglak Lee, Richard Lewis, and Satinder Singh. [Action-Conditional Video Prediction using Deep Networks in Atari Games](https://arxiv.org/abs/1507.08750). *arXiv:1507.08750*. [site](https://sites.google.com/a/umich.edu/junhyuk-oh/action-conditional-video-prediction).
* 2015 February 16, Nitish Srivastava, Elman Mansimov, and Ruslan Salakhutdinov. [Unsupervised Learning of Video Representations using LSTMs](https://arxiv.org/abs/1502.04681). *arXiv:1502.04681*. [code](https://github.com/emansim/unsupervised-videos). [site](http://www.cs.toronto.edu/~nitish/unsupervised_video/).

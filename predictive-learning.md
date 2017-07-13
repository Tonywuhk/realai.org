---
permalink: /predictive-learning/
---
# Predictive Learning

Predictive learning is machine learning with an objective of predicting future data. It is a commonly used intrinsic motivation that has a long root in neuroscience.

## Video Prediction

A general framework for video prediction is to learn a representation of an input video sequence, which can be transformed (or copied) into a new representation to be decoded into a future video sequence. [Srivastava et al. (2015)](https://arxiv.org/abs/1502.04681) used multilayer LSTM networks to predict future sequences of image patches and high-level “percepts” of video frames extracted using a pretrained convolutional net. [Mathieu et al. (2015)](https://arxiv.org/abs/1511.05440) proposed adversarial and image gradient difference losses, then used a multi-scale convolutional network to generate sharper future images. A similar multi-scale architecture is used in [Neverova & Luc et al. (2017)](https://arxiv.org/abs/1703.07684) to predict segmentation maps from earlier semantically segmented video frames, and substantially better results are achieved in the Cityscapes dataset.

Inspired by the "predictive coding" [(Rao & Ballard, 1999)](http://www.nature.com/neuro/journal/v2/n1/abs/nn0199_79.html) concept from neuroscience, [Lotter et al. (2016)](https://arxiv.org/abs/1605.08104) built a multi-layer network where each layer made local predictions and only forwarded deviations from those predictions to subsequent layers.

### Action-Conditional Prediction

Many environments change in response to the actions of agents. [Oh et al. (2015)](https://arxiv.org/abs/1507.08750) generated predictions of Atari game video frames that are both realistic and useful for control. Building on their work, [Chiappa et al. (2017)](https://arxiv.org/abs/1704.02254) developed alternative learning architectures and improved performance. [Santana & Hotz (2016)](https://arxiv.org/abs/1611.00050) built models to predict real world highway scenes for self-driving cars. In [Finn et al. (2016)](https://arxiv.org/abs/1605.07157), the distribution of pixel motions from the previous frame is modelled to achieve action-conditioned video prediction. The new frame is formed as a combination of multiple predictions in which pixels are constrained to move in a local region or to an affine image transformation from the previous frame.

In contrast to predicting future observations, [Oh et al. (2017)](https://arxiv.org/abs/1707.03497) propose the Value Prediction Network (VPN) reinforcement learning model that is trained to make action-conditional predictions of future *values*. It can then be rolled out for multi-step planning.

## References

* 2017 July 11, Junhyuk Oh, Satinder Singh, and Honglak Lee. [Value Prediction Network](https://arxiv.org/abs/1707.03497). *arXiv:1707.03497*.
* 2017 April 7, Silvia Chiappa, Sébastien Racaniere, Daan Wierstra, and Shakir Mohamed. [Recurrent Environment Simulators](https://arxiv.org/abs/1704.02254). *arXiv:1704.02254*.
* 2017 April 5, Alec Radford, Rafal Jozefowicz, and Ilya Sutskever. [Learning to Generate Reviews and Discovering Sentiment](https://arxiv.org/abs/1704.01444). *arXiv:1704.01444*.
* 2017 March 28, Natalia Neverova, Pauline Luc, Camille Couprie, Jakob Verbeek, and Yann LeCun. [Predicting Deeper into the Future of Semantic Segmentation](https://arxiv.org/abs/1703.07684). *arXiv:1703.07684*.
* 2016 December 28, David Silver, Hado van Hasselt, Matteo Hessel, Tom Schaul, Arthur Guez, Tim Harley, Gabriel Dulac-Arnold, David Reichert, Neil Rabinowitz, Andre Barreto, and Thomas Degris. [The Predictron: End-To-End Learning and Planning](https://arxiv.org/abs/1612.08810). *arXiv:1612.08810*.
* 2016 November 6, Alexey Dosovitskiy and Vladlen Koltun. [Learning to Act by Predicting the Future](https://arxiv.org/abs/1611.01779). *arXiv:1611.01779*.
* 2016 October 31, Eder Santana, Matthew Emigh, Pablo Zegers, and Jose C Principe. [Exploiting Spatio-Temporal Structure with Recurrent Winner-Take-All Networks](https://arxiv.org/abs/1611.00050). *arXiv:1611.00050*.
* 2016 October 17, Chelsea Finn, Ian Goodfellow, and Sergey Levine. [Unsupervised Learning for Physical Interaction through Video Prediction](https://arxiv.org/abs/1605.07157). *arXiv:1605.07157*.
* 2016 August 19, Micah Richert, Dimitry Fisher, Filip Piekniewski, Eugene M. Izhikevich, and Todd L. Hylton. [Fundamental principles of cortical computation: unsupervised learning with prediction, compression and feedback](https://arxiv.org/abs/1608.06277). *arXiv:1608.06277*. [code](https://github.com/braincorp/ASC).
* 2016 August 3, Eder Santana and George Hotz. [Learning a Driving Simulator](https://arxiv.org/abs/1608.01230). *arXiv:1608.01230*.
* 2016 July 22, Filip Piekniewski, Patryk Laurent, Csaba Petre, Micah Richert, Dimitry Fisher, and Todd Hylton. [Unsupervised Learning from Continuous Video in a Scalable Predictive Recurrent Network](https://arxiv.org/abs/1607.06854). *arXiv:1607.06854*. [code](https://github.com/braincorp/PVM).
* 2016 May 25, William Lotter, Gabriel Kreiman, and David Cox. [Deep Predictive Coding Networks for Video Prediction and Unsupervised Learning](https://arxiv.org/abs/1605.08104). *arXiv:1605.08104*. [site](https://coxlab.github.io/prednet/).
* 2016 May 23, Chelsea Finn, Ian Goodfellow, and Sergey Levine. [Unsupervised Learning for Physical Interaction through Video Prediction](https://arxiv.org/abs/1605.07157). *arXiv:1605.07157*. [code](https://github.com/tensorflow/models/tree/master/video_prediction). [site](https://sites.google.com/site/robotprediction/).
* 2015 November 17, Michael Mathieu, Camille Couprie, and Yann LeCun. [Deep multi-scale video prediction beyond mean square error](https://arxiv.org/abs/1511.05440). *arXiv:1511.05440*. [code](https://github.com/coupriec/VideoPredictionICLR2016). [site](http://cs.nyu.edu/~mathieu/iclr2016.html).
* 2015 July 31, Junhyuk Oh, Xiaoxiao Guo, Honglak Lee, Richard Lewis, and Satinder Singh. [Action-Conditional Video Prediction using Deep Networks in Atari Games](https://arxiv.org/abs/1507.08750). *arXiv:1507.08750*. [site](https://sites.google.com/a/umich.edu/junhyuk-oh/action-conditional-video-prediction).
* 2015 February 16, Nitish Srivastava, Elman Mansimov, and Ruslan Salakhutdinov. [Unsupervised Learning of Video Representations using LSTMs](https://arxiv.org/abs/1502.04681). *arXiv:1502.04681*. [code](https://github.com/emansim/unsupervised-videos). [site](http://www.cs.toronto.edu/~nitish/unsupervised_video/).
* 1999, Rajesh P. N. Rao and Dana H. Ballard. [Predictive coding in the visual cortex: a functional interpretation of some extra-classical receptive-field effects](http://www.nature.com/neuro/journal/v2/n1/abs/nn0199_79.html). *Nature Neuroscience*, 2:79-87.

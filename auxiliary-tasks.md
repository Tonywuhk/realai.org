---
permalink: /auxiliary-tasks/
---
# Auxiliary tasks

[Jaderberg & Mnih & Czarnecki et al. (2016)](https://arxiv.org/abs/1611.05397) introduced the **UNREAL** agent that optimizes the combined loss function of reinforcement learning and auxiliary control and reward tasks. The agent significantly outperformed the previous state-of-the-art on Atari. [Shelhamer et al. (2016)](https://arxiv.org/abs/1612.07307) showed that self-supervised pre-training on auxiliary losses also improves reinforcment learning. [Dilokthanakul et al. (2017)](https://arxiv.org/abs/1705.06769) proposed two auxiliary tasks, pixel control and feature control. Their hierarchical model has a metal controller sending tasks and rewards to a subcontroller. In pixel control, the subcontroller is rewarded for changing the pixel values of a particular patch in the input image. In feature control, the subcontroller is rewarded for changing the mean activation value of a particular feature map in a convolutional neural network that encodes the input.

## References

* 2017 May 19, Nat Dilokthanakul, Christos Kaplanis, Nick Pawlowski, and Murray Shanahan. [Feature Control as Intrinsic Motivation for Hierarchical Reinforcement Learning](https://arxiv.org/abs/1705.06769). *arXiv:1705.06769*.
* 2016 December 21, Evan Shelhamer, Parsa Mahmoudieh, Max Argus, and Trevor Darrell. [Loss is its own Reward: Self-Supervision for Reinforcement Learning](https://arxiv.org/abs/1612.07307). *arXiv:1612.07307*.
* 2016 November 16, Max Jaderberg, Volodymyr Mnih, Wojciech Marian Czarnecki, Tom Schaul, Joel Z Leibo, David Silver, and Koray Kavukcuoglu. [Reinforcement Learning with Unsupervised Auxiliary Tasks](https://arxiv.org/abs/1611.05397). *arXiv:1611.05397*.
  * 2016 March 4. [modified version](https://openreview.net/forum?id=SJ6yPD5xg). *OpenReview*.
  * 2016 December 10, Kosuke Miyoshi. [replication using TensorFlow and DeepMind Lab](https://github.com/miyosuda/unreal). *GitHub*.
* 2016 November 11, Piotr Mirowski, Razvan Pascanu, Fabio Viola, Hubert Soyer, Andrew J. Ballard, Andrea Banino, Misha Denil, Ross Goroshin, Laurent Sifre, Koray Kavukcuoglu, Dharshan Kumaran, and Raia Hadsell. [Learning to Navigate in Complex Environments](https://arxiv.org/abs/1611.03673). *arXiv:1611.03673*.
* 2016 September 18, Guillaume Lample and Devendra Singh Chaplot. [Playing FPS Games with Deep Reinforcement Learning](https://arxiv.org/abs/1609.05521). *arXiv:1609.05521*.

---
permalink: /exploration/
mathjax: true
---
# Exploration

Exploration encourages agents to cover the space of possible strategies broadly in order to avoid getting stuck in a local optima. It is an important approach to [intrinsic motivation](http://realai.org/intrinsic-motivation). A simple form of exploration is \\(\epsilon\\)-greedy where at every time step an agent picks a random action with a small probability \\(\epsilon\\). Another form is to add noise to the parameters of models used in common RL algorithms ([Plappert et al., 2017](https://arxiv.org/abs/1706.01905)). There is no obvious "motivation" in these examples, and most forms of exploration covered in this section involve more sophisticated designs, perhaps better described using the word *curiosity*.

The **Bootstrapped DQN** ([Osband et al., 2016](https://arxiv.org/abs/1602.04621)) architecture consists of several "heads" independently branching off a shared network. In each episode, a random head is selected for exploration, then the agent follows the head's optimal policy to fill the replay buffer, including a random mask per step to indicate which heads will use this step's data when trained by the standard DQN algorithm.

[Bellemare et al. (2016)](https://arxiv.org/abs/1606.01868) proposed a measure called *pseudo-count*, which can be derived from an arbitrary density model and is closely related to intrinsically motivated gains in information and prediction. [Ostrovski et al. (2017)](https://arxiv.org/abs/1703.01310) used PixelCNN ([van den Oord et al., 2016-Jan](https://arxiv.org/abs/1601.06759); [van den Oord et al., 2016-Jun](https://arxiv.org/abs/1606.05328)) to supply the pseudo-count, and improved the state of the art on several hard [Atari games](http://realai.org/games/#atari-2600).

## References

* 2017 June 6, Matthias Plappert, Rein Houthooft, Prafulla Dhariwal, Szymon Sidor, Richard Y. Chen, Xi Chen, Tamim Asfour, Pieter Abbeel, and Marcin Andrychowicz. [Parameter Space Noise for Exploration](https://arxiv.org/abs/1706.01905). *arXiv:1706.01905*.
* 2017 March 22, Ian Osband, Daniel Russo, Zheng Wen, and Benjamin Van Roy. [Deep Exploration via Randomized Value Functions](https://arxiv.org/abs/1703.07608). *arXiv:1703.07608*.
* 2017 March 15, Sainbayar Sukhbaatar, Ilya Kostrikov, Arthur Szlam, and Rob Fergus. [Intrinsic Motivation and Automatic Curricula via Asymmetric Self-Play](https://arxiv.org/abs/1703.05407). *arXiv:1703.05407*.
* 2017 March 6, Joshua Achiam and Shankar Sastry. [Surprise-Based Intrinsic Motivation for Deep Reinforcement Learning](https://arxiv.org/abs/1703.01732). *arXiv:1703.01732*.
* 2017 March 3, Georg Ostrovski, Marc G. Bellemare, Aaron van den Oord, and Remi Munos. [Count-Based Exploration with Neural Density Models](https://arxiv.org/abs/1703.01310). *arXiv:1703.01310*.
* 2017 March 3, Justin Fu, John D. Co-Reyes, and Sergey Levine. [EX2: Exploration with Exemplar Models for Deep Reinforcement Learning](https://arxiv.org/abs/1703.01260). *arXiv:1703.01260*.
* 2016 November 15, Haoran Tang, Rein Houthooft, Davis Foote, Adam Stooke, Xi Chen, Yan Duan, John Schulman, Filip De Turck, and Pieter Abbeel. [Exploration: A Study of Count-Based Exploration for Deep Reinforcement Learning](https://arxiv.org/abs/1611.04717). *arXiv:1611.04717*.
* 2016 June 16, Aaron van den Oord, Nal Kalchbrenner, Oriol Vinyals, Lasse Espeholt, Alex Graves, and Koray Kavukcuoglu. [Conditional Image Generation with PixelCNN Decoders](https://arxiv.org/abs/1606.05328). *arXiv:1606.05328*.
* 2016 June 6, Marc G. Bellemare, Sriram Srinivasan, Georg Ostrovski, Tom Schaul, David Saxton, and Remi Munos. [Unifying Count-Based Exploration and Intrinsic Motivation](https://arxiv.org/abs/1606.01868). *arXiv:1606.01868*.
* 2016 May 31, Rein Houthooft, Xi Chen, Yan Duan, John Schulman, Filip De Turck, and Pieter Abbeel. [VIME: Variational Information Maximizing Exploration](https://arxiv.org/abs/1605.09674). *arXiv:1605.09674*.
* 2016 February 15, Ian Osband, Charles Blundell, Alexander Pritzel, and Benjamin Van Roy. [Deep Exploration via Bootstrapped DQN](https://arxiv.org/abs/1602.04621). *arXiv:1602.04621*.
* 2016 January 25, Aaron van den Oord, Nal Kalchbrenner, and Koray Kavukcuoglu. [Pixel Recurrent Neural Networks](https://arxiv.org/abs/1601.06759). *arXiv:1601.06759*.

---
permalink: /intrinsic-motivation/
mathjax: true
---
# Intrinsic Motivation

The rewards reinforcement learning agents receive are commonly interpreted as signals from the achievement of desired outcomes, such as completion of tasks or high scores in games. But in most realistic settings such rewards are sparse and it's increasingly important for agents to rely on *internal* rewards to learn useful skills. These rewards should not be designed based on details of the *external* problems the agents learn to solve.

There are many approaches ([Oudeyer & Kaplan, 2008](http://www.lucs.lu.se/LUCS/139/oudeyer.pdf)) to intrinsic motivation, some commonly used ones include:

* [Prediction](http://realai.org/predictive-learning/)
* [Exploration](http://realai.org/exploration/)
* [Empowerment](http://realai.org/empowerment/)

Intrinsic motivation can depend on the architecture of agents, while agnosticity in the specifics of tasks is maintained. [Florensa et al. (2017)](https://arxiv.org/abs/1704.03012) designed a single proxy reward that encodes the prior about useful high level bahaviors, then combined Stochastic Neural Networks with mutual information to encourage diversity of skills.

## Intrinsic Curiosity

The content of this section is based on [Pathak et al. (2017)](https://arxiv.org/abs/1705.05363).

### Model

A curious agent seeks to increase its own prediction error. Being intrinsically curious, the agent mainly cares about prediction error on the parts of observations that can affect itself. To accomplish that, the agent’s observations are transformed to a feature space representing only relevant information. Such a representation can be learned using a self-supervision task, where a neural network tries to predict the agent’s action given current and next observations.

Mathematically, the agent’s goal is to

$$
  \min_{\theta_P, \theta_I, \theta_F} \Big[ -\lambda \mathbb{E} [R_t] + (1-\beta) L_I(\hat{a}_t, a_t) + \beta L_F \Big],
$$

where the three terms are used for curiosity-driven exploration, learning intrinsically useful representations, and forward prediction. The first term captures both extrinsic and intrinsic rewards:

$$
\mathbb{E}[R_t] = \mathbb{E}_{\pi(s_t; \theta_P} [ \Sigma_t ( r^e_t + r^i_t ) ],
$$

where \\(\theta_P\\) parametrizes policy \\(\pi\\). Extrinsic rewards \\(r^e_t\\) can be very sparse. Intrinsic rewards

$$
r^i_t = \frac{\eta}{2} \| \hat{\phi}(s_{t+1} - \phi(s_{t+1}) \|_2^2,
$$

where \\(\eta > 0\\) is a scaling factor, and

$$
\hat{\phi}(s_{t+1}) = f(\phi(s_t), a_t; \theta_F)
$$

is the predicted representation of observation computed by a neural network with parameters \\(\theta_F\\).

## References

* 2017 May 15, [Deepak Pathak](https://people.eecs.berkeley.edu/~pathak/), Pulkit Agrawal, Alexei A. Efros, and [Trevor Darrell](https://people.eecs.berkeley.edu/~trevor/). [Curiosity-driven Exploration by Self-supervised Prediction](https://arxiv.org/abs/1705.05363). *arXiv:1705.05363*. [site](https://pathak22.github.io/noreward-rl/). [code](https://github.com/pathak22/noreward-rl).
* 2017 April 10, Carlos Florensa, Yan Duan, and Pieter Abbeel. [Stochastic Neural Networks for Hierarchical Reinforcement Learning](https://arxiv.org/abs/1704.03012). *arXiv:1704.03012*.
* 2008 July 30, Pierre-Yves Oudeyer and Frederic Kaplan. [How can we define intrinsic motivation?](http://www.lucs.lu.se/LUCS/139/oudeyer.pdf). *Proceedings of the Eighth International Conference on Epigenetic Robotics: Modeling Cognitive Development in Robotic Systems*, 93-101.

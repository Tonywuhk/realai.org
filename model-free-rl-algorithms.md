---
permalink: /model-free-rl-algorithms/
mathjax: true
---
# Model-Free Reinforcement Learning Algorithms

A Markov Decision Process is defined by a tuple \\(M=(\mathcal{S},\mathcal{A},\mathcal{P},r,\rho_0,\gamma,T)\\), in which \\(\mathcal{S}\\) is a state set, \\(\mathcal{A}\\) an action set, \\(\mathcal{P}: \mathcal{S}\times\mathcal{A}\times\mathcal{S} \rightarrow \mathbb{R}_+\\) a transition probability function, \\(r\\) a reward function, \\(\rho_0\\) an initial state distribution, \\(\gamma\\) a discount factor, and \\(T\\) the horizon.

## References

* 2017 February 28, Ofir Nachum, Mohammad Norouzi, Kelvin Xu, and Dale Schuurmans. [Bridging the Gap Between Value and Policy Based Reinforcement Learning](https://arxiv.org/abs/1702.08892). *arXiv:1702.08892*.
* 2017 February 27, Tuomas Haarnoja, Haoran Tang, Pieter Abbeel, and Sergey Levine. [Reinforcement Learning with Deep Energy-Based Policies](https://arxiv.org/abs/1702.08165). *arXiv:1702.08165*.
* 2016 November 5, Brendan O'Donoghue, Remi Munos, Koray Kavukcuoglu, and Volodymyr Mnih. [PGQ: Combining policy gradient and Q-learning](https://arxiv.org/abs/1611.01626). *arXiv:1611.01626*.

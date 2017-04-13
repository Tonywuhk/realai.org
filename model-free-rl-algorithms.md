---
permalink: /model-free-rl-algorithms/
mathjax: true
---
# Model-Free Reinforcement Learning Algorithms

A Markov Decision Process is defined by a tuple \\(M=(\mathcal{S},\mathcal{A},\mathcal{P},r,\rho_0,\gamma,T)\\), in which \\(\mathcal{S}\\) is a state set, \\(\mathcal{A}\\) an action set, \\(\mathcal{P}: \mathcal{S}\times\mathcal{A}\times\mathcal{S} \rightarrow \mathbb{R}_+\\) a transition probability distribution, \\(r: \mathcal{S}\times\mathcal{A} \rightarrow \matbb{R}\\) a reward function, \\(\rho_0: \mathcal{S} \rightarrow \mathbb{R}_+\\) an initial state distribution, \\(\gamma \in [0,1]\\) a discount factor, and \\(T\\) a horizon.

[Hester et al. (2017)](https://arxiv.org/abs/1704.03732) used a combination of the double Q-learning, a supervised large margin classification loss, and an L2 regularization loss

$$
J(Q} = J_{DQ}(Q} + \lambda_1 J_E(Q) + \lambda_2 J_{L2}(Q)
$$

to update the work, where the \\(\lambda\\) parameters control the relative weighting.

## References

* 2017 April 12, Todd Hester, Matej Vecerik, Olivier Pietquin, Marc Lanctot, Tom Schaul, Bilal Piot, Andrew Sendonaris, Gabriel Dulac-Arnold, Ian Osband, John Agapiou, Joel Z. Leibo, and Audrunas Gruslys. [Learning from Demonstrations for Real World Reinforcement Learning](https://arxiv.org/abs/1704.03732). *arXiv:1704.03732*.
* 2017 February 28, Ofir Nachum, Mohammad Norouzi, Kelvin Xu, and Dale Schuurmans. [Bridging the Gap Between Value and Policy Based Reinforcement Learning](https://arxiv.org/abs/1702.08892). *arXiv:1702.08892*.
* 2017 February 27, Tuomas Haarnoja, Haoran Tang, Pieter Abbeel, and Sergey Levine. [Reinforcement Learning with Deep Energy-Based Policies](https://arxiv.org/abs/1702.08165). *arXiv:1702.08165*.
* 2016 November 5, Brendan O'Donoghue, Remi Munos, Koray Kavukcuoglu, and Volodymyr Mnih. [PGQ: Combining policy gradient and Q-learning](https://arxiv.org/abs/1611.01626). *arXiv:1611.01626*.

---
permalink: /model-free-rl-algorithms/
mathjax: true
---
# Model-Free Reinforcement Learning Algorithms

A Markov Decision Process is defined by a tuple \\(M=(\mathcal{S},\mathcal{A},\mathcal{P},r,\rho_0,\gamma,T)\\), in which \\(\mathcal{S}\\) is a state set, \\(\mathcal{A}\\) an action set, \\(\mathcal{P}: \mathcal{S}\times\mathcal{A}\times\mathcal{S} \rightarrow \mathbb{R}\_+\\) a transition probability distribution, \\(r: \mathcal{S}\times\mathcal{A} \rightarrow \mathbb{R}\\) a reward function, \\(\rho_0: \mathcal{S} \rightarrow \mathbb{R}\_+\\) an initial state distribution, \\(\gamma \in [0,1]\\) a discount factor, and \\(T\\) a horizon.

The goal of an agent is to optimize its policy \\(\pi: \mathcal{S} \rightarrow \mathcal{A}\\), under which the expected value of future rewards is

$$
  Q^\pi (s,a) \equiv \mathbb{E}[r_1+ \gamma r_2+... | S_0=s, A_0=a, \pi].
$$

The optimal value \\(Q^\*(s,a) = \max\_\pi Q^\pi(s,a)\\) is achieved when the agent follows an optimal policy \\(\pi^\*\\), but is often too complex for interesting problems. A parameterized function \\(Q(s, a; \theta\_t)\\) is often learned instead, by popular algorithms such as Q-learning. To reduce the algorithm's overestimation problem, [van Hasselt et al. (2015)](https://arxiv.org/abs/1509.06461) proposed the double DQN algorithm that learns the target

$$
  Y_t^{DQ} \equiv R_{t+1} + \gamma Q(S_{t+1}, \arg\max{a} Q(S_{t+1}, a; \theta_t), \theta_t^-).
$$

[Hester et al. (2017)](https://arxiv.org/abs/1704.03732) used a combination of the double DQN loss \\(J\_{DQ} \equiv (Y^{DQ} - Q(s,a; \theta))^2\\), a supervised large margin classification loss, and an L2 regularization loss

\begin{equation}
  J(Q) = J_{DQ}(Q) + \lambda_1 J_E(Q) + \lambda_2 J_{L2}(Q)
  \label{eq:DQfD}
\end{equation}

to update the network, where the \\(\lambda\\) parameters control the relative weighting.

## References

* 2017 April 12, Todd Hester, Matej Vecerik, Olivier Pietquin, Marc Lanctot, Tom Schaul, Bilal Piot, Andrew Sendonaris, Gabriel Dulac-Arnold, Ian Osband, John Agapiou, Joel Z. Leibo, and Audrunas Gruslys. [Learning from Demonstrations for Real World Reinforcement Learning](https://arxiv.org/abs/1704.03732). *arXiv:1704.03732*.
* 2017 February 28, Ofir Nachum, Mohammad Norouzi, Kelvin Xu, and Dale Schuurmans. [Bridging the Gap Between Value and Policy Based Reinforcement Learning](https://arxiv.org/abs/1702.08892). *arXiv:1702.08892*.
* 2017 February 27, Tuomas Haarnoja, Haoran Tang, Pieter Abbeel, and Sergey Levine. [Reinforcement Learning with Deep Energy-Based Policies](https://arxiv.org/abs/1702.08165). *arXiv:1702.08165*.
* 2016 November 5, Brendan O'Donoghue, Remi Munos, Koray Kavukcuoglu, and Volodymyr Mnih. [PGQ: Combining policy gradient and Q-learning](https://arxiv.org/abs/1611.01626). *arXiv:1611.01626*.
* 2015 September 22, Hado van Hasselt, Arthur Guez, and David Silver. [Deep Reinforcement Learning with Double Q-learning](https://arxiv.org/abs/1509.06461). *arXiv:1509.06461*.

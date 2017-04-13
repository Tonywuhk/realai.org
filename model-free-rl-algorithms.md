---
permalink: /model-free-rl-algorithms/
mathjax: true
---
# Model-Free Reinforcement Learning Algorithms

A Markov Decision Process is defined by a tuple \\(M=(\mathcal{S},\mathcal{A},\mathcal{P},r,\rho_0,\gamma,T)\\), in which \\(\mathcal{S}\\) is a state set, \\(\mathcal{A}\\) an action set, \\(\mathcal{P}: \mathcal{S}\times\mathcal{A}\times\mathcal{S} \rightarrow \mathbb{R}\_+\\) a transition probability distribution, \\(r: \mathcal{S}\times\mathcal{A} \rightarrow \mathbb{R}\\) a reward function, \\(\rho_0: \mathcal{S} \rightarrow \mathbb{R}\_+\\) an initial state distribution, \\(\gamma \in [0,1]\\) a discount factor, and \\(T\\) a horizon.

At time \\(t\\) an agent observes the state \\(s\_t\\) of the environment and produces an action \\(a\_t = \pi(s\_t)\\), then the environment transitions to a new state \\(s\_{t+1} \sim p(\cdot \| s\_t, a\_t)\\), and the agent receives a reward \\(r\_t = r(s\_t, a\_t)\\). The goal of an agent is to optimize its policy \\(\pi: \mathcal{S} \rightarrow \mathcal{A}\\), under which the expected value of future rewards is

$$
  Q^\pi (s,a) \equiv \mathbb{E}[r_1+ \gamma r_2+... | S_0=s, A_0=a, \pi].
$$

The optimal value \\(Q^\*(s,a) = \max\_\pi Q^\pi(s,a)\\) is achieved when the agent follows an optimal policy \\(\pi^\*\\). The two dominant approaches have been value based and policy based algorithms.

## Policy Based Reinforcement Learning Algorithms

Policy learning directly optimizes the parameters \\(\theta\\) of a policy \\(\pi(s\_t; \theta)\\). [Lillicrap & Hunt et al. (2015)](https://arxiv.org/abs/1509.02971) presented the Deep DPG (DDPG) approach, an actor-critic algorithm that can operate over continuous action spaces. [Popov et al. (2017)](https://arxiv.org/abs/1704.03073) introduced two extensions to the DDPG method, significantly improving its data efficiency.

## Value Based Reinforcement Learning Algorithms

The true \\(Q^\*(s, a)\\) is often too complex for interesting problems, and we instead learn a parameterized version \\(Q(s, a; \theta\_t)\\), by popular algorithms such as Q-learning. To reduce the algorithm's overestimation problem, [van Hasselt et al. (2015)](https://arxiv.org/abs/1509.06461) proposed the double DQN algorithm that learns the target

$$
  Y_t^{DQ} \equiv r_{t+1} + \gamma Q(S_{t+1}, \arg\max_{a} Q(S_{t+1}, a; \theta_t), \theta_t^-).
$$

[Hester et al. (2017)](https://arxiv.org/abs/1704.03732) used a combination of the double DQN loss \\(J\_{DQ} \equiv (Y\_t^{DQ} - Q(s\_t,a\_t; \theta\_t))^2\\), a supervised large margin classification loss, and an L2 regularization loss

\begin{equation}
  J(Q) = J_{DQ}(Q) + \lambda_1 J_E(Q) + \lambda_2 J_{L2}(Q)
  \label{eq:DQfD}
\end{equation}

to update the network, where the \\(\lambda\\) parameters control the relative weighting.

## References

* 2017 April 12, Todd Hester, Matej Vecerik, Olivier Pietquin, Marc Lanctot, Tom Schaul, Bilal Piot, Andrew Sendonaris, Gabriel Dulac-Arnold, Ian Osband, John Agapiou, Joel Z. Leibo, and Audrunas Gruslys. [Learning from Demonstrations for Real World Reinforcement Learning](https://arxiv.org/abs/1704.03732). *arXiv:1704.03732*.
* 2017 April 10, Ivaylo Popov, Nicolas Heess, Timothy Lillicrap, Roland Hafner, Gabriel Barth-Maron, Matej Vecerik, Thomas Lampe, Yuval Tassa, Tom Erez, and Martin Riedmiller. [Data-efficient Deep Reinforcement Learning for Dexterous Manipulation](https://arxiv.org/abs/1704.03073). *arXiv:1704.03073*.
* 2017 February 28, Ofir Nachum, Mohammad Norouzi, Kelvin Xu, and Dale Schuurmans. [Bridging the Gap Between Value and Policy Based Reinforcement Learning](https://arxiv.org/abs/1702.08892). *arXiv:1702.08892*.
* 2017 February 27, Tuomas Haarnoja, Haoran Tang, Pieter Abbeel, and Sergey Levine. [Reinforcement Learning with Deep Energy-Based Policies](https://arxiv.org/abs/1702.08165). *arXiv:1702.08165*.
* 2016 November 5, Brendan O'Donoghue, Remi Munos, Koray Kavukcuoglu, and Volodymyr Mnih. [PGQ: Combining policy gradient and Q-learning](https://arxiv.org/abs/1611.01626). *arXiv:1611.01626*.
* 2015 September 22, Hado van Hasselt, Arthur Guez, and David Silver. [Deep Reinforcement Learning with Double Q-learning](https://arxiv.org/abs/1509.06461). *arXiv:1509.06461*.
* 2015 September 9, Timothy P. Lillicrap, Jonathan J. Hunt, Alexander Pritzel, Nicolas Heess, Tom Erez, Yuval Tassa, David Silver, and Daan Wierstra. [Continuous control with deep reinforcement learning](https://arxiv.org/abs/1509.02971). *arXiv:1509.02971*.
* 2014 July 10, Volodymyr Mnih,	Koray Kavukcuoglu, David Silver, Andrei A. Rusu, Joel Veness, Marc G. Bellemare, Alex Graves, Martin Riedmiller, Andreas K. Fidjeland, Georg Ostrovski, Stig Petersen, Charles Beattie, Amir Sadik, Ioannis Antonoglou, Helen King, Dharshan Kumaran, Daan Wierstra, Shane Legg, and Demis Hassabis. [Human-level control through deep reinforcement learning](http://www.nature.com/nature/journal/v518/n7540/abs/nature14236.html). *Nature*, 518(7450):529-533, 2015.
* 2014 January 27, David Silver, Guy Lever, Nicolas Heess, Thomas Degris, Daan Wierstra, and Martin Riedmiller. [Deterministic Policy Gradient Algorithms](http://jmlr.org/proceedings/papers/v32/silver14.html). *Proceedings of The 31st International Conference on Machine Learning*, 387-395.

---
permalink: /model-free-rl-algorithms/
mathjax: true
---
# Model-Free Reinforcement Learning Algorithms

A Markov Decision Process is defined by a tuple \\(M=(\mathcal{S},\mathcal{A},\mathcal{P},r,\rho_0,\gamma,T)\\), in which \\(\mathcal{S}\\) is a state set, \\(\mathcal{A}\\) an action set, \\(\mathcal{P}: \mathcal{S}\times\mathcal{A}\times\mathcal{S} \rightarrow [0,1]\\) a transition probability distribution, \\(r: \mathcal{S}\times\mathcal{A} \rightarrow \mathbb{R}\\) a reward function, \\(\rho_0: \mathcal{S} \rightarrow [0,1]\\) an initial state distribution, \\(\gamma \in [0,1]\\) a discount factor, and \\(T\\) a horizon.

At time \\(t\\) an agent observes the state \\(s\_t\\) of the environment and produces an action \\(a\_t \sim \pi(\cdot \| s\_t)\\), then the environment transitions to a new state \\(s\_{t+1} \sim p(\cdot \| s\_t, a\_t)\\), and the agent receives a reward \\(r\_t = r(s\_t, a\_t)\\). The total accumulated reward from time \\(t\\) is

$$
  R_t = r_t + \gamma r_{t+1} + \gamma^2 r_{t+2} + ...
$$

The goal of the agent is to optimize its policy \\(\pi: \mathcal{S}\times\mathcal{A} \rightarrow \mathbb{R}\_+ \\), such that the *action-value function*

$$
  Q^\pi (s,a) = \mathbb{E}[R_0 | S_0=s, A_0=a, \pi]
$$

is maximized. The optimal action-value function \\(Q^\*(s,a) = \max\_\pi Q^\pi(s,a)\\) is achieved when the agent follows an optimal policy \\(\pi^\*\\). The \\(n\\)-step \\(Q\\)-value is defined as

$$
  Q^{(n)} (s,a) = r_t + \gamma r_{t+1} + ... + \gamma^{N-1} r_{t+N-1} + \gamma^n \max_{a'} Q(s_{t+N}, a').
$$

Similarly, the *state-value function*

$$
  V^\pi (s) = \mathbb{E}[R_0 | S_0=s, \pi],
$$

and the optimal state-value function \\(V^\*(s) = \max\_\pi V^\pi(s)\\). The *advantage function* is defined as \\(A^\pi (s,a) = Q^\pi(s,a) - V^\pi(s)\\). The true \\(Q^\*(s, a)\\) and \\(V^\*(s)\\) are often too complex for interesting problems, so in practice we learn a parameterized version \\(Q(s, a; \theta)\\) and \\(V(s; \theta_v)\\).

## Value Based Reinforcement Learning Algorithms

In the **Deep Q-Network (DQN)** algorithm ([Mnih & Kavukcuoglu & Silver et al., 2015](http://www.nature.com/nature/journal/v518/n7540/abs/nature14236.html)), we learn a target

$$
  Y^{DQN} = r+\gamma \max_{a'} Q(s', a'; \theta^-)
$$

by minimizing a loss function

$$
  L^{DQN} (\theta) = (Y^{DQN} - Q(s, a; \theta))^2,
$$

where \\(\theta^-\\) is a previous version that's periodically copied from \\(\theta\\), a random minibatch of transitions \\((s, a, r, s')\\) are sampled from a memory buffer used for experience replay, and gradient descent is used to update parameters \\(\theta\\).

To reduce the DQN algorithm's overestimation problem, [van Hasselt et al. (2015)](https://arxiv.org/abs/1509.06461) proposed the **double DQN (DDQN)** algorithm that learns the target

$$
  Y^{DDQN} = r + \gamma Q(s', \arg\max_{a'} Q(s', a'; \theta), \theta^-).
$$

In a setting where the agent has access to previous control data, [Hester et al. (2017)](https://arxiv.org/abs/1704.03732) proposed the **Deep Q-Learning from Demonstrations (DQfD)** algorithm where a combination of the double DQN loss, a supervised large margin classification loss, and an L2 regularization loss, weighted by the \\(\lambda\\) parameters,

\begin{equation}
  L^{DQfD}(\theta) = L^{DDQN}(\theta) + \lambda_1 L^E(\theta) + \lambda_2 L^{(2)}(\theta)
  \label{eq:DQfD}
\end{equation}

was used to update the network.

### Improvements

[Levine & Zahavy et al. (2017)](https://arxiv.org/abs/1705.07461) improve the performance over DQN and DDQN by repeatedly retraining the weights of the last hidden layer of the deep Q-networks. The training is based on least squares shallow learning method where it is essential to use a Bayesian regularization that treats the last layer's weights as a Bayesian prior.

### Continuous Actions

Estimating the \\(Q\\)-values is difficult when the actions can be continuous and high dimensional. [Metz et al. (2017)](https://arxiv.org/abs/1705.05035) proposed Sequential DQN (SDQN) that uses next-step prediction to model the \\(Q\\)-values and policies over discretized dimensions.

## Policy Based Reinforcement Learning Algorithms

Policy learning directly optimizes the parameters \\(\theta\\) of a policy \\(\pi(a\_t \| s\_t; \theta)\\), sometimes with the help of learning a value function \\(V(s; \theta_v)\\). In the standard REINFORCE with baseline algorithm, the policy parameters \\(\theta\\) are often updated in the direction of 

$$
  (R_t - V(s_t; \theta_v)) \cdot \nabla_\theta \log \pi(a_t | s_t; \theta),
$$

and \\(V(s\_t; \theta_v)\\) learns the target \\(R\_t\\). In actor-critic methods, the full accumulated reward \\(R\_t\\) is replaced by a target involving state values of subsequent states. Define

$$
  A(s_t, a_t; \theta, \theta_v) = r_t + \gamma r_{t+1} + ... + \gamma^{n-1} r_{t+n-1} + \gamma^n V(s_{t+n}; \theta_v) - V(s_t; \theta_v),
$$

an \\(n\\)-step estimate of the advantage function. In the asynchronous **advantage actor-critic (A3C)** algorithm proposed by [Mnih et al. (2016)](https://arxiv.org/abs/1602.01783), policy gradient is

$$
  A(s_t, a_t; \theta, \theta_v) \cdot \nabla_\theta \log \pi(a_t | s_t; \theta)
$$

augmented by the gradient of an entropy regularization term with respect to the policy parameters.

[Lillicrap & Hunt et al. (2015)](https://arxiv.org/abs/1509.02971) presented the Deep DPG (DDPG) approach, an actor-critic algorithm that can operate over continuous action spaces. [Popov et al. (2017)](https://arxiv.org/abs/1704.03073) introduced two extensions to the DDPG method, significantly improving its data efficiency.

[Gruslys et al. (2017)](https://arxiv.org/abs/1704.04651) proposed the *Reactor* actor-critic architecture in which the critic was trained by the Retrace algorithm and the actor by a novel \\(\beta\\)-leave-one-out policy gradient estimate. It used memory replay and multi-step returns.

[Schulman et al. (2017)](https://arxiv.org/abs/1704.06440) showed that entropy-regularized Q-learning is exactly equivalent to a policy gradient method.

## Episodic Control

Gradient-based learning is generally very slow and consumes a lot of data. When data is limited, agents can use episodic memory to remember past experiences, and quickly learn suboptimal policies that perform reasonably well. In [Blundell et al. (2016)](https://arxiv.org/abs/1606.04460), the maximum cumulative reward for each state-action pair is maintained in the memory:

$$
  Q^{EC}(s_t, a_t) \leftarrow
    \begin{cases}
      R_t & \text{if } (s_t, a_t) \notin Q^{EC}, \\
      \max \{ Q^{EC}(s_t, a_t), R_t \} & \text{otherwise,}
    \end{cases}
$$

and the \\(Q\\)-value for a novel state-action pair is approximated by the average of the existing \\(Q\\)-values of the k state-action pairs using the novel state’s k nearest neighbours. A differentiable version of this episodic memory is described in [Pritzel et al. (2017)](https://arxiv.org/abs/1703.01988). For each possible action, a *differentiable neural dictionary* (DND) is a dictionary of key-value pairs, where the key \\(h\\) is a representation of the agent’s observation in state \\(s\\),

$$
  Q(h) \leftarrow
    \begin{cases}
      Q^{(N)}(s, a) & \text{if } h \notin Q, \\
      Q(h) + \alpha(Q^{(N)}(s, a) - Q(h)) & \text{otherwise,}
    \end{cases}
$$

where the learning rate \\(\alpha\\) could have a high value. State representations are obtained from a convolutional embedding network. The network’s parameters and the keys and values used in DND are learned by matching \\(Q\\) and \\(Q^{(N)}\\).

## References

* 2017 May 21, Nir Levine, Tom Zahavy, Daniel J. Mankowitz, Aviv Tamar, and Shie Mannor. [Shallow Updates for Deep Reinforcement Learning](https://arxiv.org/abs/1705.07461). *arXiv:1705.07461*.
* 2017 May 14, Luke Metz, Julian Ibarz, Navdeep Jaitly, and James Davidson. [Discrete Sequential Prediction of Continuous Actions for Deep RL](https://arxiv.org/abs/1705.05035). *arXiv:1705.05035*.
* 2017 April 21, John Schulman, Pieter Abbeel, and Xi Chen. [Equivalence Between Policy Gradients and Soft Q-Learning](https://arxiv.org/abs/1704.06440). *arXiv:1704.06440*.
* 2017 April 15, Audrunas Gruslys, Mohammad Gheshlaghi Azar, Marc G. Bellemare, and Remi Munos. [The Reactor: A Sample-Efficient Actor-Critic Architecture](https://arxiv.org/abs/1704.04651). *arXiv:1704.04651*.
* 2017 April 12, Todd Hester, Matej Vecerik, Olivier Pietquin, Marc Lanctot, Tom Schaul, Bilal Piot, Andrew Sendonaris, Gabriel Dulac-Arnold, Ian Osband, John Agapiou, Joel Z. Leibo, and Audrunas Gruslys. [Learning from Demonstrations for Real World Reinforcement Learning](https://arxiv.org/abs/1704.03732). *arXiv:1704.03732*.
* 2017 April 10, Ivaylo Popov, Nicolas Heess, Timothy Lillicrap, Roland Hafner, Gabriel Barth-Maron, Matej Vecerik, Thomas Lampe, Yuval Tassa, Tom Erez, and Martin Riedmiller. [Data-efficient Deep Reinforcement Learning for Dexterous Manipulation](https://arxiv.org/abs/1704.03073). *arXiv:1704.03073*.
* 2017 March 6, Alexander Pritzel, Benigno Uria, Sriram Srinivasan, Adrià Puigdomènech, Oriol Vinyals, Demis Hassabis, Daan Wierstra, and Charles Blundell. [Neural Episodic Control](https://arxiv.org/abs/1703.01988). *arXiv:1703.01988*.
* 2017 February 28, Ofir Nachum, Mohammad Norouzi, Kelvin Xu, and Dale Schuurmans. [Bridging the Gap Between Value and Policy Based Reinforcement Learning](https://arxiv.org/abs/1702.08892). *arXiv:1702.08892*.
* 2017 February 27, Tuomas Haarnoja, Haoran Tang, Pieter Abbeel, and Sergey Levine. [Reinforcement Learning with Deep Energy-Based Policies](https://arxiv.org/abs/1702.08165). *arXiv:1702.08165*.
* 2016 November 5, Brendan O'Donoghue, Remi Munos, Koray Kavukcuoglu, and Volodymyr Mnih. [PGQ: Combining policy gradient and Q-learning](https://arxiv.org/abs/1611.01626). *arXiv:1611.01626*.
* 2016 November 3, Ziyu Wang, Victor Bapst, Nicolas Heess, Volodymyr Mnih, Remi Munos, Koray Kavukcuoglu, and Nando de Freitas. [Sample Efficient Actor-Critic with Experience Replay](https://arxiv.org/abs/1611.01224). *arXiv:1611.01224*.
* 2016 June 14, Charles Blundell, Benigno Uria, Alexander Pritzel, Yazhe Li, Avraham Ruderman, Joel Z Leibo, Jack Rae, Daan Wierstra, and Demis Hassabis. [Model-Free Episodic Control](https://arxiv.org/abs/1606.04460). *arXiv:1606.04460*.
* 2016 June 8, Rémi Munos, Tom Stepleton, Anna Harutyunyan, and Marc G. Bellemare. [Safe and Efficient Off-Policy Reinforcement Learning](https://arxiv.org/abs/1606.02647). *arXiv:1606.02647*.
* 2016 February 4, Volodymyr Mnih, Adrià Puigdomènech Badia, Mehdi Mirza, Alex Graves, Timothy P. Lillicrap, Tim Harley, David Silver, and Koray Kavukcuoglu. [Asynchronous Methods for Deep Reinforcement Learning](https://arxiv.org/abs/1602.01783). *arXiv:1602.01783*.
* 2015 September 22, Hado van Hasselt, Arthur Guez, and David Silver. [Deep Reinforcement Learning with Double Q-learning](https://arxiv.org/abs/1509.06461). *arXiv:1509.06461*.
* 2015 September 9, Timothy P. Lillicrap, Jonathan J. Hunt, Alexander Pritzel, Nicolas Heess, Tom Erez, Yuval Tassa, David Silver, and Daan Wierstra. [Continuous control with deep reinforcement learning](https://arxiv.org/abs/1509.02971). *arXiv:1509.02971*.
* 2015 February 26, Volodymyr Mnih,	Koray Kavukcuoglu, David Silver, Andrei A. Rusu, Joel Veness, Marc G. Bellemare, Alex Graves, Martin Riedmiller, Andreas K. Fidjeland, Georg Ostrovski, Stig Petersen, Charles Beattie, Amir Sadik, Ioannis Antonoglou, Helen King, Dharshan Kumaran, Daan Wierstra, Shane Legg, and Demis Hassabis. [Human-level control through deep reinforcement learning](http://www.nature.com/nature/journal/v518/n7540/abs/nature14236.html). *Nature*, 518(7450):529-533. Received 2014 July 10.
* 2014 January 27, David Silver, Guy Lever, Nicolas Heess, Thomas Degris, Daan Wierstra, and Martin Riedmiller. [Deterministic Policy Gradient Algorithms](http://jmlr.org/proceedings/papers/v32/silver14.html). *Proceedings of The 31st International Conference on Machine Learning*, 387-395.

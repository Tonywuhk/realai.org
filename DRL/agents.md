---
permalink: /DRL/agents/
---
# Reinforcement Learning Agents

## Intentional Unintentional Agent

The Intentional Unintentional (IU) agent ([Cabi et al., 2017](https://arxiv.org/abs/1707.03300)) uses the deep deterministic policy gradients (DDPG) for continuous control with the ability to solve several tasks simultaneously. It consists of two neural networks (NNs). The actor NN has multiple-heads representing different policies with shared
lower-level representations. The critic NN represents several state-action value functions, sharing a common representation for the observations.

The IU agent seeks to maximize the expected value of all tasks while following a single intentional policy solving one of the hardest tasks in the physical playroom domain. The domain is implemented using the MuJoCo physics engine which consists multiple objects placed on a tabletop with different colors, sizes, shapes, etc. The agent is embodied as an actuated "fist" whose action space consists of 2-dimensional velocities. The authors demonstrate that when acting according to the policy associated with one of the hardest tasks, the agent is able to learn all other tasks off-policy. Learning is faster and more effective when the number of tasks increases.

## Imagination-Augmented Agent

The Imagination-Augmented Agent (I2A) uses a model-based path to provide additional information to a traditional [model-free](model-free.md) RL agent. In the model-based path, the agent can "imagine" trajectories by simulating the environment. An environment model provides simulations based on the agent's imagined actions. Multiple simulations can be aggregated to help the agent decide its eventual action. The agent can tolerate imperfections in the environment model's predictions because it can learn how to extract useful information from the simulation results. In [Weber & Racanière et al. (2017)](https://arxiv.org/abs/1707.06203), the model-free portion is an [A3C agent](model-free.md#asynchronous-advantage-actor-critic-agent). They demonstrate the performance of I2A agents in two challenging game environments: Sokoban and MiniPacman.

## References

* 2017 July 19, Théophane Weber, Sébastien Racanière, David P. Reichert, Lars Buesing, Arthur Guez, Danilo Jimenez Rezende, Adria Puigdomènech Badia, Oriol Vinyals, Nicolas Heess, Yujia Li, Razvan Pascanu, Peter Battaglia, David Silver, and Daan Wierstra. [Imagination-Augmented Agents for Deep Reinforcement Learning](https://arxiv.org/abs/1707.06203). *arXiv:1707.06203*. [video](https://drive.google.com/open?id=0B4tKsKnCCZtQY2tTOThucHVxUTQ). [blog](https://deepmind.com/blog/agents-imagine-and-plan/).
* 2017 July 11, Serkan Cabi, Sergio Gómez Colmenarejo, Matthew W. Hoffman, Misha Denil, Ziyu Wang, and Nando de Freitas. [The Intentional Unintentional Agent: Learning to Solve Many Continuous Control Tasks Simultaneously](https://arxiv.org/abs/1707.03300). *arXiv:1707.03300*.


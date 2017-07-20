---
permalink: /rl/agents/
---
# Reinforcement Learning Agents

## Imagination-Augmented Agent

The Imagination-Augmented Agent (I2A) uses a model-based path to provide additional information to a traditional [model-free](http://realai.org/rl/model-free/) RL agent. In the model-based path, the agent can "imagine" trajectories by simulating the environment. An environment model provides simulations based on the agent's imagined actions. Multiple simulations can be aggregated to help the agent decide its eventual action. The agent can tolerate imperfections in the environment model's predictions because it can learn how to extract useful information from the simulation results. In [Weber & Racanière et al. (2017)](https://arxiv.org/abs/1707.06203), the model-free portion is an [A3C agent](http://realai.org/rl/model-free/#asynchronous-advantage-actor-critic-agent). They demonstrate the performance of I2A agents in two challenging game environments: Sokoban and MiniPacman.

## References

* 2017 July 19, Théophane Weber, Sébastien Racanière, David P. Reichert, Lars Buesing, Arthur Guez, Danilo Jimenez Rezende, Adria Puigdomènech Badia, Oriol Vinyals, Nicolas Heess, Yujia Li, Razvan Pascanu, Peter Battaglia, David Silver, and Daan Wierstra. [Imagination-Augmented Agents for Deep Reinforcement Learning](https://arxiv.org/abs/1707.06203). *arXiv:1707.06203*.


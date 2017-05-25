---
permalink: /planning/
---
# Planning

[Hamrick et al. (2017)](https://arxiv.org/abs/1705.02670) introduced a metacontroller agent that included one or more experts as models of the environment. The agent minimized a combined loss of performance and resource by learning to query selected agents in a number of steps depending on the difficulty of the task. This framework was demonstrated in a one-shot task of firing the thruster of a spaceship to reach a target location in a simulated space of multiple planets whose gravitational force affected the spaceship.

## Tree Search

In *Expert Iteration* ([Anthony et al., 2017](https://arxiv.org/abs/1705.08439)), tree search is used to improve a policy network, and the actions obtained from this improvement are used to train a new iteration of the policy network.

## References

* 2017 May 23, Thomas Anthony, Zheng Tian, and David Barber. [Thinking Fast and Slow with Deep Learning and Tree Search](https://arxiv.org/abs/1705.08439). *arXiv:1705.08439*.
* 2017 May 7, Jessica B. Hamrick, Andrew J. Ballard, Razvan Pascanu, Oriol Vinyals, Nicolas Heess, and Peter W. Battaglia. [Metacontrol for Adaptive Imagination-Based Optimization](https://arxiv.org/abs/1705.02670). *arXiv:1705.02670*.

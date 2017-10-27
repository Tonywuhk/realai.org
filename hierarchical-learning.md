---
permalink: /hierarchical-learning/
---
# Hierarchical Learning

The learning of some complex tasks can be a lot more efficient if these tasks are decomposed into subtasks that are easier to learn.

## Hierarchical Deep Reinforcement Learning

[Van Seijen et al. (2016)](https://arxiv.org/abs/1612.05159) generalized the traditional setting by training [multiple agents](DRL/multi-agent-learning.md) in a hierarchical way.

[Frans et al. (2017)](https://arxiv.org/abs/1710.09767) describe MLSH (metalearning shared hierarchies) where learning is broken into two components: a warmup period to optimize only a master policy, then a joint update period where both the master policy and sub-policies are learned. Master policy chooses the appropriate sub-policy at a slower timescale than that of the sub-policies themselves.

## References

* 2017 October 26, Kevin Frans, Jonathan Ho, Xi Chen, Pieter Abbeel, and John Schulman. [Meta Learning Shared Hierarchies](https://arxiv.org/abs/1710.09767). *arXiv:1710.09767*. [code](https://github.com/openai/mlsh). [blog](https://blog.openai.com/learning-a-hierarchy/). [news](https://www.wired.com/story/meet-the-high-schooler-shaking-up-artificial-intelligence/).
* 2017 March 3, Alexander Sasha Vezhnevets, Simon Osindero, Tom Schaul, Nicolas Heess, Max Jaderberg, David Silver, and Koray Kavukcuoglu. [FeUdal Networks for Hierarchical Reinforcement Learning](https://arxiv.org/abs/1703.01161). *arXiv:1703.01161*.
* 2016 December 15, Harm van Seijen, Mehdi Fatemi, Joshua Romoff, and Romain Laroche. [Separation of Concerns in Reinforcement Learning](https://arxiv.org/abs/1612.05159). *arXiv:1612.05159*.
* 2016 November 6, Carlos Florensa, Yan Duan, and Pieter Abbeel. [Stochastic Neural Networks for Hierarchical Reinforcement Learning](https://openreview.net/forum?id=B1oK8aoxe). *OpenReview*.
* 2016 October 17, Nicolas Heess, Greg Wayne, Yuval Tassa, Timothy Lillicrap, Martin Riedmiller, and David Silver. [Learning and Transfer of Modulated Locomotor Controllers](https://arxiv.org/abs/1610.05182). *arXiv:1610.05182*.
* 2016 April 20, Tejas D. Kulkarni, Karthik R. Narasimhan, Ardavan Saeedi, and Joshua B. Tenenbaum. [Hierarchical Deep Reinforcement Learning: Integrating Temporal Abstraction and Intrinsic Motivation](https://arxiv.org/abs/1604.06057). *arXiv:1604.06057*.

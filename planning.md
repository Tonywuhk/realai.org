---
permalink: /planning/
---
# Planning

## Learning to Plan

The Imagination-based Planner (IBP) is a model-based agent that learns to plan. Its architecture contains the manager, the controller, the imagination and the memory. The manager maps a history of internal and external data to either a real action in the environment, or a decision to imagine the consequence of a proposed action from a particular imagined state. The other three modules work together to generate the imagination and update the history. In [Pascanu & Li et al. (2017)](https://arxiv.org/abs/1707.06170), the IBP agents learn to build "imagination trees" that allow them to flexibly navigate previously imagined states.

The IBP is inspired by [Hamrick et al. (2017)](https://arxiv.org/abs/1705.02670), who introduce a metacontroller agent that include one or more experts as models of the environment. The agent minimizes a combined loss of performance and resource by learning to query selected agents in a number of steps depending on the difficulty of the task. This framework is demonstrated in a one-shot task of firing the thruster of a spaceship to reach a target location in a simulated space of multiple planets whose gravitational force affected the spaceship.

[Groshev et al. (2017)](https://arxiv.org/abs/1708.07280) learn a reactive policy that imitates execution traces produced by a planner.

## Planning with a Forward Model

The agent learns a forward model of the environment, which can then be used by the agent to solve for the optimal actions towards its goal. Consider a forward model that is differentiable with respect to actions. When the action space is continuous, it is straightforward to solve for the optimal actions using gradient methods. When the action space is discrete, [Henaff et al. (2017)](https://arxiv.org/abs/1705.07177) introduce a simple method in which the action space is expanded to a probability distribution over the discrete actions. The distribution is obtained from a softmax of free variables. Gradient methods are then used to solve for the free variables with the additional step of adding random noise to those variables during optimization.

## Tree Search

In *Expert Iteration* ([Anthony et al., 2017](https://arxiv.org/abs/1705.08439)), tree search is used to improve a policy network, and the actions obtained from this improvement are used to train a new iteration of the policy network.

## References

* 2017 August 24, Edward Groshev, Aviv Tamar, Siddharth Srivastava, and Pieter Abbeel. [Learning Generalized Reactive Policies using Deep Neural Networks](https://arxiv.org/abs/1708.07280). *arXiv:1708.07280*. [video](https://sites.google.com/site/learn2plannips/).
* 2017 July 19, Razvan Pascanu, Yujia Li, Oriol Vinyals, Nicolas Heess, Lars Buesing, Sebastien Racanière, David Reichert, Théophane Weber, Daan Wierstra, and Peter Battaglia. [Learning model-based planning from scratch](https://arxiv.org/abs/1707.06170). *arXiv:1707.06170*. [video](https://drive.google.com/open?id=0B3u8dCFTG5iVaUxzbzRmNldGcU0). [blog](https://deepmind.com/blog/agents-imagine-and-plan/).
* 2017 May 23, Thomas Anthony, Zheng Tian, and David Barber. [Thinking Fast and Slow with Deep Learning and Tree Search](https://arxiv.org/abs/1705.08439). *arXiv:1705.08439*.
* 2017 May 19, Mikael Henaff, William F. Whitney, and Yann LeCun. [Model-Based Planning in Discrete Action Spaces](https://arxiv.org/abs/1705.07177). *arXiv:1705.07177*.
* 2017 May 7, Jessica B. Hamrick, Andrew J. Ballard, Razvan Pascanu, Oriol Vinyals, Nicolas Heess, and Peter W. Battaglia. [Metacontrol for Adaptive Imagination-Based Optimization](https://arxiv.org/abs/1705.02670). *arXiv:1705.02670*.

---
permalink: /RL/
---
# Reinforcement Learning

In reinforcement learning (RL; [Sutton & Barto, 2017](http://incompleteideas.net/sutton/book/the-book-2nd.html)), agents learn to maximize numerical rewards provided by an environment that is influenced by the agents' actions. Sophisticated [platforms](http://realai.org/reinforcement-learning-platforms/) have been built to simulate this process. The agents can learn to explicitly build models of their environment, which they then use for [planning](http://realai.org/planning/). This type of learning is referred to as model-based, as opposed to the simpler [model-free algorithms](http://realai.org/RL/model-free/) where agents learn actions directly. When reward signals are sparse, learning is often helped by giving the agents [auxiliary tasks](http://realai.org/auxiliary-tasks/) that are believed to be helpful for the completion of their original task. Some auxiliary tasks depend so little on the specifics of the original task that they effectively become the agents' [intrinsic motivations](http://realai.org/intrinsic-motivation/). When it is not clear what the rewards should be, it is possible for the agents to infer the reward function from demonstrations, using an [imitation learning](http://realai.org/imitation-learning/) method called inverse reinforcement learning.

## Deep Reinforcement Learning

Deep reinforcement learning is a subfield that uses deep learning algorithms within RL. It is a main driving force behind rapid [progress](http://realai.org/progress/) in AI since 2013, and represents an important step towards developing AGI.

### Recent Review

* 2017 August 19, Kai Arulkumaran, Marc Peter Deisenroth, Miles Brundage, and Anil Anthony Bharath. [A Brief Survey of Deep Reinforcement Learning](https://arxiv.org/abs/1708.05866). *arXiv:1708.05866*.
* 2017 July 15, Yuxi Li. [Deep Reinforcement Learning: An Overview](https://arxiv.org/abs/1701.07274). *arXiv:1701.07274*.

## References

* 2016 September, Richard S. Sutton and Andrew G. Barto. [Reinforcement Learning: An Introduction](http://incompleteideas.net/sutton/book/the-book-2nd.html), Second Edition, in progress. *The MIT Press*. [PDF](http://incompleteideas.net/sutton/book/bookdraft2016sep.pdf).


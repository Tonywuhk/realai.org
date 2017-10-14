---
permalink: /course/reinforcement-learning/
redirect_from:
  - /RL/
  - /course/RL/
  - /course/DRL/
---
# Reinforcement Learning

In reinforcement learning (RL), agents learn to maximize numerical rewards provided by an [environment](../../environments.md) that is influenced by the agents' actions. The agents can learn to explicitly build models of their environment, which they then use for [planning](../../planning.md). This type of learning is referred to as model-based, as opposed to the simpler model-free [algorithms](../../DRL/learning-algorithms.md) where agents learn actions directly. When reward signals are sparse, learning is often helped by giving the agents [auxiliary tasks](../../auxiliary-tasks.md) that are believed to be helpful for the completion of their original task. Some auxiliary tasks depend so little on the specifics of the original task that they effectively become the agents' [intrinsic motivations](../../intrinsic-motivation.md). When it is not clear what the rewards should be, it is possible for the agents to infer the reward function from demonstrations, using an [imitation learning](../../imitation-learning.md) method called inverse reinforcement learning.

## Contents

* [Markov Decision Process](http://realai.org/course/reinforcement-learning/markov-decision-process/)

## Implementations

### OpenAI Baselines

[OpenAI Baselines](https://github.com/openai/baselines) is an open-source collection of [OpenAI](http://realai.org/research-groups/openai/)'s reinforcement learning implementations. According to their [blog](https://blog.openai.com/openai-baselines-dqn/), it is OpenAI's internal effort to reproduce published results. As of 25 May 2017, these implementations include [DQN](http://www.nature.com/nature/journal/v518/n7540/full/nature14236.html), [Double Q Learning](https://arxiv.org/abs/1509.06461), [Prioritized Replay](https://arxiv.org/abs/1511.05952), [Dueling DQN](https://arxiv.org/abs/1511.06581), [ACKTR and A2C](https://blog.openai.com/baselines-acktr-a2c/), using Python 3 and [TensorFlow](https://www.tensorflow.org/).

* [DQN Agent on CartPole](DQN-agent-on-CartPole.md)

### Other Sources

* [pytorch-a2c-ppo-acktr](https://github.com/ikostrikov/pytorch-a2c-ppo-acktr) is a PyTorch implementation of Advantage Actor Critic (A2C), Proximal Policy Optimization (PPO) and Scalable trust-region method for deep reinforcement learning using Kronecker-factored approximation (ACKTR). It is being actively maintained as of October 13, 2017.

## Further Reading

* [Reinforcement Learning Methods and Tutorials](https://github.com/MorvanZhou/Reinforcement-learning-with-tensorflow) cover topics from the basic RL algorithms to advanced algorithms developed recent years.
* 2017 August 26-27, Pieter Abbeel, Rocky Duan, Peter Chen, and Andrej Karpathy. [Deep Reinforcement Learning Bootcamp](https://www.deepbootcamp.io/). *Berkeley, CA*. [Lectures](https://sites.google.com/view/deep-rl-bootcamp/lectures).
* 2017 Fall, *University of California, Berkeley*. [CS 294: Deep Reinforcement Learning](http://rll.berkeley.edu/deeprlcourse/). Sergey Levine, Abhishek Gupta, Joshua Achiam. [/r/berkeleydeeprlcourse](https://www.reddit.com/r/berkeleydeeprlcourse/).
* 2017 June 19, Richard S. Sutton and Andrew G. Barto. [Reinforcement Learning: An Introduction](http://incompleteideas.net/sutton/book/the-book-2nd.html), Second Edition, in progress. *MIT Press*. [PDF](http://incompleteideas.net/sutton/book/bookdraft2017june19.pdf).
* 2017 Spring, *Carnegie Mellon University*. [CMU 10703: Deep Reinforcement Learning and Control](https://katefvision.github.io/). Katerina Fragkiadaki and Ruslan Satakhutdinov.
* 2017 Spring, *Stanford University*. [CS234: Reinforcement Learning](http://web.stanford.edu/class/cs234/index.html). Emma Brunskill.
* 2017 Winter, *Stanford University*. [MS&E 338: Reinforcement Learning](https://web.stanford.edu/class/msande338/). Benjamin Van Roy.
* 2016 June 17, *DeepMind Technologies*. [Blog: Deep Reinforcement Learning](https://deepmind.com/blog/deep-reinforcement-learning/). David Silver.


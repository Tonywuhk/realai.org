---
title: Welcome to Real AI
permalink: /
mathjax: true
---

## What's New

* 2017 April 18, Jürgen Schmidhuber says artificial intelligence will surpass humans’ in 2050. Source: [Jürgen Schmidhuber on the robot future: ‘They will pay as much attention to us as we do to ants'](https://www.theguardian.com/technology/2017/apr/18/robot-man-artificial-intelligence-computer-milky-way). *The Guardian*. ([Timing](http://realai.org/timing/))
* 2017 April 15, Audrunas Gruslys, Mohammad Gheshlaghi Azar, Marc G. Bellemare, and Remi Munos. [The Reactor: A Sample-Efficient Actor-Critic Architecture](https://arxiv.org/abs/1704.04651). *arXiv:1704.04651*. ([DeepMind](http://realai.org/labs/deepmind/publications/); [RL Algorithms](http://realai.org/model-free-rl-algorithms/))
* 2017 April 12, Todd Hester, Matej Vecerik, Olivier Pietquin, Marc Lanctot, Tom Schaul, Bilal Piot, Andrew Sendonaris, Gabriel Dulac-Arnold, Ian Osband, John Agapiou, Joel Z. Leibo, and Audrunas Gruslys. [Learning from Demonstrations for Real World Reinforcement Learning](https://arxiv.org/abs/1704.03732). *arXiv:1704.03732*. ([DeepMind](http://realai.org/labs/deepmind/publications/); [RL Algorithms](http://realai.org/model-free-rl-algorithms/))
* 2017 April 10, Ivaylo Popov, Nicolas Heess, Timothy Lillicrap, Roland Hafner, Gabriel Barth-Maron, Matej Vecerik, Thomas Lampe, Yuval Tassa, Tom Erez, and Martin Riedmiller. [Data-efficient Deep Reinforcement Learning for Dexterous Manipulation](https://arxiv.org/abs/1704.03073). *arXiv:1704.03073*. ([DeepMind](http://realai.org/labs/deepmind/publications/); [RL Algorithms](http://realai.org/model-free-rl-algorithms/))
* 2017 April 10, Carlos Florensa, Yan Duan, and Pieter Abbeel. [Stochastic Neural Networks for Hierarchical Reinforcement Learning](https://arxiv.org/abs/1704.03012). *arXiv:1704.03012*. ([OpenAI](http://realai.org/labs/openai/publications/); [Intrinsic Motivation](http://realai.org/intrinsic-motivation))
* 2017 April 10. [Sir Tim Berners-Lee lays out nightmare scenario where AI runs the financial world](http://www.techworld.com/social-media/sir-tim-berners-lee-lays-out-nightmare-scenario-where-ai-runs-world-economy-3657280/). *TechWorld*. ([Safety](http://realai.org/safety/); [News](http://realai.org/news/))
* 2017 April 10, Meire Fortunato, Charles Blundell, and Oriol Vinyals. [Bayesian Recurrent Neural Networks](https://arxiv.org/abs/1704.02798). *arXiv:1704.02798*. ([DeepMind](http://realai.org/labs/deepmind/publications/); [Learning Rules](http://realai.org/learning-rules/))
* 2017 April 10. [The Future of Go Summit will be held in Wuzhen, China, May 23-27, 2017, and feature AlphaGo](https://deepmind.com/blog/exploring-mysteries-alphago/). *DeepMind*. ([Conferences](http://realai.org/resources/conferences/); [News](http://realai.org/news/))

## AI and Society

Rapid [progress](http://realai.org/progress/) in artificial intelligence (AI) has raised the prospect that machines will [one day](http://realai.org/timing/) surpass humans in intelligence. Countries around the world have [policies](http://realai.org/policies/) in place to support AI research and development, [research groups](http://realai.org/labs/) are given a lot of resources, and many experts have already published [roadmaps](http://realai.org/roadmaps/) towards building artificial general intelligence (AGI).

AGI technology could represent the greatest change in the history of life on Earth. We can take steps to ensure that it is [safe and beneficial](http://realai.org/safety/).

The best place to appreciate AI’s progress is at its research frontiers. Unlike mature fields where many years of postgraduate training is needed, the [background](http://realai.org/resources/curriculum/) for cutting-edge AI is accessible to college students, whose papers often appear in top academic [conferences](http://realai.org/resources/conferences/).

## Research

The most crucial ability of an intelligent system is the ability of learning. To achieve AGI, it is widely believed that several objectives need to be accomplished:

* Unsupervised Learning: supervision should not be necessary as the system learns autonomously, often driven by [intrinsic motivations](http://realai.org/intrinsic-motivation) such as [prediction](http://realai.org/predictive-learning/).
* [Multi-Task Learning](http://realai.org/multi-task-learning/): the system can learn multiple tasks, continuously or perhaps throughout its life of operation, and transfer knowledge learned from some tasks to others.
* [Hierarchical Learning](http://realai.org/hierarchical-learning/): the system can understand data in a hierarchical way, including learning useful abstract concepts.
* [Meta-Learning](http://realai.org/meta-learning/): the system can improve its own learning architecture by learning how to learn.

As a result, the system should have the ability of reasoning, attention, and memory, build an internal world model, and understand language in a way that is [grounded](http://realai.org/symbol-grounding/) in this model.

Since 2012, deep learning has achieved phenomenal success or shown great potential in many areas, e.g., [vision](http://realai.org/computer-vision/), language, autonomous driving, [program induction](http://realai.org/program-induction/), and [automated theorem proving](http://realai.org/automated-theorem-proving/). Although we still lack a deep [theoretical understanding](http://realai.org/deep-learning-theory/) of how this is accomplished, many systems have already been [implemented](http://realai.org/deep-learning-implementation/) in large-scale.

Presently, we focus on deep learning, an area in machine learning inspired by [neuroscience](http://realai.org/neuroscience/). Our focus will shift to [other areas](http://realai.org/frontiers/) if they show more promise towards AGI.

### Deep Learning

An architecture in deep learning ([Goodfellow et al., 2016](https://mitpress.mit.edu/books/deep-learning); [LeCun et al., 2015](http://www.nature.com/nature/journal/v521/n7553/full/nature14539.html); [Schmidhuber 2014](https://arxiv.org/abs/1404.7828)) is a large and complex [network architecture](http://realai.org/network-architecture/) whose dynamics follow [learning rules](http://realai.org/learning-rules). In the architecture, there can be one or more neural networks, an agent, or [multiple agents](http://realai.org/multi-agent-learning/). Their learning can be cooperative or [adversarial](http://realai.org/adversarial-learning/). The neural networks are usually deep and hierarchical, sometimes [augmented with memory](http://realai.org/memory-augmented-neural-networks/), and can be automatically designed using [architecture search](http://realai.org/architecture-search/).

Deep learning has seen many applications in reinforcement learning, contributing to breakthroughs in [games](http://realai.org/games/) such as Atari, Go, and Poker. Their intersection, deep reinforcement learning, is a rapidly growing area of research today.

### Reinforcement Learning

In reinforcement learning ([Sutton & Barto, 2017](http://incompleteideas.net/sutton/book/the-book-2nd.html)), agents learn to maximize numerical rewards provided by an environment that is influenced by the agents' actions. Sophisticated [platforms](http://realai.org/reinforcement-learning-platforms/) have been built to simulate this process. The agents can learn to explicitly build models of their environment, which they then use for planning. This type of learning is referred to as model-based, as opposed to the simpler [model-free algorithms](http://realai.org/model-free-rl-algorithms) where agents learn actions directly. When reward signals are sparse, learning is often helped by giving the agents [auxiliary tasks](http://realai.org/auxiliary-tasks/) that are believed to be helpful for the completion of their original task. Some auxiliary tasks depend so little on the specifics of the original task that they effectively become the agents' [intrinsic motivations](http://realai.org/intrinsic-motivation). When it is not clear what the rewards should be, it is possible for the agents to infer the reward function from demonstrations, using an [imitation learning](http://realai.org/imitation-learning/) method called inverse reinforcement learning.

## References

* 2016 November,  Ian Goodfellow, Yoshua Bengio, and Aaron Courville. [Deep Learning](https://mitpress.mit.edu/books/deep-learning). *The MIT Press*. [site](http://www.deeplearningbook.org/).
* 2016 September, Richard S. Sutton and Andrew G. Barto. [Reinforcement Learning: An Introduction](http://incompleteideas.net/sutton/book/the-book-2nd.html), Second Edition, in progress. *The MIT Press*. [PDF](http://incompleteideas.net/sutton/book/bookdraft2016sep.pdf).
* 2015 February 25, Yann LeCun,	Yoshua Bengio, and Geoffrey Hinton. [Deep Learning](http://www.nature.com/nature/journal/v521/n7553/full/nature14539.html). *Nature*, 521(7553):436-444. [PDF](https://www.cs.toronto.edu/~hinton/absps/NatureDeepReview.pdf).
* 2014 April 30, Jürgen Schmidhuber. [Deep Learning in Neural Networks: An Overview](https://arxiv.org/abs/1404.7828). *arXiv:1404.7828*.

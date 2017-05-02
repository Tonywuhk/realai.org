---
permalink: /architecture-search/
---
# Architecture Search

Manually designing deep neural networks requires a lot of expert knowledge, and is very time-consuming. Many techniques have been proposed to automate this process. [Negrinho & Gordon (2017)](https://arxiv.org/abs/1704.08792) used an extensible and modular language to describe expressive spaces of model parameters, which then can be searched using Monte Carlo tree search and sequential model-based optimization.

## Evolutionary Algorithms

* 2017 March 3, Esteban Real, Sherry Moore, Andrew Selle, Saurabh Saxena, Yutaka Leon Suematsu, Quoc Le, and Alex Kurakin. [Large-Scale Evolution of Image Classifiers](https://arxiv.org/abs/1703.01041). *arXiv:1703.01041*.
* 2017 March 1, Risto Miikkulainen, Jason Liang, Elliot Meyerson, Aditya Rawal, Dan Fink, Olivier Francon, Bala Raju, Arshak Navruzyan, Nigel Duffy, and Babak Hodjat. [Evolving Deep Neural Networks](https://arxiv.org/abs/1703.00548). *arXiv:1703.00548*.
* 2016 June 8, Chrisantha Fernando, Dylan Banarse, Malcolm Reynolds, Frederic Besse, David Pfau, Max Jaderberg, Marc Lanctot, and Daan Wierstra. [Convolution by Evolution: Differentiable Pattern Producing Networks](https://arxiv.org/abs/1606.02580). *arXiv:1606.02580*.

## Reinforcement Learning

[Zoph and Le (2016)](https://arxiv.org/abs/1611.01578) used reinforcment learning to train a recurrent network that generates descriptions of neural networks to minimize validation error, then found convolutional and LTSM architectures that performed competitively in CIFAR-10 and Penn Treebank datasets, respectively.

## References

* 2017 April 28, Renato Negrinho and Geoff Gordon. [DeepArchitect: Automatically Designing and Training Deep Architectures](https://arxiv.org/abs/1704.08792). *arXiv:1704.08792*.
* 2016 November 7, Bowen Baker, Otkrist Gupta, Nikhil Naik, and Ramesh Raskar. [Designing Neural Network Architectures using Reinforcement Learning](https://arxiv.org/abs/1611.02167). *arXiv:1611.02167*.
* 2016 November 5, Barret Zoph and Quoc V. Le. [Neural Architecture Search with Reinforcement Learning](https://arxiv.org/abs/1611.01578). *arXiv:1611.01578*.

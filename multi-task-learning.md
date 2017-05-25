---
permalink: /multi-task-learning/
---
# Multi-Task Learning

A standard deep neural network can learn very different visual domains simultaneously ([Bilen & Vedaldi, 2017](https://arxiv.org/abs/1701.07275)). It's also possible to train a reinforcement learning agent to perform multiple tasks.

## Continual Learning

Continual learning focuses on an agent's ability to learn new tasks without forgeting old ones. Skills learned from old tasks may or may not transfer to new tasks, but must be largely retained. One approach is to penalize learning for weights that are important for remembering old tasks. Importance measures of weights can be computed online ([Zenke & Poole & Ganguli, 2017](https://arxiv.org/abs/1703.04200)). The elastic weight consolidation (EWC) ([Kirkpatrick et al, 2016](https://arxiv.org/abs/1612.00796)) method relies on computing the Fisher information metric at the end of each task. [Seff et al. (2017)](https://arxiv.org/abs/1705.08395) explain that both of these methods can be adapted to training conditional GANs.

Another approach to prevent catastrophic forgetting is to design novel network architectures. PathNets ([Fernando et al., 2017](https://arxiv.org/abs/1701.08734)) evolve the learning of a particular task towards a subset of parameters, then fix these parameters before moving on to the next task.

A more intuitive method is to add new components for adaption to new tasks. The progressive network ([Rusu & Rabinowitz et al., 2016](https://arxiv.org/abs/1606.04671)) instantiates a new column for each new task being solved. [Rosenfeld & Tsotsos (2017)](https://arxiv.org/abs/1705.04228) adds a controller to each convolutional layer in a trained neural network that mixes the filters in that layer to adapt to a new task. A new set of controllers is required for each new task.

We also plan to review studies that focus on augmenting the input and output layers of a neural network to adapt to new tasks without forgeting the old ones.

## Transfer Learning

Policy distillation ([Rusu et al., 2015](https://arxiv.org/abs/1511.06295)) is a technique to transfer one or more action policies from Q-networks to an untrained network. It can be used to consolidate multiple task-specific policies into a single policy. A similar way to accomplish this is Actor-Mimic ([Parisotto et al, 2015](https://arxiv.org/abs/1511.06342)).

[Ruder (2017)](http://sebastianruder.com/transfer-learning/) discussed transfer learning in a blog post and highlighted this area as "machine learning's next frontier".

## Curriculum Learning

[Graves et a. (2017)](https://arxiv.org/abs/1704.03003) consider loss-driven and complexity-driven signals to reward learning progress, then use a nonstationary multi-armed bandit algorithm to automatically generate learning curriculum.

### Adversarial 

## References

* 2017 May 23, Ari Seff, Alex Beatson, Daniel Suo, and Han Liu. [Continual Learning in Generative Adversarial Nets](https://arxiv.org/abs/1705.08395). *arXiv:1705.08395*.
* 2017 May 11, Amir Rosenfeld and John K. Tsotsos. [Incremental Learning Through Deep Adaptation](https://arxiv.org/abs/1705.04228). *arXiv:1705.04228*.
* 2017 April 10, Alex Graves, Marc G. Bellemare, Jacob Menick, Remi Munos, and Koray Kavukcuoglu. [Automated Curriculum Learning for Neural Networks](https://arxiv.org/abs/1704.03003). *arXiv:1704.03003*.
* 2017 March 21, Sebastian Ruder. [Transfer Learning - Machine Learning's Next Frontier](http://sebastianruder.com/transfer-learning/). *[Personal Blog](http://sebastianruder.com/#open)*.
* 2017 March 13, Friedemann Zenke, Ben Poole, and Surya Ganguli. [Improved multitask learning through synaptic intelligence](https://arxiv.org/abs/1703.04200). *arXiv:1703.04200*.
* 2017 January 30, Chrisantha Fernando, Dylan Banarse, Charles Blundell, Yori Zwols, David Ha, Andrei A. Rusu, Alexander Pritzel, and Daan Wierstra. [PathNet: Evolution Channels Gradient Descent in Super Neural Networks](https://arxiv.org/abs/1701.08734). *arXiv:1701.08734*.
* 2017 January 25, Hakan Bilen and Andrea Vedaldi. [Universal representations:The missing link between faces, text, planktons, and cat breeds](https://arxiv.org/abs/1701.07275). *arXiv:1701.07275*.
* 2016 December 2, James Kirkpatrick, Razvan Pascanu, Neil Rabinowitz, Joel Veness, Guillaume Desjardins, Andrei A. Rusu, Kieran Milan, John Quan, Tiago Ramalho, Agnieszka Grabska-Barwinska, Demis Hassabis, Claudia Clopath, Dharshan Kumaran, and Raia Hadsell. [Overcoming catastrophic forgetting in neural networks](https://arxiv.org/abs/1612.00796). *arXiv:1612.00796*.
* 2016 November 6, Jacob Andreas, Dan Klein, and Sergey Levine. [Modular Multitask Reinforcement Learning with Policy Sketches](https://arxiv.org/abs/1611.01796). *arXiv:1611.01796*.
* 2016 September 22, Coline Devin, Abhishek Gupta, Trevor Darrell, Pieter Abbeel, and Sergey Levine. [Learning Modular Neural Network Policies for Multi-Task and Multi-Robot Transfer](https://arxiv.org/abs/1609.07088). *arXiv:1609.07088*.
* 2016 June 15, Andrei A. Rusu, Neil C. Rabinowitz, Guillaume Desjardins, Hubert Soyer, James Kirkpatrick, Koray Kavukcuoglu, Razvan Pascanu, and Raia Hadsell. [Progressive Neural Networks](https://arxiv.org/abs/1606.04671). *arXiv:1606.04671*.
* 2015 November 19, Emilio Parisotto, Jimmy Lei Ba, and Ruslan Salakhutdinov. [Actor-Mimic: Deep Multitask and Transfer Reinforcement Learning](https://arxiv.org/abs/1511.06342). *arXiv:1511.06342*.
* 2015 November 19, Andrei A. Rusu, Sergio Gomez Colmenarejo, Caglar Gulcehre, Guillaume Desjardins, James Kirkpatrick, Razvan Pascanu, Volodymyr Mnih, Koray Kavukcuoglu, and Raia Hadsell. [Policy Distillation](https://arxiv.org/abs/1511.06295). *arXiv:1511.06295*.

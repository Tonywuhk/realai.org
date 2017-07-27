---
permalink: /transfer-learning/
---
# Transfer Learning

[Transfer learning](https://en.wikipedia.org/wiki/Transfer_learning) is a goal of machine learning to more efficiently solve new tasks by leveraging experiences learned from old tasks.

## Related Topics

* [Continual Learning](http://realai.org/continual-learning/)
* [Few-Shot Learning](http://realai.org/few-shot-learning/)
* [Multi-Task Learning](http://realai.org/multi-task-learning/)

## Recent Review

* 2017 March 21, Sebastian Ruder. [Transfer Learning - Machine Learning's Next Frontier](http://ruder.io/transfer-learning/). *[Personal Blog](http://ruder.io/)*.

## Notes

Policy distillation ([Rusu et al., 2015](https://arxiv.org/abs/1511.06295)) is a technique to transfer one or more action policies from Q-networks to an untrained network. It can be used to consolidate multiple task-specific policies into a single policy. A similar way to accomplish this is Actor-Mimic ([Parisotto et al., 2015](https://arxiv.org/abs/1511.06342)).

Another mechanism for knowledge transfer is to build new networks from existing ones ([Chen et al., 2016](https://arxiv.org/abs/1511.05641); [Wei et al., 2016](https://arxiv.org/abs/1603.01670); [Wei et al., 2017](https://arxiv.org/abs/1701.03281)).

A form of transfer learning is domain adaptation. In some reinforcement learning domain adaptation scenarios, an agent trained on a *source* domain needs to perform well on a *target* domain that is similar to the source in some aspects, such as reward structure and action space. [Higgins & Pal et al. (2017)](https://arxiv.org/abs/1707.08475) propose a multi-stage RL agent, DARLA (DisentAngled Representation Learning Agent), that learns in three stages: see, act, and transfer. Using an unsupervised model, DARLA first learns a disentangled representation ([Higgins et al., 2017](https://openreview.net/forum?id=Sy2fzU9gl)) of the observations in stage 1. In stage 2, the agent learns a policy to solve source tasks based on the representation learned earlier, fixed throughout learning during this stage. When tested on target tasks in stage 3, DARLA significantly outperforms [baselines](http://realai.org/rl/model-free/) DQN, A3C and Episodic Control.

## References

* 2017 July 26, Irina Higgins, Arka Pal, Andrei A. Rusu, Loic Matthey, Christopher P Burgess, Alexander Pritzel, Matthew Botvinick, Charles Blundell, and Alexander Lerchner. [DARLA: Improving Zero-Shot Transfer in Reinforcement Learning](https://arxiv.org/abs/1707.08475). *arXiv:1707.08475*. [video](https://youtu.be/sZqrWFl0wQ4).
* 2017 April 18, Irina Higgins, Loic Matthey, Arka Pal, Christopher Burgess, Xavier Glorot, Matthew Botvinick, Shakir Mohamed, and Alexander Lerchner. [beta-VAE: Learning Basic Visual Concepts with a Constrained Variational Framework](https://openreview.net/forum?id=Sy2fzU9gl). *OpenReview*.
* 2017 January 12, Tao Wei, Changhu Wang, and Chang Wen Chen. [Modularized Morphing of Neural Networks](https://arxiv.org/abs/1701.03281). *arXiv:1701.03281*.
* 2016 April 23, Tianqi Chen, Ian Goodfellow, and Jonathon Shlens. [Net2Net: Accelerating Learning via Knowledge Transfer](https://arxiv.org/abs/1511.05641). *arXiv:1511.05641*.
* 2016 March 8, Tao Wei, Changhu Wang, Yong Rui, and Chang Wen Chen. [Network Morphism](https://arxiv.org/abs/1603.01670). *arXiv:1603.01670*.
* 2015 November 19, Emilio Parisotto, Jimmy Lei Ba, and Ruslan Salakhutdinov. [Actor-Mimic: Deep Multitask and Transfer Reinforcement Learning](https://arxiv.org/abs/1511.06342). *arXiv:1511.06342*.
* 2015 November 19, Andrei A. Rusu, Sergio Gomez Colmenarejo, Caglar Gulcehre, Guillaume Desjardins, James Kirkpatrick, Razvan Pascanu, Volodymyr Mnih, Koray Kavukcuoglu, and Raia Hadsell. [Policy Distillation](https://arxiv.org/abs/1511.06295). *arXiv:1511.06295*.
 

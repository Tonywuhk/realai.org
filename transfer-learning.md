---
permalink: /transfer-learning/
---
# Transfer Learning

## Related Topics

* [Continual Learning](http://realai.org/continual-learning/)
* [Few-Shot Learning](http://realai.org/few-shot-learning/)
* [Multi-Task Learning](http://realai.org/multi-task-learning/)

## Recent Review

* 2017 March 21, Sebastian Ruder. [Transfer Learning - Machine Learning's Next Frontier](http://ruder.io/transfer-learning/). *[Personal Blog](http://ruder.io/)*.

## Overview

Policy distillation ([Rusu et al., 2015](https://arxiv.org/abs/1511.06295)) is a technique to transfer one or more action policies from Q-networks to an untrained network. It can be used to consolidate multiple task-specific policies into a single policy. A similar way to accomplish this is Actor-Mimic ([Parisotto et al., 2015](https://arxiv.org/abs/1511.06342)).

Another mechanism for knowledge transfer is to build new networks from existing ones ([Chen et al., 2016](https://arxiv.org/abs/1511.05641); [Wei et al., 2016](https://arxiv.org/abs/1603.01670); [Wei et al., 2017](https://arxiv.org/abs/1701.03281)).

[Ruder (2017)](http://sebastianruder.com/transfer-learning/) discussed transfer learning in a blog post and highlighted this area as "machine learning's next frontier".

## References

* 2017 January 12, Tao Wei, Changhu Wang, and Chang Wen Chen. [Modularized Morphing of Neural Networks](https://arxiv.org/abs/1701.03281). *arXiv:1701.03281*.
* 2016 April 23, Tianqi Chen, Ian Goodfellow, and Jonathon Shlens. [Net2Net: Accelerating Learning via Knowledge Transfer](https://arxiv.org/abs/1511.05641). *arXiv:1511.05641*.
* 2016 March 8, Tao Wei, Changhu Wang, Yong Rui, and Chang Wen Chen. [Network Morphism](https://arxiv.org/abs/1603.01670). *arXiv:1603.01670*.
* 2015 November 19, Emilio Parisotto, Jimmy Lei Ba, and Ruslan Salakhutdinov. [Actor-Mimic: Deep Multitask and Transfer Reinforcement Learning](https://arxiv.org/abs/1511.06342). *arXiv:1511.06342*.
* 2015 November 19, Andrei A. Rusu, Sergio Gomez Colmenarejo, Caglar Gulcehre, Guillaume Desjardins, James Kirkpatrick, Razvan Pascanu, Volodymyr Mnih, Koray Kavukcuoglu, and Raia Hadsell. [Policy Distillation](https://arxiv.org/abs/1511.06295). *arXiv:1511.06295*.
 

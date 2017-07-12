---
permalink: /multi-task-learning/
---
# Multi-Task Learning

[Kaiser et al. (2017)](https://arxiv.org/abs/1706.05137) design the *MultiModel* that is trained simultaneously and achieve decent performance across 8 tasks, including speech recognition, image recognition and captioning, English parsing, and translations between English, French and German. Their model architecture incorporates depthwise separable convolutions ([Kaiser et al., 2017](https://arxiv.org/abs/1706.03059)), multi-head dot-product attention mechanism ([Vaswani et al., 2017](https://arxiv.org/abs/1706.03762)), and sparsely-gated mixture-of-expert layers ([Shazeer et al., 2017](https://arxiv.org/abs/1701.06538)). According to a [Twitter picture](https://twitter.com/thefillm/status/845743048709464064) posted on 26 March 2017, Google's Jeff Dean talked about another single large model for multi-task learning. It is also sparsely activated, and resembles Pathnet ([Fernando et al., 2017](https://arxiv.org/abs/1701.08734)). Based on [a July 2017 slide on Facebook](https://www.facebook.com/photo.php?fbid=10208154385010936), from [seeingly the same](https://www.facebook.com/photo.php?fbid=10208154391411096) presentation, it should be [efficiently mapped](https://www.tensorflow.org/) to [specialized hardware](https://cloud.google.com/tpu/) for ML supercomputing.

[Rahmatizadeh et al. (2017)](https://arxiv.org/abs/1707.02920) propose an approach that enables inexpensive robots to learn multiple manipulation tasks from relatively few demonstrations. More data from the common patterns in different tasks helps to improve the sample efficiency in their method.

A standard deep neural network can learn very different visual domains simultaneously ([Bilen & Vedaldi, 2017](https://arxiv.org/abs/1701.07275)). It's also possible to train a reinforcement learning agent to perform multiple tasks. [Ruder (2017)](https://arxiv.org/abs/1706.05098) gives a general overview of multi-task learning, particularly in deep neural networks.

### References

* 2017 July 10, Rouhollah Rahmatizadeh, Pooya Abolghasemi, Ladislau Bölöni, and Sergey Levine. [Vision-Based Multi-Task Manipulation for Inexpensive Robots Using End-To-End Learning from Demonstration](https://arxiv.org/abs/1707.02920). *arXiv:1707.02920*.
* 2017 June 16, Lukasz Kaiser, Aidan N. Gomez, Noam Shazeer, Ashish Vaswani, Niki Parmar, Llion Jones, and Jakob Uszkoreit. [One Model To Learn Them All](https://arxiv.org/abs/1706.05137). *arXiv:1706.05137*.
* 2017 June 16, Lukasz Kaiser, Aidan N. Gomez, and Francois Chollet. [Depthwise Separable Convolutions for Neural Machine Translation](https://arxiv.org/abs/1706.03059). *arXiv:1706.03059*.
* 2017 June 15, Sebastian Ruder. [An Overview of Multi-Task Learning in Deep Neural Networks](https://arxiv.org/abs/1706.05098). *arXiv:1706.05098*.
* 2017 June 12, Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Lukasz Kaiser, and Illia Polosukhin. [Attention Is All You Need](https://arxiv.org/abs/1706.03762). *arXiv:1706.03762*.
* 2017 January 30, Chrisantha Fernando, Dylan Banarse, Charles Blundell, Yori Zwols, David Ha, Andrei A. Rusu, Alexander Pritzel, and Daan Wierstra. [PathNet: Evolution Channels Gradient Descent in Super Neural Networks](https://arxiv.org/abs/1701.08734). *arXiv:1701.08734*.
* 2017 January 25, Hakan Bilen and Andrea Vedaldi. [Universal representations:The missing link between faces, text, planktons, and cat breeds](https://arxiv.org/abs/1701.07275). *arXiv:1701.07275*.
* 2017 January 23, Noam Shazeer, Azalia Mirhoseini, Krzysztof Maziarz, Andy Davis, Quoc Le, Geoffrey Hinton, and Jeff Dean. [Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer](https://arxiv.org/abs/1701.06538). *arXiv:1701.06538*.

## Related Topics

* [Continual Learning](http://realai.org/continual-learning/)

## Transfer Learning

Policy distillation ([Rusu et al., 2015](https://arxiv.org/abs/1511.06295)) is a technique to transfer one or more action policies from Q-networks to an untrained network. It can be used to consolidate multiple task-specific policies into a single policy. A similar way to accomplish this is Actor-Mimic ([Parisotto et al, 2015](https://arxiv.org/abs/1511.06342)).

[Ruder (2017)](http://sebastianruder.com/transfer-learning/) discussed transfer learning in a blog post and highlighted this area as "machine learning's next frontier".

## Curriculum Learning

[Graves et al. (2017)](https://arxiv.org/abs/1704.03003) consider loss-driven and complexity-driven signals to reward learning progress, then use a nonstationary multi-armed bandit algorithm to automatically generate learning curriculum.

[Sukhbaatar et al. (2017)](https://arxiv.org/abs/1703.05407) used self-play where one agent builds a curriculum of increasingly more difficult tasks to challenge an identical agent.

## References

* 2017 April 19, Sainbayar Sukhbaatar, Ilya Kostrikov, Arthur Szlam, and Rob Fergus. [Intrinsic Motivation and Automatic Curricula via Asymmetric Self-Play](https://arxiv.org/abs/1703.05407). *arXiv:1703.05407*.
* 2017 April 10, Alex Graves, Marc G. Bellemare, Jacob Menick, Remi Munos, and Koray Kavukcuoglu. [Automated Curriculum Learning for Neural Networks](https://arxiv.org/abs/1704.03003). *arXiv:1704.03003*.
* 2017 March 21, Sebastian Ruder. [Transfer Learning - Machine Learning's Next Frontier](http://sebastianruder.com/transfer-learning/). *[Personal Blog](http://sebastianruder.com/#open)*.
* 2016 November 6, Jacob Andreas, Dan Klein, and Sergey Levine. [Modular Multitask Reinforcement Learning with Policy Sketches](https://arxiv.org/abs/1611.01796). *arXiv:1611.01796*.
* 2016 September 22, Coline Devin, Abhishek Gupta, Trevor Darrell, Pieter Abbeel, and Sergey Levine. [Learning Modular Neural Network Policies for Multi-Task and Multi-Robot Transfer](https://arxiv.org/abs/1609.07088). *arXiv:1609.07088*.
* 2015 November 19, Emilio Parisotto, Jimmy Lei Ba, and Ruslan Salakhutdinov. [Actor-Mimic: Deep Multitask and Transfer Reinforcement Learning](https://arxiv.org/abs/1511.06342). *arXiv:1511.06342*.
* 2015 November 19, Andrei A. Rusu, Sergio Gomez Colmenarejo, Caglar Gulcehre, Guillaume Desjardins, James Kirkpatrick, Razvan Pascanu, Volodymyr Mnih, Koray Kavukcuoglu, and Raia Hadsell. [Policy Distillation](https://arxiv.org/abs/1511.06295). *arXiv:1511.06295*.

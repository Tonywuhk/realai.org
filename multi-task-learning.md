---
permalink: /multi-task-learning/
redirect_from: /MTL/
---
# Multi-Task Learning

[Multi-task learning](https://en.wikipedia.org/wiki/Multi-task_learning) (MTL) is a goal of machine learning to *jointly* solve many tasks. [Caruana (1997)](https://link.springer.com/article/10.1023/A:1007379606734) characterises MTL as "training tasks in parallel while using a shared representation." On this page, our focus is the *parallel* aspect of deep learning.

## Related Topics

* [Continual Learning](http://realai.org/continual-learning/): Tasks are learned sequentially.
* [Curriculum Learning](http://realai.org/curriculum-learning/): Tasks are organized in groups.
* [Few-Shot Learning](http://realai.org/few-shot-learning/): The emphasis is on solving tasks using only a small number of samples.
* [Transfer Learning](http://realai.org/transfer-learning/): The emphasis is on transferring learned knowledge and skill from one task to another.

## Recent Reviews

* 2017 July 25, Yu Zhang and Qiang Yang. [A Survey on Multi-Task Learning](https://arxiv.org/abs/1707.08114). *arXiv:1707.08114*.
* 2017 June 15, [Sebastian Ruder](http://ruder.io/). [An Overview of Multi-Task Learning in Deep Neural Networks](https://arxiv.org/abs/1706.05098). *arXiv:1706.05098*. [blog](http://ruder.io/multi-task/).

## Notes

[Kaiser et al. (2017)](https://arxiv.org/abs/1706.05137) design the *MultiModel* that is trained simultaneously and achieve decent performance across 8 tasks, including speech recognition, image recognition and captioning, English parsing, and translations between English, French and German. Their model architecture incorporates depthwise separable convolutions ([Kaiser et al., 2017](https://arxiv.org/abs/1706.03059)), multi-head dot-product attention mechanism ([Vaswani et al., 2017](https://arxiv.org/abs/1706.03762)), and sparsely-gated mixture-of-expert layers ([Shazeer et al., 2017](https://arxiv.org/abs/1701.06538)). According to a [Twitter picture](https://twitter.com/thefillm/status/845743048709464064) posted on 26 March 2017, Google's Jeff Dean talked about another single large model for multi-task learning. It is also sparsely activated, and resembles Pathnet ([Fernando et al., 2017](https://arxiv.org/abs/1701.08734)). Based on [a July 2017 slide on Facebook](https://www.facebook.com/photo.php?fbid=10208154385010936), from [seeingly the same](https://www.facebook.com/photo.php?fbid=10208154391411096) presentation, it should be [efficiently mapped](https://www.tensorflow.org/) to [specialized hardware](https://cloud.google.com/tpu/) for ML supercomputing.

[Rahmatizadeh et al. (2017)](https://arxiv.org/abs/1707.02920) propose an approach that enables inexpensive robots to learn multiple manipulation tasks from relatively few demonstrations. More data from the common patterns in different tasks helps to improve the sample efficiency in their method.

A standard deep neural network can learn very different visual domains simultaneously ([Bilen & Vedaldi, 2017](https://arxiv.org/abs/1701.07275)). It's also possible to train a reinforcement learning agent to perform multiple tasks.

## References

* 2017 July 10, Rouhollah Rahmatizadeh, Pooya Abolghasemi, Ladislau Bölöni, and Sergey Levine. [Vision-Based Multi-Task Manipulation for Inexpensive Robots Using End-To-End Learning from Demonstration](https://arxiv.org/abs/1707.02920). *arXiv:1707.02920*.
* 2017 June 16, Lukasz Kaiser, Aidan N. Gomez, Noam Shazeer, Ashish Vaswani, Niki Parmar, Llion Jones, and Jakob Uszkoreit. [One Model To Learn Them All](https://arxiv.org/abs/1706.05137). *arXiv:1706.05137*.
* 2017 June 16, Lukasz Kaiser, Aidan N. Gomez, and Francois Chollet. [Depthwise Separable Convolutions for Neural Machine Translation](https://arxiv.org/abs/1706.03059). *arXiv:1706.03059*.
* 2017 June 12, Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Lukasz Kaiser, and Illia Polosukhin. [Attention Is All You Need](https://arxiv.org/abs/1706.03762). *arXiv:1706.03762*.
* 2017 January 30, Chrisantha Fernando, Dylan Banarse, Charles Blundell, Yori Zwols, David Ha, Andrei A. Rusu, Alexander Pritzel, and Daan Wierstra. [PathNet: Evolution Channels Gradient Descent in Super Neural Networks](https://arxiv.org/abs/1701.08734). *arXiv:1701.08734*.
* 2017 January 25, Hakan Bilen and Andrea Vedaldi. [Universal representations:The missing link between faces, text, planktons, and cat breeds](https://arxiv.org/abs/1701.07275). *arXiv:1701.07275*.
* 2017 January 23, Noam Shazeer, Azalia Mirhoseini, Krzysztof Maziarz, Andy Davis, Quoc Le, Geoffrey Hinton, and Jeff Dean. [Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer](https://arxiv.org/abs/1701.06538). *arXiv:1701.06538*.
* 1997 July, Rich Caruana. [Multitask Learning](https://link.springer.com/article/10.1023/A:1007379606734). *Machine Learning*, 28(1):41-75.


---
permalink: /few-shot-learning/
---
# Few-Shot Learning

Few-shot learning is about learning to solve tasks using only a small number of samples. In classification models, for example, the objective is to perform well after seeing very few samples from each class.

[Finn et al. (2017)](https://arxiv.org/abs/1703.03400) propose a model-agnostic meta-learning (MAML) algorithm to learn a good weight initialization so that subsequent learning converges rapidly. [Finn & Levine (2017)](https://arxiv.org/abs/1710.11622) find that MAML has sufficient capacity to approximate any learning algorithm. In their experiments, gradient-based MAML consistently leads to learning strategies that generalize more widely compared to RNN-based methods.

This technique is used in a *continuous adaptation* ([Al-Shedivat et al., 2017](https://arxiv.org/abs/1710.03641)) problem, where an agent learns to solve a single but nonstationary task or environment. The source of nonstationarity is some underlying properties of the task, which can also be viewed as a sequence of stationary tasks to which the agent must quickly adapt. This is important in their setup where the agent's experiences in the current task contain information about the next task. These experiences are used to construct the agent's policy for the next task.

Some few-shot learning methods:

* Weight initialization and an optimizer ([Ravi & Larochelle, 2016](https://openreview.net/forum?id=rJY0-Kcll)) that builds on weight update rules meta-learned by gradient descent ([Andrychowicz et al., 2016](https://arxiv.org/abs/1606.04474)),
* Learning an embedding of examples that facilitates classification by a linear model ([Snell et al., 2017](https://arxiv.org/abs/1703.05175)) or k-nearest neighbor ([Vinyals et al., 2016](https://arxiv.org/abs/1606.04080)), and
* Using external memory ([Santoro et al., 2016](https://arxiv.org/abs/1605.06065)) to rapidly bind information in the data.

For deep generative models, an autoencoder can be extended to learn statistics of datasets ([Edwards & Storkey, 2016](https://arxiv.org/abs/1606.02185)), rather than datapoints.

[Omniglot](https://github.com/brendenlake/omniglot) is a popular data set for evaluation.

In *continuous adaptation* ([Al-Shedivat et al., 2017](https://arxiv.org/abs/1710.03641)), an agent learns to solve a single but nonstationary task or environment, where the source of nonstationarity is some underlying properties of the task. This task can be seen as a sequence of stationary tasks for which the agent must quickly adapt to.

## References

* 2017 October 31, Chelsea Finn and Sergey Levine. [Meta-Learning and Universality: Deep Representations and Gradient Descent can Approximate any Learning Algorithm](https://arxiv.org/abs/1710.11622). *arXiv:1710.11622*.
* 2017 October 10, Maruan Al-Shedivat, Trapit Bansal, Yuri Burda, Ilya Sutskever, Igor Mordatch, and Pieter Abbeel. [Continuous Adaptation via Meta-Learning in Nonstationary and Competitive Environments](https://arxiv.org/abs/1710.03641). *arXiv:1710.03641*. [site](https://sites.google.com/view/adaptation-via-metalearning).
* 2017 July 18, Chelsea Finn, Pieter Abbeel, and Sergey Levine. [Model-Agnostic Meta-Learning for Fast Adaptation of Deep Networks](https://arxiv.org/abs/1703.03400). *arXiv:1703.03400*. [blog](http://bair.berkeley.edu/blog/2017/07/18/learning-to-learn/).
* 2017 March 15, Jake Snell, Kevin Swersky, and Richard S. Zemel. [Prototypical Networks for Few-shot Learning](https://arxiv.org/abs/1703.05175). *arXiv:1703.05175*.
* 2016 November 5, Sachin Ravi and Hugo Larochelle. [Optimization as a Model for Few-Shot Learning](https://openreview.net/forum?id=rJY0-Kcll). *OpenReview*.
* 2016 June 13, Oriol Vinyals, Charles Blundell, Timothy Lillicrap, Koray Kavukcuoglu, and Daan Wierstra. [Matching Networks for One Shot Learning](https://arxiv.org/abs/1606.04080). *arXiv:1606.04080*.
* 2016 June 7, Harrison Edwards and Amos Storkey. [Towards a Neural Statistician](https://arxiv.org/abs/1606.02185). *arXiv:1606.02185*.
* 2016 May 19, Adam Santoro, Sergey Bartunov, Matthew Botvinick, Daan Wierstra, and Timothy Lillicrap. [One-shot Learning with Memory-Augmented Neural Networks](https://arxiv.org/abs/1605.06065). *arXiv:1605.06065*.
* 2015 December 11, Brenden M. Lake, Ruslan Salakhutdinov, Joshua B. Tenenbaum. [Human-level concept learning through probabilistic program induction](http://science.sciencemag.org/content/350/6266/1332). *Science*, 350(6266):1332-1338.


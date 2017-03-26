---
permalink: /frontier/meta-learning.html
mathjax: true
---
# Meta-Learning

Meta-learning occurs at a higher level than standard learning and improves the latter's performance. It is also referred to as "learning to learn". It is theoretically possible to add another level of learning and build a system that learns to learn to learn, but this is rarely done in practice.

Based on the standard learning task that is targeted at the lower level by the meta learner, research in this area can be further organized into the following lines:

## Few-Shot Learning

Classification models that perform well after seeing very few samples from each class can be achieved in a number of ways:

* A good weight initialization ([Finn et al., 2017](https://arxiv.org/abs/1703.03400)) so that subsequent learning coverges rapidly,
* Weight initialization and an optimizer ([Ravi & Larochelle, 2016](https://openreview.net/forum?id=rJY0-Kcll)) that builds on weight update rules meta-learned by gradient descent ([Andrychowicz et al., 2016](https://arxiv.org/abs/1606.04474)),
* Learning an embedding of examples that facilitates classification by a linear model ([Snell et al., 2017](https://arxiv.org/abs/1703.05175)) or k-nearest neighbor ([Vinyals et al., 2016](https://arxiv.org/abs/1606.04080)), and
* Using external memory ([Santoro et al., 2016](https://arxiv.org/abs/1605.06065)) to rapidly bind information in the data.

For deep generative models, an autoencoder can be extended to learn statistics of datasets ([Edwards & Storkey, 2016](https://arxiv.org/abs/1606.02185)), rather than datapoints.

[Omniglot](https://github.com/brendenlake/omniglot) is a popular data set for evaluation.

## Reinforcement Learning

An agent can be trained across many different tasks to meta-learn a reinforcment learning procedure that rapidly and efficiently adapts to a new task. Works have been done focusing on relatively structured ([Wang et al., 2016](https://arxiv.org/abs/1611.05763)) and unstructured ([Duan et al., 2016](https://arxiv.org/abs/1611.02779)) distributions of tasks.

## Network Dynamics

A standard learning architecture can be made more flexible and efficient when its internal dynamics is also learned from data. Conceptually, this dynamics learning occurs at a higher level than the learning implemented by the standard architecture, thus falls within the scope of meta-learning. When these new architectures are widely used, they will become less "meta" and more closely aligned with advances in architecture design.

In a standard neural network learning setup, the update rules of how the network's weights can be learned using gradient descient ([Andrychowicz et al., 2016](https://arxiv.org/abs/1606.04474)) or guided policy search ([Li & Malik, 2016](https://arxiv.org/abs/1606.01885)). More generally, meta-learning can be applied to black-box optimizations ([Chen et al., 2016](https://arxiv.org/abs/1611.03824)). In HyperNetworks ([Ha et al., 2016](https://arxiv.org/abs/1609.09106)), one network can dynamically generate weights for another network.

## References

* 2017 March 15, Jake Snell, Kevin Swersky, and Richard S. Zemel. [Prototypical Networks for Few-shot Learning](https://arxiv.org/abs/1703.05175). *arXiv:1703.05175*.
* 2017 March 14, Olga Wichrowska, Niru Maheswaranathan, Matthew W. Hoffman, Sergio Gomez Colmenarejo, Misha Denil, Nando de Freitas, and Jascha Sohl-Dickstein. [Learned Optimizers that Scale and Generalize](https://arxiv.org/abs/1703.04813). *arXiv:1703.04813*.
* 2017 March 9, Chelsea Finn, Pieter Abbeel, and Sergey Levine. [Model-Agnostic Meta-Learning for Fast Adaptation of Deep Networks](https://arxiv.org/abs/1703.03400). *arXiv:1703.03400*.
* 2016 November 17, Jane X Wang, Zeb Kurth-Nelson, Dhruva Tirumala, Hubert Soyer, Joel Z Leibo, Remi Munos, Charles Blundell, Dharshan Kumaran, and Matt Botvinick. [Learning to reinforcement learn](https://arxiv.org/abs/1611.05763). *arXiv:1611.05763*.
* 2016 November 11, Yutian Chen, Matthew W. Hoffman, Sergio Gomez Colmenarejo, Misha Denil, Timothy P. Lillicrap, and Nando de Freitas. [Learning to Learn for Global Optimization of Black Box Functions](https://arxiv.org/abs/1611.03824). *arXiv:1611.03824*.
* 2016 November 9, Yan Duan, John Schulman, Xi Chen, Peter L. Bartlett, Ilya Sutskever, and Pieter Abbeel. [RL\\(^2\\): Fast Reinforcement Learning via Slow Reinforcement Learning](https://arxiv.org/abs/1611.02779). *arXiv:1611.02779*.
* 2016 November 5, Sachin Ravi and Hugo Larochelle. [Optimization as a Model for Few-Shot Learning](https://openreview.net/forum?id=rJY0-Kcll). *OpenReview*.
* 2016 November 5, Barret Zoph and Quoc V. Le. [Neural Architecture Search with Reinforcement Learning](https://arxiv.org/abs/1611.01578). *arXiv:1611.01578*.
* 2016 September 27, David Ha, Andrew Dai, and Quoc V. Le. [HyperNetworks](https://arxiv.org/abs/1609.09106). *arXiv:1609.09106*.
* 2016 June 14, Marcin Andrychowicz, Misha Denil, Sergio Gomez, Matthew W. Hoffman, David Pfau, Tom Schaul, Brendan Shillingford, and Nando de Freitas. [Learning to learn by gradient descent by gradient descent](https://arxiv.org/abs/1606.04474). *arXiv:1606.04474*.
* 2016 June 13, Oriol Vinyals, Charles Blundell, Timothy Lillicrap, Koray Kavukcuoglu, and Daan Wierstra. [Matching Networks for One Shot Learning](https://arxiv.org/abs/1606.04080). *arXiv:1606.04080*.
* 2016 June 7, Harrison Edwards and Amos Storkey. [Towards a Neural Statistician](https://arxiv.org/abs/1606.02185). *arXiv:1606.02185*.
* 2016 June 6, Ke Li and Jitendra Malik. [Learning to Optimize](https://arxiv.org/abs/1606.01885). *arXiv:1606.01885*.
* 2016 May 19, Adam Santoro, Sergey Bartunov, Matthew Botvinick, Daan Wierstra, and Timothy Lillicrap. [One-shot Learning with Memory-Augmented Neural Networks](https://arxiv.org/abs/1605.06065). *arXiv:1605.06065*.
* 2015 December 11, Brenden M. Lake, Ruslan Salakhutdinov, Joshua B. Tenenbaum. [Human-level concept learning through probabilistic program induction](http://science.sciencemag.org/content/350/6266/1332). *Science*, 350(6266):1332-1338.

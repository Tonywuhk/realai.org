---
permalink: /meta-learning/
mathjax: true
---
# Meta-Learning

Meta-learning occurs at a higher level than standard learning and improves the latter's performance. It is also referred to as "learning to learn". It is theoretically possible to add another level of learning and build a system that learns to learn to learn, but this is rarely done in practice.

## Related Topics

* [Few-Shot Learning](http://realai.org/few-shot-learning/): The empasis is on learning to solve tasks using only a small number of samples.

## Overview

[Mishra & Rohaninejad et al. (2017)](https://arxiv.org/abs/1707.03141) propse temporal-convolution-based meta-learner (TCML), a deep stack of dilated 1D-convolutions over the temporal dimension. It is simple and generic, has no particular strategy or algorithm encoded into it, and can be viewed as a flavor of RNN that can remember information through the activations of the network rather than through an explicit memory module.

Based on the standard learning task that is targeted at the lower level by the meta learner, research in this area can be further organized into the following lines:

## Reinforcement Learning

An agent can be trained across many different tasks to meta-learn a reinforcment learning procedure that rapidly and efficiently adapts to a new task. Works have been done focusing on relatively structured ([Wang et al., 2016](https://arxiv.org/abs/1611.05763)) and unstructured ([Duan et al., 2016](https://arxiv.org/abs/1611.02779)) distributions of tasks.

## Learning to Optimize 

A standard learning architecture can be made more flexible and efficient when its internal dynamics is also learned from data. Conceptually, this dynamics learning occurs at a higher level than the learning implemented by the standard architecture, thus falls within the scope of meta-learning. When these new architectures are widely used, they will become less "meta" and more closely aligned with advances in architecture design.

[Andrychowicz et al. (2016)](https://arxiv.org/abs/1606.04474) show that update rules modeled by learned LSTMs outperform generic, hand-designed [learning rules](http://realai.org/learning-rules/) such as Adam and RMSProp. [Wichrowska et al. (2017)](https://arxiv.org/abs/1703.04813) introduce a hierarchical RNN optimizer and achieve better generalization to new problems and large number of optimization steps.

In a standard neural network learning setup, the update rules of the network's weights can also be learned using guided policy search ([Li & Malik, 2016](https://arxiv.org/abs/1606.01885)). More generally, meta-learning can be applied to black-box optimizations ([Chen et al., 2016](https://arxiv.org/abs/1611.03824)) and neural architecture search ([Zoph & Le, 2016](https://arxiv.org/abs/1611.01578)). In HyperNetworks ([Ha et al., 2016](https://arxiv.org/abs/1609.09106)), one network can dynamically generate weights for another network.

## References

* 2017 July 11, Nikhil Mishra, Mostafa Rohaninejad, Xi Chen, and Pieter Abbeel. [Meta-Learning with Temporal Convolutions](https://arxiv.org/abs/1707.03141). *arXiv:1707.03141*.
* 2017 March 14, Olga Wichrowska, Niru Maheswaranathan, Matthew W. Hoffman, Sergio Gomez Colmenarejo, Misha Denil, Nando de Freitas, and Jascha Sohl-Dickstein. [Learned Optimizers that Scale and Generalize](https://arxiv.org/abs/1703.04813). *arXiv:1703.04813*.
* 2016 November 17, Jane X Wang, Zeb Kurth-Nelson, Dhruva Tirumala, Hubert Soyer, Joel Z Leibo, Remi Munos, Charles Blundell, Dharshan Kumaran, and Matt Botvinick. [Learning to reinforcement learn](https://arxiv.org/abs/1611.05763). *arXiv:1611.05763*.
* 2016 November 11, Yutian Chen, Matthew W. Hoffman, Sergio Gomez Colmenarejo, Misha Denil, Timothy P. Lillicrap, and Nando de Freitas. [Learning to Learn for Global Optimization of Black Box Functions](https://arxiv.org/abs/1611.03824). *arXiv:1611.03824*.
* 2016 November 9, Yan Duan, John Schulman, Xi Chen, Peter L. Bartlett, Ilya Sutskever, and Pieter Abbeel. [RL\\(^2\\): Fast Reinforcement Learning via Slow Reinforcement Learning](https://arxiv.org/abs/1611.02779). *arXiv:1611.02779*.
* 2016 November 5, Barret Zoph and Quoc V. Le. [Neural Architecture Search with Reinforcement Learning](https://arxiv.org/abs/1611.01578). *arXiv:1611.01578*.
* 2016 September 27, David Ha, Andrew Dai, and Quoc V. Le. [HyperNetworks](https://arxiv.org/abs/1609.09106). *arXiv:1609.09106*.
* 2016 June 6, Ke Li and Jitendra Malik. [Learning to Optimize](https://arxiv.org/abs/1606.01885). *arXiv:1606.01885*.


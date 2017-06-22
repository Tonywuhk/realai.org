---
permalink: /imitation-learning/
---
# Imitation Learning

Imitation learning is when a learning architecture is trained to mimic behaviors, usually human demonstrations.

## Behavioral Cloning

## Inverse Reinforcement Learning

### References

* 2017 May 15, Kareem Amin, Nan Jiang, and Satinder Singh. [Repeated Inverse Reinforcement Learning for AI Safety](https://arxiv.org/abs/1705.05427). *arXiv:1705.05427*.
* 2017 March 22, Yan Duan, Marcin Andrychowicz, Bradly C. Stadie, Jonathan Ho, Jonas Schneider, Ilya Sutskever, Pieter Abbeel, and Wojciech Zaremba. [One-Shot Imitation Learning](https://arxiv.org/abs/1703.07326). *arXiv:1703.07326*.
* 2017 March 6, Bradly C. Stadie, Pieter Abbeel, and Ilya Sutskever. [Third-Person Imitation Learning](https://arxiv.org/abs/1703.01703). *arXiv:1703.01703*.
* 2016 June 10, Jonathan Ho and Stefano Ermon. [Generative Adversarial Imitation Learning](https://arxiv.org/abs/1606.03476). *arXiv:1606.03476*.
* 2016 March 1, Chelsea Finn, Sergey Levine, and Pieter Abbeel. [Guided Cost Learning: Deep Inverse Optimal Control via Policy Optimization](https://arxiv.org/abs/1603.00448). *arXiv:1603.00448*.

## Observational Learning

In observational learning, a student agent can observe a teacher agent, but is not required to learn anything from it. It is not considered imitation learning, although it would be nice to have an experiment where imitation learning emerges from the availability of observations. In simple scenarios where a student agent seeks a sometimes hidden goal, [Borsa et al. (2017)](https://arxiv.org/abs/1706.06617) demonstrate that a reinforcement learning agent can distill useful information contained in observed teacher behavior, and learns useful policies such as seeking the teacher then simply following it to the goal.

### References

* 2017 June 20, Diana Borsa, Bilal Piot, Rémi Munos, and Olivier Pietquin. [Observational Learning by Reinforcement Learning](https://arxiv.org/abs/1706.06617). *arXiv:1706.06617*.

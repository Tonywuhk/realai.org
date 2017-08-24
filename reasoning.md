---
permalink: /reasoning/
mathjax: true
---
# Reasoning

The ability of reasoning emcompasses "algebraically manipulating knowledge to answer a question" ([Bottou, 2011](https://arxiv.org/abs/1102.1808)). [Chollet (2017)](https://blog.keras.io/the-future-of-deep-learning.html) considers reasoning a "fundamental weakness of current models". In an August 2017 [interview with QbitAI](http://mp.weixin.qq.com/s/ZNS-q7Y-6ZByHmFT0WzpvQ), Andrew Yao mentions reasoning as a potential venue for breakthrough towards AGI that is now hopeful to be found.

## Relation Networks

For an input set of objects \\(O=\\{o_1, o_2, ..., o_n\\}\\), the Relation Network (RN) is

$$
\text{RN}(O) = f_\phi \Big(\sum\limits_{i,j} g_\theta(o_i, o_j, q)\Big),
$$

where \\(f_\phi\\) and \\(g_\theta\\) are MLPs, \\(q\\) is the embedding of a query on the object's relations. Using RN, [Santoro & Raposo et al. (2017)](https://arxiv.org/abs/1706.01427) achieve super-human performance on a challenging visual QA dataset [CLEVR](http://cs.stanford.edu/people/jcjohns/clevr/). An RN is a critical component in the core of an Interaction Net, without which a Visual Interaction Network performs much worse in tasks of predicting the trajectory of simulated physical objects ([Watters et al., 2017](https://arxiv.org/abs/1706.01433)). It is worth noting that the presence of noise from a visual encoder *enhanced* the performance of its downstream Interaction Network that reasons purely in the states of objects. This is a good example where additional intelligence emerges from the composition of simple modules.

### References

* 2017 July 18, Francois Chollet. [The future of deep learning](https://blog.keras.io/the-future-of-deep-learning.html). *The Keras Blog*.
* 2017 June 5, Nicholas Watters, Andrea Tacchetti, Theophane Weber, Razvan Pascanu, Peter Battaglia, and Daniel Zoran. [Visual Interaction Networks](https://arxiv.org/abs/1706.01433). *arXiv:1706.01433*.
* 2017 June 5, Adam Santoro, David Raposo, David G. T. Barrett, Mateusz Malinowski, Razvan Pascanu, Peter Battaglia, and Timothy Lillicrap. [A simple neural network module for relational reasoning](https://arxiv.org/abs/1706.01427). *arXiv:1706.01427*.
* 2011 February 11, Leon Bottou. [From Machine Learning to Machine Reasoning](https://arxiv.org/abs/1102.1808). *arXiv:1102.1808*.


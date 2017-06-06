---
permalink: /reasoning/
mathjax: true
---
# Reasoning

## Relation Networks

For an input set of objects \\(O=\{o_1, o_2, ..., o_n\}\\), the Relation Network (RN) is

$$
\text{RN}(O) = f_\phi (\Sigma_{i,j} g_\theta(o_i, o_j, q)),
$$

where \\(f_\phi\\) and \\(g_\theta\\) are MLPs, \\(q\\) is the embedding of a query on the object's relations. Using RN, Santoro & Raposo et al. (2017) achieve super-human performance on a challenging visual QA dataset [CLEVR](http://cs.stanford.edu/people/jcjohns/clevr/).

### References

* 2017 June 5, Adam Santoro, David Raposo, David G. T. Barrett, Mateusz Malinowski, Razvan Pascanu, Peter Battaglia, and Timothy Lillicrap. [A simple neural network module for relational reasoning](https://arxiv.org/abs/1706.01427). *arXiv:1706.01427*.

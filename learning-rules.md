---
permalink: /learning-rules/
mathjax: true
---
# Learning Rules

## Regularization

[Pereyra & Tucker et al. (2017)](https://arxiv.org/abs/1701.06548) found that label smoothing and confidence penalty improved model performances.

### Bayesian Learning

Bayesian learning introduces uncertainty in the weights $\theta$ of a neural network. [Blundell et al. (2015)](https://arxiv.org/abs/1505.05424) introduced the *Bayes by Backprop* algorithm that regularises the weights of a neural network by minimizing the variationial free energy:
$$
\mathcal{L}(\theta) = -\mathbb{E}_{q(\theta)} [\log p(y | \theta, x)] + \mathrm{KL}[q(\theta)||p(\theta)]
$$
where 

[Fortunato et al. (2017)](https://arxiv.org/abs/1704.02798) extended their approach to Recurrent Neural Networks:

$$
\mathcal{L}(\theta) = -\mathbb{E}_{q(\theta)} [\log p(y_{1:T} | \theta, x_{1:T})] + \mathrm{KL}[q(\theta)||p(\theta)]
$$

## References

* 2017 April 10, Meire Fortunato, Charles Blundell, and Oriol Vinyals. [Bayesian Recurrent Neural Networks](https://arxiv.org/abs/1704.02798). *arXiv:1704.02798*.
* 2017 March 1, Wojciech Marian Czarnecki, Grzegorz Świrszcz, Max Jaderberg, Simon Osindero, Oriol Vinyals, and Koray Kavukcuoglu. [Understanding Synthetic Gradients and Decoupled Neural Interfaces](https://arxiv.org/abs/1703.00522). *arXiv:1703.00522*.
* 2017 January 23, Gabriel Pereyra, George Tucker, Jan Chorowski, Łukasz Kaiser, and Geoffrey Hinton. [Regularizing Neural Networks by Penalizing Confident Output Distributions](https://arxiv.org/abs/1701.06548). *arXiv:1701.06548*.
* 2016 August 18, Max Jaderberg, Wojciech Marian Czarnecki, Simon Osindero, Oriol Vinyals, Alex Graves, and Koray Kavukcuoglu. [Decoupled Neural Interfaces using Synthetic Gradients](https://arxiv.org/abs/1608.05343). *arXiv:1608.05343*.
* 2016 January 7, Timothy P. Lillicrap, Daniel Cownden, Douglas B. Tweed, and Colin J. Akerman. [Random synaptic feedback weights support error backpropagation for deep learning](http://www.nature.com/articles/ncomms13276). *Nature Communications*, 7:13276.
* 2015 May 20, Charles Blundell, Julien Cornebise, Koray Kavukcuoglu, and Daan Wierstra. [Weight Uncertainty in Neural Networks](https://arxiv.org/abs/1505.05424). *arXiv:1505.05424*.
* 2015 February 14, Yoshua Bengio, Dong-Hyun Lee, Jorg Bornschein, Thomas Mesnard, and Zhouhan Lin. [Towards Biologically Plausible Deep Learning](https://arxiv.org/abs/1502.04156). *arXiv:1502.04156*.

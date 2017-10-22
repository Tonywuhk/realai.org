---
permalink: /learning-rules/
mathjax: true
---
# Learning Rules

## Initialization

In a self-normalizing neural network (SNN) proposed by [Klambauer et al. (2017)](https://arxiv.org/abs/1706.02515), the weights in a feed-forward neural network are initialized in such a way that, for any unit in a higher layer with \\(n\\) input weights \\(w_i (1 \leq i \leq n)\\), \\(\Sigma_{i=1}^n w_i = 0\\) and \\(\Sigma_{i=1}^n w_i^2 = 1\\). Moreover, the "scaled exponential linear unit" (SELU) activation function is given by

$$
\text{selu}(x) = \lambda
  \begin{cases}
    x & \text{if } x>0 \\
    \alpha e^x - \alpha & \text{if } x \leq 0
  \end{cases},
$$

where \\(\alpha \approx 1.6733\\) and \\(\lambda \approx 1.0507\\). Under these conditions, the activations in a layer converge towards zero mean and unit variance as they propagate through many network layers. This is an alternative method to [normalize network activations](https://theneuralperspective.com/2016/10/27/gradient-topics/) that motivated popular techniques like batch and layer normalization. 

### References

* 2017 June 8, Günter Klambauer, Thomas Unterthiner, Andreas Mayr, and Sepp Hochreiter. [Self-Normalizing Neural Networks](https://arxiv.org/abs/1706.02515). *arXiv:1706.02515*. [code](https://github.com/bioinf-jku/SNNs).

## Activation Function

[Ramachandran et al. (2017)](https://arxiv.org/abs/1710.05941) propose a new activation function, named Swish, which is simply \\(f(x)=x \cdot \mathrm{sigmoid} (x)\\). A [brief introduction](https://medium.com/@jaiyamsharma/experiments-with-swish-activation-function-on-mnist-dataset-fc89a8c79ff7) is available on Medium.

### References

* 2017 October 16, Prajit Ramachandran, Barret Zoph, and Quoc V. Le. [Swish: a Self-Gated Activation Function](https://arxiv.org/abs/1710.05941). *arXiv:1710.05941*.

## Regularization

[Pereyra & Tucker et al. (2017)](https://arxiv.org/abs/1701.06548) found that label smoothing and confidence penalty improved model performances.

### Bayesian Learning

Bayesian learning introduces uncertainty in the weights \\(\theta\\) of a neural network. Given inputs \\(x\\) and outputs \\(y\\), the *Bayes by Backprop* algorithm ([Blundell et al., 2015](https://arxiv.org/abs/1505.05424)) regularizes the weights by minimizing the variational free energy:

$$
\mathcal{L}(\theta) = -\mathbb{E}_{q(\theta)} [\log p(y | \theta, x)] + \mathrm{KL}[q(\theta)||p(\theta)],
$$

where \\(\mathrm{KL}[q(\theta)\|\|p(\theta)]\\) is the Kullback-Leibler divergence between the posterior \\(q(\theta)\\) and prior \\(p(\theta)\\) of the weights. [Fortunato et al. (2017)](https://arxiv.org/abs/1704.02798) extended this approach to recurrent neural networks:

$$
\mathcal{L}(\theta) = -\mathbb{E}_{q(\theta)} [\log p(y_{1:T} | \theta, x_{1:T})] + \mathrm{KL}[q(\theta)||p(\theta)],
$$

where \\(p(y_{1:T} \| \theta, x_{1:T})\\) is the likelihood of a sequence of length \\(T\\).

## References

* 2017 April 10, Meire Fortunato, Charles Blundell, and Oriol Vinyals. [Bayesian Recurrent Neural Networks](https://arxiv.org/abs/1704.02798). *arXiv:1704.02798*.
* 2017 March 1, Wojciech Marian Czarnecki, Grzegorz Świrszcz, Max Jaderberg, Simon Osindero, Oriol Vinyals, and Koray Kavukcuoglu. [Understanding Synthetic Gradients and Decoupled Neural Interfaces](https://arxiv.org/abs/1703.00522). *arXiv:1703.00522*.
* 2017 January 23, Gabriel Pereyra, George Tucker, Jan Chorowski, Łukasz Kaiser, and Geoffrey Hinton. [Regularizing Neural Networks by Penalizing Confident Output Distributions](https://arxiv.org/abs/1701.06548). *arXiv:1701.06548*.
* 2016 August 18, Max Jaderberg, Wojciech Marian Czarnecki, Simon Osindero, Oriol Vinyals, Alex Graves, and Koray Kavukcuoglu. [Decoupled Neural Interfaces using Synthetic Gradients](https://arxiv.org/abs/1608.05343). *arXiv:1608.05343*.
* 2016 January 7, Timothy P. Lillicrap, Daniel Cownden, Douglas B. Tweed, and Colin J. Akerman. [Random synaptic feedback weights support error backpropagation for deep learning](http://www.nature.com/articles/ncomms13276). *Nature Communications*, 7:13276.
* 2015 May 20, Charles Blundell, Julien Cornebise, Koray Kavukcuoglu, and Daan Wierstra. [Weight Uncertainty in Neural Networks](https://arxiv.org/abs/1505.05424). *arXiv:1505.05424*.
* 2015 February 14, Yoshua Bengio, Dong-Hyun Lee, Jorg Bornschein, Thomas Mesnard, and Zhouhan Lin. [Towards Biologically Plausible Deep Learning](https://arxiv.org/abs/1502.04156). *arXiv:1502.04156*.


---
permalink: /learning-rules/
mathjax: true
---
# Learning Rules

## Gradient Descent

[Ruder (2016)](https://arxiv.org/abs/1609.04747) gave an excellent overview of commonly used gradient descient algorithms, including Momentum ([Goh, 2017](http://distill.pub/2017/momentum/)), Adagrad ([Duchi et al., 2011](http://jmlr.org/papers/v12/duchi11a.html)), RMSprop ([slides](http://www.cs.toronto.edu/~tijmen/csc321/slides/lecture_slides_lec6.pdf)), Adadelta ([Zeiler, 2012](https://arxiv.org/abs/1212.5701)) and Adam ([Kingma & Ba, 2014](https://arxiv.org/abs/1412.06980)). Let \\(\theta_t\\) be the parameters of the model during training step \\(t\\), \\(g_t\\) the gradient of the training objective that is to be minized, then the core rule of stochastic gradient descent (**SGD**) is

$$
\Delta \theta_t = -\alpha g_t,
$$

where \\(\alpha\\) is the learning rule. SGD is normally computed on a mini-batch of training examples. Define momentum as

$$
m_t = \gamma m_{t-1} + (1-\gamma) g_t
$$

for a momentum term \\(\gamma\\) that is usually close to 1. The **momentum** rule

$$
\Delta \theta_t = -\alpha m_t
$$

allows parameter moves to be more persistent along past directions. In **Adagrad**, the SGD updates are adapted to individual parameters

$$
\Delta \theta_t = -\alpha g_t (G_t + \epsilon)^{-1/2}
$$

with the help of a very small positive real number \\(\epsilon\\) to avoid division by zero. The accumulated gradients

$$
G_t = G_{t-1} + g_t^2
$$

keep growing during training, causing the size of parameter moves to decrease over time. This problem can be mitigated by using the moving average of squared gradients

$$
v_t = \beta_2 v_{t-1} + (1-\beta_2) g_t^2.
$$

In the **RMSprop** method,

$$
\Delta \theta_t = -\alpha g_t (v_t + \epsilon)^{-1/2}.
$$

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
* 2017 April 4, *Distill*. [Why Momentum Really Works](http://distill.pub/2017/momentum/). Gabriel Goh.
* 2017 March 1, Wojciech Marian Czarnecki, Grzegorz Świrszcz, Max Jaderberg, Simon Osindero, Oriol Vinyals, and Koray Kavukcuoglu. [Understanding Synthetic Gradients and Decoupled Neural Interfaces](https://arxiv.org/abs/1703.00522). *arXiv:1703.00522*.
* 2017 January 23, Gabriel Pereyra, George Tucker, Jan Chorowski, Łukasz Kaiser, and Geoffrey Hinton. [Regularizing Neural Networks by Penalizing Confident Output Distributions](https://arxiv.org/abs/1701.06548). *arXiv:1701.06548*.
* 2016 September 15, Sebastian Ruder. [An overview of gradient descent optimization algorithms](https://arxiv.org/abs/1609.04747). *arXiv:1609.04747*. [blog](http://sebastianruder.com/optimizing-gradient-descent/).
* 2016 August 18, Max Jaderberg, Wojciech Marian Czarnecki, Simon Osindero, Oriol Vinyals, Alex Graves, and Koray Kavukcuoglu. [Decoupled Neural Interfaces using Synthetic Gradients](https://arxiv.org/abs/1608.05343). *arXiv:1608.05343*.
* 2016 January 7, Timothy P. Lillicrap, Daniel Cownden, Douglas B. Tweed, and Colin J. Akerman. [Random synaptic feedback weights support error backpropagation for deep learning](http://www.nature.com/articles/ncomms13276). *Nature Communications*, 7:13276.
* 2015 May 20, Charles Blundell, Julien Cornebise, Koray Kavukcuoglu, and Daan Wierstra. [Weight Uncertainty in Neural Networks](https://arxiv.org/abs/1505.05424). *arXiv:1505.05424*.
* 2015 February 14, Yoshua Bengio, Dong-Hyun Lee, Jorg Bornschein, Thomas Mesnard, and Zhouhan Lin. [Towards Biologically Plausible Deep Learning](https://arxiv.org/abs/1502.04156). *arXiv:1502.04156*.
* 2014 December 22, Diederik P. Kingma and Jimmy Ba. [Adam: A Method for Stochastic Optimization](https://arxiv.org/abs/1412.06980). *arXiv:1412.06980*.
* 2012 December 22, Matthew D. Zeiler. [ADADELTA: An Adaptive Learning Rate Method](https://arxiv.org/abs/1212.5701). *arXiv:1212.5701*.
* 2011 July, John Duchi, Elad Hazan, and Yoram Singer. [Adaptive Subgradient Methods for Online Learning and Stochastic Optimization](http://jmlr.org/papers/v12/duchi11a.html). *Journal of Machine Learning Research*.

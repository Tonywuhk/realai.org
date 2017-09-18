---
permalink: /course/deep-learning/gradient-descent/
redirect_from: /course/DL/gradient-descent/
mathjax: true
---
# Gradient Descent

Commonly used gradient descent algorithms include momentum ([Goh, 2017](http://distill.pub/2017/momentum/)), Adagrad ([Duchi et al., 2011](http://jmlr.org/papers/v12/duchi11a.html)), RMSprop ([slides](http://www.cs.toronto.edu/~tijmen/csc321/slides/lecture_slides_lec6.pdf)), Adadelta ([Zeiler, 2012](https://arxiv.org/abs/1212.5701)) and Adam ([Kingma & Ba, 2014](https://arxiv.org/abs/1412.06980)). Let \\(\theta_t\\) be the parameters of the model during training step \\(t\\), \\(g_t\\) the gradient of the training objective that is to be minimized, then the core rule of stochastic gradient descent (**SGD**) is

$$
\Delta \theta_t = -\alpha g_t,
$$

where \\(\alpha\\) is the learning rate. SGD is normally computed on a mini-batch of training examples. Define momentum as

$$
m_t = \beta_1 m_{t-1} + (1-\beta_1) g_t
$$

for a momentum term \\(\beta_1\\) that is usually close to 1. The **momentum** rule

$$
\Delta \theta_t = -\alpha m_t
$$

allows parameter updates to be more persistent along past directions. In **Adagrad**, the SGD updates are adapted to individual parameters

$$
\Delta \theta_t = -\alpha g_t (G_t + \epsilon)^{-1/2}
$$

with the help of a very small positive real number \\(\epsilon\\) to avoid division by zero. The accumulated gradients

$$
G_t = G_{t-1} + g_t^2
$$

keep growing during training, causing the size of parameter updates to decrease over time. This problem is mitigated by using the moving average of squared gradients

$$
v_t = \beta_2 v_{t-1} + (1-\beta_2) g_t^2.
$$

In the **RMSprop** method,

$$
\Delta \theta_t = -\alpha g_t (v_t + \epsilon)^{-1/2}.
$$

Replace the above learning rate by the moving average of parameter updates, we obtain the **Adadelta** method

$$
\Delta \theta_t = - g_t D_{t-1}^{1/2} (v_t + \epsilon)^{-1/2},
$$

where \\(D_t = \gamma D_{t-1} + (1-\gamma) (\Delta \theta_t)^2\\). Using the bias-corrected versions of momentum \\(\hat{m}_t = m_t/(1-\beta_1^t)\\) and second moment \\(\hat{v}_t = v_t/(1-\beta_2^t)\\), the **Adam** method combines the above elements and updates the parameters by

$$
\Delta \theta_t = -\alpha \hat{m}_t (v_t^{-1/2} + \epsilon).
$$

[Wilson et al. (2017)](https://arxiv.org/abs/1705.08292) report that simple SGD performs better than the adaptive rules mentioned above, if learning rates are carefully tuned. [Zhang et al. (2017)](https://arxiv.org/abs/1706.03471) design *YellowFin*, an automatic tuner for both momentum and learning rate.

## Further Reading

* 2017 June 15, [Sebastian Ruder](http://ruder.io/) ([Twitter](https://twitter.com/seb_ruder)). [An overview of gradient descent optimization algorithms](http://ruder.io/optimizing-gradient-descent/). *personal blog*. [arXiv](https://arxiv.org/abs/1609.04747).

## References

* 2017 June 12, Jian Zhang, Ioannis Mitliagkas, and Christopher Ré. [YellowFin and the Art of Momentum Tuning](https://arxiv.org/abs/1706.03471). *arXiv:1706.03471*. [site](http://cs.stanford.edu/~zjian/project/YellowFin/).
* 2017 May 23, Ashia C. Wilson, Rebecca Roelofs, Mitchell Stern, Nathan Srebro, and Benjamin Recht. [The Marginal Value of Adaptive Gradient Methods in Machine Learning](https://arxiv.org/abs/1705.08292). *arXiv:1705.08292*.
* 2017 April 4, *Distill*. [Why Momentum Really Works](http://distill.pub/2017/momentum/). Gabriel Goh.
* 2014 December 22, Diederik P. Kingma and Jimmy Ba. [Adam: A Method for Stochastic Optimization](https://arxiv.org/abs/1412.06980). *arXiv:1412.06980*.
* 2012 December 22, Matthew D. Zeiler. [ADADELTA: An Adaptive Learning Rate Method](https://arxiv.org/abs/1212.5701). *arXiv:1212.5701*.
* 2011 July, John Duchi, Elad Hazan, and Yoram Singer. [Adaptive Subgradient Methods for Online Learning and Stochastic Optimization](http://jmlr.org/papers/v12/duchi11a.html). *Journal of Machine Learning Research*.

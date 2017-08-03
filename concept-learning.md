---
permalink: /concept-learning/
mathjax: true
---
# Concept Learning

[Higgins et al. (2016)](https://arxiv.org/abs/1606.05579) propose the \\(\beta\\)-VAE framework capable of learning disentangled factors that represent visual primitives. These factors can be paired with symbols using a Symbol-Concept Association Network (SCAN; [Higgins et al., 2017](https://arxiv.org/abs/1707.03389)) to achieve bi-directional inference between image samples and symbolic descriptions. By teaching logical operators to SCAN, it learns to imagine new concepts constructed from logical operators, although it is yet able to attach new symbols to these newly constructed concepts.

### References

* 2017 July 12, Irina Higgins, Nicolas Sonnerat, Loic Matthey, Arka Pal, Christopher P Burgess, Matthew Botvinick, Demis Hassabis, and Alexander Lerchner. [SCAN: Learning Abstract Hierarchical Compositional Visual Concepts](https://arxiv.org/abs/1707.03389). *arXiv:1707.03389*. [blog](https://deepmind.com/blog/imagine-creating-new-visual-concepts-recombining-familiar-ones/).
* 2016 September 20, Irina Higgins, Loic Matthey, Xavier Glorot, Arka Pal, Benigno Uria, Charles Blundell, Shakir Mohamed, and Alexander Lerchner. [Early Visual Concept Learning with Unsupervised Deep Learning](https://arxiv.org/abs/1606.05579). *arXiv:1606.05579*.

## Disentangled Representations

In [Denton & Birodkar (2017)](https://arxiv.org/abs/1705.10915), two neural network encoders are forced to learn different aspects of video frames, content and pose. To ensure that learned poses do not carry content information, the pose encoders are trained with an adversarial discriminator that learns to classify whether learned poses from the same video.

### References

* 2017 May 31, Emily Denton and Vighnesh Birodkar. [Unsupervised Learning of Disentangled Representations from Video](https://arxiv.org/abs/1705.10915). *arXiv:1705.10915*.

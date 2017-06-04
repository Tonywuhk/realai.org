---
permalink: /concept-learning/
---
# Concept Learning

## Disentangled Representations

In [Denton & Birodkar (2017)](https://arxiv.org/abs/1705.10915), two neural network encoders are forced to learn different aspects of video frames, content and pose. To ensure that learned poses do not carry content information, the pose encoders are trained with an adversarial discriminator that learns to classify whether learned poses from the same video.

### References

* 2017 May 31, Emily Denton and Vighnesh Birodkar. [Unsupervised Learning of Disentangled Representations from Video](https://arxiv.org/abs/1705.10915). *arXiv:1705.10915*.

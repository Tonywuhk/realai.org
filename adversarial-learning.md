---
permalink: /adversarial-learning/
---
# Adversarial Learning

## Adversarial Examples

Optical illusions are like adversarial examples for the human brain. Meiji University's [Koichi Sugihara](http://home.mims.meiji.ac.jp/~sugihara/Welcomee.html) has made quite a few stunning [3D illusions](https://twitter.com/machinepix/status/864543509486870528).

[Lu et al. (2017)](https://arxiv.org/abs/1707.03501) show that when the pictures of physical adversarial examples are taken from different distances and angles, they are correctly classified by trained neural networks. [Evtimov et al. (2017)](https://arxiv.org/abs/1707.08945) propose Robust Physical Perturbations, an algorithm that can generate robust adversarial examples. They physically realize an adversarial example of a Stop sign that is misclassified under varying conditions, such as distances, angles, and resolutions. [Su et al. (2017)](https://arxiv.org/abs/1710.08864) generate adversarial images with modifications on just one pixel.

## Adversarial Training Examples

[Koh & Liang (2017)](https://arxiv.org/abs/1703.04730) demonstrated that modern neural networks are vunerable to adversarial *training-set* attacks. They successfully flipped the classification output of an Inception network by making a visually-indistinguishable small change to just 1 training image.

## Evolutionary Algorithms

In the field of evolutionary algorithms, there can be two coevolving populations with adversarial goals. [Brant & Stanley (2017)](http://eplex.cs.ucf.edu/papers/brant_gecco17.pdf) introduced a novel domain wherein evolved agents learn to navigate mazes whose structures coevolve with increasing complexity.

## Generative Adversarial Networks

Generative Adversarial Networks (GAN) typically involve a pair of networks in competition with each other. [Dumoulin et al. (2017)](https://arxiv.org/abs/1710.07035) provide an overview (for the signal processing community). [Karras et al. (2017)](https://arxiv.org/abs/1710.10196) grow both the generator and discriminator progressively: starting from a low resolution, then adding new layers that model increasingly fine details as training progresses. They are able to produce CelebA images at 1024x1024 resolution.

## References

* 2017 October 27, Tero Karras, Timo Aila, Samuli Laine, and Jaakko Lehtinen. [Progressive Growing of GANs for Improved Quality, Stability, and Variation](https://arxiv.org/abs/1710.10196). *arXiv:1710.10196*. [site](http://research.nvidia.com/publication/2017-10_Progressive-Growing-of). [code](https://github.com/tkarras/progressive_growing_of_gans).
* 2017 October 24, Jiawei Su, Danilo Vasconcellos Vargas, and Sakurai Kouichi. [One pixel attack for fooling deep neural networks](https://arxiv.org/abs/1710.08864). *arXiv:1710.08864*.
* 2017 October 19, Antonia Creswell, Tom White, Vincent Dumoulin, Kai Arulkumaran, Biswa Sengupta, and Anil A Bharath. [Generative Adversarial Networks: An Overview](https://arxiv.org/abs/1710.07035). *arXiv:1710.07035*.
* 2017 July 27, Ivan Evtimov, Kevin Eykholt, Earlence Fernandes, Tadayoshi Kohno, Bo Li, Atul Prakash, Amir Rahmati, and Dawn Song. [Robust Physical-World Attacks on Machine Learning Models](https://arxiv.org/abs/1707.08945). *arXiv:1707.08945*.
* 2017 July 12, Jiajun Lu, Hussein Sibai, Evan Fabry, and David Forsyth. [NO Need to Worry about Adversarial Examples in Object Detection in Autonomous Vehicles](https://arxiv.org/abs/1707.03501). *arXiv:1707.03501*.
* 2017 April 11, Florian Tramèr, Nicolas Papernot, Ian Goodfellow, Dan Boneh, and Patrick McDaniel. [The Space of Transferable Adversarial Examples](https://arxiv.org/abs/1704.03453). *arXiv:1704.03453*.
* 2017 March 27, Aran Nayebi and Surya Ganguli. [Biologically inspired protection of deep networks from adversarial attacks](https://arxiv.org/abs/1703.09202). *arXiv:1703.09202*.
  * 2017 April 5, Wieland Brendel and Matthias Bethge. [Comment on "Biologically inspired protection of deep networks from adversarial attacks"](https://arxiv.org/abs/1704.01547). *arXiv:1704.01547*.
* 2017 March 14, Pang Wei Koh and Percy Liang. [Understanding Black-box Predictions via Influence Functions](https://arxiv.org/abs/1703.04730). *arXiv:1703.04730*.
* 2017 February 6, Jonathan C. Brant and Kenneth O. Stanley. [Minimal Criterion Coevolution: A New Approach to Open-Ended Search](http://eplex.cs.ucf.edu/papers/brant_gecco17.pdf). *The Genetic and Evolutionary Computation Conference (GECCO)*.
* 2017 January 27, Anjuli Kannan and Oriol Vinyals. [Adversarial Evaluation of Dialogue Models](https://arxiv.org/abs/1701.08198). *arXiv:1701.08198*.
* 2017 January 26, Martin Arjovsky, Soumith Chintala, and Léon Bottou. [Wasserstein GAN](https://arxiv.org/abs/1701.07875). *arXiv:1701.07875*.
* 2017 January 23, Jiwei Li, Will Monroe, Tianlin Shi, Sébastien Jean, Alan Ritter, and Dan Jurafsky. [Adversarial Learning for Neural Dialogue Generation](https://arxiv.org/abs/1701.06547). *arXiv:1701.06547*. [code](https://github.com/jiweil/Neural-Dialogue-Generation)
* 2017 January 17, Martin Arjovsky and Léon Bottou. [Towards Principled Methods for Training Generative Adversarial Networks](https://arxiv.org/abs/1701.04862). *arXiv:1701.04862*.
* 2017 January 4, Dmitry Krotov and John J Hopfield. [Dense Associative Memory is Robust to Adversarial Inputs](https://arxiv.org/abs/1701.00939). *arXiv:1701.00939*.
* 2016 October 27, Alex Lamb, Anirudh Goyal, Ying Zhang, Saizheng Zhang, Aaron Courville, and Yoshua Bengio. [Professor Forcing: A New Algorithm for Training Recurrent Networks](https://arxiv.org/abs/1610.09038). *arXiv:1610.09038*.
* 2016 October 24, Jiajun Wu, Chengkai Zhang, Tianfan Xue, William T. Freeman, and Joshua B. Tenenbaum. [Learning a Probabilistic Latent Space of Object Shapes via 3D Generative-Adversarial Modeling](https://arxiv.org/abs/1610.07584). *arXiv:1610.07584*.

---
permalink: /network-architecture/
---
# Network Architecture

## Conditional Computation

[Shazeer et al. (2017)](https://arxiv.org/abs/1701.06538) introduced a Sparsely-Gated Mixture-of-Experts (MoE) layer where each sample only activates a sparse subset of many expert networks, determined by a gating network. The layer is embedded in a larger architecture that is overall trainable by backpropagation.

## Evolutionary Algorithms

In an experiment evolving networks to produce patterns, [Huizinga et al. (2017)](https://arxiv.org/abs/1704.05143) showed that network weights encoded dimensions of image variations that are sensible to humans, possibly due to the diversity of environmental selection.

## Deep Feedforward Networks

[Greff et al. (2016)](https://arxiv.org/abs/1612.07771) argued that the functional blocks of Highway Networks ([Srivastava et al., 2015](https://arxiv.org/abs/1507.06228)) and Residual Networks ([He et al., 2015](https://arxiv.org/abs/1512.03385)) engage in an unrolled iterative estimation of representations.

## Unpublished Architectures

According to a [Twitter picture](https://twitter.com/thefillm/status/845743048709464064) posted on 26 March 2017, Google's Jeff Dean talked about a sparsely activated single large model with multiple tasks and outputs. It resembles Pathnet ([Fernando et al., 2017](https://arxiv.org/abs/1701.08734)) with the addition of sparsity as in [Shazeer & Mirhoseini et al. (2017)](https://arxiv.org/abs/1701.06538). When such a large architecture is viewed as a family of possible standard deep neural networks, [Veniat & Denoyer (2017)](https://arxiv.org/abs/1706.00046) demonstrates that reinforcement learning can be used to discover networks that are efficient in computational cost (Flop) or time (milliseconds).

## References

* 2017 May 31, Tom Veniat and Ludovic Denoyer. [Learning Time-Efficient Deep Architectures with Budgeted Super Networks](https://arxiv.org/abs/1706.00046). *arXiv:1706.00046*.
* 2017 April 18, Ronghang Hu, Jacob Andreas, Marcus Rohrbach, Trevor Darrell, and Kate Saenko. [Learning to Reason: End-to-End Module Networks for Visual Question Answering](https://arxiv.org/abs/1704.05526). *arXiv:1704.05526*.
* 2017 April 17, Joost Huizinga, Kenneth O. Stanley, and Jeff Clune. [The Emergence of Canalization and Evolvability in an Open-Ended, Interactive Evolutionary System](https://arxiv.org/abs/1704.05143). *arXiv:1704.05143*. [code](https://github.com/Evolving-AI-Lab/cppnx).
* 2017 March 10, Manzil Zaheer, Satwik Kottur, Siamak Ravanbhakhsh, Barnabas Poczos, Ruslan Ssalakhutdinov, and Alexander Smola. [Deep Sets](https://arxiv.org/abs/1703.06114). *arXiv:1703.06114*.
* 2017 January 30, Chrisantha Fernando, Dylan Banarse, Charles Blundell, Yori Zwols, David Ha, Andrei A. Rusu, Alexander Pritzel, and Daan Wierstra. [PathNet: Evolution Channels Gradient Descent in Super Neural Networks](https://arxiv.org/abs/1701.08734). *arXiv:1701.08734*.
* 2017 January 23, Noam Shazeer, Azalia Mirhoseini, Krzysztof Maziarz, Andy Davis, Quoc Le, Geoffrey Hinton, and Jeff Dean. [Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer](https://arxiv.org/abs/1701.06538). *arXiv:1701.06538*.
* 2016 December 22, Klaus Greff, Rupesh K. Srivastava, and Jürgen Schmidhuber. [Highway and Residual Networks learn Unrolled Iterative Estimation](https://arxiv.org/abs/1612.07771). *arXiv:1612.07771*.
* 2016 December 7, Michael Figurnov, Maxwell D. Collins, Yukun Zhu, Li Zhang, Jonathan Huang, Dmitry Vetrov, and Ruslan Salakhutdinov. [Spatially Adaptive Computation Time for Residual Networks](https://arxiv.org/abs/1612.02297). *arXiv:1612.02297*. [code](https://github.com/mfigurnov/sact).
* 2016 September 27, David Ha, Andrew Dai, and Quoc V. Le. [HyperNetworks](https://arxiv.org/abs/1609.09106). *arXiv:1609.09106*.
* 2016 September 6, Junyoung Chung, Sungjin Ahn, and Yoshua Bengio. [Hierarchical Multiscale Recurrent Neural Networks](https://arxiv.org/abs/1609.01704). *arXiv:1609.01704*.
* 2016 July 12, Julian Georg Zilly, Rupesh Kumar Srivastava, Jan Koutník, and Jürgen Schmidhuber. [Recurrent Highway Networks](https://arxiv.org/abs/1607.03474). *arXiv:1607.03474*.
* 2015 December 10, Kaiming He, Xiangyu Zhang, Shaoqing Ren, and Jian Sun. [Deep Residual Learning for Image Recognition](https://arxiv.org/abs/1512.03385). *arXiv:1512.03385*.
* 2015 July 22, Rupesh Kumar Srivastava, Klaus Greff, and Jürgen Schmidhuber. [Training Very Deep Networks](https://arxiv.org/abs/1507.06228). *arXiv:1507.06228*.

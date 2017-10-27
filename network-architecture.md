---
permalink: /network-architecture/
---
# Network Architecture

## Modular Networks
 
[Hafner et al. (2017)](https://arxiv.org/abs/1706.05744) propose ThalNet, a modular neural network inspired by neocortical communication via the thalamus. It comprises a tuple of computation modules that route their respective features into a shared center vector, which is then read selectively by each module to obtain its recurrent context input. It is shown that the model learns to route information hierarchically.

### References

* 2017 June 18, Danijar Hafner, Alex Irpan, James Davidson, and Nicolas Heess. [Learning Hierarchical Information Flow with Recurrent Neural Modules](https://arxiv.org/abs/1706.05744). *arXiv:1706.05744*.

## Conditional Computation

[Shazeer et al. (2017)](https://arxiv.org/abs/1701.06538) introduced a Sparsely-Gated Mixture-of-Experts (MoE) layer where each sample only activates a sparse subset of many expert networks, determined by a gating network. The layer is embedded in a larger architecture that is overall trainable by backpropagation.

## Evolutionary Algorithms

In an experiment evolving networks to produce patterns, [Huizinga et al. (2017)](https://arxiv.org/abs/1704.05143) showed that network weights encoded dimensions of image variations that are sensible to humans, possibly due to the diversity of environmental selection.

## Deep Feedforward Networks

[Greff et al. (2016)](https://arxiv.org/abs/1612.07771) argued that the functional blocks of Highway Networks ([Srivastava et al., 2015](https://arxiv.org/abs/1507.06228)) and Residual Networks ([He et al., 2015](https://arxiv.org/abs/1512.03385)) engage in an unrolled iterative estimation of representations. [Veit et al. (2016)](https://arxiv.org/abs/1605.06431) interpret Residual Networks as a collection of many paths of differing length. [Gomez & Ren et al. (2017)](https://arxiv.org/abs/1707.04585) present the Reversible Residual Network (RevNet) where each layer’s activations can be reconstructed from the next layer’s, eliminating the need to store activations in memory during backpropagation.

A deep feedforward network can be interrupted at an intermediate layer to make *anytime predictions*. [Hu et al. (2017)](https://arxiv.org/abs/1708.06832) add uniformly spaced auxiliary predictions and losses to the residual bottleneck units of Resnets, and achieve competitive results.

### References

* 2017 August 23, Hanzhang Hu, Debadeepta Dey, J. Andrew Bagnell, and Martial Hebert. [Anytime Neural Networks via Joint Optimization of Auxiliary Losses](https://arxiv.org/abs/1708.06832). *arXiv:1708.06832*.
* 2017 July 14, Aidan N. Gomez, Mengye Ren, Raquel Urtasun, and Roger B. Grosse. [The Reversible Residual Network: Backpropagation Without Storing Activations](https://arxiv.org/abs/1707.04585). *arXiv:1707.04585*.
* 2017 April 18, Ronghang Hu, Jacob Andreas, Marcus Rohrbach, Trevor Darrell, and Kate Saenko. [Learning to Reason: End-to-End Module Networks for Visual Question Answering](https://arxiv.org/abs/1704.05526). *arXiv:1704.05526*.
* 2017 April 17, Joost Huizinga, Kenneth O. Stanley, and Jeff Clune. [The Emergence of Canalization and Evolvability in an Open-Ended, Interactive Evolutionary System](https://arxiv.org/abs/1704.05143). *arXiv:1704.05143*. [code](https://github.com/Evolving-AI-Lab/cppnx).
* 2017 March 10, Manzil Zaheer, Satwik Kottur, Siamak Ravanbhakhsh, Barnabas Poczos, Ruslan Ssalakhutdinov, and Alexander Smola. [Deep Sets](https://arxiv.org/abs/1703.06114). *arXiv:1703.06114*.
* 2017 January 30, Chrisantha Fernando, Dylan Banarse, Charles Blundell, Yori Zwols, David Ha, Andrei A. Rusu, Alexander Pritzel, and Daan Wierstra. [PathNet: Evolution Channels Gradient Descent in Super Neural Networks](https://arxiv.org/abs/1701.08734). *arXiv:1701.08734*.
* 2017 January 23, Noam Shazeer, Azalia Mirhoseini, Krzysztof Maziarz, Andy Davis, Quoc Le, Geoffrey Hinton, and Jeff Dean. [Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer](https://arxiv.org/abs/1701.06538). *arXiv:1701.06538*.
* 2016 December 22, Klaus Greff, Rupesh K. Srivastava, and Jürgen Schmidhuber. [Highway and Residual Networks learn Unrolled Iterative Estimation](https://arxiv.org/abs/1612.07771). *arXiv:1612.07771*.
* 2016 December 7, Michael Figurnov, Maxwell D. Collins, Yukun Zhu, Li Zhang, Jonathan Huang, Dmitry Vetrov, and Ruslan Salakhutdinov. [Spatially Adaptive Computation Time for Residual Networks](https://arxiv.org/abs/1612.02297). *arXiv:1612.02297*. [code](https://github.com/mfigurnov/sact).
* 2016 December 1, David Ha, Andrew Dai, and Quoc V. Le. [HyperNetworks](https://arxiv.org/abs/1609.09106). *arXiv:1609.09106*.
* 2016 October 27, Andreas Veit, Michael Wilber, and Serge Belongie. [Residual Networks Behave Like Ensembles of Relatively Shallow Networks](https://arxiv.org/abs/1605.06431). *arXiv:1605.06431*.
* 2016 September 6, Junyoung Chung, Sungjin Ahn, and Yoshua Bengio. [Hierarchical Multiscale Recurrent Neural Networks](https://arxiv.org/abs/1609.01704). *arXiv:1609.01704*.
* 2016 July 12, Julian Georg Zilly, Rupesh Kumar Srivastava, Jan Koutník, and Jürgen Schmidhuber. [Recurrent Highway Networks](https://arxiv.org/abs/1607.03474). *arXiv:1607.03474*.
* 2015 December 10, Kaiming He, Xiangyu Zhang, Shaoqing Ren, and Jian Sun. [Deep Residual Learning for Image Recognition](https://arxiv.org/abs/1512.03385). *arXiv:1512.03385*.
* 2015 July 22, Rupesh Kumar Srivastava, Klaus Greff, and Jürgen Schmidhuber. [Training Very Deep Networks](https://arxiv.org/abs/1507.06228). *arXiv:1507.06228*.

## Capsules

Capsules are small groups of neurons that act together like a node in a layer of a deep neural network. [Sabour et al. (2017)](https://arxiv.org/abs/1710.09829) propose a dynamic routing algorithm where each capsule in the current layer computes a "prediction vector" for each possible parent in the layer above by multiplying the child capsule's own output by a weight matrix. If this prediction is in agreement with the output of the parent, these two capsules become more "coupled" in the next iteration. This routing operation iterates a few times between a pair of consecutive layers.

### References

* 2017 October 26, Sara Sabour, Nicholas Frosst, and Geoffrey E Hinton. [Dynamic Routing Between Capsules](https://arxiv.org/abs/1710.09829). *arXiv:1710.09829*.

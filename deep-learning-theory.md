---
permalink: /deep-learning-theory/
---
# Deep Learning Theory

Many of the successes in deep learning can be attributed to the availability of computing capacity and data. As of July 2017, performance of deep learning models in vision tasks still increases with orders of magnitude of training data size ([Sun et al., 2017](https://arxiv.org/abs/1707.02968)).

[Shalev-Shwartz et al. (2017)](https://arxiv.org/abs/1703.07950) described four types of simple problems that are difficult for common deep learning methods.

### References

* 2017 July 10, Chen Sun, Abhinav Shrivastava, Saurabh Singh, and Abhinav Gupta. [Revisiting Unreasonable Effectiveness of Data in Deep Learning Era](https://arxiv.org/abs/1707.02968). *arXiv:1707.02968*.
* 2017 June 5, Alessandro Achille and Stefano Soatto. [On the Emergence of Invariance and Disentangling in Deep Representations](https://arxiv.org/abs/1706.01350). *arXiv:1706.01350*.
* 2017 April 29, Ravid Shwartz-Ziv and Naftali Tishby. [Opening the Black Box of Deep Neural Networks via Information](https://arxiv.org/abs/1703.00810). *arXiv:1703.00810*. [video](https://www.youtube.com/watch?v=bLqJHjXihK8). [news](https://www.quantamagazine.org/new-theory-cracks-open-the-black-box-of-deep-learning-20170921/).
* 2017 April 26, Shai Shalev-Shwartz, Ohad Shamir, and Shaked Shammah. [Failures of Gradient-Based Deep Learning](https://arxiv.org/abs/1703.07950). *arXiv:1703.07950*.

## Information Theory

In the plane of the mutual information (MI) between input and representation and the MI between representation and output (called the Information Plane), [Schwartz-Ziv & Tishby (2017)](https://arxiv.org/abs/1703.00810) visualized SGD in two stages, error minimization and representation compression. The compression stage covers most training epochs and begins after training errors get small.

## Loss Surface Geometry

[Zhang et al. (2017)](https://arxiv.org/abs/1611.03530) demonstrate that standard learning architectures are expressive enough to fit commonly used image classification datasets such as CIFAR 10 and ImageNet with random labels or random pixels. Obviously these trained models don’t generalize to the equally random test sets. Therefore the key reasons that deep learning generalizes in practice must not be the ones that apply in the random setup. What are the reasons that cause deep models to converge to the solutions on training data that are generalizable instead of the memorization solutions that are not? Building on their work, [Arpit & Jastrzębski & Ballas & Krueger et al. (2017)](https://arxiv.org/abs/1706.05394) show that deep neural nets tend to prioritize learning simple patterns ﬁrst, and appropriately tuned explicit regularization (e.g., dropout) can degrade training performance on noise datasets without compromising generalization on real data.

[Krueger & Ballas & Jastrzebski & Arpit et al (2017)](https://openreview.net/forum?id=rJv6ZgHYg) hypothesize that this is because generalizable solutions are easier to find and observe that the sharpness around local minima increases with the level of noise. It is also well known ([Hochreiter & Schmidhuber, 1997](http://www.mitpressjournals.org/doi/abs/10.1162/neco.1997.9.1.1)) that sharp minima generalize poorly. Intuitively, this is because a local minimum for the test set likely differs slightly from the minimum for the training set. When the minima are sharp, this small difference translates to large degradation of model performance. Philosophically, a sharp minimum requires more bits to describe, thus more likely represents a wrong solution in the spirit of Occam’s razor. But rigorously, if one tries hard enough ([Dinh et al., 2017](https://arxiv.org/abs/1703.04933)), models can be built with generalizable sharp minima under most notions of sharpness. 

Maybe flat minima don’t exist in random data and are somehow easier to find than sharp ones in real data? [Keskar et al. (2017)](https://arxiv.org/abs/1609.04836) present numerical evidence that large-batch stochastic gradient descent (SGD)tends to converge to sharp minima, but small-batch methods consistently converge to flat minima, which should exist for real data given that they afford generalizable models. So a possible answer to why deep neural networks generalize is that in a large model that is expressive enough to memorize everything, the current practice of SGD can more easily locate flat minima.

### References

* 2017 June 16, Devansh Arpit, Stanisław Jastrzębski, Nicolas Ballas, David Krueger, Emmanuel Bengio, Maxinder S. Kanwal, Tegan Maharaj, Asja Fischer, Aaron Courville, Yoshua Bengio, and Simon Lacoste-Julien. [A Closer Look at Memorization in Deep Networks](https://arxiv.org/abs/1706.05394). *arXiv:1706.05394*.
* 2017 May 15, Laurent Dinh, Razvan Pascanu, Samy Bengio, and Yoshua Bengio. [Sharp Minima Can Generalize For Deep Nets](https://arxiv.org/abs/1703.04933). *arXiv:1703.04933*.
* 2017 April 21, Pratik Chaudhari, Anna Choromanska, Stefano Soatto, Yann LeCun, Carlo Baldassi, Christian Borgs, Jennifer Chayes, Levent Sagun, and Riccardo Zecchina. [Entropy-SGD: Biasing Gradient Descent Into Wide Valleys](https://arxiv.org/abs/1611.01838). *arXiv:1611.01838*.
* 2017 February 26, Chiyuan Zhang, Samy Bengio, Moritz Hardt, Benjamin Recht, and Oriol Vinyals. [Understanding deep learning requires rethinking generalization](https://arxiv.org/abs/1611.03530). *arXiv:1611.03530*.
* 2017 February 9, Nitish Shirish Keskar, Dheevatsa Mudigere, Jorge Nocedal, Mikhail Smelyanskiy, and Ping Tak Peter Tang. [On Large-Batch Training for Deep Learning: Generalization Gap and Sharp
  Minima](https://arxiv.org/abs/1609.04836). *arXiv:1609.04836*.
* 2017 February 20, David Krueger, Nicolas Ballas, Stanislaw Jastrzebski, Devansh Arpit, Maxinder S. Kanwal, Tegan Maharaj, Emmanuel Bengio, Asja Fischer, and Aaron Courville. [Deep Nets Don't Learn via Memorization](https://openreview.net/forum?id=rJv6ZgHYg). *OpenReview*.
* 2014 November 30, Anna Choromanska, Mikael Henaff, Michael Mathieu, Gérard Ben Arous, and Yann LeCun. [The Loss Surfaces of Multilayer Networks](https://arxiv.org/abs/1412.0233). *arXiv:1412.0233*.
* 1997 January 1, Sepp Hochreiter and Jürgen Schmidhuber. [Flat Minima](http://www.mitpressjournals.org/doi/abs/10.1162/neco.1997.9.1.1). *Neural Computation*, 9(1):1-42.

## Physics

[Lin et al. (2017)](https://arxiv.org/abs/1608.08225) explore how physical properties frequently translate to simple neural networks, then argue that a deep neural network could be more efficient than a shallow one when the data is generated by a hierarchical statistical process. They prove it is exponentially more efficient to approximate the product of input variables using a deep network than a shallow one. This theorem is extended in [Rolnick & Tegmark (2017)](https://arxiv.org/abs/1705.05502) to include broad natural classes of multivariate polynomials.

### References

* 2017 May 16, David Rolnick and Max Tegmark. [The power of deeper networks for expressing natural functions](https://arxiv.org/abs/1705.05502). *arXiv:1705.05502*.
* 2017 May 2, Henry W. Lin, Max Tegmark, and David Rolnick. [Why does deep and cheap learning work so well?](https://arxiv.org/abs/1608.08225). *arXiv:1608.08225*.
* 2017 April 5, Yoav Levine, David Yakira, Nadav Cohen, and Amnon Shashua. [Deep Learning and Quantum Physics : A Fundamental Bridge](https://arxiv.org/abs/1704.01552). *arXiv:1704.01552*.

## Topology

* 2014 January 6, Monica Bianchini and Franco Scarselli. [On the Complexity of Neural Network Classifiers: A Comparison Between Shallow and Deep Architectures](http://ieeexplore.ieee.org/document/6697897/). *IEEE Transactions on Neural Networks and Learning Systems*, 25(8):1553-1565.

## Transparency

[Weller (2017)](https://openreview.net/forum?id=SJR9L5MQ-) provides a brief survey on transparency and reviews settings where it may be unhelpful.

### Cognitive Psychology

[Ritter & Barrett et al. (2017)](https://arxiv.org/abs/1706.08606) use cognitive psychology to study the one-shot word learning Matching Networks and an Inception Baseline model. They find that the networks prefer to categorize objects according to shape rather than color.

### References

* 2017 July 4, Adrian Weller. [Challenges for Transparency](https://openreview.net/forum?id=SJR9L5MQ-). *OpenReview*.
* 2017 June 26, Samuel Ritter, David G. T. Barrett, Adam Santoro, and Matt M. Botvinick. [Cognitive Psychology for Deep Neural Networks: A Shape Bias Case Study](https://arxiv.org/abs/1706.08606). *arXiv:1706.08606*.

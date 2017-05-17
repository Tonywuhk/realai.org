---
permalink: /automated-theorem-proving/
---
# Automated Theorem Proving

Automated Theorem Proving (ATP) is about proving math theorems automatically. In June 2016, it was demonstrated for the first time ([Alemi et al., (2016)](https://arxiv.org/abs/1606.04442)) that neural networks are useful in large scale ATP. Two months later, [Whalen (2016)](https://arxiv.org/abs/1608.02644) proposed a complete architecture combining deep learning and tree search for the [Metamath](http://us.metamath.org/) system. Deep learning was incorporated by [Loos et al. (2017)](https://arxiv.org/abs/1701.06972) into the proof search procedure of the [E Theorem Prover](http://wwwlehre.dhbw-stuttgart.de/~sschulz/E/E.html) in January 2017. In March, [Kaliszyk et al. (2017)](https://arxiv.org/abs/1703.00426) introduced a [HOL Light](https://www.cl.cam.ac.uk/~jrh13/hol-light/) dataset to the public.

## Metamath

Metamath is a formal math system started by Norman Megill in 1992, and has been under continuous development since then. It has a small community of users that are active on [Google Group](http://groups.google.com/group/metamath). Over 19,000 proofs have been worked out in Metamath, including some [well known theorems](http://us.metamath.org/mpegif/mmset.html#theorems). [Metamath 100](http://us.metamath.org/mm_100.html) currently lists 63 proofs for [“top 100” theorems](http://www.cs.ru.nl/~freek/100/) maintained by [Freek Wiedijk](http://www.cs.ru.nl/~freek/), behind more popular systems HOL Light (86), Isabelle (74) and Mizar (65). An algorithm has been proposed by [Carneiro (2015)](https://arxiv.org/abs/1412.8091) to convert HOL Light proofs into Metamath, but it is not yet implemented.

Metamath is built for extreme simplicity. It has only one rule, substitution, that replaces symbols with various expressions. Starting with the well-known Zermelo-Frankel set theory with choice, all of math (that most people care about) follows. The flipside of simplicity is long and tedious proofs. The proof of “2+2=4” is a theorem named [2p2e4](http://us.metamath.org/mpegif/2p2e4.html) that has 10 steps, all of which can be expanded further into more basic blocks such as [df-2](http://us.metamath.org/mpegif/df-2.html), the definition of “2”. All proof steps can be mechanically followed without any semantic understanding of math. This is better experienced when readers follow a proof with unfamiliar symbols, such as [aleph1re](http://us.metamath.org/mpegif/aleph1re.html), and can be really confusing when symbols in referenced theorems overlaps with those in the main proof ([id1](http://us.metamath.org/mpegif/id1.html)). [Metamath Proof Explorer Home Page](http://us.metamath.org/mpegif/mmset.html) is an excellent tutorial.

## References

* 2017 March 1, Cezary Kaliszyk, François Chollet, and Christian Szegedy. [HolStep: A Machine Learning Dataset for Higher-order Logic Theorem Proving](https://arxiv.org/abs/1703.00426). *arXiv:1703.00426*. [code](https://github.com/tensorflow/deepmath/tree/master/deepmath/holstep_baselines). [site](http://cl-informatik.uibk.ac.at/cek/holstep/).
* 2017 January 24, Sarah Loos, Geoffrey Irving, Christian Szegedy, and [Cezary Kaliszyk](http://cl-informatik.uibk.ac.at/cek/). [Deep Network Guided Proof Search](https://arxiv.org/abs/1701.06972). *arXiv:1701.06972*.
* 2016 August 10, Daniel Whalen. [Holophrasm: a neural Automated Theorem Prover for higher-order logic](https://arxiv.org/abs/1608.02644). *arXiv:1608.02644*. [code](https://github.com/dwhalen/holophrasm) ([release](https://github.com/dwhalen/holophrasm/releases)).
* 2016 June 14, Alex A. Alemi, Francois Chollet, Niklas Een, Geoffrey Irving, Christian Szegedy, and Josef Urban. [DeepMath - Deep Sequence Models for Premise Selection](https://arxiv.org/abs/1606.04442). *arXiv:1606.04442*.
* 2015 June 18, Mario Carneiro. [Conversion of HOL Light proofs into Metamath](https://arxiv.org/abs/1412.8091). *arXiv:1412.8091*.

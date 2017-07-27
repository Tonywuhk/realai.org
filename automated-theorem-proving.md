---
permalink: /automated-theorem-proving/
redirect_from: /ATP/
---
# Automated Theorem Proving

From counting to Clay Mathematics Institute's [Millennium Problems](http://www.claymath.org/millennium-problems), the [mathematics trench](https://i.imgur.com/muXx1kp.jpg) is incredibly deep. Automated Theorem Proving (ATP) is about proving math theorems automatically. In June 2016, it was demonstrated for the first time ([Alemi et al., (2016)](https://arxiv.org/abs/1606.04442)) that neural networks are useful in large scale ATP. Two months later, [Whalen (2016)](https://arxiv.org/abs/1608.02644) proposed a complete architecture combining deep learning and tree search for the [Metamath](http://realai.org/metamath/) system. Deep learning was incorporated by [Loos et al. (2017)](https://arxiv.org/abs/1701.06972) into the proof search procedure of the [E Theorem Prover](http://wwwlehre.dhbw-stuttgart.de/~sschulz/E/E.html) in January 2017. In March, [Kaliszyk et al. (2017)](https://arxiv.org/abs/1703.00426) introduced a [HOL Light](https://www.cl.cam.ac.uk/~jrh13/hol-light/) dataset to the public.

## Resources

* [Conferences](http://realai.org/resources/conferences/): AITP ([2017](http://aitp-conference.org/2017/), [2016](http://aitp-conference.org/2016/)), LPAR ([2017](http://easychair.org/smart-program/LPAR-21/LPAR-index.html)).
* The [Deepmath](https://github.com/tensorflow/deepmath) project is a collaboration between Google Research and several universities that seeks to improve automated theorem proving using deep learning and other machine learning techniques.

## References

* 2017 March 1, Cezary Kaliszyk, François Chollet, and Christian Szegedy. [HolStep: A Machine Learning Dataset for Higher-order Logic Theorem Proving](https://arxiv.org/abs/1703.00426). *arXiv:1703.00426*. [code](https://github.com/tensorflow/deepmath/tree/master/deepmath/holstep_baselines). [site](http://cl-informatik.uibk.ac.at/cek/holstep/).
* 2017 January 24, Sarah Loos, Geoffrey Irving, Christian Szegedy, and [Cezary Kaliszyk](http://cl-informatik.uibk.ac.at/cek/). [Deep Network Guided Proof Search](https://arxiv.org/abs/1701.06972). *arXiv:1701.06972*.
* 2016 August 10, Daniel Whalen. [Holophrasm: a neural Automated Theorem Prover for higher-order logic](https://arxiv.org/abs/1608.02644). *arXiv:1608.02644*. [code](https://github.com/dwhalen/holophrasm) ([release](https://github.com/dwhalen/holophrasm/releases)).
* 2016 June 14, Alex A. Alemi, Francois Chollet, Niklas Een, Geoffrey Irving, Christian Szegedy, and Josef Urban. [DeepMath - Deep Sequence Models for Premise Selection](https://arxiv.org/abs/1606.04442). *arXiv:1606.04442*.


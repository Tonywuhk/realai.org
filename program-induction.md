---
permalink: /program-induction/
---
# Program Induction

The capability of inducing programs is a key to solving AI.

[Neelakantan et al. (2015)](https://arxiv.org/abs/1511.04834) proposed *Neural Programmer*, a neural network augmented with discrete operations that can be trained end-to-end. The model performed well on a synthetic dataset, and was enhanced in [Neelakantan et al. (2016)](https://arxiv.org/abs/1611.08945) to map natural language queries to executable programs on a database.

[Ling et al. (2017)](https://arxiv.org/abs/1705.04146) built a model to generate human-readable answer *rationales* that led to correct answers to algebraic word problems. Frequently used math operations such as `Log` and `Sine` are provided to the model. They combined techniques from sequence to sequence framework, program generation, and made use of pointer networks to attend to input and output tokens stored in memory.

[Ellis et al. (2017)](https://arxiv.org/abs/1707.09627) learn a CNN that proposes plausible drawing primitives to explain an image, which are then synthesized into programs by a state-of-the-art Sketch tool.

[Becker & Gottschlich (2017)](https://arxiv.org/abs/1709.05703) use genetic algorithms to create software programs in [Brainfuck](https://en.wikipedia.org/wiki/Brainfuck), an esoteric programming language. More materials can be found in the first author's blog posts ([Part 1](http://www.primaryobjects.com/2013/01/27/using-artificial-intelligence-to-write-self-modifying-improving-programs/), [Part 2](http://www.primaryobjects.com/2013/03/04/pushing-the-limits-of-self-programming-artificial-intelligence/), and [Part 3](http://www.primaryobjects.com/2015/01/05/self-programming-artificial-intelligence-learns-to-use-functions/)) in 2013 and 2015.

## References

* 2017 September 17, Kory Becker and Justin Gottschlich. [AI Programmer: Autonomously Creating Software Programs Using Genetic Algorithms](https://arxiv.org/abs/1709.05703). *arXiv:1709.05703*.
* 2017 August 1, Kevin Ellis, Daniel Ritchie, Armando Solar-Lezama, and Joshua B. Tenenbaum. [Learning to Infer Graphics Programs from Hand-Drawn Images](https://arxiv.org/abs/1707.09627). *arXiv:1707.09627*.
* 2017 May 11, Wang Ling, Dani Yogatama, Chris Dyer, and Phil Blunsom. [Program Induction by Rationale Generation: Learning to Solve and Explain Algebraic Word Problems](https://arxiv.org/abs/1705.04146). *arXiv:1705.04146*.
* 2017 April 21, Jonathon Cai, Richard Shin, and Dawn Song. [Making Neural Programming Architectures Generalize via Recursion](https://arxiv.org/abs/1704.06611). *arXiv:1704.06611*.
* 2016 November 28, Arvind Neelakantan, Quoc V. Le, Martin Abadi, Andrew McCallum, and Dario Amodei. [Learning a Natural Language Interface with Neural Programmer](https://arxiv.org/abs/1611.08945). *arXiv:1611.08945*.
* 2015 November 23, Wojciech Zaremba, Tomas Mikolov, Armand Joulin, and Rob Fergus. [Learning Simple Algorithms from Examples](https://arxiv.org/abs/1511.07275). *arXiv:1511.07275*.
* 2015 November 19, Scott Reed and Nando de Freitas. [Neural Programmer-Interpreters](https://arxiv.org/abs/1511.06279). *arXiv:1511.06279*.
* 2015 November 16, Arvind Neelakantan, Quoc V. Le, and Ilya Sutskever. [Neural Programmer: Inducing Latent Programs with Gradient Descent](https://arxiv.org/abs/1511.04834). *arXiv:1511.04834*.

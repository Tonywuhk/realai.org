---
permalink: /symbol-grounding/
---
# Symbol Grounding

Language is a tool of communication in which words (symbols) trigger thoughts in the brains of the communicators. These thoughts are complex, vary across people, and contain a lot more information than can be practically encoded in the symbols. In order to use a language effectively, a computer system needs to ground its symbols into their semantic meanings that humans intuitively understand. This is called the symbol grounding problem ([Harnad 1990](http://www.sciencedirect.com/science/article/pii/0167278990900876)).

[Hermann & Hill et al. (2017)](https://arxiv.org/abs/1706.06551) train an agent that learned simple English that is grounded in its embodied experience in a simulated 3D world. It is a reinforcement learning agent trained using A3C with auxiliary tasks to predict its visual perception and instruction to be received. The architecture is a modular network where visual input is encoded by a convolution net, and language is encoded by a recurrent net. A mixing module combines visual and language signals and passes them to an action module. Learning in the agent reflects various effects that are characteristic of human development, such as rapidly accelerating rates of vocabulary growth, the ability to learn from both rewarded interactions and predictions about the world, a natural tendency to generalise and re-use semantic knowledge, and improved outcomes when learning is moderated by curricula. Concurrently, [Denil et al. (2017)](https://arxiv.org/abs/1706.06383) and [Chaplot et al. (2017)](https://arxiv.org/abs/1706.07230) also propose models where agents ground language in their environments.

[Garnelo et al. (2016)](https://arxiv.org/abs/1609.05518) proposed an end-to-end reinforcement learning architecture where a neural back end must learn a symbolic representation of its raw data to communicate with the front end.

## References

* 2017 June 22, Devendra Singh Chaplot, Kanthashree Mysore Sathyendra, Rama Kumar Pasumarthi, Dheeraj Rajagopal, and Ruslan Salakhutdinov. [Gated-Attention Architectures for Task-Oriented Language Grounding](https://arxiv.org/abs/1706.07230). *arXiv:1706.07230*. [site](https://sites.google.com/view/gated-attention/home).
* 2017 June 20, Karl Moritz Hermann, Felix Hill, Simon Green, Fumin Wang, Ryan Faulkner, Hubert Soyer, David Szepesvari, Wojtek Czarnecki, Max Jaderberg, Denis Teplyashin, Marcus Wainwright, Chris Apps, Demis Hassabis, and Phil Blunsom. [Grounded Language Learning in a Simulated 3D World](https://arxiv.org/abs/1706.06551). *arXiv:1706.06551*. [video](https://www.youtube.com/watch?v=wJjdu1bPJ04) uploaded on 7 April 2017.
* 2017 June 20, Misha Denil, Sergio Gómez Colmenarejo, Serkan Cabi, David Saxton, and Nando de Freitas. [Programmable Agents](https://arxiv.org/abs/1706.06383). *arXiv:1706.06383*. [video](https://www.youtube.com/playlist?list=PLs1LSEoK_daRDnPUB2u7VAXSonlNU7IcV).
* 2016 September 18, Marta Garnelo, Kai Arulkumaran, and Murray Shanahan. [Towards Deep Symbolic Reinforcement Learning](https://arxiv.org/abs/1609.05518). *arXiv:1609.05518*.
* 1990 June, Stevan Harnad. [The Symbol Grounding Problem](http://www.sciencedirect.com/science/article/pii/0167278990900876). *Physica D: Nonlinear Phenomena*, 42(1-3):335-346. [html](http://users.ecs.soton.ac.uk/harnad/Papers/Harnad/harnad90.sgproblem.html).

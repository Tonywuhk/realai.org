---
permalink: /research/
---
# Research

This is where the [Home](http://realai.org) section of this site meets the [About](http://realai.org/about/) section. We will document our own results that are not yet covered by existing literature. Our research is aimed at building an AGI system and will be guided by knowledge-based [big-picture understanding](http://realai.org/background/) of intelligence, regardless of its near-term publication potential. We expect that many of our results won't be publishable by today's academic standard, because "the bar is quite high for a general system to be able to beat specialized systems" whose performance can be easily honed for a given task ([Vincent, 2017](https://www.theverge.com/2017/7/19/15998610/ai-neuroscience-machine-learning-deepmind-demis-hassabis-interview)). When determining where to allocate resources most productively, if a non-publishable result shows signs of promise consistent with our understanding of intelligence, even if it doesn't attain state-of-the-art performance, we're likely to redouble engineering efforts geared to making it work. This strategy is also advocated in [Hassabis et al. (2017)](http://www.cell.com/neuron/fulltext/S0896-6273(17)30509-3).

## System Requirements

As of September 2017, our concept of an AGI system is a [chatbot](http://realai.org/chatbot/) capable of common sense [reasoning](http://realai.org/reasoning/) with the abilities to communicate with its users in [natural language](http://realai.org/natural-language-processing/) and to access the Internet. Such a system is referred to as an [oracle](http://realai.org/safety/oracle-ai/) in the field of [AI safety](http://realai.org/safety/). As a small research company constrained by human and financial resources, we will focus on the most essential aspects of general intelligence. For example, we're unlikely to work on a shiny graphical user interface before our text-based chatbot can talk sensibly, let alone building robots with highly realistic appearances. We design our system with the balance in mind to support flexible working conditions without losing the ability to scale when the demand of large computational complexity arises. We rely on open-source libraries and commoditized IT systems as much as possible.

* Hardware: [Windows](http://realai.org/course/windows/)-based PC, laptop, or [(Google) cloud](http://realai.org/course/google-cloud-platform/) computers
* Operating System: [Ubuntu](http://realai.org/course/ubuntu/)
* Programming Language: [Python 3](http://realai.org/course/python/) (managed by [Conda](http://realai.org/course/conda/))
* Development Environment: [Jupyter](http://realai.org/course/jupyter/), tmux and [vim](course/system/vim.md)
* Documentation: realai.org [viewed on the web](http://realai.org/), a Jekyll site on [GitHub](course/system/github.md)
* Source: realai.org [viewed on GitHub](https://github.com/real-ai/realai.org)
* Deep Learning Library: PyTorch

This setup is subject to change over time, but it is likely a satisfactory package that allows our contributors to have a largely consistent development experience across a wide range of working conditions.

## Reinforcement Learning

Modern (as of September 2017) [reinforcement learning](http://realai.org/course/reinforcement-learning/) (RL) is based on maximizing the expected value of reward an agent can accumulate over its future ([Sutton & Barto, 2017](http://incompleteideas.net/sutton/book/the-book-2nd.html)). It is only consistent with, but *not* equivalent to, the classic principles of utility theory, which is already based on unrealistic assumptions on human preferences. An RL theory for the purpose of AGI development needs to be flexible enough to accommodate complex human behavior, and likely will be framed in a way different from its current form. Promising developments such as successor representation ([Momennejad & Russek et al., 2017](http://www.biorxiv.org/content/early/2017/07/04/083824)) and value distribution ([Bellemare, Dabney & Munos, 2017](https://arxiv.org/abs/1707.06887)) already point to this direction. One of our research topics is a more suitable RL foundation for AGI. We think this version of RL will be mathematically less rigorous in terms of solving the original reward maximization problem, but better grounded in [neuroscience](http://realai.org/background/neuroscience/) and [philosophy](http://realai.org/background/philosophy/).

## References

* 2017 July 21, Marc G. Bellemare, Will Dabney, and Rémi Munos. [A Distributional Perspective on Reinforcement Learning](https://arxiv.org/abs/1707.06887). *arXiv:1707.06887*. [video](http://youtu.be/yFBwyPuO2Vg). [blog](https://deepmind.com/blog/going-beyond-average-reinforcement-learning/).
* 2017 July 19, James Vincent. [DeepMind's founder says to build better computer brains, we need to look at our own](https://www.theverge.com/2017/7/19/15998610/ai-neuroscience-machine-learning-deepmind-demis-hassabis-interview). *The Verge*.
* 2017 July 19, Demis Hassabis, Dharshan Kumaran, Christopher Summerfield, and Matthew Botvinick. [Neuroscience-Inspired Artificial Intelligence](http://www.cell.com/neuron/fulltext/S0896-6273(17)30509-3). *Neuron*, 95(2):245-258. [PDF](https://deepmind.com/documents/113/Neuron.pdf). [interview](https://www.theverge.com/2017/7/19/15998610/ai-neuroscience-machine-learning-deepmind-demis-hassabis-interview). [blog](https://deepmind.com/blog/ai-and-neuroscience-virtuous-circle/).
* 2017 July 4, Ida Momennejad, Evan M. Russek, Jin H. Cheong, Matthew M. Botvinick, Nathaniel Daw, and Samuel J. Gershman. [The successor representation in human reinforcement learning](http://www.biorxiv.org/content/early/2017/07/04/083824). *bioRxiv:083824*.
* 2016 September, Richard S. Sutton and Andrew G. Barto. [Reinforcement Learning: An Introduction](http://incompleteideas.net/sutton/book/the-book-2nd.html), Second Edition, in progress. *The MIT Press*. [PDF](http://incompleteideas.net/sutton/book/bookdraft2016sep.pdf).



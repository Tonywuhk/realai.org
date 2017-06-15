---
permalink: /games/
mathjax: true
---
# Games

## Atari 2600

On the Atari game Ms. Pac-Man, a reinforcement learning agent using the Hybrid Reward Architecture (HRA) achieved the maximum possible score of 999,990 points in less than 3,000 episodes ([van Seijen et al., 2017](https://arxiv.org/abs/1706.04208)). The overall \\(Q\\)-value function in the HRA is a weighted sum of individual \\(Q\\)-value functions whose weights correspond to in-game rewards for eating a pellet, blue ghost or fruit. The weights for Ms. Pac-Man to lose a life are set to -1,000.

In June 2017, Wired [reported](https://www.wired.com/story/vicarious-schema-networks-artificial-intelligence-atari-demo/) that AI company [Vicarious](https://www.vicarious.com/) developed Schema Networks. In [Kansky et al. (2017)](https://arxiv.org/abs/1706.04317), specific Schema Networks are designed for the Atari game Breakout, and after training, they outperform the general learning algorithms [A3C](http://realai.org/rl/model-free/) in several variations of Breakout.

### References

* 2017 June 14, Ken Kansky, Tom Silver, David A. Mély, Mohamed Eldawy, Miguel Lázaro-Gredilla, Xinghua Lou, Nimrod Dorfman, Szymon Sidor, Scott Phoenix, and Dileep George. [Schema Networks: Zero-shot Transfer with a Generative Causal Model of Intuitive Physics](https://arxiv.org/abs/1706.04317). *arXiv:1706.04317*. [blog](https://www.vicarious.com/general-game-playing-with-schema-networks.html).
* 2017 June 13, Harm van Seijen, Mehdi Fatemi, Joshua Romoff, Romain Laroche, Tavian Barnes, and Jeffrey Tsang. [Hybrid Reward Architecture for Reinforcement Learning](https://arxiv.org/abs/1706.04208). *arXiv:1706.04208*. [blog](http://www.maluuba.com/hra).

## Starcraft

* 2017 April 19, Justesen and Risi. [Continual Online Evolutionary Planning for In-Game Build Order Adaptation in StarCraft](http://sebastianrisi.com/wp-content/uploads/justesen_gecco17.pdf). *Proceedings of the Conference on Genetic and Evolutionary Computation (GECCO)*.
* 2017 March 29, Peng Peng, Quan Yuan, Ying Wen, Yaodong Yang, Zhenkun Tang, Haitao Long, and Jun Wang. [Multiagent Bidirectionally-Coordinated Nets for Learning to Play StarCraft Combat Games](https://arxiv.org/abs/1703.10069). *arXiv:1703.10069*.
* 2017 February 28, Jakob Foerster, Nantas Nardelli, Gregory Farquhar, Philip. H. S. Torr, Pushmeet Kohli, and Shimon Whiteson. [Stabilising Experience Replay for Deep Multi-Agent Reinforcement Learning](https://arxiv.org/abs/1702.08887). *arXiv:1702.08887*.
* 2016 September 10, Nicolas Usunier, Gabriel Synnaeve, Zeming Lin, and Soumith Chintala. [Episodic Exploration for Deep Deterministic Policies: An Application to StarCraft Micromanagement Tasks](https://arxiv.org/abs/1609.02993). *arXiv:1609.02993*.

The [StarCraft AI Competition](http://www.cs.mun.ca/~dchurchill/starcraftaicomp/) ([history](http://www.cs.mun.ca/~dchurchill/starcraftaicomp/history.shtml)) is organized by the [RTS Game AI Research Group](https://skatgame.net/mburo/) at the University of Alberta and sponsored by [AIIDE](http://aiide.org/) - AI and Interactive Digital Entertainment.

## Poker

Texas Hold'em Poker is a family of games that exhibit imperfect information, where players do not have full knowledge of past events. [Bowling et al. (2015)](http://science.sciencemag.org/content/347/6218/145) essentially weakly solved the heads-up limit version of the game. Using deep learning, [Moravčík & Schmid et al. (2017)](https://arxiv.org/abs/1701.01724) built a system that defeated professional players in the heads-up no-limit version. One of its co-authors, Michael Bowling, estimated in a [tweet](https://twitter.com/MichaelHBowling/status/838426697817067520) on 6 March 2017 that computer will beat pros at multi-player level in "a couple years".

## Go

## References

* 2017 March 10, Tim Salimans, Jonathan Ho, Xi Chen, and Ilya Sutskever. [Evolution Strategies as a Scalable Alternative to Reinforcement Learning](https://arxiv.org/abs/1703.03864). *arXiv:1703.03864*.
* 2017 January 6, Matej Moravčík, Martin Schmid, Neil Burch, Viliam Lisý, Dustin Morrill, Nolan Bard, Trevor Davis, Kevin Waugh, Michael Johanson, and Michael Bowling. [DeepStack: Expert-Level Artificial Intelligence in No-Limit Poker](https://arxiv.org/abs/1701.01724). *arXiv:1701.01724*.
* 2016 February 4, Volodymyr Mnih, Adrià Puigdomènech Badia, Mehdi Mirza, Alex Graves, Timothy P. Lillicrap, Tim Harley, David Silver, and Koray Kavukcuoglu. [Asynchronous Methods for Deep Reinforcement Learning](https://arxiv.org/abs/1602.01783). *arXiv:1602.01783*.
* 2015 November 11, David Silver, Aja Huang, Chris J. Maddison, Arthur Guez, Laurent Sifre, George van den Driessche, Julian Schrittwieser, Ioannis Antonoglou, Veda Panneershelvam, Marc Lanctot, Sander Dieleman, Dominik Grewe, John Nham, Nal Kalchbrenner, Ilya Sutskever, Timothy Lillicrap, Madeleine Leach, Koray Kavukcuoglu, Thore Graepel, and Demis Hassabis. [Mastering the game of Go with deep neural networks and tree search](http://www.nature.com/nature/journal/v529/n7587/full/nature16961.html). *Nature*, 529(7587):484-489.
* 2015 January 9, Michael Bowling, Neil Burch, Michael Johanson, and Oskari Tammelin. [Heads-up limit hold’em poker is solved](http://science.sciencemag.org/content/347/6218/145). *Science*, 347(6218):145-149.
* 2014 July 10, Volodymyr Mnih,	Koray Kavukcuoglu, David Silver, Andrei A. Rusu, Joel Veness, Marc G. Bellemare, Alex Graves, Martin Riedmiller, Andreas K. Fidjeland, Georg Ostrovski, Stig Petersen, Charles Beattie, Amir Sadik, Ioannis Antonoglou, Helen King, Dharshan Kumaran, Daan Wierstra, Shane Legg, and Demis Hassabis. [Human-level control through deep reinforcement learning](http://www.nature.com/nature/journal/v518/n7540/abs/nature14236.html). *Nature*, 518(7450):529-533.
* 2013 December 19, Volodymyr Mnih, Koray Kavukcuoglu, David Silver, Alex Graves, Ioannis Antonoglou, Daan Wierstra, and Martin Riedmiller. [Playing Atari with Deep Reinforcement Learning](https://arxiv.org/abs/1312.5602). *arXiv:1312.5602*.

---
permalink: /DRL/environments/
mathjax: true
---
# Environments

Deep reinforcement learning ([DRL](README.md)) agents learn from interactions with the environments. Intuitively, training a sophisticated agent requires high complexity in its training input, which can come from environmental dynamics as well as other agents' behavior. Since 2013, DRL environments have become increasingly more complex, often encompassing [multiple agents](multi-agent-learning.md) participating in a diverse range of tasks.

## OpenAI Gym

[OpenAI Gym](https://github.com/openai/gym) is a toolkit for developing and comparing RL algorithms. It supports teaching agents everything from walking to playing games like Pong or Go. OpenAI Gym depends on [MuJoCo](http://www.mujoco.org/) an advanced physics simulation engine that [costs money](https://www.roboti.us/license.html). As of [September 2017](https://github.com/openai/gym/issues/717#issuecomment-329282160), PyBullet is being developed at Google Brain that can be used in Gym environments.

Following [the closure of OpenAI Gym's website](https://www.reddit.com/r/MachineLearning/comments/6zvlm2/d_openai_closing_down_gym_toolkit_website/) in September 2017, [Montréal.AI](http://www.montreal.ai/) offered in a [tweet](https://twitter.com/Montreal_AI/status/908108070026399745) to maintain the website and create an enhanced version of OpenAI Gym.

OpenAI's [Universe](https://universe.openai.com/) is a software platform for measuring and training AI across many games, websites and other applications. As of June 2017, there is an attempt to [remake Universe](https://blog.aqnichol.com/2017/06/11/why-im-remaking-openai-universe/) that avoids Flash and VNC. A bunch of HTML5 games are wrapped in a single API in project [μniverse](https://github.com/unixpickle/muniverse).

* 2016 December 5. [Universe](https://blog.openai.com/universe/). *OpenAI*.
* 2016 April 27. [OpenAI Gym Beta](https://blog.openai.com/openai-gym-beta/). *OpenAI*.

## Physics Simulations

**Pybullet** is the official Python Interface for the [Bullet Physics SDK](https://github.com/bulletphysics/bullet3) Robotics Simulator. As of August 29, 2017, pybullet 1.2.9 is [available on PyPI](https://pypi.python.org/pypi/pybullet). Its homepage redirects to a [quickstart guide](http://pybullet.org) hosted on Google Docs.

[DeepMind Lab](https://github.com/deepmind/lab) is a 3D learning environment based on the [Quake III Arena](https://github.com/id-Software/Quake-III-Arena).

On 15 February 2017, Microsoft [announced](https://blogs.microsoft.com/next/2017/02/15/microsoft-shares-open-source-system-training-drones-gadgets-move-safely/) the [Aerial Informatics and Robotics Platform](https://www.microsoft.com/en-us/research/project/aerial-informatics-robotics-platform/), also known as AirSim ([Shah et al., 2017](https://arxiv.org/abs/1705.05065)). It is an [open-source](https://github.com/Microsoft/AirSim), high-fidelity physics and photo-realistic robot simulator that aims to narrow the gap between simulation and reality in order to aid development of autonomous vehicles.

### References

* 2017 May 15, Shital Shah, Debadeepta Dey, Chris Lovett, and Ashish Kapoor. [AirSim: High-Fidelity Visual and Physical Simulation for Autonomous Vehicles](https://arxiv.org/abs/1705.05065). *arXiv:1705.05065*.
* 2016 December 3. [Open-sourcing DeepMind Lab](https://deepmind.com/blog/open-sourcing-deepmind-lab/). *DeepMind*.

## Games

Deep learning methods have been applied to games of various genres such as arcade, open-world, real-time strategy, board, and text-based games. Prominent examples include [Atari 2600 games](#the-arcade-learning-environment), [StarCraft](#starcraft), [Dota 2](#dota-2), [Poker](#poker), and [Go](#go). In many arcade games, deep learning has achieved above human-level performance.

### Video Games

#### Recent Review

* 2017 August 26, Niels Justesen, Philip Bontrager, Julian Togelius, and Sebastian Risi. [Deep Learning for Video Game Playing](https://arxiv.org/abs/1708.07902). *arXiv:1708.07902*.

#### Unity ML Agents

[Unity Machine Learning Agents](https://github.com/Unity-Technologies/ml-agents) allows researchers and developers to create games and simulations using the [Unity Editor](https://unity3d.com/unity/editor) which serve as environments where intelligent agents can be trained through a Python API. It was [introduced in September 2017](https://blogs.unity3d.com/2017/09/19/introducing-unity-machine-learning-agents/) by [Unity Technologies](https://unity3d.com/), the developer of [the leading global game industry software](https://unity3d.com/public-relations). Unity was reportedly [worth $2.6 billion](https://venturebeat.com/2017/05/25/why-unity-was-able-to-raise-400-million-at-a-2-6-billion-valuation/) as of May 2017.

In an earlier [blog post](https://blogs.unity3d.com/2017/06/26/unity-ai-themed-blog-entries/), it was stated that Unity believed the progress in deep learning was going to change how games were built, from the generation of texture and 3D-models, to the programming of non playable characters.

#### The Arcade Learning Environment

[The Arcade Learning Environment](https://github.com/mgbellemare/Arcade-Learning-Environment) (ALE) is a simple object-oriented framework that allows researchers and hobbyists to develop AI agents for [Atari 2600](https://en.wikipedia.org/wiki/Atari_2600) games. It was introduced by [Bellemare et al. (2013)](https://arxiv.org/abs/1207.4708) in July 2012.

##### Recent Review

* 2017 September 18, Marlos C. Machado, Marc G. Bellemare, Erik Talvitie, Joel Veness, Matthew Hausknecht, and Michael Bowling. [Revisiting the Arcade Learning Environment: Evaluation Protocols and Open Problems for General Agents](https://arxiv.org/abs/1709.06009). *arXiv:1709.06009*.

##### Results

On the Atari game Ms. Pac-Man, a reinforcement learning agent using the Hybrid Reward Architecture (HRA) achieved the maximum possible score of 999,990 points in less than 3,000 episodes ([van Seijen et al., 2017](https://arxiv.org/abs/1706.04208)). The overall \\(Q\\)-value function in the HRA is a weighted sum of individual \\(Q\\)-value functions whose weights correspond to in-game rewards for eating a pellet, blue ghost or fruit. The weights for Ms. Pac-Man to lose a life are set to -1,000. An *executive memory* records every sequence of actions that pass a level without any kill, so that they can be used for the same level. This particular technique contributes to achieving the maximum possible score, but does not generalize. It received a [negative review](https://www.theregister.co.uk/2017/06/15/microsoft_pac_man/) on The Register.

In June 2017, Wired [reported](https://www.wired.com/story/vicarious-schema-networks-artificial-intelligence-atari-demo/) that AI company [Vicarious](https://www.vicarious.com/) developed Schema Networks. In [Kansky et al. (2017)](https://arxiv.org/abs/1706.04317), specific Schema Networks are designed for the Atari game Breakout, and after training, they outperform the general [learning algorithms](learning-algorithms.md) A3C in several variations of Breakout.

##### References

* 2017 June 14, Ken Kansky, Tom Silver, David A. Mély, Mohamed Eldawy, Miguel Lázaro-Gredilla, Xinghua Lou, Nimrod Dorfman, Szymon Sidor, Scott Phoenix, and Dileep George. [Schema Networks: Zero-shot Transfer with a Generative Causal Model of Intuitive Physics](https://arxiv.org/abs/1706.04317). *arXiv:1706.04317*. [blog](https://www.vicarious.com/general-game-playing-with-schema-networks.html).
* 2017 June 13, Harm van Seijen, Mehdi Fatemi, Joshua Romoff, Romain Laroche, Tavian Barnes, and Jeffrey Tsang. [Hybrid Reward Architecture for Reinforcement Learning](https://arxiv.org/abs/1706.04208). *arXiv:1706.04208*. [blog](http://www.maluuba.com/hra).
* 2017 March 10, Tim Salimans, Jonathan Ho, Xi Chen, and Ilya Sutskever. [Evolution Strategies as a Scalable Alternative to Reinforcement Learning](https://arxiv.org/abs/1703.03864). *arXiv:1703.03864*.
* 2016 February 4, Volodymyr Mnih, Adrià Puigdomènech Badia, Mehdi Mirza, Alex Graves, Timothy P. Lillicrap, Tim Harley, David Silver, and Koray Kavukcuoglu. [Asynchronous Methods for Deep Reinforcement Learning](https://arxiv.org/abs/1602.01783). *arXiv:1602.01783*.
* 2014 July 10, Volodymyr Mnih,	Koray Kavukcuoglu, David Silver, Andrei A. Rusu, Joel Veness, Marc G. Bellemare, Alex Graves, Martin Riedmiller, Andreas K. Fidjeland, Georg Ostrovski, Stig Petersen, Charles Beattie, Amir Sadik, Ioannis Antonoglou, Helen King, Dharshan Kumaran, Daan Wierstra, Shane Legg, and Demis Hassabis. [Human-level control through deep reinforcement learning](http://www.nature.com/nature/journal/v518/n7540/abs/nature14236.html). *Nature*, 518(7450):529-533.
* 2013 December 19, Volodymyr Mnih, Koray Kavukcuoglu, David Silver, Alex Graves, Ioannis Antonoglou, Daan Wierstra, and Martin Riedmiller. [Playing Atari with Deep Reinforcement Learning](https://arxiv.org/abs/1312.5602). *arXiv:1312.5602*.
* 2013 June 21, Marc G. Bellemare, Yavar Naddaf, Joel Veness, and Michael Bowling. [The Arcade Learning Environment: An Evaluation Platform for General Agents](https://arxiv.org/abs/1207.4708). *arXiv:1207.4708*.

#### StarCraft

[StarCraft](https://en.wikipedia.org/wiki/StarCraft) is a series of military science fiction real-time strategy video games developed by [Blizzard Entertainment](http://us.blizzard.com/en-us/company/about/). The first game, [StarCraft](https://en.wikipedia.org/wiki/StarCraft_(video_game)), was released for Windows on March 31, 1998. Its official sequel, [StarCraft II: Wings of Liberty](https://en.wikipedia.org/wiki/StarCraft_II:_Wings_of_Liberty), released in July 2010, is the base game of the StarCraft II (SC2) series. It has two expansion packs, [StarCraft II: Heart of the Swarm](https://en.wikipedia.org/wiki/StarCraft_II:_Heart_of_the_Swarm) and [StarCraft II: Legacy of the Void](https://en.wikipedia.org/wiki/StarCraft_II:_Legacy_of_the_Void), released in March 2013 and November 2015, respectively.

##### StarCraft II

There are three distinct *races* in SC2: Terran, Protoss, and Zerg, each with own strengths and weaknesses. Each race has unique units that fill specific roles on the battlefield. The most basic worker units harvest resources to expand base, add more units to a growing army, and create new buildings. In multiplayer matches, a player wins the game when all enemy’s buildings are wiped off the map or the other players surrender. A [guide](http://us.battle.net/sc2/en/game/guide/whats-sc2) for new players is available at SC2’s [official game site](http://us.battle.net/sc2/en/).

The StarCraft II Learning Environment (SC2LE; [Vinyals et al., 2017](https://arxiv.org/abs/1708.04782)) consists of three sub-components: a Linux StarCraft II binary, the [StarCraft II API](https://github.com/Blizzard/s2client-proto) and [PySC2](https://github.com/deepmind/pysc2), a Python environment. PySC2 includes several [mini-games](https://github.com/deepmind/pysc2/blob/master/docs/mini_games.md) as small steps towards playing the full game.

* 2017 August 30, Chris Hoyean Song. [StarCraft II RL Tutorial 1](http://chris-chris.ai/2017/08/30/pysc2-tutorial1/). *personal blog*.

##### StarCraft

* 2017 August 7, Zeming Lin, Jonas Gehring, Vasil Khalidov, and Gabriel Synnaeve. [STARDATA: A StarCraft AI Research Dataset](https://arxiv.org/abs/1708.02139). *arXiv:1708.02139*.
* 2017 April 19, Justesen and Risi. [Continual Online Evolutionary Planning for In-Game Build Order Adaptation in StarCraft](http://sebastianrisi.com/wp-content/uploads/justesen_gecco17.pdf). *Proceedings of the Conference on Genetic and Evolutionary Computation (GECCO)*.
* 2017 March 29, Peng Peng, Quan Yuan, Ying Wen, Yaodong Yang, Zhenkun Tang, Haitao Long, and Jun Wang. [Multiagent Bidirectionally-Coordinated Nets for Learning to Play StarCraft Combat Games](https://arxiv.org/abs/1703.10069). *arXiv:1703.10069*.
* 2017 February 28, Jakob Foerster, Nantas Nardelli, Gregory Farquhar, Philip. H. S. Torr, Pushmeet Kohli, and Shimon Whiteson. [Stabilising Experience Replay for Deep Multi-Agent Reinforcement Learning](https://arxiv.org/abs/1702.08887). *arXiv:1702.08887*.
* 2016 September 10, Nicolas Usunier, Gabriel Synnaeve, Zeming Lin, and Soumith Chintala. [Episodic Exploration for Deep Deterministic Policies: An Application to StarCraft Micromanagement Tasks](https://arxiv.org/abs/1609.02993). *arXiv:1609.02993*.

The [StarCraft AI Competition](http://www.cs.mun.ca/~dchurchill/starcraftaicomp/) ([history](http://www.cs.mun.ca/~dchurchill/starcraftaicomp/history.shtml)) is organized by the [RTS Game AI Research Group](https://skatgame.net/mburo/) at the University of Alberta and sponsored by [AIIDE](http://aiide.org/) - AI and Interactive Digital Entertainment.

Facebook's [TorchCraft](https://github.com/TorchCraft/TorchCraft) is a bridge between Torch and StarCraft.

##### References

* 2017 August 16, Oriol Vinyals, Timo Ewalds, Sergey Bartunov, Petko Georgiev, Alexander Sasha Vezhnevets, Michelle Yeo, Alireza Makhzani, Heinrich Küttler, John Agapiou, Julian Schrittwieser, John Quan, Stephen Gaffney, Stig Petersen, Karen Simonyan, Tom Schaul, Hado van Hasselt, David Silver, Timothy Lillicrap, Kevin Calderone, Paul Keet, Anthony Brunasso, David Lawrence, Anders Ekermo, Jacob Repp, and Rodney Tsing. [StarCraft II: A New Challenge for Reinforcement Learning](https://arxiv.org/abs/1708.04782). *arXiv:1708.04782*.
* 2016 November 1, Gabriel Synnaeve, Nantas Nardelli, Alex Auvolat, Soumith Chintala, Timothée Lacroix, Zeming Lin, Florian Richoux, and Nicolas Usunier. [TorchCraft: a Library for Machine Learning Research on Real-Time Strategy Games](https://arxiv.org/abs/1611.00625). *arXiv:1611.00625*.

#### Dota 2

[Dota 2](http://www.dota2.com/) is a [multiplayer online battle arena](https://en.wikipedia.org/wiki/Multiplayer_online_battle_arena) video game developed by [Valve Corporation](http://www.valvesoftware.com/), the creator of game platform [Steam](http://store.steampowered.com/) that distributes and manges thousands of games directly to a community of more than 65 million players around the world. Dota 2 is [free on Steam](http://store.steampowered.com/app/570/Dota_2/), and has a paid component of downloadable content, [The International 2017 Battle Pass](http://store.steampowered.com/app/633890/The_International_2017_Battle_Pass/). [The International](http://www.dota2.com/international/overview/) is a Dota 2 Championships event held in August 7-12, 2017 in Seattle, with a prize pool of over $24 million. [OpenAI](http://realai.org/research-groups/openai/) created a bot which [beats the world’s top professionals at 1v1 matches](https://blog.openai.com/dota-2/) under standard rules. The bot won a best-of-three match on mainstage at The International. Random players at the venue were given chances to challenge the bot and win a free [Shadow Fiend](http://www.dota2.com/hero/nevermore/) arcana. Dot Esports [reported](https://dotesports.com/dota-2/open-ai-one-on-one-competition-ti7-16617) that All 50 arcanas were snatched up by the end of the day. The winning strategy was [discussed on reddit](https://www.reddit.com/r/DotA2/comments/6t8qvs/openai_bots_were_defeated_atleast_50_times/). According to a [follow-up blog from OpenAI](https://blog.openai.com/more-on-dota-2/), it started research in a Dota environment no later than March 1st.

#### ViZDoom

[ViZDoom](http://vizdoom.cs.put.edu.pl/) is a [ZDoom](https://github.com/rheit/zdoom)-based platform that allows AI bots to play Doom using only the screen buffer. It is primarily intended for research in DRL.

#### Project Malmö

Microsoft's [Project Malmö](https://github.com/Microsoft/malmo) is built on top of Minecraft.

* 2016 March 13. [Project Malmo: Using Minecraft to build more intelligent technology](https://blogs.microsoft.com/next/2016/03/13/project-malmo-using-minecraft-build-intelligent-technology/). *The Official Microsoft Blog*.

### Board and Card Games

#### Poker

Texas Hold'em Poker is a family of games that exhibit imperfect information, where players do not have full knowledge of past events. [Bowling et al. (2015)](http://science.sciencemag.org/content/347/6218/145) essentially weakly solved the heads-up limit version of the game. Using deep learning, [Moravčík & Schmid et al. (2017)](https://arxiv.org/abs/1701.01724) built a system that defeated professional players in the heads-up no-limit version. One of its co-authors, Michael Bowling, estimated in a [tweet](https://twitter.com/MichaelHBowling/status/838426697817067520) on 6 March 2017 that computer will beat pros at multi-player level in "a couple years".

* 2017 January 6, Matej Moravčík, Martin Schmid, Neil Burch, Viliam Lisý, Dustin Morrill, Nolan Bard, Trevor Davis, Kevin Waugh, Michael Johanson, and Michael Bowling. [DeepStack: Expert-Level Artificial Intelligence in No-Limit Poker](https://arxiv.org/abs/1701.01724). *arXiv:1701.01724*.
* 2015 January 9, Michael Bowling, Neil Burch, Michael Johanson, and Oskari Tammelin. [Heads-up limit hold’em poker is solved](http://science.sciencemag.org/content/347/6218/145). *Science*, 347(6218):145-149.

#### Go

* 2016 March 15. AlphaGo defeated [Lee Sedol](https://en.wikipedia.org/wiki/Lee_Sedol) 4-1. [*The Guardian*](https://www.theguardian.com/technology/2016/mar/15/googles-alphago-seals-4-1-victory-over-grandmaster-lee-sedol), [*Wikipedia*](https://en.wikipedia.org/wiki/AlphaGo_versus_Lee_Sedol).
* 2015 November 11, David Silver, Aja Huang, Chris J. Maddison, Arthur Guez, Laurent Sifre, George van den Driessche, Julian Schrittwieser, Ioannis Antonoglou, Veda Panneershelvam, Marc Lanctot, Sander Dieleman, Dominik Grewe, John Nham, Nal Kalchbrenner, Ilya Sutskever, Timothy Lillicrap, Madeleine Leach, Koray Kavukcuoglu, Thore Graepel, and Demis Hassabis. [Mastering the game of Go with deep neural networks and tree search](http://www.nature.com/nature/journal/v529/n7587/full/nature16961.html). *Nature*, 529(7587):484-489.

## Dialog Platforms

On 15 May 2017, Facebook [announced](https://code.facebook.com/posts/266433647155520/parlai-a-new-software-platform-for-dialog-research/) dialog research platform [ParlAI](https://github.com/facebookresearch/ParlAI) ([Miller et al., 2017](https://arxiv.org/abs/1705.06476)) for training and testing dialog models across multiple tasks at once. Its first release included more than 20 public datasets covering question answering, sentence completion, goal-oriented dialog, chit-chat dialog and visual dialog.

* 2017 May 18, Alexander H. Miller, Will Feng, Adam Fisch, Jiasen Lu, Dhruv Batra, Antoine Bordes, Devi Parikh, and Jason Weston. [ParlAI: A Dialog Research Software Platform](https://arxiv.org/abs/1705.06476). *arXiv:1705.06476*.


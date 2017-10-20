---
permalink: /forecasts/
---
# Forecasts

## Milestones

Below is a list of milestones that we forecast will be achieved based on our *subjective* views of progress in deep learning. These forecasts are highly likely to change as new discoveries are made and new results announced.

* 2018 March 17 (± 3 months). [Groundbreaking Results from DeepMind](#groundbreaking-results-from-deepmind).
* 2019 March 6 (± 3 months). [Multi-Player No-Limit Poker](#multi-player-no-limit-poker).
* 2021 July 19 (± 12 months). [Proving Mathematical Theorems](http://realai.org/forecasts/proving-mathematical-theorems/).
* 2022 September 24 (± 12 months). [StarCraft](#starcraft).

### Groundbreaking Results from DeepMind

Financial Times [reported](https://www.ft.com/content/cada14c4-d366-11e6-b06b-680c49b4b4c0) on March 17, 2017 that [DeepMind](http://realai.org/research-groups/deepmind/
) hoped to publish six more papers in highly regarded scientific journals [Nature](https://en.wikipedia.org/wiki/Nature_(journal)) or [Science](https://en.wikipedia.org/wiki/Science_(journal)) “within the next year”. DeepMind is an [Alphabet](http://realai.org/industry/alphabet/) subsidiary that has published [over two hundred papers](http://realai.org/research-groups/publications/deepmind/), including [three](http://www.nature.com/nature/journal/v518/n7540/abs/nature14236.html) [Nature](http://www.nature.com/nature/journal/v529/n7587/full/nature16961.html) [papers](http://www.nature.com/nature/journal/v538/n7626/abs/nature20101.html) between February 2015 and October 2016.

In October 2017, DeepMind published another [paper](https://www.nature.com/nature/journal/v550/n7676/full/nature24270.html) on Nature, which leaves five papers in the pipeline.

A September 2017 [blog post](https://machinethoughts.wordpress.com/2017/09/01/deep-meaning-beyond-thought-vectors/) suggests that "there is currently a significant effort at DeepMind based on deep inductive logic programming (Deep ILP) for bottom-up programs and that a paper will appear in the next few months."

Given its track record, and the existence of five [high-quality](https://arxiv.org/abs/1706.06551) [preprint](https://arxiv.org/abs/1707.02286) [papers](https://arxiv.org/abs/1707.03389) [on](https://arxiv.org/abs/1707.06170) [arXiv](https://arxiv.org/abs/1707.06887), we are convinced of this estimate and assign a **90% confidence interval of ± 3 months** that five groundbreaking results will come from DeepMind by **March 17, 2018**.

*Last Updated: October 20, 2017*

### Multi-Player No-Limit Poker

Multi-player no-limit [Texas hold’em](https://en.wikipedia.org/wiki/Texas_hold_%27em) is one of the most popular forms of poker, widely televised in events like the [World Series of Poker](http://www.wsop.com/). On March 6, 2017, University of Alberta professor [Michael Bowling](https://webdocs.cs.ualberta.ca/~bowling/) [said on Twitter](https://twitter.com/MichaelHBowling/status/838426697817067520) that in this game, computer programs would beat human pros in “a couple years”. Prof. Bowling is a world-leading expert in computer poker. He led a [research group](http://poker.cs.ualberta.ca/) that published [Cepheus](http://poker.srv.ualberta.ca/) in [January 2015](http://science.sciencemag.org/content/347/6218/145.full), the first AI to solve *heads-up limit* Texas hold’em, and [DeepStack](https://www.deepstack.ai/) in [March 2017](http://science.sciencemag.org/content/early/2017/03/01/science.aam6960), the first AI capable of beating pros at *heads-up no-limit* Texas Hold’em. Given Prof. Bowling’s track record, we are convinced of his estimate and assign a **90% confidence interval of ± 3 months** that computers will beat pros in *multi-player no-limit* poker on **March 6, 2019**.

In July 2017, Prof. Bowling joined DeepMind to colead its [newly created research office in Edmonton, Alberta](https://deepmind.com/blog/deepmind-office-canada-edmonton/). DeepMind is the Alphabet subsidiary that developed [AlphaGo](https://deepmind.com/research/alphago/), the first computer program to achieve superhuman performance in the ancient Chinese game of [Go](https://en.wikipedia.org/wiki/Go_(game)).

*Last Updated: July 29, 2017*

### StarCraft

According to a [CBC News](http://www.cbc.ca/news) report [posted](http://www.cbc.ca/news/canada/newfoundland-labrador/artificial-intelligence-robots-battle-memorial-university-starcraft-1.4298844) on September 24, 2017, [David Churchill](http://www.cs.mun.ca/~dchurchill/) predicts that AI is about five years off from being able to beat StarCraft world champions. Churchill is an assistant professor with the [computer science department](http://www.mun.ca/computerscience/) of Memorial University of Newfoundland. He has organized and run the [AIIDE StarCraft AI Competition](http://www.starcraftaicompetition.com/) since 2011. The confidence interval of ± 12 months is currently based on our subjective estimate only.

*Last Updated: September 26, 2017*

## Research

Future work of [Pascanu & Li et al. (2017)](https://arxiv.org/abs/1707.06170) should "explore using RNNs or local navigation within the tree to handle variable sized sets of route choices for the manager" component of the Imagination-based Planner (IBP).

[Hessel et al. (2017)](https://arxiv.org/abs/1710.02298) introduce the first *Rainbow* agent that integrates six extensions to the DQN algorithm and achieves new state-of-the-art results in Atari games. There are many more algorithmic components that they're not able to include, which would be promising candidates for further experiments. Several such components include pure policy-based RL algorithms, episodic control, exploration methods other than noisy nets, hierarchical RL, and auxiliary tasks.

[Bansal et al. (2017)](https://arxiv.org/abs/1710.03748) introduce several new competitive multi-agent 3D physically simulated environments. Future experiments can be conducted in larger scale and more complex environments that encourage agents to both compete and cooperate with each other, potentially with the ability to reason about other agents.

### References

* 2017 October 10, Trapit Bansal, Jakub Pachocki, Szymon Sidor, Ilya Sutskever, and Igor Mordatch. [Emergent Complexity via Multi-Agent Competition](https://arxiv.org/abs/1710.03748). *arXiv:1710.03748*. [site](https://sites.google.com/view/multi-agent-competition). [blog](https://blog.openai.com/competitive-self-play/).
* 2017 October 6, Matteo Hessel, Joseph Modayil, Hado van Hasselt, Tom Schaul, Georg Ostrovski, Will Dabney, Dan Horgan, Bilal Piot, Mohammad Azar, and David Silver. [Rainbow: Combining Improvements in Deep Reinforcement Learning](https://arxiv.org/abs/1710.02298). *arXiv:1710.02298*.
* 2017 July 19, Razvan Pascanu, Yujia Li, Oriol Vinyals, Nicolas Heess, Lars Buesing, Sebastien Racanière, David Reichert, Théophane Weber, Daan Wierstra, and Peter Battaglia. [Learning model-based planning from scratch](https://arxiv.org/abs/1707.06170). *arXiv:1707.06170*.

## Other Forecasts

* 2017 January 4, Miles Brundage. [My AI Forecasts--Past, Present, and Future (Main Post)](http://www.milesbrundage.com/blog-posts/my-ai-forecasts-past-present-and-future-main-post). *Personal Blog*.


---
permalink: /background/neuroscience/
mathjax: true
---
# Neuroscience

## Background

Neuroscience can provide a rich source of inspiration for new types of AI algorithms and architectures, as well as help validate existing techniques ([Hassabis, 2012](http://www.nature.com/nature/journal/v482/n7386/full/482462a.html)), for example, based on if they mimic a function within the brain. Looking forward, [Summerfield et al. (2017)](https://deepmind.com/blog/ai-and-neuroscience-virtuous-circle/) believe that neuroscience will become "indispensable" for tackling unsolved problems.

The contribution of neuroscience to AI progress is further explained in [Hassabis et al. (2017)](http://www.cell.com/neuron/fulltext/S0896-6273(17)30509-3), a review paper published in July 2017, where it is stated that "if one scratches the surface, one can uncover many cases in which recent developments have been inspired and guided by neuroscientific considerations." They then provide four examples: attention, episodic memory, working memory, and continual learning.

We broadly share this belief that neuroscience has been and will continue to be crucial for AI progress, however, since June 2017, our view has been that there isn't much space for *new* neuroscience discoveries to significantly impact the direction and methodologies of current technical development towards AGI. In other words, despite numerous unanswered questions in neuroscience, we have already known enough for the purpose of *building* an AGI system. We maintain this page to monitor the field just in case there is any surprise.

### References

* 2017 August 2, Christopher Summerfield, Matt Botvinick, and Demis Hassabis. [AI and Neuroscience: A virtuous circle](https://deepmind.com/blog/ai-and-neuroscience-virtuous-circle/). *DeepMind Blog*.
* 2017 July 26, A. Emin Orhan and Wei Ji Ma. [Efficient probabilistic inference in generic neural networks trained with non-probabilistic feedback](https://www.nature.com/articles/s41467-017-00181-8). *Nature Communications*, 8(138).
* 2017 July 19, Demis Hassabis, Dharshan Kumaran, Christopher Summerfield, and Matthew Botvinick. [Neuroscience-Inspired Artificial Intelligence](http://www.cell.com/neuron/fulltext/S0896-6273(17)30509-3). *Cell*, 95(2):245-258. [PDF](https://deepmind.com/documents/113/Neuron.pdf). [interview](https://www.theverge.com/2017/7/19/15998610/ai-neuroscience-machine-learning-deepmind-demis-hassabis-interview).
* 2017 April 25, Yukiko Kikuchi, Adam Attaheri, Benjamin Wilson, Ariane E. Rhone, Kirill V. Nourski, Phillip E. Gander, Christopher K. Kovach, Hiroto Kawasaki, Timothy D. Griffiths, Matthew A. Howard III, and Christopher I. Petkov. [Sequence learning modulates neural responses and oscillatory coupling in human and monkey auditory cortex](http://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.2000219). *PLOS Biology*.
* 2017 April 11, Partha Mitra. [Is Neuroscience Limited by Tools or Ideas?](https://www.scientificamerican.com/article/is-neuroscience-limited-by-tools-or-ideas/). *Scientific American*.
* 2017 April 7, Takashi Kitamura, Sachie K. Ogawa, Dheeraj S. Roy, Teruhiro Okuyama, Mark D. Morrissey, Lillian M. Smith, Roger L. Redondo, and Susumu Tonegawa. [Engrams and circuits crucial for systems consolidation of a memory](http://science.sciencemag.org/content/356/6333/73). *Science*, 356(6333):73-78.
* 2017 March 16, Ruth Fong, Walter Scheirer, and David Cox. [Using Human Brain Activity to Guide Machine Learning](https://arxiv.org/abs/1703.05463). *arXiv:1703.05463*.
* 2017 February 24, Sara Reardon. [A giant neuron found wrapped around entire mouse brain](http://www.nature.com/news/a-giant-neuron-found-wrapped-around-entire-mouse-brain-1.21539). *Nature* 543, 14-15.
* 2016 September 3, Jason J. Moore, Pascal M. Ravassard, David Ho, Lavanya Acharya, Ashley L. Kees, Cliff Vuong, and Mayank R. Mehta. [Dynamics of cortical dendritic membrane potential and spikes in freely behaving rats](http://science.sciencemag.org/content/early/2017/03/08/science.aaj1497). *Science*.
* 2016 August 11, Haiguang Wen, Junxing Shi, Yizhen Zhang, Kun-Han Lu, and Zhongming Liu. [Neural Encoding and Decoding with Deep Learning for Dynamic Natural Vision](https://arxiv.org/abs/1608.03425). *arXiv:1608.03425*.
* 2016 May 26, Eric Jonas and Konrad Kording. [Could a neuroscientist understand a microprocessor?](http://biorxiv.org/content/early/2016/05/26/055624). *bioRxiv:055624*.
* 2012 February 22, Demis Hassabis. Model the brain's algorithms. In [Turing centenary: Is the brain a good model for machine intelligence?](http://www.nature.com/nature/journal/v482/n7386/full/482462a.html) *Nature*, 482(7386):462-463.

## Imagination

* 2009 March 30, Demis Hassabis and Eleanor A. Maguire. [The construction system of the brain](http://rstb.royalsocietypublishing.org/content/364/1521/1263.long). *Philosophical Transactions of the Royal Society B*, 364(1521): 1263-71.

## Reasoning

* 2014 June 27, Maël Donoso, Anne G. E. Collins, and Etienne Koechlin. [Foundations of human reasoning in the prefrontal cortex](http://science.sciencemag.org/content/344/6191/1481.long). *Science*, 334(6191):1481-1486.

## Memory

* 2016 July 21. [How the Brain Builds Memory Chains](https://www.scientificamerican.com/article/how-the-brain-builds-memory-chains/). *Scientific American*.

## Spiking Neural Networks

[Zenke & Ganguli (2017)](https://arxiv.org/abs/1705.11146) propose to train spiking neurons by a gradient descent rule that takes the form

$$
\frac{\partial w_{ij}}{\partial t} = r \int^t_{-\infty}ds [\alpha * (\hat{S}_i-S_i)(s)] [ \alpha * ({\sigma}'(U_i(s))(\epsilon * S_j)(s) ],
$$

where \\(r\\) is the learning rate, and the integrand is the product of an error signal and a Hebbian term which combines pre- and postsynaptic activity. They demonstrate that a single LIF neuron can learn to emit a predefined target spike pattern.

### References

* 2017 May 31, Friedemann Zenke and Surya Ganguli. [SuperSpike: Supervised learning in multi-layer spiking neural networks](https://arxiv.org/abs/1705.11146). *arXiv:1705.11146*.

## Some Theories of Intelligence

Neuroscience has spurred many attempts at building machine intelligence, such as [Hierarchical Temporal Memory](http://numenta.org/) ([Hawkins et al., 2016](http://numenta.com/biological-and-machine-intelligence/)) and [Feynman Machine](https://hackernoon.com/feynman-machine-a-new-approach-for-cortical-and-machine-intelligence-5855c0e61a70).

### References

* 2016, J. Hawkins, S. Ahmad, S. Purdy, and A. Lavin. [Biological and Machine Intelligence (BAMI)](http://numenta.com/biological-and-machine-intelligence/). *online release*.

## Further Reading

* Eric S. Lander, Graham Walker, Michelle Mischke, Brian White, and Mary Ellen Wiltrout. [Introduction to Biology - The Secret of Life](https://www.edx.org/course/introduction-biology-secret-life-mitx-7-00x-6). *MITx 7.00x*.
* Leonard E. White. [Medical Neuroscience](https://www.coursera.org/learn/medical-neuroscience). *Duke University*.
* 2016 January, *Harvard University*. [The Fundamentals of Neuroscience](https://www.mcb80x.org/). David Cox.
* 2010 January 13, *Nature Reviews Neuroscience*. [The free-energy principle: a unified brain theory?](http://www.fil.ion.ucl.ac.uk/~karl/The%20free-energy%20principle%20A%20unified%20brain%20theory.pdf). Karl Friston.
* 2004 September 9, Jeff Hawkins. [On Intelligence](https://www.amazon.com/Intelligence-Jeff-Hawkins/dp/0805074562). *Time Books*.


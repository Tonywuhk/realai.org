---
permalink: /neuroscience/
mathjax: true
---
# Neuroscience

## Background

As of June 2017, our view is that there isn't much space for new neuroscience discoveries to impact the technical development towards AGI. The main purpose of this page is to monitor the field just in case there is any surprise.

Our impression is echoed in [Hassabis et al. (2017)](http://www.cell.com/neuron/fulltext/S0896-6273(17)30509-3), a review paper published in July 2017. They counter that "if one scratches the surface, one can uncover many cases in which recent developments have been inspired and guided by neuroscientific considerations." They then provide four examples: attention, episodic memory, working memory, and continual learning.

### References

* 2017 July 26, A. Emin Orhan and Wei Ji Ma. [Efficient probabilistic inference in generic neural networks trained with non-probabilistic feedback](https://www.nature.com/articles/s41467-017-00181-8). *Nature Communications*, 8(138).
* 2017 July 19, Demis Hassabis, Dharshan Kumaran, Christopher Summerfield, and Matthew Botvinick. [Neuroscience-Inspired Artificial Intelligence](http://www.cell.com/neuron/fulltext/S0896-6273(17)30509-3). *Cell*, 95(2):245-258. [interview](https://www.theverge.com/2017/7/19/15998610/ai-neuroscience-machine-learning-deepmind-demis-hassabis-interview).
* 2017 April 25, Yukiko Kikuchi, Adam Attaheri, Benjamin Wilson, Ariane E. Rhone, Kirill V. Nourski, Phillip E. Gander, Christopher K. Kovach, Hiroto Kawasaki, Timothy D. Griffiths, Matthew A. Howard III, and Christopher I. Petkov. [Sequence learning modulates neural responses and oscillatory coupling in human and monkey auditory cortex](http://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.2000219). *PLOS Biology*.
* 2017 April 11, Partha Mitra. [Is Neuroscience Limited by Tools or Ideas?](https://www.scientificamerican.com/article/is-neuroscience-limited-by-tools-or-ideas/). *Scientific American*.
* 2017 April 7, Takashi Kitamura, Sachie K. Ogawa, Dheeraj S. Roy, Teruhiro Okuyama, Mark D. Morrissey, Lillian M. Smith, Roger L. Redondo, and Susumu Tonegawa. [Engrams and circuits crucial for systems consolidation of a memory](http://science.sciencemag.org/content/356/6333/73). *Science*, 356(6333):73-78.
* 2017 March 16, Ruth Fong, Walter Scheirer, and David Cox. [Using Human Brain Activity to Guide Machine Learning](https://arxiv.org/abs/1703.05463). *arXiv:1703.05463*.
* 2017 February 24, Sara Reardon. [A giant neuron found wrapped around entire mouse brain](http://www.nature.com/news/a-giant-neuron-found-wrapped-around-entire-mouse-brain-1.21539). *Nature* 543, 14-15.
* 2016 September 3, Jason J. Moore1, Pascal M. Ravassard, David Ho, Lavanya Acharya, Ashley L. Kees, Cliff Vuong, and Mayank R. Mehta. [Dynamics of cortical dendritic membrane potential and spikes in freely behaving rats](http://science.sciencemag.org/content/early/2017/03/08/science.aaj1497). *Science*.
* 2016 August 11, Haiguang Wen, Junxing Shi, Yizhen Zhang, Kun-Han Lu, and Zhongming Liu. [Neural Encoding and Decoding with Deep Learning for Dynamic Natural Vision](https://arxiv.org/abs/1608.03425). *arXiv:1608.03425*.
* 2016 May 26, Eric Jonas and Konrad Kording. [Could a neuroscientist understand a microprocessor?](http://biorxiv.org/content/early/2016/05/26/055624). *bioRxiv:055624*.

## Spiking Neural Networks

[Zenke & Ganguli (2017)](https://arxiv.org/abs/1705.11146) propose to train spiking neurons by a gradient descent rule that takes the form

$$
\frac{\partial w_{ij}}{\partial t} = r \int^t_{-\infty}ds [\alpha * (\hat{S}_i-S_i)(s)] [ \alpha * ({\sigma}'(U_i(s))(\epsilon * S_j)(s) ],
$$

where \\(r\\) is the learning rate, and the integrand is the product of an error signal and a Hebbian term which combines pre- and postsynaptic activity. They demonstrate that a single LIF neuron can learn to emit a predefined target spike pattern.

### References

* 2017 May 31, Friedemann Zenke and Surya Ganguli. [SuperSpike: Supervised learning in multi-layer spiking neural networks](https://arxiv.org/abs/1705.11146). *arXiv:1705.11146*.

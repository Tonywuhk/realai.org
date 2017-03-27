---
permalink: /frontier/towards-neural-network-based-general-intelligence.html
---
# Towards Neural Network-Based General Intelligence

We hope to evolve this preliminary document into a concrete roadmap towards general AI. As a first step, we make a list of problems that we think should be solved before a learning system can be declared "general".

## 1. Learning Architecture

It is not yet clear how a general AI system's internal states should change according to inputs. At present, the optimization of an objective function motivates most of the standard update rules, e.g. SGD, momentum, Adagrad, Adadelta, RMSprop, and Adam.

There may be new update rules that are more directly linked to inputs. Network weights and topology can also change over time, sometimes according to outputs from other networks.

## 2. Unsupervised Learning

In the more likely case that update rules are motivated by optimization, the ability of unsupervised learning requires the objectives of optimization to be relatively stable and likely intrinsic.

### 2.1 Intrinsic Motivations

Here we include the type of update rules that are driven by the optimization of physics-inspired quantities such as free energy.

#### 2.1.1 Predictive Learning

The system learns to predict future inputs.

#### 2.1.2 Exploration / Curiosity

The system prefers novel states.

## 3. Continual Learning

A general AI system can learn new tasks while largely retaining old knowledge.

### 3.1 Cumulative Learning

Training and testing phases should not be completely separate and can happen concurrently. 

## 4. Few Shot Learning

The system can easily generalize. Its encoded knowledge and continual learning ability allow it to learn new behaviors from much fewer data than today's narrow AI systems.

## 5. Hierarchical Learning

A hierarchy of learning structures eases the difficulty of learning in long time horizon and facilitates abstract thinking.

### 5.1 Abstraction

The ability to extract concepts from data and conduct inferences.

## 6. Neural Interface and Modules

* The architecture needs to be independent enough to allow unlocked learning, so that modules can learn autonomously while communicating with other modules via cleverly designed interface;
* Multi-agent learning where each agent is considered a module and their means of communication the interface; and
* Stable input and output interfaces for interactions with the environment.

## 7. Memory

### 7.1 Episodic and long-term memory

### 7.2 Temporary memory that facilitates learning e.g. used for experience replay

## 8. World Model

The learning system should contain a vast amount of knowledge that forms the basis of "common sense", which can be the result of continual learning.

## 9. Language Grounding

The system's understanding of language should be grounded to its representation of common sense knowledge, not merely finding patterns in texts. Language can be considered as the interface between neural network agents who need to communicate.

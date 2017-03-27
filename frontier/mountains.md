---
permalink: /frontier/mountains.html
---
# Mountains

We hope to evolve this preliminary document into a concrete roadmap towards general AI. As a first step, we make a list of problems that we think should be solved before a learning system can be declared "general".

## 1. Unsupervised Learning

### 1.1 Learning Rules

It is not yet clear how a general AI system's internal states should change according to inputs. At present, the optimization of an objective function motivates most of the standard update rules, e.g. SGD, momentum, Adagrad, Adadelta, RMSprop, and Adam. There may be new update rules that are more directly linked to inputs.

In the more likely case that update rules are motivated by optimization, the ability of unsupervised learning requires the objectives of optimization to be relatively stable and likely intrinsic.

### 1.2 Intrinsic Motivations

Here we include the type of update rules that are driven by the optimization of physics-inspired quantities such as free energy.

#### 1.2.1 Predictive Learning

The system learns to predict future inputs.

#### 1.2.2 Exploration / Curiosity

The system prefers novel states.

## 2. Continual Learning

A general AI system can learn new tasks while largely retaining old knowledge.

### 2.1 Cumulative Learning

Training and testing phases should not be completely separate and can happen concurrently. 

## 3. Few Shot Learning

The system can easily generalize. Its encoded knowledge and continual learning ability allow it to learn new behaviors from much fewer data than today's narrow AI systems.

## 4. Hierarchical Learning

A hierarchy of learning structures eases the difficulty of learning in long time horizon and facilitates abstract thinking.

### 4.1 Abstraction

The ability to extract concepts from data and conduct inferences.

## 5. Neural Interface and Modules

* The architecture needs to be independent enough to allow unlocked learning, so that modules can learn autonomously while communicating with other modules via cleverly designed interface;
* Multi-agent learning where each agent is considered a module and their means of communication the interface; and
* Stable input and output interfaces for interactions with the environment.

## 6. Dynamic Architecture

Network weights and topology can change over time, sometimes according to outputs from other networks.

## 7. Memory

### 7.1 Episodic and long-term memory

### 7.2 Temporary memory that facilitates learning e.g. used for experience replay

## 8. World Model

The learning system should contain a vast amount of knowledge that forms the basis of "common sense", which can be the result of continual learning.

## 9. Language Grounding

The system's understanding of language should be grounded to its representation of common sense knowledge, not merely finding patterns in texts. Language can be considered as the interface between neural network agents who need to communicate.

---
permalink: /frontier/towards-neural-network-based-general-intelligence.html
---
# Towards Neural Network-Based General Intelligence

*[Jonathan Yan](mailto:jyan@realai.org)*

Building computer systems based on neural networks (NNs) is a promising path towards the development of artificial general intelligence (AGI). The capabilities of today's systems are still very limited and can only successfully learn narrow tasks at best. We review problems that likely need to be solved before AGI can be achieved. 

## Introduction 

The problems listed below are interrelated, the solution of one part of a problem is often closely related to the solution of one part of another problem. AGI may be attainable after satisfactory solutions of only a few problems.

We do not include the topics of supervised learning and reinforcement learning because they can be considered solved ([Hassabis 2017](https://www.youtube.com/watch?v=V0aXMTpZTfc)), at least in the very narrow sense of still image recognition and simple gameplay. Further improvements of the performances in these tasks will likely be driven by solutions to other topics covered in this article.

We also stress that deep learning is only one way towards building general AI and we by no means imply that it is the only way. There are a lot of interesting discoveries that are motivated by symbolic AI, statistical machine learning, cognitive science, robotics, neuromorphic engineering, physics and other fields. Even inside machine learning, advanced systems can be built that do not use neural networks. They're promising directions but are beyond the scope of this preview.

## 1. Learning Architecture

In the sense that the eventual implementation of an NN-based AGI system is a large learning architecture, this is the problem that captures all the others. Here we specifically focus on the algorithmic and architectural aspects of learning, while leaving the characteristics of learning to later sections.

### 1.1 Update Rules

It is not yet clear how a general AI system's internal states should change according to inputs. At present, the optimization of an objective function motivates most of the standard update rules, e.g. SGD, momentum, Adagrad, Adadelta, RMSprop, and Adam.

There may be new update rules that are more directly linked to inputs. Network weights and topology can also change over time, sometimes according to outputs from other networks.

### 1.2 Meta-Networks

A *meta* neural network can operate on the weights and topology of an underlying neural network.

### 1.3 Learning Network Topology

The topology of a neural network can also change in the course of learning.

## 2. Unsupervised Learning

In the more likely case that update rules are motivated by optimization, the ability of unsupervised learning requires the objectives of optimization to be relatively stable and likely intrinsic.

### 2.1 Intrinsic Motivations

Here we include the type of update rules that are driven by the optimization of physics-inspired quantities such as free energy.

#### 2.1.1 Predictive Learning

The system learns to predict future inputs. This is likely harder than the study of *generative models* which only need to generate data without making extra moves through time.

#### 2.1.2 Exploration / Curiosity

The system prefers novel states.

## 3. Continual Learning

A general AI system can learn new tasks while largely retaining old knowledge.

### 3.1 Cumulative Learning

Training and testing phases should not be completely separate and can happen concurrently. 

## 4. Few-Shot Learning

The system can easily generalize. Its encoded knowledge and continual learning ability allow it to learn new behaviors from much fewer data than today's narrow AI systems.

## 5. Hierarchical Learning

The ability to learn hierarchical structures in the data and use them for abstract planning and reasoning, sometimes in long time horizon. Hierarchies in network architeture are likely necessary.

### 5.1 Deep Representation Learning

Build a hierarchy of feature representations that are useful for one or more tasks.

**Concept learning** focuses on meaningful abstractions of data that are embedded in the representations

## 6. Neural Interface and Modules

* The architecture needs to be independent enough to allow unlocked learning, so that modules can learn autonomously while communicating with other modules via cleverly designed interface;
* Multi-agent learning where each agent is considered a module and their means of communication the interface; and
* Stable input and output interfaces for interactions with the environment.

### 6.1 Communication

When the communication between neural networks takes the form of more explicit data such as language or image, this problem can include standard topics such as NLP and generative models.

## 7. Basic Cognitive Functions

### 7.1 Memory

Memory can be a very useful component of the learning architecture and is often times not in the form neural networks, which are not particularly good at recording data.

#### 7.1.1 Episodic and long-term memory

#### 7.1.2 Temporary memory that facilitates learning e.g. used for experience replay

### 7.2 Attention

Selectively attend to the part of data that are important for the current context in which the system is operating.

### 7.3 Reasoning

The ability to reason in abstract terms is one way of hierarchical thinking.

## 8. Language Grounding

The system's understanding of language should be grounded to its representation of common sense knowledge, not merely finding patterns in texts. Language can be considered as the interface between neural network agents who need to communicate.

## 9. World Model

The learning system should contain a vast amount of knowledge that forms the basis of "common sense", which can be the result of continual learning.

## References

* 2017 February 9, Demis Hassabis. [Creating Human-level AI: How and When?](https://www.youtube.com/watch?v=V0aXMTpZTfc). *[BAI 2017](https://futureoflife.org/bai-2017/)*, (YouTube video)24:40-25:10.

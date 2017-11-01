---
permalink: /chatbot/
---
# Chatbot

A [chatbot](https://en.wikipedia.org/wiki/Chatbot) is a computer system that interacts with users via common [input/output](https://en.wikipedia.org/wiki/Input/output) devices such as monitors and keyboards. A chatbot can have access to the Internet. Chatbot [safety](http://realai.org/safety/) is studied under the topic of [Oracle AI](http://realai.org/safety/oracle-ai/).

## What’s New

MILABOT ([Serban et al., 2017](https://arxiv.org/abs/1709.02349)) is a chatbot developed by the [MILA](https://mila.umontreal.ca/en/) [team](https://developer.amazon.com/alexaprize/teams/mila-team) for the [Amazon Alexa Prize](#alexa-prize) competition. It uses [DRL](DRL/README.md) to select a response from an ensemble of 22 lower-level chatbots that are based on templates, knowledge bases, retrieval models using neural networks or logistic regression, search engine results chosen by neural networks, and a deep generative model. One of their approaches, called *Q-learning AMT*, uses Q-learning with experience replay to learn the response selection policy. The policy takes as input a sample drawn from the set of all recorded dialogues, which grows over time when the system is deployed in practice. As new data become available, the policy can continuously improve. Other obvious means of improvement include modeling individual users, adding more lower-level chatbots, and more sophisticated abstractions of the state of dialogue in the Q-learning AMT approach.

Based on the system’s architecture and training environment, an intuitive, but not obviously certain assessment is that the current version of MILABOT does not possess advanced intelligence. On the other hand, it can and likely will become more intelligent in the foreseeable future. Given its complexity and its future versions’ long-range dependency on real-world user ratings, which is what the system is optimized for, the chatbot can potentially provide a response to a user query that results in a non-beneficial outcome. However, no reference is made in [Serban et al. (2017)](https://arxiv.org/abs/1709.02349) to [AI safety](http://realai.org/safety/), or in particular, safety regarding [Oracle AIs](http://realai.org/safety/oracle-ai/).

## Industry

### Alexa

[Alexa](https://en.wikipedia.org/wiki/Amazon_Alexa) is a chatbot developed by [Amazon](http://realai.org/industry/amazon/) and available on Amazon devices including the popular smartspeaker [Amazon Echo](https://en.wikipedia.org/wiki/Amazon_Echo).

#### Alexa Prize

[The Alexa Prize](https://developer.amazon.com/alexaprize) is an annual university competition that focuses solely on *socialbots*, an Alexa skill that converses with users about popular topics and news events. During the semifinals between July 1 and August 15, 2017, Alexa users in the US asked to converse with the teams’ socialbots and were prompted to rate them. Participants in the September 2016 - November 2017 competition could receive a total prize of $2.5 million.

## Libraries

* [Bottery](https://github.com/google/bottery) is a conversational agent prototyping platform by [Kate Compton](https://github.com/galaxykate). It is a syntax, editor, and simulator for prototyping generative contextual conversations modeled as finite state machines.

## References

* 2017 September 7, Iulian V. Serban, Chinnadhurai Sankar, Mathieu Germain, Saizheng Zhang, Zhouhan Lin, Sandeep Subramanian, Taesup Kim, Michael Pieper, Sarath Chandar, Nan Rosemary Ke, Sai Mudumba, Alexandre de Brebisson, Jose M. R. Sotelo, Dendi Suhubdy, Vincent Michalski, Alexandre Nguyen, Joelle Pineau, and Yoshua Bengio. [A Deep Reinforcement Learning Chatbot](https://arxiv.org/abs/1709.02349). *arXiv:1709.02349*.


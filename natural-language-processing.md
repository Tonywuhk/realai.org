---
permalink: /nlp/
---
# Natural Language Processing

## Chatbot

[Lewis et al. (2017)](https://s3.amazonaws.com/end-to-end-negotiator/end-to-end-negotiator.pdf) train an end-to-end chatbot that can negotiate with humans in natural language. In a simple negotiation task involving three item types with assigned numerical values, the chatbot is pre-trained with supervised learning, then fine-tuned by reinforcement learning against a version of itself. They introduce dialogue rollouts, in which the chatbot plans ahead by simulation. This technique might be useful together with Monte Carlo Tree Search in other domains. Without explicit human design, the chatbot learns to deceive by initially feigning interest in a valueless item, only to conceding it later. Chatbots training together are also capable of developing their own language.

### References

* 2017 June 15, Mike Lewis, Denis Yarats, Yann N. Dauphin, Devi Parikh, and Dhruv Batra. [Deal or No Deal? End-to-End Learning for Negotiation Dialogues](https://s3.amazonaws.com/end-to-end-negotiator/end-to-end-negotiator.pdf). *Facebook Artificial Intelligence Research*. [blog](https://code.facebook.com/posts/1686672014972296). [code](https://github.com/facebookresearch/end-to-end-negotiator).

## Abstractive Summarization

[Paulus et al. (2017)](https://metamind.io/research/your-tldr-by-an-ai-a-deep-reinforced-model-for-abstractive-summarization) proposed a reinforcement learning model with intra-decoder attention, and achieved state-of-the-art results on the CNN/Daily Mail dataset.

### References

* 2017 May 11, Romain Paulus, Caiming Xiong, and Richard Socher. [Your tl;dr by an ai: a deep reinforced model for abstractive summarization](https://metamind.io/research/your-tldr-by-an-ai-a-deep-reinforced-model-for-abstractive-summarization). *Salesforce MetaMind*.

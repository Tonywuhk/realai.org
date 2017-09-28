---
permalink: /course/reinforcement-learning/markov-decision-process/
redirect_from:
  - /course/RL/MDP/
  - /course/RL/markov-decision-process/
  - /course/reinforcement-learning/MDP/
mathjax: true
---
# Markov Decision Process

A Markov Decision Process (MDP) is a RL task in which an agent acts to maximize its cumulated rewards based on the Markov state of the environment. Mathematically, it is defined by a tuple \\(M=(\mathcal{S},\mathcal{A},\mathcal{P},r,\rho_0,\gamma,T)\\), in which \\(\mathcal{S}\\) is a state set, \\(\mathcal{A}\\) an action set, \\(\mathcal{P}: \mathcal{S}\times\mathcal{A}\times\mathcal{S} \rightarrow [0,1]\\) a transition probability distribution, \\(r: \mathcal{S}\times\mathcal{A} \rightarrow \mathbb{R}\\) a reward function, \\(\rho_0: \mathcal{S} \rightarrow [0,1]\\) an initial state distribution, \\(\gamma \in [0,1]\\) a discount factor, and \\(T\\) a horizon.

At time \\(t\\) an agent observes the state \\(s\_t\\) of the environment and produces an action \\(a\_t \sim \pi(\cdot \| s\_t)\\), then the environment transitions to a new state \\(s\_{t+1} \sim p(\cdot \| s\_t, a\_t)\\), and the agent receives a reward \\(r\_t = r(s\_t, a\_t)\\). The total accumulated reward from time \\(t\\) is

$$
  R_t = r_t + \gamma r_{t+1} + \gamma^2 r_{t+2} + ...
$$

The goal of the agent is to optimize its policy \\(\pi: \mathcal{S}\times\mathcal{A} \rightarrow \mathbb{R}\_+ \\), such that the *action-value function*

$$
  Q^\pi (s,a) = \mathbb{E}[R_0 | S_0=s, A_0=a, \pi]
$$

is maximized. The optimal action-value function \\(Q^\*(s,a) = \max\_\pi Q^\pi(s,a)\\) is achieved when the agent follows an optimal policy \\(\pi^\*\\). The \\(n\\)-step \\(Q\\)-value is defined as

$$
  Q^{(n)} (s,a) = r_t + \gamma r_{t+1} + ... + \gamma^{N-1} r_{t+N-1} + \gamma^n \max_{a'} Q(s_{t+N}, a').
$$

Similarly, the *state-value function*

$$
  V^\pi (s) = \mathbb{E}[R_0 | S_0=s, \pi],
$$

and the optimal state-value function \\(V^\*(s) = \max\_\pi V^\pi(s)\\). The *advantage function* is defined as \\(A^\pi (s,a) = Q^\pi(s,a) - V^\pi(s)\\). The true \\(Q^\*(s, a)\\) and \\(V^\*(s)\\) are often too complex for interesting problems, so in practice we learn a parameterized version \\(Q(s, a; \theta)\\) and \\(V(s; \theta_v)\\).

## Value and Policy Functions

Given the optimal action-value function \\(Q^*\\), it is relatively easy to determine the policy function assuming it is deterministic:

$$
\pi^*(s) = \arg\max_{a \in \mathcal{A}} Q^*(s, a).
$$

The state-value function can be obtained at a similar level of difficulty:

$$
V^*(s) = \max_{a \in \mathcal{A}} Q^*(s, a) = Q^*(s, \pi^*(s)).
$$

All we need to do is to solve a maximization problem over the space of actions \\(\mathcal{A}\\). The converse, however, is more difficult. Given the optimal state-value function \\(V^\*\\), the optimal action-value function \\(Q^\*\\) is given by:

$$
Q^*(s, a) = r(s, a) + \gamma \mathbb{E}_{s' \sim p(\cdot | s, a)} V^*(s').
$$

This involves the expectation over the space of states, which further depends on the transition probability distribution of the environment. In a realistic RL setting, both are much more complex than the agent's space of actions. For example, the environment can contain other equally complex agents. On the other hand, the optimal state-value function is intuitively less complex than the \\(Q^*\\) because it is independent of the agent's action.

The optimal policy function \\(\pi^*\\) contains even less information than the optimal state-value function, since it only needs to cover the space of actions. To obtain \\(V^\*\\):

$$
V^*(s) = r(s, \pi^*(s)) + \gamma \mathbb{E}_{s' \sim p(\cdot | s, a)} V^*(s').
$$

Not only there is an expectation over the space of states, we also need to *solve* for the function \\(V^*\\) as it appears on both sides of the equation.

This intuition about value and policy functions is important. From \\(Q^\*\\) to \\(V^\*\\) to \\(\pi^\*\\), our solution contains less and less information about the entire MDP. In general we have no choice but to move down the spectrum when we have less clue about how to solve a particular MDP.


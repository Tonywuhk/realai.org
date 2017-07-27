---
permalink: /metamath/
---
# Metamath

[Metamath](http://us.metamath.org/) is a formal math system started by Norman Megill in 1992, and has been under continuous development since then. It has a small community of users that are active on [Google Group](http://groups.google.com/group/metamath). The simple text-based Metamath language can be used to encode mathematical theorems and proofs. For example, the statement of [Fermat's Last Theorem](https://en.wikipedia.org/wiki/Fermat%27s_Last_Theorem) can be encoded as

```metamath
|- ( ( x e. ZZ /\ y e. ZZ /\ z e. ZZ /\ n e. ( ZZ>= ` 3 ) ) -> ( ( ( x ^ n ) + ( y ^ n ) = ( z ^ n ) ) -> ( x = 0 \/ y = 0 ) ) )
```

Over 19,000 proofs have been worked out in Metamath, including some [well known theorems](http://us.metamath.org/mpegif/mmset.html#theorems). [Metamath 100](http://us.metamath.org/mm_100.html) currently lists 63 proofs for [“top 100” theorems](http://www.cs.ru.nl/~freek/100/) maintained by [Freek Wiedijk](http://www.cs.ru.nl/~freek/), behind more popular systems HOL Light (86), Isabelle (74) and Mizar (65). An algorithm has been proposed by [Carneiro (2015)](https://arxiv.org/abs/1412.8091) to convert HOL Light proofs into Metamath, but it is not yet implemented.

Metamath is built for extreme simplicity. It has only one rule, substitution, that replaces symbols with various expressions. Starting with the well-known Zermelo-Frankel set theory with choice (ZFC), all of math (that most people care about) follows from 22 [axioms](http://us.metamath.org/mpegif/mmset.html#axioms) (4 axioms for [propositional calculus](http://us.metamath.org/mpegif/mmset.html#scaxioms), 11 for [predicate calculus](http://us.metamath.org/mpegif/mmset.html#pcaxioms), and 7 for [ZFC](http://us.metamath.org/mpegif/mmset.html#staxioms)). The flipside of simplicity is long and tedious proofs. The proof of “2+2=4” is a theorem named [2p2e4](http://us.metamath.org/mpegif/2p2e4.html) that has 10 steps, all of which can be expanded further into more basic blocks such as [df-2](http://us.metamath.org/mpegif/df-2.html), the definition of “2”. All proof steps can be mechanically followed without any semantic understanding of math. This is better experienced when readers follow a proof with unfamiliar symbols, such as [aleph1re](http://us.metamath.org/mpegif/aleph1re.html), and can be really confusing when symbols in referenced theorems overlaps with those in the main proof ([id1](http://us.metamath.org/mpegif/id1.html)). [Metamath Proof Explorer Home Page](http://us.metamath.org/mpegif/mmset.html) is an excellent tutorial.

## References

* 2015 June 18, Mario Carneiro. [Conversion of HOL Light proofs into Metamath](https://arxiv.org/abs/1412.8091). *arXiv:1412.8091*.


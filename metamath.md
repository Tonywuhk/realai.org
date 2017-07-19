---
permalink: /metamath/
---
# Metamath

Metamath is a simple text-based language that can be used to encode mathematical theorems and proofs. For example, the statement of [Fermat's Last Theorem](https://en.wikipedia.org/wiki/Fermat%27s_Last_Theorem) can be encoded as

```metamath
|- ( ( x e. ZZ /\ y e. ZZ /\ z e. ZZ /\ n e. ( ZZ>= ` 3 ) ) -> ( ( ( x ^ n ) + ( y ^ n ) = ( z ^ n ) ) -> ( x = 0 \/ y = 0 ) ) )
```

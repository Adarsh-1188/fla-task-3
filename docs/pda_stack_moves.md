# PDA Stack Moves

## Balanced parentheses `(()())`
| Step | Input | Action | Stack |
|---:|---|---|---|
|0|—|start|Z|
|1|( |push|Z(|
|2|( |push|Z((|
|3|)|pop|Z(|
|4|( |push|Z((|
|5|)|pop|Z(|
|6|)|pop|Z|
|7|—|accept|Z|

## Palindrome `abba`
Conceptual nondeterministic PDA: push `a`, push `b`, guess the middle, read `b` and pop `b`, read `a` and pop `a`, then accept.

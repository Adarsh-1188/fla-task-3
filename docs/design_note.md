# Design Note – PDA and CFG Case Studies

## 1. Arithmetic Expression Validation
CFG:
```text
E -> T E'
E' -> + T E' | epsilon
T -> F T'
T' -> * F T' | epsilon
F -> ( E ) | id
```
This grammar gives `*` higher precedence than `+` and supports nested parentheses.
Accepted: `a`, `a+b`, `a*b`, `a+b*c`, `(a+b)*c`. Rejected: `a+`, `+a`, `a**b`, `(a+b`, `a+b)`.

## 2. Balanced Parentheses
CFG: `S -> (S)S | epsilon`. PDA pushes an opening parenthesis and pops on a closing parenthesis. Accepted: `()`, `(())`, `()()`, `(()())`, `((()))`. Rejected: `(`, `)`, `())(`, `(()`, `())`.

## 3. Palindrome
CFG: `S -> aSa | bSb | a | b | epsilon`. The PDA pushes the first half, guesses the middle, then pops matching symbols from the second half. Accepted: `a`, `b`, `aa`, `aba`, `abba`, `aabbaa`. Rejected: `ab`, `aabb`, `abab`, `abb`, `aaba`, `abc`.

## Why FA is insufficient
A DFA has finite memory. Arbitrarily nested parentheses require unbounded stack-like memory. A general palindrome requires remembering an arbitrarily long first half. A PDA provides stack memory for these context-free patterns.

## Ambiguity/determinism
The arithmetic grammar separates expressions into terms and factors to establish precedence. The parentheses grammar is a standard unambiguous form. A general palindrome PDA is naturally nondeterministic because it must guess the midpoint.

## Syntax vs semantics
These models check structure, not meaning. Real systems additionally need symbol tables, type checking, database lookup, authentication, and business rules.

## SDG 9
Automated syntax processing supports reliable software infrastructure and digital systems, aligning the project with SDG 9 – Industry, Innovation and Infrastructure.

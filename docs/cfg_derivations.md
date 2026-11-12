# CFG Derivations

## Arithmetic `a+b`
```text
E => T E' => F T' E' => id E' => id + T E' => id + F T' E' => id + id E' => id + id
```

## Parentheses `()()`
```text
S => (S)S => ()S => ()(S)S => ()()S => ()()
```

## Palindrome `abba`
```text
S => aSa => abSba => abba
```

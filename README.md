Quick and dirty tool for generating passwords, given a word or list of words. Useful if you think a person may use certain words (e.g., name, birthday, etc.) in their password.

Supports: 
- Capitalization and non-capitalization
- Arbitrary number of end digits
- Passwords starting with a hashtag
- Passwords ending with an exclamation point
- Common substitutions, for example `@` for `a`, or `!` for `i`

```
usage: permutor.py [-h] [-n DIGITS] [-nS] [-nL] WORDS [WORDS ...]

Generate potential passwords from a given word or list of words

positional arguments:
  WORDS                 words used to generate passwords

optional arguments:
  -h, --help            show this help message and exit
  -n DIGITS, --digits DIGITS
                        maximum number of digits at the end of a password
  -nS, --no-special     do not include permutations with `#` at the beginning
                        and `!` at the end
  -nL, --no-substitutions
                        do not include common letter substitutions, for
                        example `@` for `a
```

###  Example 1

```
$ python permutor.py apple | head -10
\#@pple26!
@pple32!
apple98!
apple45!
Appl385!
\#Appl332
\#Appl333
\#Appl330
\#Appl331
\#Appl336
```

### Example 2

```
$ python permutor.py tom brady | head -10
BradyTom95!
\#bradyT0m34!
\#bradyT0m43!
bradyt0m69!
BradyT0m95!
br@dyTom76!
Br@dyT0m60!
\#tom59!
Br@dyT0m35!
Tom27
```

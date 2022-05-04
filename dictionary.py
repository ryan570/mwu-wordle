from re import match as rematch

from numpy import add_docstring

with open('lists/answers.txt') as f:
    words = f.read().splitlines()[2:]

def match(pattern, guess):
    exact = [letter if pattern[i] == 2 else '.' for i, letter in enumerate(guess)]
    contains = [letter for i, letter in enumerate(guess) if pattern[i] == 1]
    block = [letter for i, letter in enumerate(guess) if pattern[i] == 0]

    p = ""
    for c in contains:
        p += f'(?=.*{c}.*)'

    ignore = set(block) - set(contains)
    for i in range(5):
        if pattern[i] == 2:
            p += guess[i]
        elif len(ignore) > 0:
            p += f'[^{"".join(ignore)}]'
        else:
            p += '.'

    test = list(filter(lambda m: rematch(p, m), words))
    return set(test)

# print(match([0, 1, 0, 0, 0], 'salet') & match([0, 0, 1, 0, 1], 'curio') & match([2, 1, 0, 1, 0], 'arbor'))

# GREAN
# ERNE


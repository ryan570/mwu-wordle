from re import match as rematch

with open('lists/answers.txt') as f:
    words = f.read().splitlines()[2:]

def match(pattern, guess):
    """Matches a particular pattern with a guess to cut down on 'words' list."""
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

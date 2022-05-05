from re import match as rematch

# Retrieve word list
with open('lists/answers.txt') as f:
    words = f.read().splitlines()[2:]

def match(pattern, guess):
    """Matches a particular pattern with a guess to cut down on 'words' list."""
    # exact = [letter if pattern[i] == 2 else '.' for i, letter in enumerate(guess)]

    # Handle correct letter in wrong position (yellow)
    contains = [letter for i, letter in enumerate(guess) if pattern[i] == 1]

    # Handle letters that don't exist in the word (gray)
    block = [letter for i, letter in enumerate(guess) if pattern[i] == 0]

    # Create regex pattern
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

    # Pattern matching to find remaining possible words
    remaining = list(filter(lambda m: rematch(p, m), words))
    return set(remaining)

# print(match([0, 1, 0, 0, 0], 'salet') & match([0, 0, 1, 0, 1], 'curio') & match([2, 1, 0, 1, 0], 'arbor'))
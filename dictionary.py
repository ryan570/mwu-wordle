from re import match as rematch

# Retrieve answers list
with open('lists/answers.txt') as f:
    answers = f.read().splitlines()[2:]

# Retrieve word list
with open('lists/dictionary.txt') as f:
    words = f.read().splitlines()[2:]

letters = set(chr(c + 97) for c in range(26))


def match(pattern, guess, all=False):
    """Matches a particular pattern with a guess to cut down on 'words' list."""
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
    remaining = list(filter(lambda m: rematch(p, m), words if all else answers))
    return set(remaining)

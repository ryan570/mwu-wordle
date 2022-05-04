from re import match as rematch

with open('lists/dictionary.txt') as f:
    words = f.read().splitlines()[2:]

def match(pattern, guess):
    exact = [letter if pattern[i] == 2 else '.' for i, letter in enumerate(guess)]
    contains = [letter for i, letter in enumerate(guess) if pattern[i] == 1]
    block = [letter for i, letter in enumerate(guess) if pattern[i] == 0]

    initial = list(filter(lambda m: rematch(f"^{''.join(exact)}$", m), words))
    return list(filter(lambda x: all(c in x for c in contains) and all(b not in x for b in block), initial))

print(match([0, 0, 1, 2, 0], 'curio'))
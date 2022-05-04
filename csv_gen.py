import csv
from wordle import Wordle
from dictionary import words
from solvers.one import one
from solvers.two import two
import numpy as np

N = 2
T = 1000

game = Wordle()
solvers = [one(), two()]
guess_counts = [[] for _ in range(T)]

for t in range(T):
    for n in range(N):
        game.reset(words[t])
        print(game.word)

        while not game.solved:
            guess = solvers[n].guess()
            feedback = game.guess(guess)
            print(guess, feedback)
            solvers[n].inform(feedback)
        
        guess_counts[t].append(game.guesses)
        solvers[n].reset()

with open('guesses.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(guess_counts)

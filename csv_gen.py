import csv
from wordle import Wordle
from dictionary import words
from solvers.one import one
from solvers.two import two
from solvers.three import three
from solvers.four import four
from solvers.five import five
import numpy as np

N = 5
T = 1000

game = Wordle()
solvers = [one(), two(), three(), four(), five()]
guess_counts = [[] for _ in range(T)]

for t in range(T):
    for n in range(N):
        game.reset(words[t])
        if t % 20 == 0:
            print(t, game.word)

        while not game.solved:
            guess = solvers[n].guess()
            feedback = game.guess(guess)
            if t % 20 == 0:
                print(guess, feedback)
            solvers[n].inform(feedback)
        
        guess_counts[t].append(game.guesses)
        solvers[n].reset()

with open('guesses.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(guess_counts)

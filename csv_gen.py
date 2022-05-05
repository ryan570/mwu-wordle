import csv

from dictionary import words
from solvers.SolverOne import SolverOne
from solvers.SolverThree import SolverThree
from solvers.SolverTwo import SolverTwo
from wordle import Wordle

# Number of algorithms/experts
N = 3

# Number of words to run through
T = 1000

# Initialize new game, algorithms, as well as guess counts for each algorithm
game = Wordle()
solvers = [SolverOne(), SolverTwo(), SolverThree()]
guess_counts = [[] for _ in range(T)]

# Generate data for csv file
for t in range(T):
    for n in range(N):
        game.reset(words[t])
        print(game.word)

        while not game.solved:
            guess = solvers[n].guess()
            feedback = game.guess(guess)

            solvers[n].inform(feedback)
        
        guess_counts[t].append(game.guesses)
        solvers[n].reset()

# Write guess counts to guesses.csv
with open('guesses.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(guess_counts)

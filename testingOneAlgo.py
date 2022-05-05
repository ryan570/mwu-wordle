from dictionary import words
from solvers.SolverFour import SolverFour
from wordle import Wordle
import random
from statistics import mean
from statistics import variance

# Number of algorithms/experts
N = 1

# Number of words to run through
T = 50

# Initialize new game, algorithms, as well as guess counts for each algorithm
game = Wordle()
solvers = [SolverFour()]
guess_counts = []

# Generate data for csv file
for t in range(T):
    for n in range(N):
        game.reset(random.choice(tuple(words)))
        print(t, game.word)

        while not game.solved:
            guess = solvers[n].guess()
            feedback = game.guess(guess)
            solvers[n].inform(feedback)
            print(guess, feedback)
        
        guess_counts.append(game.guesses)
        solvers[n].reset()

means = mean(guess_counts)
variances = variance(guess_counts)
print(means, variances)
import csv
import math
from statistics import mean
from statistics import variance

import numpy as np


# Number of algorithms/experts
N = 8

# Number of words to run through
T = 2309

# Initialize hyperparamters
epsilon = math.sqrt(math.log(N) / T) 
rho = 8 # Maximum absolute value of error

# Initialize weights to 1
weights = [1] * N

# Read guess counts from guesses.csv
guess_counts = [ [] for i in range(N) ]
with open('guesses.csv', newline='') as csvfile:
	csv_reader = csv.reader(csvfile, delimiter=',')

	for row in csv_reader:
		for n in range(N):
			guess_counts[n].append(int(row[n]))
			

# MWU algorithm
for t in range(T):
	# Generate probabilities of choosing each algorithm
	probs = [w / sum(weights) for w in weights]

	# Randomly choose an algorithm according to distribution
	chosen = np.random.choice(N, p=probs)

	# Record chosen guess count from chosen algorithm
	outcome = guess_counts[chosen][t]

	# Update weights
	weights[chosen] = weights[chosen] * (1 - epsilon * ((outcome - 4) / rho))   

# Final weights
means = [0]*N
variances = [0]*N
for n in range(N):
	means[n] = mean(guess_counts[n])
	variances[n] = variance(guess_counts[n])

print("mean guesses: ", means)
print("variance: ", variances)
print("weights: ", weights)

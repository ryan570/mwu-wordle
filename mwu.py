import numpy as np
import math
import csv

# Number of algorithms/experts
N = 3

# Number of words to run through
T = 1000

# Initialize hyperparamters
epsilon = math.sqrt(math.log(N) / T) 
rho = 5 # Maximum absolute value of error

# Initialize weights to 1
weights = [1] * N

# Read guess counts from guesses.csv
guess_counts = [ [] for i in range(N) ]
with open('guesses.csv', newline='') as csvfile:
	csv_reader = csv.reader(csvfile, delimiter=',')

	for row in csv_reader:
		guess_counts[0].append(int(row[0]))
		guess_counts[1].append(int(row[1]))
		guess_counts[2].append(int(row[2]))
		# guess_counts[3].append(int(row[3]))
		# guess_counts[4].append(int(row[4]))

# MWU algorithm
for t in range(T):
	# Generate probabilities of choosing each algorithm
	probs = [w / sum(weights) for w in weights]

	# Randomly choose an algorithm according to distribution
	chosen = np.random.choice(N, p=probs)

	# Record chosen guess count from chosen algorithm
	outcome = guess_counts[chosen][t]

	# Update weights
	weights[chosen] = weights[chosen] * (1 - epsilon * ((outcome - 3.92) / rho))   

# Final weights
print(weights)
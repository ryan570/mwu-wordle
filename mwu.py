import numpy as np
import math
import csv

T = 1000
N = 2

epsilon = math.sqrt(math.log(N) / T)
rho = 5 # ?
weights = [1] * N

guess_counts = [ [] for i in range(N) ]
with open('guesses.csv', newline='') as csvfile:
	csv_reader = csv.reader(csvfile, delimiter=',')

	for row in csv_reader:
		guess_counts[0].append(int(row[0]))
		guess_counts[1].append(int(row[1]))
		# guess_counts[2].append(int(row[2]))
		# guess_counts[3].append(int(row[3]))
		# guess_counts[4].append(int(row[4]))

for t in range(T):
    probs = [w / sum(weights) for w in weights]
    chosen = np.random.choice(N, p=probs)

    outcome = guess_counts[chosen][t]
    weights[chosen] = weights[chosen] * (1 - epsilon * ((outcome - 3.92) / rho))   

print(weights)
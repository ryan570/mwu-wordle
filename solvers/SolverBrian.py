from dictionary import words, match
from collections import Counter
import random

# ALL ALGOS NEED TO FOLLOW THIS INTERFACE
class SolverBrian:
    """
    Algorithm 4:
    Next word decision: chooses next word based on using the letters with the highest frequency in the remaining words

    Note: Always starts with "alert" because a, l, e, r, and t have the highest frequency for the words in our word bank
    - particularly bad at picking words with double letters

    guesses: An array storing all guesses that have been made
    first_guesses: An array storing the starting guesses
    curr_guess: The current guess index
    info: A dictionary storing all information the algorithm has gathered from the guesses; (key, value) => ("guess", [0, 1, 2, 1, 0])
    possible_guesses: A set of all possible remaining answers
    """
    def __init__(self):
        self.guesses = []
        self.first_guesses = ["alert"]
        self.curr_guess = 0

        self.info = {} # (key, value) => ("guess", [0, 1, 2, 1, 0])
        self.possible_guesses = set(words)

    def guess(self):
        # print(self.guesses)
        if self.curr_guess < len(self.first_guesses):
            self.guesses.append(self.first_guesses[self.curr_guess])
            self.curr_guess += 1
            return self.guesses[-1]
        
        self.curr_guess += 1
        freq = {i : str(self.possible_guesses).count(i) for i in str(self.possible_guesses)}
        optimal_guess = ''
        optimal_guess_sum = 0
        for word in self.possible_guesses:
            sum = 0
            for i in ''.join(set(word)):
                sum += freq[i]
            if sum > optimal_guess_sum:
                optimal_guess = word
                optimal_guess_sum = sum

        self.guesses.append(optimal_guess)
        return self.guesses[-1]

    def inform(self, feedback):
        self.curr_guess += 1
        self.possible_guesses &= match(feedback, self.guesses[-1])

    def reset(self):
        self.curr_guess = 0
        self.info.clear()
        self.guesses.clear()
        self.possible_guesses = set(words)
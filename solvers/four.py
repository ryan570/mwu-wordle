from dictionary import words, match
import random

# ALL ALGOS NEED TO FOLLOW THIS INTERFACE
class four:
    def __init__(self):
        self.guesses = []
        self.first_guesses = []
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
        self.guesses.append(random.choice(tuple(self.possible_guesses)))
        return self.guesses[-1]

    def inform(self, feedback):
        self.possible_guesses &= match(feedback, self.guesses[-1])

    def reset(self):
        self.curr_guess = 0
        self.info.clear()
        self.guesses.clear()
        self.possible_guesses = set(words)

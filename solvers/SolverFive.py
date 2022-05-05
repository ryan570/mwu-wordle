from dictionary import answers, match
import random

# ALL ALGOS NEED TO FOLLOW THIS INTERFACE
class SolverFive:
    """
    Algorithm 5:
    Starting word combo: "glent" + "brick" + "jumpy" + "vozhd" + "waqfs"

    Covers 25 letters of the English alphabet (everything except x, one of the rarer letters).

    guesses: An array storing all guesses that have been made
    first_guesses: An array storing the starting guesses
    curr_guess: The current guess index
    info: A dictionary storing all information the algorithm has gathered from the guesses; (key, value) => ("guess", [0, 1, 2, 1, 0])
    possible_guesses: A set of all possible remaining answers
    """
    def __init__(self):
        self.guesses = []
        self.first_guesses = ["glent", "brick", "jumpy", "vozhd", "waqfs"]
        self.curr_guess = 0

        self.info = {} # (key, value) => ("guess", [0, 1, 2, 1, 0])
        self.possible_guesses = set(answers)

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
        self.possible_guesses = set(answers)

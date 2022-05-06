import random

from Levenshtein import distance

from dictionary import match, words


class SolverLevenshtein:
    """
    Algorithm 1:
    Starting word: none

    Random starting word, good for a baseline of comparison for other algorithms. 

    guesses: An array storing all guesses that have been made
    first_guesses: An array storing the starting guesses
    curr_guess: The current guess index
    info: A dictionary storing all information the algorithm has gathered from the guesses; (key, value) => ("guess", [0, 1, 2, 1, 0])
    possible_guesses: A set of all possible remaining answers
    """
    def __init__(self):
        self.guesses = []
        self.first_guesses = ["crane"]
        self.curr_guess = 0
        self.info = {}
        self.possible_guesses = set(words)

    def guess(self):
        """Handles a guess."""
        # Starting words
        if self.curr_guess < len(self.first_guesses):
            self.guesses.append(self.first_guesses[self.curr_guess])
            self.curr_guess += 1
            return self.guesses[-1]
        
        self.curr_guess += 1
        # Randomly choose from possible guesses
        possible = list(self.possible_guesses)

        best_word = possible[0]
        best_word_distance = distance(possible[0],self.guesses[-1])
        for word in possible:
            if distance(word,self.guesses[-1]) > best_word_distance:
                best_word = word
                best_word_distance = distance(word,self.guesses[-1])
        
        #print(best_word)
        self.guesses.append(best_word)
        return self.guesses[-1]

    def inform(self, feedback):
        """Cuts down on possible_guesses."""
        self.possible_guesses &= match(feedback, self.guesses[-1])

    def reset(self):
        """Resets solver."""
        self.guesses.clear()
        self.curr_guess = 0
        self.info.clear()
        self.possible_guesses = set(words)

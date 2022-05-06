import random
from re import I

from Levenshtein import distance

from dictionary import match, words


class SolverLevenFreq:
    """
    Algorithm 1:
    Starting word: crane
    
    Go through the list of possible valid words and choose the word with the greatest Levenshtein Distance to the previous guess.
    

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
        
        possible = list(self.possible_guesses)

        best_word = possible[0]
        best_word_distance = self.distance_to_all(best_word,self.guesses)

        #Go through each word and pick the word with the greatest distance to the previous guess
        good_words = [best_word]

        for word in possible:
            if self.distance_to_all(word,self.guesses) > best_word_distance:
                best_word = word
                best_word_distance = self.distance_to_all(word,self.guesses)
            elif self.distance_to_all(word,self.guesses) ==best_word_distance:
                good_words.append(word)
        
        if len(good_words)<2:
            self.guesses.append(best_word)
            return self.guesses[-1]

   
        
        freq = {i : str(self.possible_guesses).count(i) for i in str(self.possible_guesses)}
        optimal_guess = ''
        optimal_guess_sum = 0
        for word in good_words:
            sum = 0
            for i in ''.join(set(word)):
                sum += freq[i]
            if sum > optimal_guess_sum:
                optimal_guess = word
                optimal_guess_sum = sum

        
        self.guesses.append(optimal_guess)
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

    def distance_to_all(self,word,guesses):
        total = 0
        for guess in guesses:
            total+=distance(word,guess)
        return total


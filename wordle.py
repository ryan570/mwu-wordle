from collections import Counter

# test the guess feedback for edge cases, I have not tested this very thoroughly but I think it might be right
class Wordle:
    def __init__(self):
        self.guesses = 0
        self.solved = False

    def guess(self, guess):
        # return list where 0 = gray, 1 = yellow, 2 = green
        out = [0] * 5
        temp_word = list(self.word)
        temp_guess = list(guess)

        for i in [i for i, letter in enumerate(self.word) if letter == guess[i]]:
            temp_word[i] = ' '
            temp_guess[i] = ' '

            out[i] = 2

        for i, g in enumerate(temp_guess):
            if g != ' ':
                if g in temp_word:
                    temp_word[temp_word.index(g)] = ' '
                    out[i] = 1

        self.guesses += 1
        if sum(out) == 10:
            self.solved = True

        return out

    def reset(self, new_word):
        self.word = new_word
        self.guesses = 0
        self.solved = False
                        
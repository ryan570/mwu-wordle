class Wordle:
    """
    Simulates a Wordle game with unlimited guesses.

    guesses: An integer count of the number of guesses that have been made
    solved: A boolean representing if the Wordle has been completed
    word: A string representing the answer word (won't be initialized)
    """
    def __init__(self):
        self.guesses = 0
        self.solved = False

    def guess(self, guess):
        """Handles a guess."""
        # Represents state of the game; 0 = gray, 1 = yellow, 2 = green
        out = [0] * 5
        temp_word = list(self.word)
        temp_guess = list(guess)

        # Finds correct letter in correct position (green)
        for i in [i for i, letter in enumerate(self.word) if letter == guess[i]]:
            temp_word[i] = ' '
            temp_guess[i] = ' '

            out[i] = 2

        # Finds correct letter in wrong position (yellow)
        for i, g in enumerate(temp_guess):
            if g != ' ':
                if g in temp_word:
                    temp_word[temp_word.index(g)] = ' '
                    out[i] = 1

        self.guesses += 1

        # Wordle has been solved; out = [2, 2, 2, 2, 2]
        if sum(out) == 10:
            self.solved = True

        return out

    def reset(self, new_word):
        """Resets game."""
        self.guesses = 0
        self.solved = False
        self.word = new_word
                        
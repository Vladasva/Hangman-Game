import random


class WordToGuess:

    def __init__(self, words):
        self.words = words
        self.word = ""
        self.hided_word = ""
        self.guesses = 0

    def choose_word(self):
        self.word = random.choice(self.words)
        return self.word

    def guess(self):
        self.guesses = len(self.word) + 2
        return self.guesses
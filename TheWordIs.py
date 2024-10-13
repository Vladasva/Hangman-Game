class TheWordIs:

    def __init__(self, word, guessed_letter):
        self.word = word
        self.guessed_letter = guessed_letter
        self.indexes = []
        self.guessed_letters_indexes = []
        self.response = ""
        self.guessed_letters = []

    def is_letter_in_word(self):
        self.indexes = [i for i, letter in enumerate(self.word) if letter == self.guessed_letter]
        return self.indexes

    def show_the_word(self, indexes):
        for inner_list in indexes:
            for index in inner_list:
                self.guessed_letters_indexes.append(index)

        word_list = list(self.word)
        for index in range(0, len(word_list)):
            if word_list[index] != self.guessed_letter and index not in self.guessed_letters_indexes:
                word_list[index] = "_"
        self.response = "".join(word_list)
        return self.response

    def was_letter_guessed(self, guessed_letters):
        if self.guessed_letter not in guessed_letters:
            guessed_letters.append(self.guessed_letter)
        return guessed_letters

    def is_word_guessed(self):
        if self.word == self.response:
            print("Congratulations! You have guessed the word!")
            return False
        else:
            return True

    @staticmethod
    def guess_controler(guesses):
        if guesses == 0:
            return False
        else:
            return True




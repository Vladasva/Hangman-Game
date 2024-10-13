from WordToGuess import WordToGuess
from TheWordIs import TheWordIs

words = ["apple", "banana", "mango", "strawberry", "orange", "grape", "pineapple",
         "apricot", "lemon", "coconut", "watermelon", "cherry", "papaya", "berry", "peach",
         "lychee", "muskmelon"]

word_mechanism = WordToGuess(words)
word = word_mechanism.choose_word()
guesses = word_mechanism.guess()


def play_game(word, guesses):
    guessed_letters = []
    indexes = []
    flag = True
    while flag:
        print("Guess the word! HINT: word is a name of a fruit")
        guessed_letter = input("Enter a letter to guess: ")
        if guessed_letter.isalpha() and len(guessed_letter) == 1:
            guessing_mechanism = TheWordIs(word, guessed_letter)
            flag = guessing_mechanism.guess_controler(guesses)
            if guessed_letter in guessed_letters:
                print("You have already guessed this letter.")
            else:
                guesses -= 1
                indexes.append(guessing_mechanism.is_letter_in_word())
                word_is = guessing_mechanism.show_the_word(indexes)
                print(f'The word is {word_is}')
                guessed_letters = guessing_mechanism.was_letter_guessed(guessed_letters)
                is_guessed = guessing_mechanism.is_word_guessed()
                if is_guessed:
                    flag = is_guessed
                else:
                    flag = is_guessed
                if guesses == 0 and flag:
                    print("You have used all the guesses. Please, try again!")
                    break
        else:
            print("Please, enter a letter")
            guesses -= 1


play_game(word, guesses)


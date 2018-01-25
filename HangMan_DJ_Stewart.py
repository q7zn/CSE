import random
import string
'''
general guide for hangman
make a word bank, ten items
pick a random item from the list
take in a letter and add it to a list of letters_guessed
hide and reveal letters
create win condition
'''

guesses_left = 10
letters_guessed = list(string.punctuation + " ")

word_list = ["hidden word", "word is hidden", "computer class", "Mister Wiebe's class", "find the way", "whiteboard",
             "desktop", "painting", "t pose", "keyboard"]


hidden_word = random.choice(word_list)
print(hidden_word)


while hidden_word != "stop":
    output = []
    for letter in hidden_word:
        if letter in letters_guessed:
            output.append(letter)
        else:
            output.append("*")
    print(output)

    guessed_letter = input("Guess any letter in the alphabet.   ")
    letters_guessed.append(guessed_letter)
    # print(letters_guessed)

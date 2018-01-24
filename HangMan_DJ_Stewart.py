import random
'''
general guide for hangman
make a word bank, ten items
pick a random item from the list
take in a letter and add it to a list of letters_guessed
hide and reveal letters
create win condition
'''

guesses_left = 10
letters_guessed = []

word_list = ["hidden word", "word is hidden", "computer class", "Mister Wiebe's class", "find the way", "whiteboard",
             "desktop", "painting", "t pose", "keyboard"]

hidden_word = [random.choice(word_list)]
guessed_letter = input("Guess any letter in the alphabet.")
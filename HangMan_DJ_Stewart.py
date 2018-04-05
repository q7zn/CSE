import random
import string

guesses_left = 10
letters_guessed = list(string.punctuation + " ")

word_list = ["hidden word", "word is hidden", "computer class", "mister wiebe's class", "find the way", "whiteboard",
             "desktop", "painting", "t pose tuesday", "keyboard"]


hidden_word = random.choice(word_list)
#  print(hidden_word)  # comment this out before turning in


output = ["*"]
while guesses_left > 0 and "*" in output:
    output = []
    for letter in hidden_word:
        if letter in letters_guessed:
            output.append(letter)
        else:
            output.append("*")
    s = ""
    print(s.join(output))

    if "*" not in output:
        print("Congratulations! You guessed the word! You had %s guesses remaining. Good job!" % guesses_left)
        continue

    guessed_letter = input("Guess any letter in the alphabet.   ")
    letters_guessed.append(guessed_letter)

    if guessed_letter not in hidden_word:
        guesses_left -= 1
        print("Nope. That's not a letter in the word. You have %s guesses left." % guesses_left)
    if guesses_left == 0:
        print('You lost. The word you were attempting to guess was "%s."' % hidden_word)
    # print(letters_guessed)


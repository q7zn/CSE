import random

guessesTaken = 0

print('Oh, hello there! What is your name?')
myName = input()
global guess
number = random.randint(1, 50)
print(myName + "?!?! " + "That's a terrible name! I would feel bad for you, but I'm not programmed to."
               " Anyway, " + myName + ", I am thinking of a number between 1 and 50.")

while guessesTaken < 5:
    print("Take a shot at the number I'm thinking of.")
    guess = input()
    guess = int(guess)

    guessesTaken = guessesTaken + 1

    if guess < number:
        print('Go higher. Your guess is too low.')

    if guess > number:
        print('Overshot it there, go lower. Your guess is too high.')

    if guess == number:
        break

    if guess == number:
        guessesTaken = str(guessesTaken)
        print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')

if guess != number:
    number = str(number)
print('Nope. The number I was thinking of was ' + number)

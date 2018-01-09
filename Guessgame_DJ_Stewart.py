import random

guessesTaken = 0

print('Oh, hello human! What is your name?')
myName = input()
number = random.randint(1, 50)
print(myName + "?!?! " + "That's a terrible name! I would feel bad for you, but I'm not programmed to."
               " Anyway, " + myName + ", I am thinking of a number between 1 and 50.")
guess = ""

while int(guessesTaken) < 5:
    print("Take a shot at the number I'm thinking of.")
    guess = input()
    guess = int(guess)

    guessesTaken = guessesTaken + 1

    if guess > 50:
        print("Dude, I said one through fifty! Is it really that hard to hit two different numbers that are almost "
              "all the way across the keyboard from each other? You should be playing \na typing games instead...")

    if guess < 1:
        print("C'mon, man, I said one through fifty. You can't guess lower than 1 by accident! Get with the program.")

    if guess < number:
        print('Go higher. Your guess is too low.')

    if guess > number:
        print('Overshot it there, go lower. Your guess is too high.')

    if guess == number:
        guessesTaken = str(guessesTaken)
        print('Good job, ' + myName + '! God knows how many times it took you to run this code to '
                                      'actually beat the game. You guessed my number in ' + guessesTaken + ' guesses!')

    if guess == number:
        break

if guess != number:
    number = str(number)
    print("Nope. Turns out you're a terrible guesser. The number I was thinking of was " + number)

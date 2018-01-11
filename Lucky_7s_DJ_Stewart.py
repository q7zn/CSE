import random

print("Welcome to Lucky Sevens. You have fifteen dollars, and you must place a bet of one dollar every round.")
print("You will then roll two die with six sides, and if the numbers add up to seven, you win five dollars.")
print("Let's get started. Good luck!")

money_owned = 15


def roll():
    return random.randint(1, 6)


dice_1 = roll()
dice_2 = roll()

while money_owned > 0:
    print("Okay. You have %s dollars. I'll take a dollar, now roll your die. Go ahead and roll." % money_owned)
    if (dice_1 + dice_2) == 7:
        print("Nice! you rolled a seven! Here's five dollars, since you won the round.")
        money_owned += 5
    elif money_owned != 7:
        print("Dang, that's a bummer. You rolled a %s. Roll again." % (dice_1 + dice_2))
        roll()
    money_owned -= 1
    if money_owned == 0:
        print("Congratulations! You managed to blow all your money gambling. You lost your money in %s rounds.")

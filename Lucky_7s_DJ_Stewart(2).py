import random

print("Welcome to Lucky Sevens. You have fifteen dollars, and you must place a bet of one dollar every round.")
print("You will then roll two die with six sides, and if the numbers add up to seven, you win five dollars.")
print("Let's get started. Good luck!")


def lucky_7s(dice_1, dice_2, money_owned, highest_round, most_money):
    if money_owned < 0:
        if most_money < money_owned:
            most_money = money_owned
            highest_round = round
        round += 1
        money_owned -= 1
        dice_1 = random.randint(1, 6)
        dice_2 = random.randint(1, 6)
        if dice_1 + dice_2 == 7:
            money_owned += 5
            print("Nice! You rolled a seven!")
            lucky_7s(dice_1, dice_2, money_owned, highest_round, most_money)
        elif dice_1 + dice_2 != 7:
            print("You rolled a %s. That's not a seven, unfortunately. I'll keep your money." % (dice_1 + dice_2))
            lucky_7s(dice_1, dice_2, money_owned, highest_round, most_money)
    else: print("Congratulations, you blew all your money gambling. You lost all your money to me in %d rounds. You "
                "had the most amount of money, %d,  at round %d." %(round, most_money, highest_round))


lucky_7s(0, 0, 0, 15, 0, 0)

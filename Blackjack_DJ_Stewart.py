import random

print("Heyo and welcome to Blackjack! The terrible gambling game where I get all your money at some point or another!")
print("I'll tell you the rules. I'll give you two cards and you'll see how much it equals. I'll give you more")
print(" cards as you tell me to, but be careful. If you go over twenty-one, you bust. Anyway, let's get started")

random.randint(1, 13)


def lucky_7s(card_1, card_2, round, money_owned, highest_round, most_money):
    if money_owned > 0:
        if most_money < money_owned:
            most_money = money_owned
            highest_round = round
        round += 1
        money_owned -= 1
        card_1 = random.randint(1, 11)
        card_2 = random.randint(1, 11)
        if card_1 + card_2 <= 21:
            money_owned += 5
            print("Nice! You rolled a seven!")
            lucky_7s(card_1, card_2, round, money_owned, highest_round, most_money)
        elif card_1 + card_2 != 7:
            print("You rolled a %s. That's not a seven, unfortunately. I'll keep your money." % (card_1 + card_2))
            lucky_7s(card_1, card_2, round, money_owned, highest_round, most_money)
    if money_owned == 0:
        print("Congratulations, you blew all your money gambling. You lost all your money to me in %d rounds. "
              "You had the most amount of money, %d,  at round %d." % (round, most_money, highest_round))


lucky_7s(random.randint(1, 6), random.randint(1, 6), 1, 15, 1, 15)

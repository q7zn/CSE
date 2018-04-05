import math
# Defining functions


def hello_world():
    print("Hello World")


hello_world()


def square_it(number):
    return number**2


print(square_it(3))


def bill_plus_tip_calc(bill):
    tax_amt = bill * 0.18
    total_bill = bill + tax_amt
    return total_bill


print("Your bill is $%d." % bill_plus_tip_calc(1))


def distance_calc(x1, y1, x2, y2):
    inside = (x1 - x2) ** 2 + (y1 - y2) ** 2
    answer = math.sqrt(inside)
    return answer


print(distance_calc(0, 0, 3, 4))


def pythag_calc(a, b):
    c = math.sqrt(a ** 2 + b ** 2)
    return c


print(pythag_calc(5, 12))

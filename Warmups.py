"""def reverse_order():
    first_name: input()
    last_name: input()


print(last_name)
print(" ")
print(first_name)
"""


def add_py(name):
    print(name + ".py")


add_py("your mom")

"""Write a function called 'add'
which takes three parameters
and prints the sum of the numbers
"""


def add(number_1, number_2, number_3):
    print(number_1 + number_2 + number_3)


add(15, 18, 9000)
add(80, 90, 100)


def repeat(sentence):
    print(sentence)
    print(sentence)
    print(sentence)


repeat("hello")

# here's a few fancier ways of doing the above function

for x in range(3):
    print("sentence")


def date(month, day, year):
    print(str(month) + "/" + str(day) + "/" + str(year))


date(12, 8, 17)
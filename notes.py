print("Hello, world!")

# DJ Stewart

a = 4
b = 3

print(3 + 5)
print(5 - 3)
print(3 * 5)
print(6 / 2)
print(3 ** 2)

print()
print("Try to figure out how this works")
print(13 % 5)

car_name = "The Dug-Mobile"
car_type = "Bugatti"
car_cylinders = 16
car_mpg = 5000.9

"""print("I have a car called %s. It's pretty nice." % car_name)
print("I have a car called %s. It's a %s." % (car_name, car_type))
print("What is your name?")
name = input(">_")
print("Hello %s." % name)
age = input("How old are you?")
print("%s?! That's really old. You belong in a retirement home." % age)
#this is a new line
this is another new line because Github was being weird"""


def print_hw():
    print("Hello, World!")
    print("Enjoy your day.")


print_hw()


def say_hi(name):
    print("Hello, %s" % name)
    print("Coding is great!")


say_hi("John")  # Name is a "parameter"


def print_age(name, age):
    print("%s is %d years old" % (name, age))
    age += 1  # age + 1
    print("Next year, %s will be %d year old." % (name, age))


print_age("John", 14)


def algebra_hw(x):
    return x**3 + 4*x**2 + 7 * x - 4


print(algebra_hw(3))
print(algebra_hw(4))
print(algebra_hw(5))
print(algebra_hw(6))
print(algebra_hw(7))

# if statements


def grade_calc(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 80:  # elif means else if
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    else:
        return "F"


print(grade_calc(59))

"""write a function call "happy_bday" that "sings" (prints) Happy Birthday

It must take one parameter called "name"
"""


def happy_bday(name):
    print("Happy Birthday to you" + ',')
    print("Happy Birthday to you" + ',')
    print("Happy Birthday dear " + name)
    print("Happy Birthday to you")


happy_bday("DJ")

# Loops

'''for num in range(10):
    print(num)
while a < 10:
    print(a)
    a += 1
'''

# random numbers
import random  # this should be on line 1
print(random.randint(0, 1000))

# New Python File: Warmups.py

# 12.4.17
# Write a Python function
# which accepts the user's
# first and last name
# and prints them in reverse order
# with a space in between them.

# Recasting
c = "1"
print(c == 1)  # we have a string and an integer.
# this should work.
print(int(c) == 1)
# or...
print(c == str(1))


# Comparisons

print(1 == 1)  # use a double equal sign
print(1 != 2)  # meaning: 1 is NOT equal to 2
print(not (1 != 1))  # "!" is the "not" operator
print(not False)

the_count = [1, 2, 3, 4, 5]
cheeseburger_ingredients = ['cheese', 'ground beef', 'thousand island', 'buns']
print(cheeseburger_ingredients[0])
print(cheeseburger_ingredients[3])
print(len(cheeseburger_ingredients))
print(len(the_count))

for generic_item_name in cheeseburger_ingredients:
    print(generic_item_name)

for num in the_count:
    print(num)

length = len(cheeseburger_ingredients)
range(5)  # A list of the numbers 0 through 4
range(len(cheeseburger_ingredients))  # Generates a list of all indices
for num in range(len(cheeseburger_ingredients)):
    item = cheeseburger_ingredients[num]
    print("The item at index %d is %s" % (num, item))


# Recasting into a list
strOne = "Hello World!"
listOne = list(strOne)
print(listOne)
listOne[11] = '.'
print(listOne)

# Adding things to a list
cheeseburger_ingredients.append("Fries")

# Remove things from a list
cheeseburger_ingredients.pop(1)
print(cheeseburger_ingredients)
cheeseburger_ingredients.remove("cheese")
print(cheeseburger_ingredients)

# Getting the alphabet
import string
print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.punctuation)

# Making things Lowercase
strTwo = "ThIs Is A VeRY oDd sEnTeNCe"
lowercase = strTwo.lower()
print(lowercase)

s = "-"
seq = ("a", "b", "c")  # This is sequence of strings.
print(s.join(seq))

#  Dictionaries - made up of (key: value) pair

dictionary = {"name": 'Lance', 'age': 26, 'height': 6 * 12 + 2}

# accessing things from a dictionary
print(dictionary["name"])
print(dictionary["age"])
print(dictionary["height"])
dictionary["profession"] = "telemarketer"
large_dictionary = {
    "CA": 'California',
    "AZ": "Arizona",
    "NY": "New York",
    "TX": "Texas"
}
print(large_dictionary['NY'])

larger_dictionary = {
    "CA": [
        'Fresno',
        'San Fransisco',
        "San Jose"
    ],
    'AZ': [
        "Phoenix",
        "Tuscon"
    ],
    'NY': [
        "New York City",
        "Brooklyn"
    ]
}
print(larger_dictionary['NY'])
print(larger_dictionary['NY'][1])
print(larger_dictionary['AZ'][0])
largest_dictionary = {
    'CA': {
        'NAME': 'California',
        'POPULATION': 39250000,
        'BORDER ST': [
            'Oregon',
            'Nevada',
            'Arizona'
        ]
    },
    'AZ': {
        'NAME': 'Arizona',
        'POPULATION': 6931000,
        'BORDER ST': [
            'California',
            'Utah',
            'Nevada',
            'New Mexico'
        ]
    },
    'NY': {
        'NAME': 'New York',
        'POPULATION': 19750000,
        'BORDER ST': [
            'Vermont',
            'Massachusetts',
            'Connecticut',
            'Pennsylvania',
            'New Jersey'
        ]
    }
}

current_node = (largest_dictionary['CA'])
print(current_node['NAME'])
print(current_node['POPULATION'])

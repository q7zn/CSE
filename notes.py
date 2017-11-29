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
    elif percentage >= 80 : #elif means else if
        return "B"
    elif percentage >= 70 :
        return "C"
    elif percentage >= 60 :
        return "D"
    else:
        return "F"

print (grade_calc(59))
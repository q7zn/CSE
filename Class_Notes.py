# Defining a class
class CheeseBurger(object):
    def __init__(self, patty, cheese):  # TWO UNDERSCORES before and after
        self.patty = patty
        self.cheese = cheese
        self.eaten = False

    def give(self, name):
        print(name + "is thankful")

    def cut(self):
        print("You cut the cheeseburger")

    def eat(self):
        print("You eat the cheeseburger")
        self.eaten = True


# Instantiating (Creating) two cheeseburgers
burger1 = CheeseBurger("Ground Beef", "Swiss")
burger2 = CheeseBurger("Bacon", "Swiss")

print(burger1.eaten)
print(burger2.cheese)

burger1.eat()
print(burger1.eaten)
print(burger2.eaten)


class Car(object):
    def __init__(self, name, color, num_of_doors, hp):
        self.color = color
        self.doors = num_of_doors
        self.running = False
        self.HP = hp
        self.passengers = 0
        self.name = name
        self.accelerating = False
        self.brake = True
        self.air_conditioning = True

    def turn_on(self):
        if self.running:
            print("the car is already on you dumb")
        else:
            self.running = True
            print("You start the car.")

    def turn_off(self):
        if self.running:
            self.running = False
            print("You turn off the car.")
        else:
            print("The car is already off you dumb")

    def move_forward(self):
        if self.running:
            print("The car moves forward.")
        else:
            print("The car is off, nothing happens.")

    def go_for_drive(self, passengers):
        print("%d passengers get in." % passengers)
        self.turn_on()
        self.move_forward()
        self.move_forward()
        self.move_forward()
        self.turn_off()
        print("%d passengers get out." % passengers)
        self.passengers = 0


my_car = Car("Bugatti", "red", 2, 1200)
my_car.go_for_drive(1)

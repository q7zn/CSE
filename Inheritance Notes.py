class Vehicle(object):
    def __init__(self, seat, source, material, speed, passengers):
        self.power_source = source
        self.material = material
        self.seat_location = seat
        self.top_speed = speed
        self.passengers = passengers

    def move(self):
        print("You move forward")

    def change_direction(self):
        print("You change directions")


class Car(Vehicle):
    def __init__(self, material, seat, speed, passengers):
        super(Car, self).__init__('engine', material, seat, speed, passengers)

    def roll_down_windows(self):
        print("You roll the windows down")

    def turn_on(self):
        print('You turn the key and the engine starts')


test_car = Car("Aluminum", 'Driver side', 140, 2)
test_car.change_direction()


class KeylessCar(Car):
    def __init__(self, material, seat, speed, passengers):
        super(KeylessCar, self).__init__(material, seat, speed, passengers)

    def turn_on(self):
        print("You push the button and the car turns on")


test_car.turn_on()
cool_car = KeylessCar('Aluminum', 'Driver side', 140, 2)
cool_car.turn_on()


class Tesla(Car):
    def __init__(self, material, seat, speed, passengers):
        super(Tesla, self).__init__(material, seat, speed, passengers)

    def fly(self):
        print("You launch the car into a low orbit around earth")

    def turn_on(self):
        Car.turn_on(self)

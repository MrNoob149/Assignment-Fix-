# assignment 1
class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def show(self):
        print('The registration number is ', car.registration_number)
        print("The maximum speed is ", car.maximum_speed)
        print("The current speed of the car is ", car.current_speed)
        print("The traveled distance of the car is ", car.travelled_distance)

car = Car('ABC-123', 142)
car.show()


# assignment 2

class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change):
        self.current_speed += change
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        if self.current_speed < 0:
            self.current_speed = 0

car = Car('ABC-123', 142)
car.accelerate(30)
car.accelerate(50)
car.accelerate(70)
print("The current speed of the car is ", car.current_speed)

car.accelerate(-200)
print("The current speed of the car is ", car.current_speed)

# assignment 3
class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change):
        self.current_speed += change
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        if self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours

car = Car('ABC-123', 142)
print("The travel distance is ", car.travelled_distance)

# assignment 4
import random
class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change):
        self.current_speed += change
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        if self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours

race_list = []
for n in range(1, 11):
    name = f"ABC-{n}"
    speed = random.randint(100, 200)
    race_list.append(Car(name, speed))

race_start = True
while race_start:
    for car in race_list:
        change = random.randint(-10, 15)
        Car.accelerate(change)
        car.drive(1)

        if car.travelled_distance == 10000:
            race_start = False
            break

print("Race ended")
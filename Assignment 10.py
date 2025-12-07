# assignment 1
# class Elevator:
#     def __init__(self, bottom_floor, top_floor):
#         self.bottom_floor = bottom_floor
#         self.top_floor = top_floor
#
#     def floor_up(self):
#         if self.bottom_floor < self.top_floor:
#             self.bottom_floor += 1
#             print("You are now at floor", self.bottom_floor)
#
#     def floor_down(self):
#         if self.bottom_floor > self.bottom_floor:
#             self.bottom_floor -= 1
#             print("You are now at floor", self.bottom_floor)
#
#     def go_to_floor(self, wanted_floor):
#         while self.bottom_floor < wanted_floor:
#             self.floor_up()
#
#         while self.bottom_floor > wanted_floor:
#             self.floor_down()

# elevator = (Elevator(1, 10))
# elevator.go_to_floor(3)
# elevator.go_to_floor(8)

# exercise 2
# class Elevator:
#     def __init__(self, bottom_floor, top_floor):
#         self.bottom_floor = bottom_floor
#         self.top_floor = top_floor
#
#     def floor_up(self):
#         if self.bottom_floor < self.top_floor:
#             self.bottom_floor += 1
#             print("You are now at floor", self.bottom_floor)
#
#     def floor_down(self):
#         if self.bottom_floor > self.top_floor:
#             self.bottom_floor -= 1
#             print("You are now at floor", self.bottom_floor)
#
#     def go_to_floor(self, wanted_floor):
#         while self.bottom_floor < wanted_floor:
#             self.floor_up()
#
#         while self.bottom_floor > wanted_floor:
#             self.floor_down()
#
# class Building:
#     def __init__(self, bot, top, count):
#         self.elevator_list = []
#         for i in range(count):
#             self.elevator_list.append(Elevator(bot, top))
#
#     def run_elevator(self, elevator_number, chosen_floor):
#         elevator = self.elevator_list[elevator_number]
#         elevator.go_to_floor(chosen_floor)
#
# building = Building(1, 10, 3)
# building.run_elevator(0, 3)
# building.run_elevator(0, 9)

# exercise 3
# class Elevator:
#     def __init__(self, bottom_floor, top_floor):
#         self.bottom_floor = bottom_floor
#         self.top_floor = top_floor
#
#     def floor_up(self):
#         if self.bottom_floor < self.top_floor:
#             self.bottom_floor += 1
#             print("You are now at floor", self.bottom_floor)
#
#     def floor_down(self):
#         if self.bottom_floor > self.top_floor:
#             self.bottom_floor -= 1
#             print("You are now at floor", self.bottom_floor)
#
#     def go_to_floor(self, wanted_floor):
#         while self.bottom_floor < wanted_floor:
#             self.floor_up()
#
#         while self.bottom_floor > wanted_floor:
#             self.floor_down()
#
# class Building:
#     def __init__(self, bot, top, count):
#         self.bot = bot
#         self.elevator_list = []
#         for i in range(count):
#             self.elevator_list.append(Elevator(bot, top))
#
#     def run_elevator(self, elevator_number, chosen_floor):
#         elevator = self.elevator_list[elevator_number]
#         elevator.go_to_floor(chosen_floor)
#
#     def fire_alarm(self):
#         print("Fire detected, all elevators move to bottom floor")
#         for elevator in self.elevator_list:
#             elevator.go_to_floor(self.bot)
# building = Building(1, 10, 3)
# building.run_elevator(0, 3)
# building.run_elevator(0, 9)
# building.fire_alarm()

# exercise 4
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

class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            change = random.randint(-10, 15)
            car.accelerate(change)
            car.drive()
    def print_status(self):
        print("Car                  Max    Speed    Distance")
        print("------------------------------------------------")
        for car in self.cars:
            print(car.registration_number, car.maximum_speed, car.current_speed, car.travelled_distance)
    def race_finished(self):
        for car in self.cars:
            if car.travelled_distance >= self.distance:
                return True
        return False

race_list = []
for n in range(1, 11):
    name = f"ABC-{n}"
    speed = random.randint(100, 200)
    race_list.append(Car(name, speed))
race = Race("Grand Demolition Derby", 8000, race_list)
hours = 0
race_started = True
while race_started:
    race.hour_passes()
    hours += 1
    if hours % 10 ==0:
        print("After", hours)
        race.print_status()
        break
print("Race finished after ", hours)
race.print_status()
# question 1

class Publication:
    def __init__(self, name: str):
        self.name = name

class Book(Publication):
    def __init__(self, name ,author_name, page_count):
        super().__init__(name)
        self.author_name = author_name
        self.page_count = page_count

    def print_information(self):
        print("The author of this book is ", self.author_name)
        print("The number of this page is ", self.page_count)
        print("The name of this book is", self.name)

class Magazine(Publication):
    def __init__(self, name ,chief_editor):
        super().__init__(name)
        self.chief_editor = chief_editor

    def print_information(self):
        print("The chief editor of this magazine is ", self.chief_editor)
        print("The name of this magazine is", self.name)

book = Book("Compartment No. 6", "Rosa Liksom", 192)
book.print_information()
magazine = Magazine("Donald Duck", "Aki Hyyppä")
magazine.print_information()

# question 2
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

class ElectricCar (Car):
    def __init__(self, registration_number, maximum_speed, battery):
        super().__init__(registration_number, maximum_speed)
        self.battery = battery

class GasolineCar(Car):
    def __init__(self, registration_number, maximum_speed, tank):
        super().__init__(registration_number, maximum_speed)
        self.tank = tank
gaso1 = GasolineCar("ACD-123", 165, 32.3)
ele1 = ElectricCar("ABC-15", 180, 52.5)
gaso1.accelerate(140)
ele1.accelerate(150)
gaso1.drive(3)
ele1.drive(3)

print("The distance that electric car made is", ele1.travelled_distance)
print("The distance that gasoline car travelled is", gaso1.travelled_distance)

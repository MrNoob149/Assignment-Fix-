import random
# Task 1
def dice():
    roll = random.randint(1,6)
    return roll
result = 0
while result != 6:
    result = dice()
    print("You roll:", result)
    if result == 6:
        break

# task 2
def side(sides):
    roll = random.randint(1,sides)
    return roll
sides = int(input("Enter the number of sides: "))
result = 0
while result != sides:
    result = side(sides)
    print("The side is: ", result)

# task 3
def convertion():
    convert = gallon * 3.78541
    return convert
while True:
    gallon = int(input("Enter the gallon: "))
    if gallon < 0:
        break
    elif gallon >= 0:
        print(f"The gallon {gallon} is {convertion()}")

# task 4
def list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total
numbers = [1, 2, 3, 4, 5]
result = list(numbers)
print("The result is", result)
task 5
def list(numbers):
    even = []
    for num in numbers:
        if num % 2 == 0:
            even.append(num)
    return even
numbers = [1, 2, 3, 4, 5]
result = list(numbers)
print("The original is", numbers)
print("The result is", result)
# task 6
import math

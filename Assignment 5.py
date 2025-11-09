# Task 1
import random
total = 0
chosen_number = int(input("How many dices do you want to roll?:  "))
for number in range(chosen_number):
    roll = random.randint(1, 6)
    print(f"dice is {roll}")
    total += roll

print("The total number is", total)

# task 2
number_list = []
while True:
    numbers = input("Enter numbers: ")
    if numbers == "":
        break
    else:
        number_list.append(float(numbers))
number_list.sort(reverse=True)
print(number_list[:5])


# task 3
number = int(input("Enter your number: "))
is_prime = True
if number > 1:
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            print("This is not a prime number.")
            break
    else:
        print("This number is prime number")
elif number <= 1:
   print("Error")


# task 4
cities = []
for command in range(5):
    enter = input("Enter your city: ")
    cities.append(enter)
for city in cities:
    print(cities)
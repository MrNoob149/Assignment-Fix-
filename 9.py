# Assignment 4.1
import math

import decimal
num = 2
while 1 < num < 1000:
    if num % 3 == 0:
        print('current number:', num)
    num = num + 1


# Assignment 4.2
inches = int(input("Enter your number"))
centimeters = inches * 2.54
while inches >= 0:
    print("Your number is:", centimeters)
    if inches < 0:
      break

# Assignment 4.3
largest_number = input(str("Enter your largest number"))
smallest_number = input(str("Enter your smallest number"))
while largest_number != "" and smallest_number != "":
    print("Largest number: ", largest_number)
    print("Smallest number: ", smallest_number)
    if largest_number == "" and smallest_number == "":
     print("Goodbye")
    break


# Assignment 4.4
import random
dice1 = random.randint(1, 100)
user = 0
while user != dice1:
    user = (int(input("Enter the number")))
    if user == dice1:
        print("This is correct")
    elif user < dice1:
        print("This is too low.")
    elif user > dice1:
        print("This is too high.")
print("Done")


# Assignment 4.5
username = "python"
password = "rules"
attempts = 5
while attempts > 0:
    username = (input("Enter your username"))
    password = (input("Enter your password"))
    if username == "python" and password == "rules":
        print("Welcome")
    else:
        attempts = attempts - 1
        print("Sorry, try again")
    if attempts == 0:
        print("Access Denied")
        break


# Assignment 4.6
import math
import random
N = int(input("Enter your number"))
A = 1
B = 0
while N > 0:
    x = random.randint(-1, 1)
    y = random.randint(-1, 1)
    total = x * x + y * y
    if total < A:
        B = B + 1
    elif total == A:
        B = B + 1
    elif total > A:
        print("The square is bigger than the circle")
        pass

n = 4 * total / N
print("Pi is: ", total)

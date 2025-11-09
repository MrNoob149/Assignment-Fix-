# Assignment 4.1
import math

import decimal
num = 2
while 1 < num < 1000:
    if num % 3 == 0:
        print('current number:', num)
    num = num + 1


# Assignment 4.2
while True:
    inches = int(input("Enter your number: "))
    if inches >= 0:
        centimeters = inches * 2.54
        print("Your number is:", centimeters)
    elif inches < 0:
        break


# Assignment 4.3
list = []
while True:
    number = input("Enter the number: ")
    if number != "":
        list.append(int(number))
        print("Number entered")
        continue
    if number == "":
        print("Largest number: ", max(list))
        print("Smallest number: ", min(list))
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
    username = (input("Enter your username: "))
    password = (input("Enter your password: "))
    if username == "python" and password == "rules":
        print("Welcome")
        break
    else:
        attempts = attempts - 1
        print("Sorry, try again")
    if attempts == 0:
        print("Access Denied")
        break

# # Assignment 4.6
import random
N = int(input("Enter your number"))
A = 1
B = 0
count = 0
while N > count:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    total = x * x + y * y
    if total <= A:
        B = B + 1
    elif total > A:
        pass
    count += 1

n = 4 * B / N
print("Pi is: ", n)
# assignment 2.1
name = input("Enter your name")
print (f"Hello, {name}")

# assignment 2.2
import math
radius = float(input("Enter the radius of the circle:"))
area = 3.14 * radius * radius
print("The area of the circle is",area)

# assignment 2.3"
length = int(input("enter the length: "))
width = int(input("enter the width: "))
area = length * width
perimeter = 2 * (length + width)
print("the area of the circle is ", area)
print("the perimeter of the circle is ", perimeter)

# assignment 2.4
a = float(input("Enter your number: "))
b = float(input("Enter your number: "))
c = float(input("Enter your number: "))
sum = a + b + c
product = a * b * c
average = (a + b + c) / 3
print(f"Your product is {product}")
print(f"Your sum is {sum}")
print(f"Your average is {average}")

# assignment 2.5
import math
talent = int(input("Enter Talent: "))
pounds = int(input("Enter Pounds: "))
lot = int(input("Enter lot: "))
talent_to_pound = talent * 20
pound_to_lot = (pounds + talent_to_pound) * 32
lot_to_gram = (lot + pound_to_lot) * 13.3
gram_to_kilogram = lot_to_gram / 1000
print("You have", lot_to_gram, "and", gram_to_kilogram)

# assignment 2.6
code3 = []
code4 = []
import random
for n in range(3):
    code3.append(random.randint(0, 9))
for i in range(4):
    code4.append(random.randint(1, 6))

print("3 digit code is: ", code3)
print("4 digit code is: ", code4)


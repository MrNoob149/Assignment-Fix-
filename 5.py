print("assignment 3.1")
length = int(input("enter the length of the zander in centimeters: "))
if length < 42:
    zander_limit = 42 - (length)
    print(f"Please release the fish back to the lake. Your zander is {zander_limit} centimeters less than the requirement.")
if length >= 42:
    print("Your zander meet the size limit. You can catch the fish now")

print("assignment 3.2")
cabin_class = input("enter the cabin class: ")
if cabin_class == "LUX":
    print("the cabin is an upper-deck cabin with a balcony.")
elif cabin_class == "A":
    print("The cabin is above the car deck, equipped with a window.")
elif cabin_class == "B":
    print("The cabin is a windowless cabin above the car deck.")
elif cabin_class == "C":
    print("The cabin is a windowless cabin below the car deck.")
else:
    print("Invalid cabin class")

print("assignment 3.3")
gender = (input("enter your gender: "))
hemoglobin_value = int(input("enter the hemoglobin value: "))
if gender == "female" or gender == "fem" or gender == "FEM" or gender == "Fem" or gender == "Female" and hemoglobin_value > 155:
    print(f"Your hemoglobin value is high")
elif hemoglobin_value < 117:
    print("Your hemoglobin value is low")
elif 117 <= hemoglobin_value <= 150:
    print(f"Your hemoglobin value is normal")

if gender == "male" or gender == "m" or gender == "M" or gender == "Male" and hemoglobin_value > 167:
    print(f"Your hemoglobin value is high")
elif hemoglobin_value < 134:
    print("Your hemoglobin value is low")
elif 134 <= hemoglobin_value <= 167:
    print(f"Your hemoglobin value is normal")

print("assignment 3.4")
year = int(input("please enter the year: "))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("This year is a leap year")
else:
    print("This year is not a leap year")



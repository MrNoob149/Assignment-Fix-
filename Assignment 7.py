# assignment 1

seasons = ("Spring", "Summer", "autumn", "winter")
months = int(input("Choose your month (1 - 12): "))
if months in (1, 2, 3):
    print("This season is: ", (seasons[0]))
elif months in (4, 5, 6):
    print("This season is: ", (seasons[1]))
elif months in (7, 8, 9):
    print("This season is: ", (seasons[2]))
elif months in (10, 11, 12):
    print("This season is: ", (seasons[3]))
else:
    print("Invalid input")

# assignment 2
name_list = set()
while True:
    name = input("Enter your name: ")
    if name == "":
        print("Goodbye")
        break
    elif name in name_list:
        print("Name entered")
    elif name != "":
        print("Enter new name")
    name_list.add(name)

for n in name_list:
    print(n)
# assignment 3

airports = {}
while True:
    choices = int(input("There are 3 modes \n 1: Enter airport ICAO code and airport name \n 2: Enter airport information \n 3: Exit \n You can select any:"))
    if choices == 1:
        airport_name = input("Enter Airport Name: ")
        ICAO_code = input("Enter ICAO code: ")
        airports[ICAO_code] = airport_name
        print("Airport added")
    elif choices == 2:
        search = input("Enter ICAO code: ")
        if search in airports:
            print("The airport you searching for is: ", airports["search"])
        elif search not in airports:
            print("The airport you searching for is not in the list")
    elif choices == 3:
        print("Goodbye")
        break

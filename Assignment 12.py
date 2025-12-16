import requests
import json
# question 1
request ="https://api.chucknorris.io/jokes/random"
response = requests.get(request)
data = response.json()
print(data["value"])

# question 2
import requests

api_key = "e14253e3588bc861f0e30accaff4ad08"

city = input("Enter municipality name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=API_KEY"


response = requests.get(url)
data2 = response.json()

if response.status_code == 200:
    description = data2["weather"][0]["description"]
    temp_kelvin = data2["main"]["temp"]
    temp_celsius = temp_kelvin - 273.15

    print(f"The temperature in {city} is {temp_celsius:.2f} degree")
else:
    print("Error")
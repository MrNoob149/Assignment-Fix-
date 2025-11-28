# Main program
from unittest import result

import mysql.connector

connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='Mrnoob',
         password='123456789',
         autocommit=True
         )

# exercise 1 (look for country name, not location like (town)
def get_icao(ICAO_code):
    sql = f"select airport.ident, airport.name FROM airport WHERE airport.ident = '{ICAO_code}'"
    cursor = (connection.cursor())
    cursor.execute(sql)
    result = cursor.fetchall()
    for row in result:
        print(f"Your ICAO code is {ICAO_code}, your airport is {row[1]}")

ICAO_code = input("Enter ICAO code: ")
get_icao(ICAO_code)

# exercise 2
def airport_type(area_code):
    sql = f"select airport.type, country.name, count(*) FROM airport JOIN country on airport.iso_country = country.iso_country WHERE airport.iso_country = '{area_code}' GROUP BY type "
    cursor = (connection.cursor())
    cursor.execute(sql)
    result = cursor.fetchall()
    for row in result:
        # print(f"About {row[1]} airports have {row[0]}")
        print(f"{row[1]} have {row[2]} {row[0]}")

area_code = input("Enter area code: ")
airport_type(area_code)

# exercise 3
import geopy
from geopy import distance, Point


def calculate_airport(ICAO_code1, ICAO_code2):
    sql = (f"SELECT name, latitude_deg, longitude_deg FROM airport WHERE airport.ident = '{ICAO_code1}'"
           f"or airport.ident = '{ICAO_code2}'")
    cursor = connection.cursor()
    cursor.execute(sql)
    results = cursor.fetchall()
    airports1 = []
    airports2 = []
    for row in results:
        name1 = row[0]
        name2 = row[0]
        lat1 = row[1]
        lat2 = row[1]
        lon1 = row[2]
        lon2 = row[2]
        airports1.append(name1)
        airports2.append(name2)
        location1 = [lat1, lon1]
        location2 = [lat2, lon2]
        distance_difference = geopy.distance.distance((location1, location2)).km
        print(f"The distance between", airports1[0], "and", airports2[0], f"is {distance_difference} km")


ICAO_code1 = input("Enter ICAO code: ")
ICAO_code2 = input("Enter ICAO code: ")
calculate_airport(ICAO_code1, ICAO_code2)
from flask import Flask, request
## question 1
app = Flask(__name__)
@app.route('/prime_number/<int:number>')
def prime_checking(n):
    is_prime = True
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                is_prime = False
                print("This is not a prime number.")
                break
        else:
            print("This number is prime number")
    elif n <= 1:
        print("Error")
def calculate_sum(number):
    respond = {
        "number": number,
        "is_prime": prime_checking(number)
    }
    return respond
if __name__== '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)


## question 2
import mysql.connector

connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='Mrnoob',
         password='123456789',
         autocommit=True
         )

app = Flask(__name__)
@app.route('/airport/<int:number>')
def get_icao(ICAO_code):
    sql = f"select airport.ident, airport.name, country.name FROM airport JOIN country on airport.iso_country = country.iso_country WHERE airport.ident = '{ICAO_code}'"
    cursor = (connection.cursor())
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

def airport(icao):
    icao = icao.upper()
    for row in get_icao(icao):
        airport.ident, airport.name, name = row
        respond = {
                "ICAO": airport.ident,
                "airport": airport.name,
                "location": name,
            }
        return respond
    return None
if __name__== '__main__':
     app.run(use_reloader=True, host='127.0.0.1', port=5000)

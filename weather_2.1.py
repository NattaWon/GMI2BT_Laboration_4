from flask import Flask, jsonify, request, render_template
import random
import time
import datetime
import sqlite3

app = Flask(__name__)

# Json data from a post request and then save it to the sqlite database


@app.route('/temp', methods=['POST'])
def printjson():
    print(request.is_json)
    stuff = request.get_json()
    print(stuff)
    conn = sqlite3.connect('weather.db')
    c = conn.cursor()
    vader = (
        request.json['City'],
        request.json['Temprature'],
        request.json['Humidity'],
        request.json['Pressure'])
    c.execute(
        'INSERT INTO SensorData(City,Temprature,Humidity, Pressure) VALUES(?,?,?,?)', vader)
    conn.commit()
    return 'JSON-post has been successfully'

# retrieve data from table


@app.route("/")
def retrieve():
    conn = sqlite3.connect('weather.db')
    c = conn.cursor()
    c.execute(
        'SELECT id, City, Temprature, Humidity, Pressure, reading_time FROM SensorData')
    data = c.fetchall()
    conn.commit()
    return render_template("weather.html", data=data)


app.run(host='127.0.0.1', port=5000, debug=True)

from flask import Flask
import grovepi
from datetime import datetime

app = Flask(__name__)
print("test test")
dht_sensor = 4
dht_type = 0

@app.route("/temperature")
def temp():
    print("test2")
    #temp,hum=grovepi.dht(dht_sensor,dht_type)
    temp,hum=grovepi.dht(dht_sensor,dht_type)
   # print("temp: " + temp)
    return str(temp)
@app.route("/humidity")
def hum():
    temp, hum = grovepi.dht(dht_sensor, dht_type)
    return str(hum)

app.run(host="0.0.0.0", port=5000)

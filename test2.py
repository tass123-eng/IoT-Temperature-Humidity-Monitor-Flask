from flask import Flask, render_template
import grovepi
import time
from datetime import datetime

app = Flask(__name__)

# Port du capteur DHT
dht_sensor = 4
dht_type = 0

@app.route("/temperature")
def temp():
    try:
        [temp, hum] = grovepi.dht(dht_sensor, dht_type)
        detection_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return render_template("temp.html", temperature=temp, time=detection_time)
    except:
        return "Erreur de lecture du capteur"

@app.route("/humidity")
def hum():
    try:
        [temp, hum] = grovepi.dht(dht_sensor, dht_type)
        detection_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return render_template("hum.html", humidity=hum, time=detection_time)
    except:
        return "Erreur de lecture du capteur"

app.run(host="0.0.0.0", port=5000)

from flask import Flask, render_template
import grovepi
import time
from datetime import datetime
import threading

app = Flask(__name__)

dht_sensor = 4
dht_type = 0

history = []

def read_sensor():
    while True:
        temp, hum = grovepi.dht(dht_sensor, dht_type)
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        history.append({"time": now, "temperature": temp, "humidity": hum})
        time.sleep(2)

thread = threading.Thread(target=read_sensor)
thread.daemon = True
thread.start()

@app.route("/temperature")
def temp_page():
    latest = history[-1]
    return render_template("temp.html", temperature=latest["temperature"], time=latest["time"])

@app.route("/humidity")
def hum_page():
    latest = history[-1]
    return render_template("hum.html", humidity=latest["humidity"], time=latest["time"])

app.run(host="0.0.0.0", port=5000)

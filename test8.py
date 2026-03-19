from flask import Flask, render_template
import grovepi
from datetime import datetime
app = Flask(__name__)
dht_sensor = 4
dht_type = 0
history = []
@app.route("/temperature")
def temp_page():
    temp, hum = grovepi.dht(dht_sensor, dht_type)
    detection_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    history.append({"time": detection_time, "temperature": temp, "humidity": hum})
    return render_template("temp.html", temperature=temp, time=detection_time, history=history)

@app.route("/humidity")
def hum_page():
    temp, hum = grovepi.dht(dht_sensor, dht_type)
    detection_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    history.append({"time": detection_time, "temperature": temp, "humidity": hum})
    return render_template("hum.html", humidity=hum, time=detection_time, history=history)

app.run(host="0.0.0.0", port=5000)

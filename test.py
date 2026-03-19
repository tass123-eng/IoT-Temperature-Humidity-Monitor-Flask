from flask import Flask,render_template
app=Flask(__name__)
@app.route("/temperature")
def temp():
  return render_template("temp.html")
@app.route("/humidity")
def hum():
  return render_template("hum.html")
app.run(host="0.0.0.0")


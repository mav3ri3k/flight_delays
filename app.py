from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

# Load your ML artifacts once at startup
model = joblib.load("flight_delay_model.pkl")
labels = joblib.load("Labels.pkl")

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html", carriers=labels.carriers, airports=labels.airports)

@app.route("/predict", methods=["POST"])
def predict():
    # Extract form inputs
    data = {
        'carrier':          labels.le_carrier.transform([request.form['carrier']])[0],
        'airport':          labels.le_airport.transform([request.form['airport']])[0],
        'month':            int(request.form['month']),
        'arr_flights':      int(request.form['arr_flights']),
        'arr_cancelled':    int(request.form['arr_cancelled']),
        'arr_del15':        int(request.form['arr_del15']),
        'arr_diverted':     int(request.form['arr_diverted']),
        'carrier_ct':       int(request.form['carrier_ct']),
        'weather_ct':       int(request.form['weather_ct']),
        'nas_ct':           int(request.form['nas_ct']),
        'security_ct':      int(request.form['security_ct']),
        'late_aircraft_ct': int(request.form['late_aircraft_ct']),
    }
    df = pd.DataFrame([data])
    pred = model.predict(df)[0]
    result = "On Time" if pred == 0 else "Delayed"
    return render_template("index.html",
                           carriers=labels.carriers,
                           airports=labels.airports,
                           result=result,
                           input=data)

if __name__ == "__main__":
    app.run(debug=True)


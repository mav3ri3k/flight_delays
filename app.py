import streamlit as st
import pandas as pd
import os
import joblib
from utils import Labels

# Load the model
model = joblib.load("./flight_delay_model.pkl")
labels = joblib.load("./Labels.pkl")

st.title("✈️ Flight Delay Predictor")
st.write("Enter flight and airport details to predict delay status.")

with st.form("flight_form"):
    carrier_code = st.selectbox("Carrier Code", labels.carriers)
    airport_code = st.selectbox("Airport Code", labels.airports)

    month = st.number_input("Month (1–12)", min_value=1, max_value=12, value=6)
    year = st.number_input("Year", min_value=2000, max_value=2025, value=2023)
    arr_flights = st.number_input("Arriving Flights", min_value=0, value=100)
    arr_cancelled = st.number_input("Cancelled Arrivals", min_value=0, value=0)
    arr_del15 = st.number_input("Arrivals Delayed >15 min", min_value=0, value=10)
    arr_diverted = st.number_input("Diverted Arrivals", min_value=0, value=0)
    carrier_ct = st.number_input("Carrier Delay Count", min_value=0, value=5)
    weather_ct = st.number_input("Weather Delay Count", min_value=0, value=3)
    nas_ct = st.number_input("NAS Delay Count", min_value=0, value=4)
    security_ct = st.number_input("Security Delay Count", min_value=0, value=0)
    late_aircraft_ct = st.number_input("Late Aircraft Delay Count", min_value=0, value=6)

    carrier_delay = st.number_input("Carrier Delay (minutes)", min_value=0, value=50)
    weather_delay = st.number_input("Weather Delay (minutes)", min_value=0, value=30)
    nas_delay = st.number_input("NAS Delay (minutes)", min_value=0, value=40)
    security_delay = st.number_input("Security Delay (minutes)", min_value=0, value=0)
    late_aircraft_delay = st.number_input("Late Aircraft Delay (minutes)", min_value=0, value=60)

    month_input = month  # included above
    submitted = st.form_submit_button("Predict Delay")

    if submitted:
        new_data = pd.DataFrame([{
            'carrier': labels.le_carrier.transform([carrier_code]),
            'month': month_input,
            # 'carrier_name': carrier_name,
            'airport': labels.le_airport.transform([airport_code]),
            # 'airport_name': airport_name,
            'arr_diverted': arr_diverted,
            # 'late_aircraft_delay': late_aircraft_delay,
            'arr_flights': arr_flights,
            'arr_cancelled': arr_cancelled,
            'carrier_ct': carrier_ct,
            # 'weather_delay': weather_delay,
            'late_aircraft_ct': late_aircraft_ct,
            'nas_ct': nas_ct,
            # 'security_delay': security_delay,
            'arr_del15': arr_del15,
            # 'year': year,
            # 'nas_delay': nas_delay,
            'security_ct': security_ct,
            'weather_ct': weather_ct,
            # 'carrier_delay': carrier_delay
        }])

        pred = model.predict(new_data)[0]
        result = "🟢 On Time" if pred == 0 else "🔴 Delayed"
        st.markdown(f"### Prediction: **{result}**")


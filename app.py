import streamlit as st

import pandas as pd

import numpy as np

import datetime

import requests

'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

1. Let's ask for:
- date and time
- pickup longitude
- pickup latitude
- dropoff longitude
- dropoff latitude
- passenger count
'''

event_time = st.datetime_input(
    "Schedule your event",
    datetime.datetime(2025, 11, 19, 16, 45),
)
st.write("Event scheduled for", event_time)

number = st.number_input('Insert a number')

st.write('The current number is ', number)



pickup_longitude = st.number_input(
    "Pickup longitude",
    value=-74.00,
    format="%.6f"
)

pickup_latitude = st.number_input(
    "Pickup latitude",
    value=40.00,
    format="%.6f"
)

dropoff_longitude = st.number_input(
    "Dropoff longitude",
    value=-74.01,
    format="%.6f"
)

dropoff_latitude = st.number_input(
    "Dropoff latitude",
    value=40.01,
    format="%.6f"
)


'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''

url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

'''

2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user

'''

params = {

    "pickup_datetime": "2026-05-28 12:00:00",
    "pickup_longitude": -74.00,
    "dropoff_latitude": 40.01,
    "dropoff_longitude": -74.01,
    "passenger_count": 1

}



pickup_longitude = st.number_input(
    "Pickup longitude",
    value=-73.95
)

pickup_latitude = st.number_input(
    "Pickup latitude",
    value=40.78
)

dropoff_longitude = st.number_input(
    "Dropoff longitude",
    value=-73.98
)

dropoff_latitude = st.number_input(
    "Dropoff latitude",
    value=40.76
)

passenger_count = st.number_input(
    "Passenger count",
    value=1,
    step=1
)

params = {
    "pickup_datetime": "2026-05-28 12:00:00",
    "pickup_longitude": pickup_longitude,
    "pickup_latitude": pickup_latitude,
    "dropoff_longitude": dropoff_longitude,
    "dropoff_latitude": dropoff_latitude,
    "passenger_count": passenger_count
}


data = pd.DataFrame({
    "lat": [pickup_latitude, dropoff_latitude],
    "lon": [pickup_longitude, dropoff_longitude]
})

st.map(data)


url = "https://taxifare.lewagon.ai/predict"

response = requests.get(url, params=params)

print(response.json())

pickup_datetime = st.datetime_input(
    "Pickup datetime",
    datetime.datetime(2026, 5, 28, 12, 0)
)

if st.button("Predict fare"):

    params = {
        
        "pickup_datetime": pickup_datetime.strftime("%Y-%m-%d %H:%M:%S"),
        "pickup_longitude": pickup_longitude,
        "pickup_latitude": pickup_latitude,
        "dropoff_longitude": dropoff_longitude,
        "dropoff_latitude": dropoff_latitude,
        "passenger_count": passenger_count
    }

    response = requests.get(url, params=params)

    prediction = response.json()
      
    st.success(f"Estimated fare: ${prediction['fare']:.2f}")

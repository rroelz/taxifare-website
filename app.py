import streamlit as st # type: ignore
import pandas as pd
import requests
import datetime
import json

'''
# TaxiFareModel front
'''

st.markdown('''
Welcome to our taxicab prediction. No promises 🙂
''')

'''
### When are you travelling?
'''
now = datetime.datetime.now()
pickup_date = st.date_input(
    "What date do you want to travel?",
    value="today"
    )

pickup_time = st.time_input(
    "When do you want to travel",
    value="now",
)

pickup_datetime = datetime.datetime.combine(pickup_date,pickup_time)
pickup_datetime = pickup_datetime.strftime("%Y-%m-%d %H:%M:%S")
'''
### Select pickup:
'''
pickup_longitude = st.number_input('Pickup longitude', -73.842341, step = 0.0001)
pickup_latitude = st.number_input('Pickup latitude', 40.740216, step = 0.0001)

'''
### Select dropoff:
'''
dropoff_longitude = st.number_input('Dropoff longitude', -73.979518, step = 0.0001)
dropoff_latitude = st.number_input('Dropoff latitude', 40.757935, step = 0.0001)

df_latlon = pd.DataFrame({
    'lat': [pickup_latitude, dropoff_latitude],
    'lon': [pickup_longitude, dropoff_longitude],
})
'''
## How many passengers
- passenger count
'''
passenger_count = st.slider('## How many passengers', 1,8,1)
'''
'''
url = 'https://taxifare-1086583640100.europe-west1.run.app/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

query_string = f"?pickup_datetime={pickup_datetime}&pickup_longitude={pickup_longitude}&pickup_latitude={pickup_latitude}&dropoff_longitude={dropoff_longitude}&dropoff_latitude={dropoff_latitude}&passenger_count={passenger_count}"
api_call = url+query_string
r = requests.get(api_call)
fare = r.json()['fare']
st.markdown(f"Expected Taxi fare is **${fare:.2f}**")

st.map(df_latlon)

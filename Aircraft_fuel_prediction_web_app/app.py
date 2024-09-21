import streamlit as st
import joblib
import pandas as pd 
import numpy as np

# Load the Model
model = joblib.load('fuel_consumption_model.pkl')

# App Title
st.title('Aircraft Fuel Consumption Predictor')

# Input Fields
flight_distance =st.number_input('Flight Distance (km)')
number_of_passengers = st.number_input('Number of Passengers')
flight_duration =st.number_input('Flight Duration (hours)')
aircraft_type = st.selectbox('Aircraft Type', ['light jets','midsize jets','ultra long range jets'])

# Dataframe
input_data = pd.DataFrame({
    'Flight_Distance':[flight_distance],
    'Number_of_Passengers':[number_of_passengers],
    'Flight_Duration':[flight_duration],
    'Aircraft_Type_Type1':[1 if aircraft_type == 'light jets' else 0],
    'Aircraft_Type_Type2':[1 if aircraft_type == 'midsize jets' else 0],
    'Aircraft_Type_Type3':[1 if aircraft_type == 'ultra long range jets' else 0]
})

# Prediction
if st.button('Predict'):
    fuel_consumption = model.predict(input_data)
    st.header('Fuel consumption')
    st.write(fuel_consumption[0],'litres')

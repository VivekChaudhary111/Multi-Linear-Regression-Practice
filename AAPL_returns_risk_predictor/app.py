import streamlit as st
import joblib
import pandas as pd 
import numpy as np

# Load the Model
model = joblib.load('https://github.com/VivekChaudhary111/Multi-Linear-Regression-Practice/blob/4aafb9764342a7df671cf87134b63375ad7d1672/AAPL_returns_risk_predictor/AAL_stock_risk_return_model.pkl')

# App Title
st.title('Apple Inc. Stocks Returns and Risk Predictor')

# Input Fields
open_price =st.number_input('Open ($)')
close_price = st.number_input('Close ($)')
high_of_the_day =st.number_input('High ($)')
low_of_the_day = st.number_input('Low ($)')

# Dataframe
input_data = pd.DataFrame({
    'Open':[open_price],
    'Close':[close_price],
    'High':[high_of_the_day],
    'Low':[low_of_the_day]
})

# # Prediction
# if st.button('Predict'):
#     Return_Risk = model.predict(input_data)
#     st.write(Return_Risk,'')

# Prediction
if st.button('Predict'):
    Return_Risk = model.predict(input_data)
    predicted_return = Return_Risk[0][0]
    predicted_risk = Return_Risk[0][1]
    
    # Display the results in two columns
    col1, col2 = st.columns(2)
    
    with col1:
        st.header("Predicted Return")
        st.write(predicted_return)
    
    with col2:
        st.header("Predicted Risk")
        st.write(predicted_risk)
        

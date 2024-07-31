import streamlit as st
import pandas as pd
import requests
from io import BytesIO

# Endpoint of the Flask API
prediction_endpoint = "http://127.0.0.1:5000/predict"

st.title("Text Sentiment Predictor")

# File uploader for bulk prediction
uploaded_file = st.file_uploader(
    "Choose a CSV file for bulk prediction - Upload the file and click on Predict",
    type="csv"
)

# Text input for single text sentiment prediction
user_input = st.text_input("Enter text and click on Predict", "")

# Handle prediction requests
if st.button("Predict"):
    if uploaded_file is not None:
        # Handle bulk prediction with file upload
        file = {"file": uploaded_file}
        response = requests.post(prediction_endpoint, files=file)
        
        if response.status_code == 200:
            response_bytes = BytesIO(response.content)
            response_df = pd.read_csv(response_bytes)
            
            st.write("Predictions:")
            st.dataframe(response_df)  # Display predictions in a table
            
            st.download_button(
                label="Download Predictions",
                data=response_bytes,
                file_name="Predictions.csv",
                key="result_download_button"
            )
        else:
            st.error("Error occurred while processing the file.")
            
    elif user_input.strip():
        # Handle single text prediction
        response = requests.post(prediction_endpoint, json={"text": user_input})
        
        if response.status_code == 200:
            response_json = response.json()
            st.write(f"Predicted sentiment: {response_json['prediction']}")
        else:
            st.error("Error occurred while processing the text.")
            
    else:
        st.warning("Please provide either a CSV file or text input for prediction.")

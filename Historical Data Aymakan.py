import streamlit as st
import pandas as pd

# Title for the dashboard
st.title("CSV Data Dashboard")

# Upload the CSV file
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

# Check if a file is uploaded
if uploaded_file is not None:
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(uploaded_file)

    # Display the DataFrame as a table
    st.write("Data Preview:")
    st.write(df)

    # Show basic statistics
    st.write("Summary Statistics:")
    st.write(df.describe())

pip install streamlit

import streamlit as st
import pandas as pd

# Load the dataset
df = pd.read_excel('Revenue by Account Managers.xlsx')

# Streamlit layout
st.title("Revenue Dashboard")
st.write("Revenue data by Account Managers")

# Display the dataframe
st.write(df)

# Add some interactive filters (e.g., filter by Account Manager)
selected_manager = st.selectbox("Select Account Manager", df['Account Manager'].unique())
filtered_data = df[df['Account Manager'] == selected_manager]
st.write(filtered_data)

# Display some summary statistics
st.write("Summary statistics")
st.write(filtered_data.describe())

# Simple bar chart showing revenue over months
st.bar_chart(filtered_data[['months', 'Revenue']].set_index('months'))

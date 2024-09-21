import streamlit as st
import pandas as pd

# Load the dataset
df = pd.read_excel('Revenue by Account Managers.xlsx')

# Sidebar for filtering options
st.sidebar.header("Filter Options")
selected_manager = st.sidebar.selectbox("Select Account Manager", df['Account Manager'].unique())

# Main page layout
st.title("Revenue Dashboard")
st.subheader("Overview of Revenue Data by Account Managers")

# Display the dataframe as an expandable section
with st.expander("View Raw Data"):
    st.write(df)

# Filter data based on selected account manager
filtered_data = df[df['Account Manager'] == selected_manager]

# Display filtered data
st.markdown(f"### Data for Account Manager: **{selected_manager}**")
st.write(filtered_data)

# Display summary statistics for the filtered data
st.markdown("### Summary Statistics")
st.write(filtered_data.describe())

# Display bar chart for revenue over months
st.markdown("### Revenue Over Time")
st.bar_chart(filtered_data[['months', 'Revenue']].set_index('months'))

# Additional section for future insights or analysis
st.markdown("---")
st.markdown("#### Future insights can go here...")
st.info("This section can be used to provide additional insights or analyses in the future.")

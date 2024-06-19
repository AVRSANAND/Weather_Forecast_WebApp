import streamlit as st
import plotly.express as px
from backend import get_data

st.set_page_config(layout="wide")
st.title("Weather Forecast Web App")

st.subheader("Weather Forecast for the Next Days")

place = st.text_input("Place: ", placeholder="Enter a city name")

days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of forecasted days")

data_option = st.selectbox("Select data to view",
                           options=("Temperature", "Sky"),)

st.subheader(f"{data_option} for the next {days} days in {place}")



date = get_data(place, days, data_option)

# figure = px.line(x=d, y=t, labels={"x": "Date", "y": "Temperature (C)"})
# st.plotly_chart(figure)


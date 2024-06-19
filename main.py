import streamlit as st
import plotly.express as px

st.set_page_config(layout="wide")
st.title("Weather Forecast Web App")

st.subheader("Weather Forecast for the Next Days")

place = st.text_input("Place: ", placeholder="Enter a city name")

days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of forecasted days")

data_option = st.selectbox("Select data to view",
                           options=("Temperature", "Sky"),)

st.subheader(f"{data_option} for the next {days} days in {place}")

def get_data(days):
    dates = ["2024-06-10","2024-06-11","2024-06-12"]
    temperatures = [10, 11, 15]
    temperatures = [days * i for i in temperatures]
    return dates, temperatures


d, t = get_data(days)

figure = px.line(x=d, y=t, labels={"x": "Date", "y": "Temperature (C)"})
st.plotly_chart(figure)


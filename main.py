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

if place:

    # Get Temperature & Sky Data
    filtered_data = get_data(place, days)

    if data_option == "Temperature":
        temperatures = [dict["main"]["temp"]/10 for dict in filtered_data]
        dates = [dict["dt_txt"] for dict in filtered_data]
        # Create Temperature Plot
        figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (C)"})
        st.plotly_chart(figure)

    if data_option == "Sky":
        # Create Sky View
        images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
                  "Rain": "images/rain.png", "Snow": "images/snow.png"}
        sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
        image_path = [images[condition] for condition in sky_conditions]
        st.image(image_path,width=110)
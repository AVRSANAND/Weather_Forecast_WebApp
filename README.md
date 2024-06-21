# Weather Forecast Web App

## Overview
This project is a web application built with Streamlit and Plotly for displaying weather forecasts. The app uses the OpenWeatherMap API to fetch weather data and provides a visual representation of temperature trends and sky conditions over the next few days for a specified location.

## Live Demo

You can try the live demo of the app [here](https://avrsanand-weather-forecast-webapp.streamlit.app/).

## Features
- **Weather Forecast**: Displays temperature and sky conditions for the next few days.
- **User Inputs**:
  - API Key: Required for accessing the OpenWeatherMap API.
  - Place: The city name for which to fetch the weather forecast.
  - Forecast Days: Number of days to forecast (1 to 5 days).
  - Data Option: Choice between viewing temperature data or sky conditions.

## Project Structure
```
weather-forecast-web-app/
│
├── images/                   # Folder containing images for sky conditions
│   ├── clear.png             # Image for clear sky
│   ├── cloud.png             # Image for cloudy sky
│   ├── rain.png              # Image for rainy sky
│   └── snow.png              # Image for snowy sky
│
├── main.py                   # Main application script
├── backend.py                # Script for fetching weather data
├── requirements.txt          # Project dependencies
└── README.md                 # Project README file
```

## Installation
1. **Clone the repository**:
    ```bash
    git clone https://github.com/AVRSANAND/Weather_Forecast_WebApp.git
    cd Weather_Forecast_WebApp
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the application**:
    ```bash
    streamlit run main.py
    ```

## Usage
Once the application is running, you can use the following features:

### API Key
- **Description**: Enter your OpenWeatherMap API Key. You need to create an account on `openweathermap.org` to get an API Key.

### Place
- **Description**: Enter the city name for which you want to fetch the weather forecast.

### Forecast Days
- **Description**: Select the number of days (1 to 5) for which you want the weather forecast.

### Data Option
- **Description**: Choose between viewing temperature data or sky conditions.

## Dependencies
- streamlit
- plotly
- requests

## Notes
- **Temperature Data**: The temperature values are fetched from the OpenWeatherMap API and divided by 10 for display purposes.

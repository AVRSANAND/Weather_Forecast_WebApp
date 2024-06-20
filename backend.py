import requests
API_KEY = ""

def get_data(place, days=None, data_option=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    values = 8 * days
    filtered_data = filtered_data[:values]
    if data_option == "Temperature":
        filtered_data = [dict["main"]["temp"] for dict in filtered_data]
    if data_option == "Sky":
        filtered_data = [dict["weather"][0]["main"] for dict in filtered_data]
    return filtered_data


if __name__ == "__main__":
    print(get_data(place="Hyderabad", days=3, data_option="Temperature"))
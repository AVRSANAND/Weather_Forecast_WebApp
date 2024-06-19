import requests
API_KEY = "728a0bf7d6bcfea87796ce58cc2aae63"

def get_data(place, days=None, data_option=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    return data

if __name__ == "__main__":
    print(get_data(place="Hyderabad"))
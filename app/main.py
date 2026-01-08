import os
import requests

API_KEY = os.getenv("API_KEY")
CITY = "Paris"
URL = "https://api.weatherapi.com/v1/current.json"


def get_weather() -> None:
    if not API_KEY:
        print("Error: API_KEY environment variable is not set")
        return

    params = {
        "key": API_KEY,
        "q": CITY,
        "lang": "en",
    }

    response = requests.get(URL, params=params, timeout=10)
    response.raise_for_status()

    data = response.json()

    print(
        f"{data['location']['name']}/{data['location']['country']} "
        f"{data['location']['localtime']} "
        f"Weather: {data['current']['temp_c']} Celsius, "
        f"{data['current']['condition']['text']}"
    )


if __name__ == "__main__":
    get_weather()

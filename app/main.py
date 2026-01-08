import requests


def get_weather() -> None:
    API_KEY = "5b86ef3c0e204fdbab2150451260801"
    CITY = "Paris"
    URL = "https://api.weatherapi.com/v1/current.json"

    params = {
        "key": API_KEY,
        "q": CITY,
        "lang": "en",
    }

    response = requests.get(URL, params=params, timeout=10)
    response.raise_for_status()

    data = response.json()

    location = data["location"]
    current = data["current"]

    print(
        f"{location['name']}/{location['country']} "
        f"{location['localtime']} "
        f"Weather: {current['temp_c']} Celsius, "
        f"{current['condition']['text']}"
    )


if __name__ == "__main__":
    get_weather()

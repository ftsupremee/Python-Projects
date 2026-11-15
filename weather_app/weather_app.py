import os
import requests # used for making requests to openweather
from dotenv import load_dotenv # used for getting api key out of .env
import questionary

load_dotenv()
api_key = os.getenv("OPENWEATHER_API_KEY")

def display_weather(data: dict, choices: list) -> dict:
        # getting data
        weather = data["weather"]
        main = data["main"]
        wind = data["wind"]
        clouds = data["clouds"]

        weather_description = weather[0]["description"]
        temperature = main["temp"]
        feels_like = main["feels_like"]
        humidity = main["humidity"]
        visibility = data["visibility"]
        wind_speed = wind["speed"]
        wind_direction = wind["deg"]
        cloudiness = clouds["all"]

        # making a dictionary of the weather info
        weather = {
            "Weather description": weather_description,
            "Temperature": temperature,
            "Feels like": feels_like,
            "Humidity": humidity,
            "Visibility": visibility, 
            "Wind_speed": wind_speed, 
            "Wind direction": wind_direction, 
            "Cloudiness": cloudiness,
        }

        # creating a new dictionary of that city's weather by taking info from the weather dict
        city_weather = {}
        for choice in choices:
            city_weather[choice] = weather[choice]

        return city_weather

def main():
    city = input("Enter the city you want to get weather out of: ")
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"} # setting parameters for future api call

    try:
        response = requests.get(base_url, params=params, timeout=15)
        response.raise_for_status()          # raises HTTPError for bad status codes
        data = response.json()

        # OpenWeather returns 200 even for bad cities — check the cod field
        if str(data.get("cod")) != "200":
            print(f"Error: {data.get('message', 'City not found')}")
            return

        options = ["Weather description", "Temperature", "Feels like", "Humidity",
                   "Visibility", "Wind_speed", "Wind direction", "Cloudiness"]
        choices = questionary.checkbox("What do you want to get?", choices=options).ask() # use questionary to take better CLI input for a checkbox

        if not choices: # user didn't choose anything
            print("No options selected.")
            return

        weather = display_weather(data, choices)
        for description, info in weather.items():
            print(f"{description}: {info}")

    except requests.exceptions.HTTPError as e:
        print(f"HTTP error: {e}")
    except requests.exceptions.ConnectionError:
        print("Connection error. Check your internet.")
    except requests.exceptions.Timeout:
        print("Request timed out. Try again later.")
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
    except KeyError as e:
        print(f"Unexpected response format (missing key {e})")

if __name__ == "__main__":
    main()
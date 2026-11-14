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
    params = {"q": city, "appid": api_key, "units": "metric"} # parameters for the request

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if data["cod"] == 200:
            options = ["Weather description", "Temperature", "Feels like", "Humidity",
                       "Visibility", "Wind_speed", "Wind direction", "Cloudiness"]
            choices = questionary.checkbox("What do you want to get?", options).ask()
            weather = display_weather(data, choices)
            for description, info in weather.items():
                print(f"{description}: {info}")

    except requests.exceptions.HTTPError as http_error:
        match response.status_code:
                case 400:
                    print("Bad request") 
                case 401:
                    print("Unauthorized. Please check your API key") 
                case 403:
                    print("Forbidden") 
                case 404:
                    print("City not found") 
                case 500:
                    print("Internal Server Error") 
                case 502:
                    print("Bad Gateway.") 
                case 504:
                    print("Gatway Timeout")
                case _:
                    print("HTTP Error") 
    except requests.exceptions.ConnectionError:
        print("Connection error \nPlease check your internet connection.")
    except requests.exceptions.Timeout:
        print("Request timed out \nPlease try again later.")
    except requests.exceptions.TooManyRedirects:
        print("Too many redirects \nPlease try again later.")
    except requests.exceptions.RequestException as req_error:
        print(f"Request Error: {req_error}")

if __name__ == "__main__":
    main()
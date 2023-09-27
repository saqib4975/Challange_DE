import pandas as pd
import requests

def get_weather_data(city_name):
    # Initialize the API key with your actual API key
    api_key = 'c961850a61dc345e93bd9415d74b7688'  # Replace with your API key

    # Define the base URL for the OpenWeatherMap API
    base_url = 'https://api.openweathermap.org/data/2.5/weather?'

    # Specify the units (metric for Celsius, imperial for Fahrenheit)
    units = 'metric'

    # Create the complete API URL with parameters
    url = f'{base_url}q={city_name}&units={units}&appid={api_key}'

    # Send a GET request to the API
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        weather_data = response.json()

        # Extract relevant information
        temperature = weather_data['main']['temp']
        weather_description = weather_data['weather'][0]['description']

        # Create a DataFrame from the extracted data
        weather_df = pd.DataFrame({
            "Temperature": [temperature],
            "Weather Description": [weather_description]
        })

        # Print the weather information
        print(weather_df)
    else:
        print('Failed to retrieve weather data. Status code:', response.status_code)

# Example usage:
city_name = 'Dubai'  # Replace with the city name you want
get_weather_data(city_name)


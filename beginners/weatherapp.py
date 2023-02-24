import requests

api_key = "YOUR_API_KEY"
base_url = "http://api.openweathermap.org/data/2.5/weather?"

# Get the city name from the user
city_name = input("Enter city name: ")

# Build the API URL
complete_url = base_url + "appid=" + api_key + "&q=" + city_name

# Send a request to the API and get the response
response = requests.get(complete_url)

# Parse the response and extract the weather data
if response.status_code == 200:
    data = response.json()
    weather = data["weather"][0]["description"]
    temp = data["main"]["temp"]
    temp_celsius = round(temp - 273.15, 2)
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]
    print("Weather: ", weather)
    print("Temperature: ", temp_celsius, "°C")
    print("Humidity: ", humidity, "%")
    print("Wind speed: ", wind_speed, "m/s")
else:
    print("Error getting weather data.")

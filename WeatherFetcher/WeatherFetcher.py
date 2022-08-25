from urllib import request, response
import requests

#Key and URL
API_KEY = "632bfc487be7cc97db5df875d736a942"

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

#request 
city = input("Enter a city name: ")

request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"

#response
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    print("Weather:", weather)
    temperature = round(data["main"]["temp"] - 273.15, 2)
    print("Temperature:", temperature, "Celsius")
   
  

else: 
    print("An error orrcured.")


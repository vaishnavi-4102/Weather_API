import requests
import json
import pyttsx3

text = pyttsx3.init()

input_city = input("Enter the city: \n ")
url ="https://api.weatherapi.com/v1/current.json?key=8959504613174b699bd105821233107&q={city}"

response = requests.get(url.format(city=input_city))

# print(response.json())

weather_dict = json.loads(response.text)

print(weather_dict['current']['temp_c'])

input_text = "The temperature in " + input_city + " is " + str(weather_dict['current']['temp_c']) + " degree celsius"

text.say(input_text)
text.runAndWait()
text.stop()
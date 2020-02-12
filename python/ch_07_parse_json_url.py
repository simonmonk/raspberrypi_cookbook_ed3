import json
import urllib.request

key = 'paste_your_key_here'

response = urllib.request.urlopen('http://api.weatherstack.com/current?access_key=' + key + '&query=Paris')
j = json.load(response)

print(j['current']['weather_descriptions'][0])

import json
import urllib.request

key = 'paste_your_key_here'

response = urllib.request.urlopen('http://api.apixu.com/v1/current.json?key=' + key + '&q=Paris')
j = json.load(response)

print(j['current']['condition']['text'])

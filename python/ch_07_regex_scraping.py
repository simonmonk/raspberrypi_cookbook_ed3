import re
import urllib.request

regex = '#([\d,]+) in Books'
url = 'https://www.amazon.com/Raspberry-Pi-Cookbook-Software-Solutions/dp/1492043222/'

print("The Amazon rank is.....")
 
text = urllib.request.urlopen(url).read().decode('utf-8')

print(re.search(regex, text).group())
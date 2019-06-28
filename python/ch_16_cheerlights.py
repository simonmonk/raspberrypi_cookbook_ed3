from gpiozero import RGBLED
from colorzero import Color
import time, requests

led = RGBLED(18, 23, 24)
cheerlights_url = "http://api.thingspeak.com/channels/1417/field/2/last.txt"

while True:
    try:
        cheerlights = requests.get(cheerlights_url) 
        c = cheerlights.content
        print(c)
        led.color = Color(c)
    except Exception as e:
        print(e)
    time.sleep(2)

from gpiozero import RGBLED
from guizero import App, Slider
from colorzero import Color

rgb_led = RGBLED(18, 23, 24)

red = 0
green = 0
blue = 0

def red_changed(value):
    global red
    red = int(value)
    rgb_led.color = Color(red, green, blue)

def green_changed(value):
    global green
    green = int(value)
    rgb_led.color = Color(red, green, blue)

def blue_changed(value):
    global blue
    blue = int(value)
    rgb_led.color = Color(red, green, blue)

app = App(title='RGB LED', width=500, height=400)

Slider(app, command=red_changed, end=255, width='fill', height=50).text_size = 30
Slider(app, command=green_changed, end=255, width='fill', height=50).text_size = 30
Slider(app, command=blue_changed, end=255, width='fill', height=50).text_size = 30

app.display()

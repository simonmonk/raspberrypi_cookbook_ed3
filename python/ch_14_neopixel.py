import time
import board
from neopixel import NeoPixel

led_count = 5
red = (100, 0, 0)
no_color = (0, 0, 0)

strip = NeoPixel(board.D18, led_count, auto_write=False)

def clear():
    for i in range(0, led_count):
        strip[i] = no_color
    strip.show()


i = 0
while True:
    clear()
    strip[i] = red
    strip.show()
    time.sleep(1)
    i += 1
    if i >= led_count:
        i = 0

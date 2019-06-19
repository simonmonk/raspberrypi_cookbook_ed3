import time
import unicornhat as unicorn
from random import randint

unicorn.set_layout(unicorn.AUTO)
unicorn.rotation(0)
unicorn.brightness(1)
width, height = unicorn.get_shape()

while True:
    x = randint(0, width)
    y = randint(0, height)
    r, g, b = (randint(0, 255), randint(0, 255), randint(0, 255))
    unicorn.set_pixel(x, y, r, g, b)
    unicorn.show()
    time.sleep(0.01)

time.sleep(1)

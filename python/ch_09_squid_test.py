from gpiozero import RGBLED
from time import sleep
from colorzero import Color

led = RGBLED(18, 23, 24)
led.color = Color('red')
sleep(2)
led.color = Color('green')
sleep(2)
led.color = Color('blue')
sleep(2)
led.color = Color('white')
sleep(2)


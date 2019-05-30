from gpiozero import Button, LED
from time import sleep

led = LED(23)

def toggle_led():
    print("toggling")
    led.toggle()

button = Button(18)
button.when_pressed = toggle_led


while True:
    print("Busy doing other stuff")
    sleep(2)

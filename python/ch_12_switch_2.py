from gpiozero import Button
from time import sleep

def do_stuff():
    print("Button Pressed")

button = Button(18)
button.when_pressed = do_stuff

while True:
    print("Busy doing other stuff")
    sleep(2)

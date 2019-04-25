from gpiozero import Button
import time

button = Button(7)

while True:
    if button.is_pressed:
        print(time.time())

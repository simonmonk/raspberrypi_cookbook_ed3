from gpiozero import Button, DigitalOutputDevice
import time

rows = [Button(17), Button(25), Button(24), Button(23)]
cols = [DigitalOutputDevice(27), DigitalOutputDevice(18), DigitalOutputDevice(22)]
keys = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9'],
    ['*', '0', '#']]

def get_key():
    key = 0
    for col_num, col_pin in enumerate(cols):
        col_pin.off()
        for row_num, row_pin in enumerate(rows):
            if row_pin.is_pressed:
                key = keys[row_num][col_num]
        col_pin.on()
    return key

while True:
    key = get_key()
    if key :
        print(key)
        time.sleep(0.3)

import time
import board
import busio
import adafruit_mpr121
i2c = busio.I2C(board.SCL, board.SDA)
mpr121 = adafruit_mpr121.MPR121(i2c)

while True:
    if mpr121[0].value:
        print("Pin 0 touched!")

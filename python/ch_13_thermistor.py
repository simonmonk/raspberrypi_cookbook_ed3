from PiAnalog import *
import time

p = PiAnalog()

while True:
    print(p.read_temp_c())
    time.sleep(1)
    
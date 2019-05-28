from rrb4 import *
import time

rr = RRB4(12.0, 12.0) # battery, motor

try: 
    while True:
        delay = input("Delay between steps (milliseconds)?")
        steps = input("How many steps forward? ")
        rr.step_forward(int(delay) / 1000.0, int(steps))
        steps = input("How many steps backwards? ")
        rr.step_reverse(int(delay) / 1000.0, int(steps))

finally:
    GPIO.cleanup()

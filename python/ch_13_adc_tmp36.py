from gpiozero import MCP3008
import time

analog_input = MCP3008(channel=0)

while True:
    reading = analog_input.value
    voltage = reading * 3.3 
    temp_c = voltage * 100 - 50
    temp_f = temp_c * 9.0 / 5.0 + 32
    print("Temp C={:.2f}\tTemp F={:.2f}".format(temp_c, temp_f))
    time.sleep(1)

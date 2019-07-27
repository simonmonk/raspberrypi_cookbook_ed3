from gpiozero import MCP3008
import time

analog_input = MCP3008(channel=0)

while True:
    reading = analog_input.value
    voltage = reading * 3.3 
    print("Reading={:.2f}\tVoltage={:.2f}".format(reading, voltage))
    time.sleep(1)

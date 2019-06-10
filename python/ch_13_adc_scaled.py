from gpiozero import MCP3008
import time

R1 = 10000.0
R2 = 3300.0
analog_input = MCP3008(channel=0)

while True:
    reading = analog_input.value
    voltage_adc = reading * 3.3
    voltage_actual =  voltage_adc / (R2 / (R1 + R2))
    print("Battery Voltage=" + str(voltage_actual))
    time.sleep(1)

import time, os 
import requests


PERIOD = 60 # seconds
BASE_URL = 'https://api.thingspeak.com/update.json'
KEY = 'your key goes here'

def send_data(temp):
    data = {'api_key' : KEY, 'field1' : temp}
    response = requests.post(BASE_URL, json=data)

def cpu_temp():
    dev = os.popen('/opt/vc/bin/vcgencmd measure_temp')
    cpu_temp = dev.read()[5:-3]
    return float(cpu_temp)

while True:
    temp = cpu_temp()
    print("CPU Temp (C): " + str(temp))
    send_data(temp)
    time.sleep(PERIOD)

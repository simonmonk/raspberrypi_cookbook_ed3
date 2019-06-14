import serial, time

request_reading = bytes([0xFF, 0x01, 0x86, 0x00, 0x00, 0x00, 0x00, 0x00, 0x79])

def read_co2():
    sensor.write(request_reading)
    time.sleep(0.1)
    raw_data = sensor.read(9)
    high = raw_data[2]
    low = raw_data[3]
    return high * 256 + low;

sensor = serial.Serial('/dev/ttyS0')
print(sensor.name)
if sensor.is_open:
    print("Open")

while True:
    print("CO2 (ppm):" + str(read_co2()))
    time.sleep(1)

import smbus
import time

bus = smbus.SMBus(1)

i2c_address = 0x1D
control_reg = 0x2A

bus.write_byte_data(i2c_address, control_reg, 0x01) # Start
bus.write_byte_data(i2c_address, 0x0E, 0x00) # 2g range

time.sleep(0.5)

def read_acc():
    data = bus.read_i2c_block_data(i2c_address, 0x00, 7)
    x = (data[1] * 256 + data[2]) / 16
    if x > 2047 :
        x -= 4096
    y = (data[3] * 256 + data[4]) / 16
    if y > 2047 :
        y -= 4096
    z = (data[5] * 256 + data[6]) / 16
    if z > 2047 :
        z -= 4096
    return (x, y, z)

while True:
    x, y, z = read_acc()
    if x > 400:
        print("Left")
    elif x < -400:
        print("Right")
    elif y > 400:
        print("Back")
    elif y < -400:
        print("Forward")
    time.sleep(0.2)

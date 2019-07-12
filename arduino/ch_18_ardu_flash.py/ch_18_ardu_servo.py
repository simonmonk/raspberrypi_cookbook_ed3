import pyfirmata

board = pyfirmata.Arduino('/dev/ttyACM0')
servo_pin = board.get_pin('d:11:s')

while True:
    angle_s = input("Enter Angle (0 to 180):")
    angle = int(angle_s)
    servo_pin.write(angle)

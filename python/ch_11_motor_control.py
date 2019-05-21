from gpiozero import Motor

motor = Motor(forward=23, backward=24)
 
while True:
    cmd = input("Command, f/r 0..9, E.g. f5 :")
    direction = cmd[0]
    speed = float(cmd[1]) / 10.0
    if direction == "f":
        motor.forward(speed=speed)
    else: 
        motor.backward(speed=speed)


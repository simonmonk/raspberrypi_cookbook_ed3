from bluedot import BlueDot
bd = BlueDot()
while True:
    bd.wait_for_press()
    print("You pressed the blue dot!")

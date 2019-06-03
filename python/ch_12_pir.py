from gpiozero import MotionSensor

pir = MotionSensor(18)

while True:
    pir.wait_for_motion()
    print("Motion detected!")

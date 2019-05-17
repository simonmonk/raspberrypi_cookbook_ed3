from adafruit_servokit import ServoKit
from guizero import App, Slider

servo_kit = ServoKit(channels=16)

def slider_changed(angle):
    servo_kit.servo[0].angle = int(angle) + 90  

app = App(title='Servo Angle', width=500, height=150)
slider = Slider(app, start=-90, end=90, command=slider_changed, width='fill', height=50)
slider.text_size = 30
app.display()

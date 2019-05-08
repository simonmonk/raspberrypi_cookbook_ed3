import os
from guizero import App, Slider

servo_min = 500  # uS
servo_max = 2500  # uS
servo = 2 # GPIO 18

def map(value, from_low, from_high, to_low, to_high): 
  from_range = from_high - from_low
  to_range = to_high - to_low
  scale_factor = float(from_range) / float(to_range)
  return to_low + (value / scale_factor)
  
def set_angle(angle):
  pulse = int(map(angle+90, 0, 180, servo_min, servo_max))
  command = "echo {}={}us > /dev/servoblaster".format(servo, pulse)
  os.system(command)

def slider_changed(angle):
  set_angle(int(angle))  

app = App(title='Servo Angle', width=500, height=150)
slider = Slider(app, start=-90, end=90, command=slider_changed, width='fill', height=50)
slider.text_size = 30
app.display()

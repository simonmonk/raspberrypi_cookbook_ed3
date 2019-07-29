import pyfirmata
from guizero import App, Slider

board = pyfirmata.Arduino('/dev/ttyACM0')
pin = board.get_pin('d:10:p')

def slider_changed(percent):
    pin.write(int(percent) / 100.0) 

app = App(title='PWM', width=500, height=150)
slider = Slider(app, command=slider_changed, width='fill', height=50)
slider.text_size = 30
app.display()

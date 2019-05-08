from gpiozero import PWMOutputDevice 
from guizero import App, Slider

pin = PWMOutputDevice(18)

def slider_changed(percent):
    pin.value = int(percent) / 100  

app = App(title='PWM', width=500, height=150)
slider = Slider(app, command=slider_changed, width='fill', height=50)
slider.text_size = 30
app.display()

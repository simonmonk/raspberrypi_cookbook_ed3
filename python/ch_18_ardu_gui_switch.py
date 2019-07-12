import pyfirmata
from guizero import App, PushButton

board = pyfirmata.Arduino('/dev/ttyACM0')
pin = board.get_pin('d:10:o')

def start():
    start_button.disable()
    stop_button.enable()
    pin.write(1)

def stop():
    start_button.enable()
    stop_button.disable()
    pin.write(0)

app = App(width=100, height=150)
start_button = PushButton(app, command=start, text="On")
start_button.text_size = 30
stop_button = PushButton(app, command=stop, text="Off", enabled=False)
stop_button.text_size = 30
app.display()

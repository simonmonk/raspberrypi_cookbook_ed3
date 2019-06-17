import VL53L1X, time
from guizero import App, Text

tof = VL53L1X.VL53L1X(i2c_bus=1, i2c_address=0x29)
tof.open() 
tof.start_ranging(1)

def update_reading():
    mm = tof.get_distance()
    reading_text.value = str(mm)

app = App(width=300, height=150)
reading_text = Text(app, size=100) 
reading_text.repeat(1000, update_reading)
app.display()

from sense_hat import SenseHat
import time

sense = SenseHat()

while True:
    bearing = sense.get_compass()
    print('Bearing: {:.0f} to North'.format(bearing))
    time.sleep(0.5)

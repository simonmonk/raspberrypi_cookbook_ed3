import VL53L1X, time

tof = VL53L1X.VL53L1X(i2c_bus=1, i2c_address=0x29)
tof.open() 
tof.start_ranging(1) # Start ranging, 1 = Short Range, 2 = Medium Range, 3 = Long Range

while True:
    mm = tof.get_distance() # Grab the range in mm
    print("mm=" + str(mm))
    time.sleep(1)

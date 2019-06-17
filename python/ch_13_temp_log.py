import os, glob, time, datetime

log_period = 60 # seconds

logging_folder = glob.glob('/media/*')[0]
dt = datetime.datetime.now()
file_name = "temp_log_{:%Y_%m_%d}.csv".format(dt)
logging_file = logging_folder + '/' + file_name

def read_temp():
    dev = os.popen('/opt/vc/bin/vcgencmd measure_temp')
    cpu_temp = cpu_temp_s = dev.read()[5:-3] # top and tail string
    return cpu_temp

def log_temp():
    temp_c = read_temp()
    dt = datetime.datetime.now()
    f = open(logging_file, 'a')
    line = '\n"{:%H:%M:%S}","{}"'.format(dt, temp_c)
    f.write(line)
    print(line)
    f.close()

print("Logging to: " + logging_file)
while True:
    log_temp()
    time.sleep(log_period)

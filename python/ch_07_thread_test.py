import threading, time, random

def annoy(message):
    while True:
        time.sleep(random.randint(1, 3))
        print(message)
          
t = threading.Thread(target=annoy, args=('BOO !!',))
t.start()

x = 0
while True:
    print(x)
    x += 1
    time.sleep(1)

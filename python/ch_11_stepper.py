from gpiozero import Motor
import time

coil1 = Motor(forward=18, backward=23, pwm=False)
coil2 = Motor(forward=24, backward=17, pwm=False)
 
forward_seq = ['FF', 'BF', 'BB', 'FB']
reverse_seq = list(forward_seq) # to copy the list
reverse_seq.reverse()
 
def forward(delay, steps):  
  for i in range(steps):
    for step in forward_seq:
      set_step(step)
      time.sleep(delay)
 
def backwards(delay, steps):  
  for i in range(steps):
    for step in reverse_seq:
      set_step(step)
      time.sleep(delay)
 
def set_step(step):
  if step == 'S':
    coil1.stop()
    coil2.stop()
  else:
    if step[0] == 'F':
      coil1.forward()
    else:
      coil1.backward()
    if step[1] == 'F':
      coil2.forward()
    else:
      coil2.backward()


while True:
  set_step('S')
  delay = input("Delay between steps (milliseconds)?")
  steps = input("How many steps forward? ")
  forward(int(delay) / 1000.0, int(steps))
  set_step('S')
  steps = input("How many steps backwards? ")
  backwards(int(delay) / 1000.0, int(steps))

from gpiozero import PWMLED

led = PWMLED(18)

while True:
    f_s = input("Enter Frequncy in Hz:")
    f = int(f_s)
    led.close()
    led = PWMLED(18, frequency=f)
    led.value = 0.5

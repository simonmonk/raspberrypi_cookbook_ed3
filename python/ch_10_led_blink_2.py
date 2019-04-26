from gpiozero import LED

led = LED(18)

led.blink(0.5, 0.5, background=True)

print("here")
input()
print("there")
led.off()
input()

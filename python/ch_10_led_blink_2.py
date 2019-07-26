from gpiozero import LED

led = LED(18)

led.blink(0.5, 0.5, background=True)

print("Notice that control has moved away - hit Enter to continue")
input()
print("Control is now back")
led.off()
input()

from gpiozero import PWMLED

led = PWMLED(18)

while True:
    brightness_s = input("Enter Brightness (0.0 to 1.0):")
    brightness = float(brightness_s)
    led.value = brightness

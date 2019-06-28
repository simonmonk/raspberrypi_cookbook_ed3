from gpiozero import Buzzer

buzzer = Buzzer(18)

def buzz(pitch, duration):
    period = 1.0 / pitch
    delay = period / 2
    cycles = int(duration * pitch)
    buzzer.beep(on_time=period, off_time=period, n=int(cycles/2))

while True:
    pitch_s = input("Enter Pitch (200 to 2000): ")
    pitch = float(pitch_s)
    duration_s = input("Enter Duration (seconds): ")
    duration = float(duration_s)
    buzz(pitch, duration)

import time
import dweepy
from gpiozero import LED

KEY = 'tweet_about_me'
led = LED(18)

while True:
    try:
        for dweet in dweepy.listen_for_dweets_from(KEY):
            print('Tweet: ' + dweet['content']['text'])
            led.on()
            time.sleep(10)
            led.off()
    except Exception:
        pass

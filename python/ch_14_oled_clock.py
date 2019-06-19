import Adafruit_SSD1306
from PIL import Image, ImageDraw, ImageFont
import time
from datetime import datetime

# Set up display
disp = Adafruit_SSD1306.SSD1306_128_64(rst=None, i2c_address=0x3C)
small_font = ImageFont.truetype('FreeSans.ttf', 12)
large_font = ImageFont.truetype('FreeSans.ttf', 33)
disp.begin()
disp.clear()
disp.display()
# Make an image to draw on in 1-bit color.
width = disp.width
height = disp.height
image = Image.new('1', (width, height))
draw = ImageDraw.Draw(image)

# Display a message on 3 lines, first line big font        
def display_message(top_line, line_2):
    draw.rectangle((0,0,width,height), outline=0, fill=0)
    draw.text((0, 0),  top_line, font=large_font, fill=255)
    draw.text((0, 50),  line_2, font=small_font, fill=255)
    disp.image(image)
    disp.display()

while True:
    now = datetime.now()
    date_message = '{:%d %B %Y}'.format(now)
    time_message = '{:%H:%M:%S}'.format(now)
    display_message(time_message, date_message)
    time.sleep(0.1)

import cv2
import numpy as np
from imutils.video import VideoStream
from imutils import resize

diff_threshold = 1000000

vs = VideoStream(src=0).start()

def getImage():
    im = vs.read()
    im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    im = cv2.blur(im, (20, 20))
    return im

old_image = getImage()

while True:
    new_image = getImage()
    diff = cv2.absdiff(old_image, new_image)
    diff_score = np.sum(diff)
    # print(diff_score)
    if diff_score > diff_threshold:
        print("Movement detected")
    old_image = new_image

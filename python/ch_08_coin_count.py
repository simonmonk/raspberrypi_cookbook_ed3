import cv2
import time
import numpy as np
from imutils.video import VideoStream
from imutils import resize

vs = VideoStream(src=1).start()
img = vs.read()
img = resize(img, width=800)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

img = cv2.blur(img, (3, 3)) 

detected_circles = cv2.HoughCircles(img,  
                   cv2.HOUGH_GRADIENT, 1, 20, param1 = 50, 
               param2 = 30, minRadius = 15, maxRadius = 100)

detected_circles = np.uint16(np.around(detected_circles))

print(detected_circles)

for pt in detected_circles[0, :]: 
        a, b, r = pt[0], pt[1], pt[2] 
        cv2.circle(img, (a, b), r, (0, 255, 0), 2) 

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
vs.stop()

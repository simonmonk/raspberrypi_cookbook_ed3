import cv2
from imutils.video import VideoStream
from imutils import resize

vs = VideoStream(src=0).start()
old_count = 0

while True:
    try:
        img = vs.read()
        img = resize(img, width=800)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = cv2.blur(img, (3, 3)) 

        detected_circles = cv2.HoughCircles(img,  
            cv2.HOUGH_GRADIENT, 1, 20, param1 = 50, 
            param2 = 30, minRadius = 15, maxRadius = 100)

        count = len(detected_circles[0]	)
        if count != old_count:
            print(count)
            old_count = count
    except:
        vs.stop()

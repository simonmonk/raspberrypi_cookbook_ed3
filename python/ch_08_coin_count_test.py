import cv2
from imutils.video import VideoStream
from imutils import resize

vs = VideoStream(src=0).start()

while True:
    img = vs.read()
    img = resize(img, width=800)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.blur(img, (3, 3)) 

    detected_circles = cv2.HoughCircles(img,  
        cv2.HOUGH_GRADIENT, 1, 20, param1 = 50, 
        param2 = 30, minRadius = 15, maxRadius = 100)

    print(detected_circles)

    for pt in detected_circles[0]: 
        a, b, r = pt[0], pt[1], pt[2] 
        cv2.circle(img, (a, b), r, (0, 0, 0), 2) 

    cv2.imshow('image', img)
    key = cv2.waitKey(0)
    cv2.destroyAllWindows()
    if key == ord('x'):
        break

vs.stop()

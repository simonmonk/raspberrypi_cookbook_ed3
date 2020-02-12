import cv2

cv2_data_dir = '/usr/local/lib/python3.7/dist-packages/cv2/data/'
face_cascade = cv2.CascadeClassifier(cv2_data_dir + 'haarcascade_frontalface_default.xml')

img = cv2.imread('faces.jpg', cv2.IMREAD_GRAYSCALE)

scale_factor = 1.4
min_neighbours = 5

faces = face_cascade.detectMultiScale(img, scale_factor, min_neighbours)
print(faces)

for (x,y,w,h) in faces:
    img = cv2.rectangle(img, (x,y), (x+w,y+h), (255, 255, 255), 2)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

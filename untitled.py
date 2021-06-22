import cv2

face_cascade = cv2.CascadeClassifier('face_detector.xml')

photo = cv2.imread('image.png')
faces = face_cascade.detectMultiScale(img, 1.1, 4)

for (x, y, w, h) in faces: 
  cv2.rectangle(img, (x, y), (x+w, y+h), (245, 0, 0), 3)
cv2.imwrite("face_detected.png", img) 
print('Successfully saved')



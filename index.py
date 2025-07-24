import cv2


img = cv2.imread('face.jpg')

face_cascade = cv2.CascadeClassifier("frontal_face.xml")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=4)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

cv2.imshow("Yüz Tespiti", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
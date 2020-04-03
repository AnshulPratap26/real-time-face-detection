# live coding to detect faces using python and opencv
import cv2

faces = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    face = faces.detectMultiScale(frame, 1.3, 5)
    for (x,y,w,h) in face:
        cv2.rectangle(frame, (x,y),(x+w,y+h),(255,0,0),2)

    cv2.imshow("detecting faces", frame)
    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()


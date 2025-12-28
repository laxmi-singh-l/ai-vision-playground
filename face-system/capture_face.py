import cv2
import os

NAME = "laamu"
SAVE_PATH = f"dataset/{NAME}"
os.makedirs(SAVE_PATH, exist_ok=True)

face_cascade = cv2.CascadeClassifier(
    "haarcascade_frontalface_default.xml"
)

cap = cv2.VideoCapture(0)
count = 0

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        face = gray[y:y+h, x:x+w]
        count += 1
        cv2.imwrite(f"{SAVE_PATH}/{count}.jpg", face)

        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)

    cv2.imshow("Capture Face", frame)

    if cv2.waitKey(1) == 27 or count == 20:
        break

cap.release()
cv2.destroyAllWindows()
print("Face captured and saved")

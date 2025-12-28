import cv2
import os
import numpy as np
from datetime import datetime

face_cascade = cv2.CascadeClassifier(
    "haarcascade_frontalface_default.xml"
)

recognizer = cv2.face.LBPHFaceRecognizer_create()

faces = []
labels = []
label_map = {}
label_id = 0

# Load dataset
for person in os.listdir("dataset"):
    label_map[label_id] = person
    person_path = os.path.join("dataset", person)

    for img in os.listdir(person_path):
        image = cv2.imread(
            os.path.join(person_path, img),
            cv2.IMREAD_GRAYSCALE
        )
        faces.append(image)
        labels.append(label_id)

    label_id += 1

recognizer.train(faces, np.array(labels))

cap = cv2.VideoCapture(0)
logged = False

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces_detected = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces_detected:
        face = gray[y:y+h, x:x+w]
        label, confidence = recognizer.predict(face)
        name = label_map[label]

        if confidence < 60 and not logged:
            with open("capture_log.txt", "a") as f:
                f.write(f"{name} captured at {datetime.now()}\n")
            logged = True

        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)
        cv2.putText(frame, name, (x,y-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8,
                    (0,255,0), 2)

    cv2.imshow("Recognition", frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
print("Recognition and logging completed")

import cv2
import time
import os
import json
import serial


# Define relative paths
base_path = os.path.dirname(os.path.abspath(__file__))
haarcascades_path = os.path.join(
    base_path, "haarcascades/haarcascade_frontalface_alt2.xml"
)
models_path = os.path.join(base_path, "Models/Models.yml")

face_cascade = cv2.CascadeClassifier(haarcascades_path)

names = []
filename = "names.json"

# Load JSON data from the file
try:
    with open(filename, "r") as file:
        data = json.load(file)
except FileNotFoundError:
    print(f"File '{filename}' not found.")
    data = []

# Extract "name" property from each object and create a string array
names = [item["name"] for item in data]

try:
    model = cv2.face.LBPHFaceRecognizer_create()
    model.read(models_path)
except:
    print("Error opening Models")
    exit()

print("Opening camera")

try:
    for _ in range(10):
        i = 0
        cap = cv2.VideoCapture(i)

        if cap.isOpened():
            print("Camera opened on port {}".format(i))
            break

        if not cap.isOpened():
            i += 1

except:
    pass

if not cap.isOpened():
    print("Camera not opened")
    exit()

print("Press q to quit")

# Serial communication setup
ser = serial.Serial("COM5", 9600)
ser.timeout = 1
time.sleep(2)
last_write_time = 0
write_interval = 2.5


while 1:
    _, img = cap.read()
    img = cv2.flip(img, 1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for x, y, w, h in faces:
        face = img[y : y + h, x : x + w]
        cv2.rectangle(img, (x, y), (x + w, y + h), (200, 150, 0), 2)
        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

        try:
            result = model.predict(face)

            if result[1] < 500:
                confidence = int(100 * (1 - (result[1]) / 300))
                id = result[0]
                print(id, confidence)

            if confidence >= 83:
                cv2.putText(
                    img,
                    "{},{}".format(str(names[id]), confidence),
                    (x, y),
                    cv2.FONT_HERSHEY_COMPLEX,
                    0.8,
                    (0, 255, 0),
                    2,
                )
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

                # Sending data name to arduino
                current_time = time.time()
                if current_time - last_write_time >= write_interval:
                    name = str(names[id]) + "\n"
                    ser.write(name.encode())
                    ser.flush()
                    last_write_time = current_time
                    time.sleep(0.2)

            else:
                cv2.putText(
                    img,
                    "Unknown",
                    (x, y),
                    cv2.FONT_HERSHEY_COMPLEX,
                    0.8,
                    (0, 0, 255),
                    2,
                )
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

        except:
            pass

    cv2.imshow("Kamera", img)

    k = cv2.waitKey(30) & 0xFF
    if k == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

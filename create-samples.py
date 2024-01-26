import cv2
import os

id = []

parent_dir = (
    "Samples"  # Assuming Samples folder is in the same directory as this script
)

for path, subdirname, filenames in os.walk(parent_dir):
    if os.path.basename(path) == "Samples":
        continue
    else:
        id.append(os.path.basename(path))

if not id:
    id_new = "0"
else:
    id_new = str(int(id[-1]) + 1)

print(id_new)
created_dir = os.path.join(parent_dir, id_new)
os.makedirs(created_dir)  # Using os.makedirs to create nested directories if necessary

cap = None
count = 0
face_cascade = cv2.CascadeClassifier(
    "haarcascades/haarcascade_frontalface_alt2.xml"  # Using relative path
)
target = 100

print("Opening camera")
try:
    for _ in range(10):
        i = 1
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


def create_sample(img):
    global count
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    if faces is ():
        return None

    for x, y, w, h in faces:
        cropped = img[y : y + h, x : x + w]
        cv2.rectangle(img, (x, y), (x + w, y + h), (200, 150, 0), 2)
        face = cv2.cvtColor(cropped, cv2.COLOR_BGR2GRAY)

        file_name_path = os.path.join(
            parent_dir, id_new, "Sample" + str(count) + ".jpg"
        )
        print(file_name_path)
        cv2.imwrite(file_name_path, face)

        cv2.putText(
            face, str(count), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2
        )
        cv2.imshow("train", face)

        count += 1


while True:
    _, img = cap.read()

    img = cv2.flip(img, 1)

    if create_sample(img) is None:
        pass

    cv2.imshow("Training camera", img)

    k = cv2.waitKey(30) & 0xFF
    if k == ord("q") or count == target:
        break

cap.release()
cv2.destroyAllWindows()
print("Collecting samples completed!")

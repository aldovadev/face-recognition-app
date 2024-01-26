import cv2
import numpy as np
import time

face_cascade = cv2.CascadeClassifier('D:/MES/Tugas Akhir Mahasiswa/D4/Nilam PNP/Face Detection/haarcascades/haarcascade_frontalface_alt2.xml')
names = ['ID 0 = Aldova', 'ID 1 = Anji*g']
try:
    model = cv2.face.LBPHFaceRecognizer_create()
    model.read('D:/MES/Tugas Akhir Mahasiswa/D4/Nilam PNP/Face Detection/Face Recognition V2/Models/Models.yml')

except:
    print('error opening Models')
    exit()

print('Opening camera')
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
    print('Camera not opened')
    exit()

print('Press q to quit')
while(1):
    _, img = cap.read()
    img = cv2.flip(img,1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        face = img[y:y+h, x:x+w]
        cv2.rectangle(img, (x,y), (x+w, y+h), (200,150,0),2)
        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

        try:
            result = model.predict(face)
            
            if result[1] < 500:
                confidece = int(100*(1-(result[1])/300))
                id = result[0]
                print(id,confidece)

            if confidece >= 83:
                cv2.putText(img,'{},{}'.format(str(names[id]),confidece), (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 2)
                cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0),2)

            else:
                cv2.putText(img, "Unknown ID", (x,y), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 255), 2)
                cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255),2)

        except:
            pass


    cv2.imshow('Kamera',img)

    k = cv2.waitKey(30) &0xff
    if k == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


    

import cv2
import numpy as np
import os

try:
    model = cv2.face.LBPHFaceRecognizer_create()
    model.read('D:\Data Rifqi\Belajar Python\Cascade classification\Face detection\Face Recognition V2\Models\Models.yml')

except:
    print('error opening Models')
    exit()

names = ['Rifqi']
def Recognize(img):
    face_cascade = cv2.CascadeClassifier('D:\Data Rifqi\Belajar Python\Cascade classification\Face detection\haarcascades\haarcascade_frontalface_alt2.xml')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        face = img[y:y+h, x:x+w]
        cv2.rectangle(img, (x,y), (x+w, y+h), (200,150,0),2)
        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

        result = model.predict(face)
        print(result)
        if result[1] < 500:
            confidece = int(100*(1-(result[1])/300))
            ids = result[0]
            print(ids,confidece)

        if confidece >= 92:
            cv2.putText(img,'{},{}'.format(str(names[ids]),confidece), (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 2)
            cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0),2)

        else:
            cv2.putText(img, "Unclassified Object", (x,y), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 255), 2)
            cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255),2)

    cv2.imshow('images',img)
        
dir = 'D:\Data Rifqi\Belajar Python\Cascade classification\Face detection\Face Recognition V2\Test Image'
for path,subdirname,filenames in os.walk(dir):
    for filename in filenames:
        if filename.endswith('png') or filename.endswith('.jpg'):
            img_path = os.path.join(path,filename)
            img = cv2.imread(img_path)
            Recognize(img)
            #cv2.imshow('images',img)
            k = cv2.waitKey(0)

cv2.destroyAllWindows()


    

import cv2
import numpy as np
import os

id = [None]

parent_dir = 'D:\Data Rifqi\Belajar Python\Cascade classification\Face detection\Face Recognition V2\Samples'
for path,subdirname,filenames in os.walk(parent_dir):
    if os.path.basename(path) == 'Samples':
        continue
    else:
        id.append(os.path.basename(path))

    id.remove(None)

if id[0] == None:
    id_new = '0'

else:
    id_new = str(int(id[len(id)-1])+1)

print(id_new)
created_dir = os.path.join(parent_dir,id_new)
os.mkdir(created_dir)
cap = None
count = 0
face_cascade = cv2.CascadeClassifier('D:\Data Rifqi\Belajar Python\Cascade classification\Face detection\haarcascades\haarcascade_frontalface_alt2.xml')
target = 100

def create_sample(img):
    global count
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    if faces is():
        return None

    for (x,y,w,h) in faces:
        cropped = img[y:y+h, x:x+w]
        cv2.rectangle(img, (x,y), (x+w, y+h), (200,150,0),2)
        face = cv2.cvtColor(cropped, cv2.COLOR_BGR2GRAY)
        
        file_name_path = 'D:/Data Rifqi/Belajar Python/Cascade classification/Face detection/Face Recognition V2/Samples/'+id_new+'/Sample'+str(count)+'.jpg'
        print(file_name_path)
        cv2.imwrite(file_name_path,face)

        cv2.putText(face,str(count),(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
        cv2.imshow('train',face)
        count +=1

dir = 'D:\Data Rifqi\Belajar Python\Cascade classification\Face detection\Face Recognition V2\Input Image'
for _ in range(10):
    for path,subdirname,filenames in os.walk(dir):
        for filename in filenames:
            if filename.endswith('png') or filename.endswith('.jpg'):
                img_path = os.path.join(path,filename)
                img = cv2.imread(img_path)
                create_sample(img)
                cv2.imshow('images',img)
            k = cv2.waitKey(10)

cv2.destroyAllWindows()
print('collecting samples completed!')


import cv2
import numpy as np
import os
import time

Training_Data = []
Labels = []
parent_dir = 'D:/MES/Tugas Akhir Mahasiswa/D4/Nilam PNP/Face Detection/Face Recognition V2/Samples'
for path,subdirname,filenames in os.walk(parent_dir):
    for filename in filenames:
        if filename.endswith('png') or filename.endswith('.jpg'):
            id = os.path.basename(path)
            img_path = os.path.join(path,filename)
            print('id:',id, '| path:',img_path)
            images = cv2.imread(img_path,cv2.IMREAD_GRAYSCALE)
            cv2.imshow('Input',images)
            Training_Data.append(np.asarray(images,dtype=np.uint8))
            Labels.append(int(id))
            k = cv2.waitKey(5)
            
Labels = np.asarray(Labels,dtype=np.int32)
awal = time.time()
model = cv2.face.LBPHFaceRecognizer_create()
model.train(np.asarray(Training_Data),np.asarray(Labels))
model.save('D:/MES/Tugas Akhir Mahasiswa/D4/Nilam PNP/Face Detection/Face Recognition V2/Models/Models.yml')
print('Training data saved at Models')
akhir = time.time()
print('Model Training Completed in {:.4f}S'.format(akhir-awal))

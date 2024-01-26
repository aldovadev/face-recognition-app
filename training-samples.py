import cv2
import numpy as np
import os
import time

Training_Data = []
Labels = []
parent_dir = (
    "Samples"  # Assuming Samples folder is in the same directory as this script
)

# Define a fixed size for your images (adjust as needed)
img_size = (200, 200)

for path, subdirname, filenames in os.walk(parent_dir):
    for filename in filenames:
        if filename.endswith("png") or filename.endswith(".jpg"):
            id = os.path.basename(path)
            img_path = os.path.join(path, filename)
            print("id:", id, "| path:", img_path)

            # Read the image and resize it to a fixed size
            images = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
            images = cv2.resize(images, img_size)

            cv2.imshow("Input", images)

            Training_Data.append(np.asarray(images, dtype=np.uint8))
            Labels.append(int(id))
            k = cv2.waitKey(5)

Labels = np.asarray(Labels, dtype=np.int32)
awal = time.time()

# Using __file__ to get the current script's directory
script_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(script_dir, "Models/Models.yml")

model = cv2.face.LBPHFaceRecognizer_create()
model.train(np.asarray(Training_Data), np.asarray(Labels))
model.save(model_path)
print("Training data saved at Models")
akhir = time.time()
print("Model Training Completed in {:.4f}S".format(akhir - awal))

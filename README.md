#TEST# Face Recognition App

This Python application implements a face recognition system using the OpenCV library. The application detects and recognizes faces in images or real-time video streams. It provides functionalities to create samples for face recognition, reset the samples, train the samples into a model, and run the face recognition system.

## How to Use

1. **Create Samples**: 
    - Run `create-samples.py` to capture samples of faces for training the recognition model.
    - Follow the on-screen instructions to capture multiple samples for each person.

2. **Reset Samples**: 
    - Run `reset.py` to delete all previously captured samples.
    - This is useful when you want to start fresh with a new set of samples.

3. **Train Samples**: 
    - Run `training-samples.py` to train the captured samples into a recognition model (`model.yml`).
    - The model will be trained based on the captured samples to recognize faces accurately.

4. **Run the Application**: 
    - Run `main.py` to start the face recognition application.
    - The application will use the trained model to recognize faces in images or real-time video streams.

## Algorithm Overview

1. **Face Detection**: 
    - The application uses Haarcascades classifiers to detect faces in images or video frames.

2. **Face Recognition**: 
    - After detecting faces, the application matches them with the trained model to recognize known faces.

3. **Sample Creation**: 
    - During the sample creation process, multiple images of each person's face are captured for training.

4. **Model Training**: 
    - The captured samples are used to train a recognition model using machine learning algorithms.

5. **Real-time Recognition**: 
    - Once trained, the recognition model is used to identify faces in real-time video streams.

## Dependencies

- Python 3.x
- OpenCV library (cv2)

## Stack Used

![Python and OpenCV](https://img.shields.io/badge/Python-OpenCV-blue)

## How to Run

1. Clone this repository to your local machine.
2. Make sure you have Python and OpenCV installed.
3. Navigate to the directory where the repository is cloned.
4. Follow the instructions above to perform the desired actions.
5. Run `main.py` to start the face recognition application.

## Credits

This application is developed by aldovadev.
The Haarcascades classifiers used for face detection are from the [OpenCV GitHub repository](https://github.com/opencv/opencv).

This game is developed by Aldovadev.

<p align="left">
<a href="https://linkedin.com/in/aldovadev" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="ey afif habibie" height="30" width="40" /></a>
<a href="https://instagram.com/aldovadev" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/instagram.svg" alt="ey_afif_habibie" height="30" width="40" /></a>
<a href="https://discord.gg/aldovadev" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/discord.svg" alt="habibdev" height="30" width="40" /></a>
</p>
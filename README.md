# Image Recognition with YOLO

## Introduction

This project utilizes YOLO (You Only Look Once), an advanced object detection algorithm, to identify, count, and label objects in a video. The YOLO model is loaded from the 'yolov8n.pt' file to make predictions on each frame of the input video. Detected objects are highlighted with bounding boxes and labeled with their class names. Additionally, the code counts the number of instances of each class in each frame and displays this count in a rectangle at the top left corner of the video output. The processed video is saved as 'output.mp4'.

## Requirements

Ensure you have the following libraries installed:

- OpenCV
- YOLO
- Numpy

You can install the required Python libraries using pip:
```bash
pip install opencv-python numpy

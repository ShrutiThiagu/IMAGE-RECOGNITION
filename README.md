# IMAGE-RECOGNITION

# Introduction
This code leverages YOLO (You Only Look Once), an object detection algorithm, to identify, count, and label objects in a video. By loading the YOLO model from the 'yolov8n.pt' file, the algorithm predicts objects in each video frame, draws bounding boxes around detected objects, and labels them with their respective class names. Additionally, it counts the instances of each class in every frame and displays this count, along with the class name, in a rectangle at the top left corner of the video output. The processed video is saved as 'output.mp4'.

# Requirements
~ OpenCV
~ YOLO
~ Numpy

# Output
The code outputs a video file, 'output.mp4', with objects labeled and counted.

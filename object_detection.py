from ultralytics import YOLO
import cv2
import numpy as np
from item_list import things

# Load the video
cap = cv2.VideoCapture("Student Stops Bus After Driver Passes Out.mp4")

# Load the YOLO model
model = YOLO('yolov8n.pt')

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output.mp4', fourcc, 30.0, (int(cap.get(3)), int(cap.get(4))))

def count(item, items):
    return str(sum([1 for item_ in items if item_ == item]))

a = 0
while True:
    ret, frame = cap.read()
    if not ret:
        break
    if a % 5 == 0:
        z = model.predict(frame)
        items_ = list(z[0].boxes.cls)
        items = [int(item) for item in items_]

    # Draw the video output rectangle
    cv2.rectangle(frame, (0, 0), (225, 75 + 15 * len(set(items))), (245, 117, 16), -1)

    # Draw the class and count in the video output rectangle
    for i, item in enumerate(list(set(items))):
        cv2.putText(frame, count(item, items) + "  " + item_list[item + 1], 
                    (15, 12 + 20 * (i + 1)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)

    # Write the frame to the output video file
    out.write(frame)

    a += 1
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

# Release everything and close the windows
cap.release()
out.release()
cv2.destroyAllWindows()

# Play the output video file
cap = cv2.VideoCapture('output.mp4')
while True:
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow('Output Video', frame)
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

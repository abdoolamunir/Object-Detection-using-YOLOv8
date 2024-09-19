import cv2  # OpenCV for handling video and image processing
from ultralytics import YOLO  # YOLOv8 model for object detection
import numpy as np  # Numpy for working with arrays (bounding boxes and classes)

# Load video file
cap = cv2.VideoCapture("TrafficPolice.mp4")

# Load the YOLOv8 model (using the medium version here)
model = YOLO("yolov8m.pt")

# List of class names from the COCO dataset
class_names = [
    "person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat", "traffic light", 
    "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat", "dog", "horse", "sheep", "cow", 
    "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella", "handbag", "tie", "suitcase", "frisbee", 
    "skis", "snowboard", "sports ball", "kite", "baseball bat", "baseball glove", "skateboard", "surfboard", 
    "tennis racket", "bottle", "wine glass", "cup", "fork", "knife", "spoon", "bowl", "banana", "apple", 
    "sandwich", "orange", "broccoli", "carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa", 
    "pottedplant", "bed", "diningtable", "toilet", "tvmonitor", "laptop", "mouse", "remote", "keyboard", 
    "cell phone", "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors", 
    "teddy bear", "hair drier", "toothbrush"
]

# Generate random colours for each class
colours = np.random.uniform(0, 255, size=(len(class_names), 3))

# Loop through each frame in the video
while True:
    # Capture each frame from the video
    ret, frame = cap.read()

    # If no frame is captured (end of video), break the loop
    if not ret:
        break

    # Run YOLOv8 object detection on the current frame
    results = model(frame)
    result = results[0]

    # Extract bounding boxes and class labels from the results
    bboxes = np.array(result.boxes.xyxy.cpu(), dtype='int')  # Bounding boxes in (x1, y1, x2, y2) format
    classes = np.array(result.boxes.cls.cpu(), dtype='int')  # Class labels (integers)

    # Loop through each detected object
    for class_id, bbox in zip(classes, bboxes):
        x, y, x2, y2 = bbox  # Unpack the bounding box coordinates

        # Get the class name and its corresponding colour
        class_name = class_names[class_id]
        colour = colours[class_id]

        # Draw a rectangle around the detected object with the class-specific colour
        cv2.rectangle(frame, (x, y), (x2, y2), colour, 2)

        # Put the class name just above the bounding box
        cv2.putText(frame, class_name, (x, y - 5), cv2.FONT_HERSHEY_PLAIN, 1, colour, 2)

    # Display the frame with bounding boxes and class labels
    cv2.imshow("Detected Objects", frame)

    # Wait for a key press, move to the next frame, or break if 'Esc' is pressed
    key = cv2.waitKey(1)  # Set to 1 ms to move through frames
    if key == 27:  # 'Esc' key to exit
        break

# Release the video capture object and close any OpenCV windows
cap.release()
cv2.destroyAllWindows()

---

# Object Detection using YOLOv8 

This project started off as me trying to see if my Macbook Air M1 could handle object detection but ended up being very educational for me. i followed the video and blogpost by PYSOURCE from this link: https://pysource.com/2023/03/28/object-detection-with-yolo-v8-on-mac-m1/ 
The project demonstrates object detection using the **YOLOv8 (You Only Look Once)** model with OpenCV. The model detects various objects in a video, draws bounding boxes around them, and labels them with their corresponding class names. YOLOv8 is a state-of-the-art real-time object detection model, making it perfect for this task.

## Project Overview

- **Video Source**: A video of traffic ("TrafficPolice.mp4") is used to detect different objects like cars, people, buses, etc.
- **Model**: We are using the **YOLOv8 medium model (`yolov8m.pt`)** for object detection.
- **Tech Stack**: 
  - **Python**: Main programming language.
  - **OpenCV**: For video capture and image processing.
  - **YOLOv8**: For object detection.
  - **Numpy**: For handling arrays (bounding box coordinates and classes).
  
The program processes each frame of the video, detects objects using the YOLOv8 model, and draws bounding boxes around detected objects. Class names are displayed along with different colours for each detected object, making it easy to identify what objects are being detected. This is what it should look like (colours for your bounding boxes might be different but you get the idea)

<img width="965" alt="image" src="https://github.com/user-attachments/assets/4fc070ac-c50a-4dff-9efc-e63984cf13a4">

## Key Features

- **Object Detection**: The model detects objects and draws bounding boxes in real-time.
- **Class Labels**: Each detected object is labeled with its class name (e.g., "car", "person").
- **Coloured Bounding Boxes**: Different classes are displayed with unique colours for easy distinction.
- **Real-time Video Processing**: Processes video frame by frame, updating the output dynamically.

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/abdoolamunir/Object-Detection-using-YOLOv8
   ```
   
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Python script:
   ```bash
   python main.py
   ```

   - Make sure your video file (`TrafficPolice.mp4`) is in the same directory as the script, or adjust the path accordingly.

## Requirements

- Python 3.8+
- OpenCV
- Ultralytics YOLOv8
- Numpy

Install all dependencies using the `requirements.txt` file.

## Future Ideas for Enhancements

In the next iteration of the project, I plan to add the following features to make the project more advanced. These are also open for anyone interested in contributing:

1. **Object Tracking**: Implement object tracking to follow objects across multiple frames, rather than treating each frame independently.
2. **Object Counting**: Count specific objects, like cars or people, and display the count in real-time.
3. **Region-based Detection**: Detect objects only within a specific region of the video (useful for traffic monitoring, etc.).
4. **Real-time Webcam Detection**: Switch to real-time object detection using a webcam feed.
5. **Save Detected Objects**: Save images of detected objects into separate files for further analysis or evidence collection.
6. **Display Confidence Scores**: Overlay confidence scores on the detected objects to show how confident the model is about each detection.
7. **Alert System**: Implement a real-time alert system that triggers when specific objects (like people or cars) are detected.
8. **FPS Monitoring**: Display and optimize frames per second (FPS) for better real-time performance.

Feel free to fork the repository and add these features or any others you'd like to explore!

---

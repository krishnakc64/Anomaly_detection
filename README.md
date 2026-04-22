# Anomaly Detection System using Object Detection (Jetson Orin Nano)

##  Project Overview
This project is an **Anomaly Detection System** built using real-time object detection.  
It detects objects from a live camera feed and identifies **bottle as an anomaly object**.  

When a bottle is detected:
- The system triggers an anomaly alert
- Highlights the object on screen
- Saves a screenshot automatically

---

##  Objective
To build a real-time anomaly detection system using:
- Computer vision (OpenCV)
- Object detection (YOLO / detection model)
- Live camera feed on Jetson Orin Nano

---

##  Technologies Used
- Python 3
- OpenCV
- Ultralytics YOLO (or detection model used)
- Jetson Orin Nano
- USB / CSI Camera

---

##  Anomaly Definition
In this project:
- **Normal state:** No bottle detected
- **Anomaly state:** Bottle detected in frame

---

##  Project Structure
detector.py → Object detection logic
ui.py → Camera UI + anomaly visualization
images/ → Output screenshots


---

##  How to Run

### 1. Install dependencies
pip3 install opencv-python numpy ultralytics

create two file 
detector.py for detecting anomaly objects and ui for window display

2. Run the project
python3 ui.py

---
Output Examples
 Normal Detection
Objects detected with bounding boxes
Status: SYSTEM NORMAL
 Anomaly Detection
Bottle detected
Red warning displayed
Screenshot saved automatically

---
Features
Real-time object detection
Anomaly detection (bottle)
Live camera window
Automatic image capture on anomaly
Bounding box visualization

---
 Results
Normal Case



Anomaly Case



Face-Detector 👤🔍

Real-Time Face Detection and Recognition using Python, OpenCV, and Tkinter

This repository contains a facial recognition system that I developed over approximately 7 months.
It combines image-based learning, OpenCV’s computer vision tools, and a Tkinter-based GUI to create a functional desktop application for face detection and recognition.

The system captures video frames from a webcam, detects faces in real time using a Haar Cascade Classifier, and recognizes them with an LBPH (Local Binary Patterns Histogram) model that has been previously trained.

✨ Main Features

Real-Time Face Detection
Uses OpenCV’s Haar Cascade classifier to detect faces directly from the webcam stream.

Facial Recognition
Trains an LBPH model with images stored in a training dataset folder and performs recognition on detected faces.

Graphical User Interface (Tkinter)

Displays a live video stream with bounding boxes around detected faces.

Shows recognition results in real time.

Provides simple control and interaction for end users.

Access Control Logic
Based on recognition results, the system displays “Access Granted” or “Access Denied” messages dynamically.

🗂️ Project Structure

Training Data: A folder containing face images used to train the model.

Model Output: The trained LBPH model is saved as face_trainer.yml inside the models/ directory.

GUI: Tkinter-based window for live video and results display.

🛠️ Technologies Used

Python 3.x

OpenCV (cv2) – for image processing and Haar Cascade detection.

NumPy – matrix operations for image handling.

Tkinter – graphical user interface.

OS library – file and directory management.

🚀 How It Works

Data Collection:
Store images of faces in a dedicated folder (photos/).

Training:
Train the LBPH recognizer with the collected dataset.

Detection & Recognition:

Start webcam capture.

Detect faces in each frame using Haar cascades.

Recognize faces using the LBPH model.

Display results and access messages in the GUI.

📸 Example Workflow

User stores face images in a dataset folder.

The system trains and saves the model as models/face_trainer.yml.

The application opens a Tkinter window:

Webcam feed with detected faces.

Recognition results displayed on screen.

Access message: “Granted” or “Denied.”

🔮 Future Improvements

Replace Haar Cascades with modern DNN-based face detectors.

Integrate deep learning models (e.g., FaceNet, dlib) for higher accuracy.

Add user management and dynamic dataset updates.

Improve GUI with more interaction options.

📄 License

MIT License © 2025 — Face-Detector Project

Face-Detector — “Smart recognition at the speed of sight.” 👁️✨

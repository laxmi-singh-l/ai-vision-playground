# AI Vision Playground

Welcome to the **AI Vision Playground**! This repository contains a collection of Python-based Computer Vision and Web Application projects. It demonstrates capabilities in file management, facial recognition, and web-based image capture using Flask and OpenCV.

## 📂 Project Structure

The repository is divided into three main independent components:

1.  **File Uploader** (`File_uploader/`)
    *   A Flask web application that organizes uploaded files into specific directories (Images, Audio, Video, PDF, Datasets) based on their file extensions.
2.  **Face Recognition System** (`face-system/`)
    *   A real-time face detection and recognition system. It includes scripts to build a dataset using your webcam and then recognize faces to log their attendance.
3.  **Face Capture Web App** (`face_capture/`)
    *   A web interface to capture images from the client side, save them to the server, and log the metadata into a SQLite database.

---

## 🛠️ Prerequisites

Before running any of the projects, ensure you have Python installed. You will need to install the following dependencies via pip.

It is recommended to create a virtual environment first:
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
```

Install necessary libraries:
```bash
pip install flask opencv-python opencv-contrib-python numpy
```

*(Note: `opencv-contrib-python` is required for the `LBPHFaceRecognizer` used in the face system)*

---

## 🚀 Usage Guide

### 1. File Uploader
This tool helps organize files automatically upon upload.

**Navigate to the directory:**
```bash
cd File_uploader
```

**Run the application:**
```bash
python app.py
```
*   Open your browser and visit `http://127.0.0.1:5000`.
*   Upload any file, and it will be saved in `uploads/<Category>/` based on its type.

### 2. Face Recognition System
This is a two-step process: capturing data and then running recognition.

**Navigate to the directory:**
```bash
cd face-system
```

**Step A: Capture Face Data**
Create a dataset for a new person (Default name: "laamu", editable in code).
```bash
python capture_face.py
```
*   The script will open your webcam.
*   It captures 20 images of your face and saves them in `dataset/`.
*   Press `Esc` to exit early if needed.

**Step B: Recognize and Log**
Train the model on the captured dataset and start recognition.
```bash
python recognize_and_log.py
```
*   The system scans the `dataset/` folder to train the model.
*   It opens the webcam to detect faces.
*   If a face is recognized (Confidence < 60), it logs the name and timestamp to `capture_log.txt`.

### 3. Face Capture Web App
A Flask app that captures images via an API endpoint and stores them.

**Navigate to the directory:**
```bash
cd face_capture
```

**Run the application:**
```bash
python app.py
```
*   This starts a server that accepts image uploads via a POST request to `/upload`.
*   Images are saved in `static/captures`.
*   Metadata (filename, timestamp) is stored in `database.db`.

---

## 📝 Notes
*   **Webcams**: Ensure your webcam is accessible when running the computer vision scripts.
*   **Database**: The `face_capture` app uses a lightweight SQLite database (`database.db`) which is automatically created on the first run.

---
*Created for the AI Vision Playground project.*

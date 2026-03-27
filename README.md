<div align="center">
  <h1>🤖 AI Vision Playground</h1>
  <p><i>A collection of computer vision and web application projects blending Python, Flask, and OpenCV.</i></p>

  <p>
    <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
    <img src="https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white" alt="OpenCV" />
    <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask" />
    <img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite" />
  </p>
</div>

---

## 📖 Table of Contents
- [About The Project](#-about-the-project)
- [Project Structure](#-project-structure)
- [Tech Stack](#-tech-stack)
- [Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#-usage)
  - [1. File Uploader](#1-file-uploader-)
  - [2. Face Recognition System](#2-face-recognition-system-)
  - [3. Face Capture Web App](#3-face-capture-web-app-)
- [Notes](#-notes)
- [License](#-license)

---

## 🌟 About The Project

Welcome to the **AI Vision Playground**! This repository serves as a practical showcase of integrating computer vision models with web applications. It demonstrates core capabilities across three distinct domains:
1. **Automated File Management**
2. **Real-Time Facial Recognition**
3. **Web-Based Image Capture & Database Logging**

---

## 📂 Project Structure

```text
ai-vision-playground/
├── File_uploader/       # Flask app for smart file categorization
├── face-system/         # OpenCV-based facial recognition & attendance
├── face_capture/        # Web app for client-side image capture
└── README.md
```

---

## 💻 Tech Stack

- **Backend:** Python, Flask
- **Computer Vision:** OpenCV (`opencv-python`, `opencv-contrib-python`)
- **Data & Computation:** NumPy
- **Database:** SQLite

---

## 🚀 Getting Started

Follow these instructions to set up the projects locally.

### Prerequisites

Ensure you have **Python 3.8+** installed. It is highly recommended to use a virtual environment.

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/ai-vision-playground.git
   cd ai-vision-playground
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   # Mac/Linux
   source venv/bin/activate
   ```

3. **Install the required dependencies:**
   ```bash
   pip install flask opencv-python opencv-contrib-python numpy
   ```
   *Note: `opencv-contrib-python` is explicitly required for the `LBPHFaceRecognizer` module.*

---

## 💡 Usage

### 1. File Uploader 📁
A smart web app that categorizes uploaded files (Images, Audio, Video, PDF, Datasets) into designated directories based on their extensions.

<details>
<summary><b>Show Instructions</b></summary>

1. Navigate to the directory:
   ```bash
   cd File_uploader
   ```
2. Run the Flask application:
   ```bash
   python app.py
   ```
3. Open your browser and go to `http://127.0.0.1:5000`. You can now upload files and have them automatically sorted into `uploads/<Category>/`.
</details>

### 2. Face Recognition System 👤
A real-time face detection system capable of capturing datasets and recognizing faces to log attendances.

<details>
<summary><b>Show Instructions</b></summary>

1. Navigate to the directory:
   ```bash
   cd face-system
   ```

**Step A: Capture Training Data**
Generate a dataset for a new person (Default: "laamu", can be changed in the script).
```bash
python capture_face.py
```
*This will open your webcam, capture 20 frames, and save them in the `dataset/` directory. Press `Esc` to cancel.*

**Step B: Train and Recognize**
Train the recognizer on the generated dataset and identify faces in real-time.
```bash
python recognize_and_log.py
```
*The system will train itself, activate the webcam, and if a face is confidently recognized, it will log the event in `capture_log.txt`.*
</details>

### 3. Face Capture Web App 📸
A Flask-powered interface for capturing images directly from the browser, saving them on the server, and logging metadata into a SQLite database.

<details>
<summary><b>Show Instructions</b></summary>

1. Navigate to the directory:
   ```bash
   cd face_capture
   ```
2. Run the application:
   ```bash
   python app.py
   ```
3. The server will start and provide a web interface where you can capture images. Images are stored in `static/captures` and metadata is logged to `database.db` (auto-generated on the first run).
</details>

---

## 📝 Notes

- **Camera Permissions:** Ensure your terminal or IDE has permission to access the webcam when running the OpenCV scripts.
- **Port Conflicts:** The Flask applications default to port `5000`. Ensure this port is free or modify the port in `app.py`.

---

## 📜 License

Distributed under the MIT License. See `LICENSE` for more information.

----

<div align="center">
  <i>Built with ❤️ for the AI Vision Playground</i>
</div>

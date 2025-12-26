# -----------------------------
# Import required libraries
# -----------------------------
from flask import Flask, render_template, request, jsonify
import cv2
import base64
import numpy as np
import sqlite3
import os
from datetime import datetime

# -----------------------------
# Flask app init
# -----------------------------
app = Flask(__name__)

# Folder jahan images save hongi
CAPTURE_FOLDER = "static/captures"
os.makedirs(CAPTURE_FOLDER, exist_ok=True)

# -----------------------------
# Database setup (SQLite)
# -----------------------------
def init_db():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    # Table create (agar pehle se nahi hai)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS photos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT,
            timestamp TEXT
        )
    """)

    conn.commit()
    conn.close()

init_db()

# -----------------------------
# Home page route
# -----------------------------
@app.route("/")
def index():
    return render_template("index.html")

# -----------------------------
# Image receive + save route
# -----------------------------
@app.route("/upload", methods=["POST"])
def upload_image():
    data = request.json["image"]

    # Base64 header remove
    encoded_data = data.split(',')[1]

    # Base64 decode → numpy array
    img_bytes = base64.b64decode(encoded_data)
    img_array = np.frombuffer(img_bytes, np.uint8)

    # OpenCV image
    frame = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

    # Filename with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{timestamp}.jpg"
    filepath = os.path.join(CAPTURE_FOLDER, filename)

    # Image save using OpenCV
    cv2.imwrite(filepath, frame)

    # Database entry
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO photos (filename, timestamp) VALUES (?, ?)",
        (filename, timestamp)
    )
    conn.commit()
    conn.close()

    return jsonify({"status": "saved", "file": filename})

# -----------------------------
# App start
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)

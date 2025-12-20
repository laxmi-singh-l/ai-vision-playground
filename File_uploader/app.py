from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")

FILE_TYPES = {
    "images": ["jpg", "jpeg", "png", "gif"],
    "audio": ["mp3", "wav", "ogg"],
    "video": ["mp4", "mkv", "avi"],
    "pdf": ["pdf"],
    "datasets": ["csv", "xlsx", "json"]
}

def get_upload_folder(extension):
    for folder, extensions in FILE_TYPES.items():
        if extension in extensions:
            return folder
    return None

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    if "file" not in request.files:
        return "No file part"

    file = request.files["file"]

    if file.filename == "":
        return "No selected file"

    if "." not in file.filename:
        return "Invalid file"

    filename = secure_filename(file.filename)
    extension = filename.rsplit(".", 1)[1].lower()
    folder = get_upload_folder(extension)

    if folder is None:
        return "Unsupported file type"

    target_dir = os.path.join(UPLOAD_FOLDER, folder)
    os.makedirs(target_dir, exist_ok=True)

    save_path = os.path.join(target_dir, filename)
    file.save(save_path)

    return f"File uploaded successfully to {folder} folder"

if __name__ == "__main__":
    app.run(debug=True)

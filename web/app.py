import base64

import cv2
import numpy as np
from flask import Flask, Response, jsonify, render_template, request

from ultralytics import YOLO

app = Flask(__name__)
MODEL_PATH = r"C:\Users\Lenovo\Desktop\boat_YOLO\web\best.pt"
CAMERA_INDEX = 0
CONFIDENCE_THRESHOLD = 0.5
print("正在加载 YOLO 模型...")
model = YOLO(MODEL_PATH)
print("模型加载成功！")


def generate_frames():
    cap = cv2.VideoCapture(CAMERA_INDEX)
    if not cap.isOpened():
        print("无法打开摄像头")
        return

    try:
        while True:
            success, frame = cap.read()
            if not success:
                break
            results = model.predict(source=frame, conf=CONFIDENCE_THRESHOLD, show=False, verbose=False)
            annotated_frame = results[0].plot()

            _ret, buffer = cv2.imencode(".jpg", annotated_frame)
            frame_bytes = buffer.tobytes()

            yield (b"--frame\r\nContent-Type: image/jpeg\r\n\r\n" + frame_bytes + b"\r\n")
    finally:
        cap.release()
        print("摄像头已释放")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/video_feed")
def video_feed():
    return Response(generate_frames(), mimetype="multipart/x-mixed-replace; boundary=frame")


@app.route("/upload_image", methods=["POST"])
def upload_image():
    if "file" not in request.files:
        return jsonify({"error": "没有收到文件"})

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "文件为空"})

    try:
        file_bytes = np.frombuffer(file.read(), np.uint8)
        img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
        results = model.predict(source=img, conf=CONFIDENCE_THRESHOLD, show=False, verbose=False)
        annotated_frame = results[0].plot()
        _ret, buffer = cv2.imencode(".jpg", annotated_frame)
        img_base64 = base64.b64encode(buffer).decode("utf-8")

        return jsonify({"success": True, "image_data": img_base64, "message": "检测成功"})
    except Exception as e:
        return jsonify({"error": str(e)})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)

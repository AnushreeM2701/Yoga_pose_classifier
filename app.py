from flask import Flask, render_template, request, redirect, url_for
import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
import cv2
import os

app = Flask(__name__)
model = tf.keras.models.load_model("models/yoga_pose_model.keras")
class_names = ['down_dog', 'goddess', 'plank', 'tree', 'warrior']

# Route: Home - Upload & Predict
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            img_path = os.path.join("static", "upload.jpg")
            file.save(img_path)

            img = image.load_img(img_path, target_size=(224, 224))
            img_array = image.img_to_array(img) / 255.0
            img_array = np.expand_dims(img_array, axis=0)

            prediction = model.predict(img_array)
            predicted_class = class_names[np.argmax(prediction)]
            confidence = np.max(prediction)

            return render_template('index.html',
                                   prediction=predicted_class,
                                   confidence=round(confidence * 100, 2),
                                   image_path=img_path)
    return render_template('index.html', prediction=None)

# Route: Webcam page
@app.route('/webcam')
def webcam_page():
    return render_template('webcam.html')

# Route: Webcam video stream
@app.route('/video')
def video():
    def gen():
        cap = cv2.VideoCapture(0)
        while True:
            success, frame = cap.read()
            if not success:
                break

            # Preprocess frame
            img = cv2.resize(frame, (224, 224))
            img_array = img.astype(np.float32) / 255.0
            img_array = np.expand_dims(img_array, axis=0)

            prediction = model.predict(img_array)
            predicted_class = class_names[np.argmax(prediction)]
            confidence = np.max(prediction)

            label = f"{predicted_class} ({confidence * 100:.1f}%)"
            cv2.putText(frame, label, (20, 40),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            _, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()

            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
        cap.release()

    return app.response_class(gen(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(debug=True)

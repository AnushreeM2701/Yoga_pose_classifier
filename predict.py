# scripts/predict.py

import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
import os

# Load model
model = tf.keras.models.load_model("models/yoga_pose_model.keras")

# Class labels (must match train_generator.class_indices order)
class_names = ['down_dog', 'goddess', 'plank', 'tree', 'warrior']

# Load and preprocess image
def predict_pose(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    # Predict
    prediction = model.predict(img_array)
    predicted_class = class_names[np.argmax(prediction)]
    confidence = np.max(prediction)
    print(f"🧘 Predicted Pose: {predicted_class} (Confidence: {confidence:.2f})")

# Example usage
if __name__ == "__main__":
    test_image_path = "/Users/anushreem/Desktop/yoga_pose_classifier/DATASET/TEST/downdog/00000000.jpg"  # change this path
    predict_pose(test_image_path)

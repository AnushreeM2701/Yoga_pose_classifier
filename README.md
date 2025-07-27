
# 🧘‍♀️ Yoga Pose Classifier

A deep learning project to classify five yoga poses using TensorFlow and MobileNetV2, with real-time webcam prediction and a clean Flask-based frontend.

---

## 📁 Project Structure

```
yoga_pose_classifier/
│
├── app.py                   # Flask backend
├── scripts/
│   ├── train_model.py       # Train the MobileNetV2 model
│   └── predict.py           # Predict from image
│
├── models/
│   └── yoga_pose_model.keras   # Trained model
│
├── templates/
│   ├── index.html           # Upload and predict page
│   └── webcam.html          # Real-time webcam prediction
│
├── static/
│   └── style.css            # Optional CSS
│
├── notebooks/
│   └── Yoga.ipynb           # Jupyter Notebook
│
├── dataset/
│   ├── TRAIN/               # Training images (5 classes)
│   └── TEST/                # Testing images (5 classes)
│
├── .gitignore
├── requirements.txt         # Python dependencies
└── README.md
```

---

## ✅ Features

- 🔍 Classifies 5 yoga poses:
  - `downdog`, `goddess`, `plank`, `tree`, `warrior2`
- 🧠 Uses transfer learning with MobileNetV2
- 🎯 95%+ accuracy on validation set
- 🖼 Upload image to predict pose
- 🎥 Real-time webcam capture and prediction (with 5 sec delay)

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/yoga-pose-classifier.git
cd yoga-pose-classifier
```

### 2. Create a virtual environment

```bash
python3.10 -m venv venv
source venv/bin/activate  # Mac/Linux
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Train the model (optional)

```bash
python scripts/train_model.py
```

### 5. Run the app

```bash
python app.py
```

Then visit:  
🌐 `http://localhost:5000` – Home Page  
🌐 `http://localhost:5000/webcam` – Webcam Prediction

---

## 💻 Frontend

- `index.html` – Upload image & see predicted pose
- `webcam.html` – Real-time webcam capture (auto capture after 5 sec)

---

## 📦 Requirements

- Python 3.10
- TensorFlow 2.19.0
- Flask
- Pillow
- OpenCV (cv2)

Install via:

```bash
pip install tensorflow flask pillow opencv-python
```

---

## 🙋‍♀️ Created By

**Anushree M**  
Aspiring Software Developer | Data Science Enthusiast

---

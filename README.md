
# Yoga Pose Classification using MobileNetV2

This project classifies 5 different yoga poses using a deep learning model based on the MobileNetV2 architecture.

## 🧘‍♀️ Yoga Pose Classes
1. Down Dog
2. Goddess
3. Plank
4. Tree
5. Warrior

## 📁 Dataset Structure

```
DATASET/
├── TRAIN/
│   ├── down_dog/
│   ├── goddess/
│   ├── plank/
│   ├── tree/
│   └── warrior/
├── TEST/
    ├── down_dog/
    ├── goddess/
    ├── plank/
    ├── tree/
    └── warrior/
```

## 🧠 Model

- Architecture: MobileNetV2 (Transfer Learning)
- Format: `.keras`
- Loss: Categorical Crossentropy
- Optimizer: Adam
- Metrics: Accuracy

## 🧪 Evaluation

The model was evaluated using a confusion matrix and test accuracy.

## 🔧 Requirements

Install dependencies:

```bash
pip install -r requirements.txt
```

## 🚀 How to Use

1. Clone the repository:

```bash
git clone https://github.com/your-username/yoga-pose-classification.git
cd yoga-pose-classification
```

2. Run the training/testing scripts in a Jupyter notebook or Python script.

3. Load the model:
```python
from keras.models import load_model
model = load_model("yoga_model.keras")
```

## 📊 Visualizations

Confusion matrix and class-wise accuracy are available in the notebook.

## 📦 Model Checkpoint

- `yoga_model.keras` — Final saved model.

## 🛠️ Tools Used

- TensorFlow / Keras
- Scikit-learn
- Matplotlib
- Jupyter

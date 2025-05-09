# 🧠 Fake AI Image Detector (CNN with TensorFlow)

This project is a deep learning application designed to detect **deepfake images** using a custom **Convolutional Neural Network (CNN)** built with **TensorFlow**.

---

## 📂 Dataset Structure & Source

We used the [Deepfake Image Dataset](https://www.kaggle.com/datasets/saurabhbagchi/deepfake-image-detection) from Kaggle.

### 📌 Important Note:
The original dataset was split into `train/` and `test/` folders. In this project, the dataset was **reorganized into a simplified structure**:

```
deepfake_dataset/
├── real/
└── fake/
```

- All real and fake images were merged into two folders.
- The model code automatically splits this into training and testing sets (e.g., using an 80/20 split with `image_dataset_from_directory`).

### 🔽 Download Dataset (Options)

1. **Manual**: Download the dataset manually from [Kaggle](https://www.kaggle.com/datasets/saurabhbagchi/deepfake-image-detection), extract and restructure as above.

2. **Auto Download (Optional)**: Enable and use the following in the notebook:
```python
import kagglehub
path = kagglehub.dataset_download("saurabhbagchi/deepfake-image-detection")
```

---

## 🛠️ How to Run

```bash
# Install dependencies
pip install tensorflow matplotlib kagglehub
```

Then open and run `fake_ai_image_detector.ipynb`.

---

## 🔍 Model Architecture

- Input: RGB images resized to 128x128
- 3 Convolutional blocks + MaxPooling
- Dense + Dropout layers
- Sigmoid output for binary classification

---

## 📈 Performance

Example training results:
- Training Accuracy: ~79%
- Validation Accuracy: ~77%

(Metrics depend on training duration and hardware)

---

## 🚀 Future Improvements

- Transfer learning with Xception or EfficientNet
- Augmentation & regularization tuning
- Confusion matrix + precision/recall reporting
- Export to web or mobile

---

## 📜 License

This project is open-source under the MIT License.

---

## 🙌 Acknowledgments

- Dataset: [Kaggle - Deepfake Image Detection](https://www.kaggle.com/datasets/saurabhbagchi/deepfake-image-detection)
- Libraries: TensorFlow, Matplotlib

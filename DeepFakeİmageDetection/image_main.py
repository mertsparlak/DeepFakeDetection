"""
import kagglehub

# Download latest version
path = kagglehub.dataset_download("saurabhbagchi/deepfake-image-detection")

print("Path to dataset files:", path)
"""

import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt


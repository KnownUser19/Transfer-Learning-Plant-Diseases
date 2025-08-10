# Transfer-Learning-Plant-Diseases

A deep learning project that employs **Transfer Learning** to detect plant diseases from leaf images using popular deep neural network architectures. This approach enables efficient and highly accurate classification to support plant health monitoring and management.

---

## 🌱 Plant Disease Classification using Transfer Learning

This project applies transfer learning techniques with Keras on the publicly available **PlantVillage** dataset, consisting of labeled plant leaf images. The goal is to classify images into distinct disease categories accurately.

---

## 📌 Features

- **Dataset:** PlantVillage dataset with plant leaf images labeled by disease type.
- **Models Used:** Various pretrained architectures including:
  - EfficientNetB0
  - MobileNetV2
  - VGG16
  - InceptionV3
  - ResNet50
- **Input Image Size:** 128 x 128 pixels.
- **Data Split:** 
  - 70% training
  - 20% validation
  - 10% testing
- **Performance:** High accuracy achieved on test datasets varies by model.
- **Visualization:** 
  - Training/validation accuracy and loss curves
  - Confusion matrices
  - Classification reports with precision, recall, F1-score

---

## 🚀 How to Run

1. **Prepare Dataset:**
   - Organize images into folders for training, validation, and testing (Keras `ImageDataGenerator` format).

2. **Initialize Image Data Generators:**
   - Normalize pixel values.
   - Set batch size and target size (128x128).

3. **Setup Transfer Learning Model:**
   - Load a pretrained model (e.g., VGG16, InceptionV3, ResNet50) without the top classification layer.
   - Freeze base layers for initial training.
   - Add custom dense layers for classification.

4. **Compile Model:**
   - Optimizer: Adam
   - Loss: Categorical Cross-Entropy

5. **Train Model:**
   - Use GPU acceleration (Colab recommended).
   - Monitor accuracy and loss.

6. **Evaluate Performance:**
   - Use test dataset for final accuracy.
   - Generate confusion matrix & classification reports.

7. **Save and Load Models:**
   - Save as `.h5` files for reuse.
   - Reload for inference or fine-tuning.

8. **Visualize Results:**
   - Plot accuracy/loss curves.
   - Show confusion matrices and performance reports.

---

## Additional Insights

- **ImageNet Pretraining:** Speeds up convergence and improves feature extraction.
- **Architecture Trade-offs:**
  - MobileNetV2 — lightweight, faster inference
  - ResNet50 — higher accuracy, more compute
- **Training Curves:** Useful for detecting overfitting/underfitting.
- **Class-wise Metrics:** Identify strengths/weaknesses for each disease category.

---

## 📜 License

This project is licensed under the MIT License.

---

⭐ **If you like this project, give it a star on GitHub!**

---

✦ This pipeline supports practical AI-powered plant disease diagnosis which is used for boosting agricultural productivity and smart farming.

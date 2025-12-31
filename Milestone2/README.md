# 📘 Milestone 2: Model Training & Evaluation

**Phase:** Milestone 2  
**Focus:** Deep Learning & Classification  
**🎯 Target Accuracy:** >95%  
**🏆 Achieved Accuracy:** **96–97%**

---

## 📖 Milestone Overview

This milestone covers **Modules 3 and 4** of the AI-Based PCB Defect Detection & Classification project.
Using the labeled dataset prepared in Milestone 1, a **Convolutional Neural Network (CNN)** was trained to classify PCB defects into **six categories**:

- Missing Hole  
- Mouse Bite  
- Open Circuit  
- Short  
- Spur  
- Spurious Copper  

The trained model achieved **~97% validation accuracy**, successfully meeting and exceeding the target performance.

---

## 📂 Folder Structure

```
Milestone2/
│
├── src/ # Source Code
│ ├── train_model.py # Module 3: Training Logic
│ ├── evaluate_model.py # Module 4: Evaluation Logic
│ ├── inference.py # Module 4: Inference & Visualization
│ └── init.py
│
├── output/ # Milestone 2 Results
│ ├── pcb_defect_model.keras
│ ├── confusion_matrix.png
│ ├── train_val_acc_n_train_val_loss.png
│ ├── Inference_Grid.png
│ └── Annotated_Test_Images/
│
├── requirements.txt # Project Dependencies
└── README.md # Documentation
```

---

## 🧠 Module 3: Model Training

A deep learning–based image classification model was trained using **TensorFlow/Keras**.
Data augmentation and regularization were applied to improve generalization and reduce overfitting.

### ✔️ Model Configuration

| Parameter              | Value                          |
|------------------------|--------------------------------|
| Input Size             | 128 × 128                      |
| Architecture           | CNN / Transfer Learning Model  |
| Optimizer              | Adam                           |
| Loss Function          | Categorical Crossentropy       |
| Data Augmentation      | Rotation, Flip, Zoom           |
| Train/Validation Split | 80% / 20%                      |
| Batch Size             | 32                             |

---

## 🧩 Model Architecture

The classification system consists of:
- Feature extraction layers for PCB texture and edge detection
- Fully connected layers for defect classification
- Dropout layers to reduce overfitting

Input → Feature Extractor → Dense Layers → Output (6 Classes)


This architecture enables accurate differentiation between visually similar PCB defects such as *Spur* and *Spurious Copper*.

---

## 📊 Module 4: Evaluation Results

The trained model was evaluated on the validation dataset.

### ✔️ Final Metrics

| Metric       | Result     |
|--------------|------------|
| **Accuracy** | **~97%**   |
| Precision    | ~0.97      |
| Recall       | ~0.97      |
| F1-Score     | ~0.97      |

---

## 🖼️ Visual Results

### 📈 Training & Validation Curves

![](output/train_val_acc_n_train_val_loss.png)

### 🔢 Confusion Matrix

![](output/confusion_matrix.png)

### 🖼️ Inference Grid (Model Predictions)

![](output/Inference_Grid.png)

Annotated test images with true and predicted labels are available in:

output/Annotated_Test_Images/


---

## 🧪 How to Run the Code

### 1️⃣ Install Dependencies

bash
pip install -r requirements.txt

2️⃣ Train the Model
python src/train_model.py

3️⃣ Evaluate the Model
python src/evaluate_model.py

4️⃣ Run Inference
python src/inference.py

📂 Dataset Summary

Dataset path used during training:

/content/drive/MyDrive/Milestone2_Training_Data


Detected Class Labels:

['missing_hole', 'mouse_bite', 'open_circuit',
 'short', 'spur', 'spurious_copper']

✅ Milestone 2 Completed Successfully!

Achieved >95% accuracy, meeting the milestone target.

Implemented a robust CNN-based classification pipeline.

Generated evaluation metrics and visual proof of model performance.

Saved a trained model ready for further optimization or deployment.






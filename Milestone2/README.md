# 📘 Milestone 2: Model Training & Evaluation

**Phase:** Milestone 2  
**Focus:** Deep Learning–Based PCB Defect Classification  
**Author:** Gunal  
**Final Validation Accuracy:** **96.78%**

---

## 📖 Milestone Overview

In Milestone 2, I focused on building a **robust deep learning classifier** for PCB defect detection using the labeled dataset prepared in **Milestone 1**.

The objective was not only to achieve high accuracy, but also to **reduce confusion between visually similar defect classes** by carefully choosing the model architecture, training strategy, and regularization techniques.

This milestone corresponds to **Modules 3 and 4** of the project:
- **Module 3:** Model Training  
- **Module 4:** Model Evaluation & Inference  

---

## 🧠 Defect Classes

The trained model classifies PCB images into the following **6 defect categories**:

- Missing Hole  
- Mouse Bite  
- Open Circuit  
- Short  
- Spur  
- Spurious Copper  

---
```
## 📂 Folder Structure

Milestone2/
│
├── src/
│ ├── train_model.py # Model training logic
│ ├── evaluate_model.py # Evaluation & metrics generation
│ └── inference.py # Visual inference on test images
│
├── output/
│ ├── pcb_defect_model.keras
│ ├── confusion_matrix.png
│ ├── train_val_acc_n_train_val_loss.png
│ └── Annotated_Test_Images/
│ └── Inference_Grid.png
│
├── requirements.txt
└── README.md

```
---

## 🧩 Model Architecture & Design Choice

### 🔹 Base Model: EfficientNetB0
- Pretrained on ImageNet
- Used as a **frozen feature extractor**
- Captures low-level PCB patterns such as edges, holes, and copper traces

### 🔹 Custom Classification Head
To improve class separation, especially between **Short** and **Open Circuit**, a custom dense head was added:

Input Image (128×128)
→ EfficientNetB0 (Frozen)
→ Global Average Pooling
→ Dense (256, ReLU)
→ Dropout (0.3)
→ Dense (6, Softmax)


---

## 🧠 Why This Architecture Works Well

- **Transfer Learning Stability:**  
  Freezing the backbone prevents overfitting on a relatively small PCB dataset.

- **Higher Discriminative Power:**  
  The 256-unit dense layer allows the model to learn non-linear differences between visually similar defects.

- **Regularization:**  
  Dropout layers reduce memorization and improve generalization.

- **Adaptive Learning:**  
  `ReduceLROnPlateau` dynamically lowers the learning rate when validation loss stops improving.

---

## 🏋️ Model Training Details

- **Input Size:** 128 × 128  
- **Loss Function:** Sparse Categorical Cross-Entropy  
- **Optimizer:** Adam  
- **Train / Validation Split:** 80% / 20%  
- **Callbacks Used:**
  - EarlyStopping
  - ReduceLROnPlateau

Training was performed on **Google Colab** with GPU acceleration.

The final trained model was saved as:

output/pcb_defect_model.keras


---

## 📊 Evaluation Results

### 📈 Training & Validation Curves

The following plot shows smooth convergence without severe overfitting:

![Training Curves](output/train_val_acc_n_train_val_loss.png)

---

### 🔢 Confusion Matrix

The confusion matrix demonstrates strong classification performance across all defect classes:

![Confusion Matrix](output/confusion_matrix.png)

---

## 🧪 Classification Report (Validation Set)

             precision    recall  f1-score   support
missing_hole       0.98   0.99     0.99
mouse_bite          0.97  0.98     0.98
open_circuit        1.00  1.00     1.00
short               0.98  1.00     0.99
spur                0.95  0.94     0.95
spurious_copper     0.97  0.95     0.96


   accuracy                           0.9678
  macro avg       0.98      0.98      0.98
 weighted avg     0.97      0.97      0.97


**Key Observation:**  
Critical defects such as **Open Circuit** and **Short** achieved **near-perfect recall**, indicating high reliability for safety-critical PCB inspection.

---

## 🖼️ Inference Results

Predictions on unseen PCB images were visualized to validate real-world performance:

![Inference Grid](output/Annotated_Test_Images/Inference_Grid.png)

---

## 🚀 How to Run the Code

```bash
pip install -r requirements.txt
python src/train_model.py
python src/evaluate_model.py
python src/inference.py
```
✅ Milestone 2 Status
✔ Model trained and evaluated successfully
✔ Real outputs generated and committed
✔ Overfitting controlled using regularization
✔ Model ready for deployment in Milestone 3

Milestone 2 completed successfully.

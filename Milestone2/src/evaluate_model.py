import os
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.metrics import classification_report, confusion_matrix

# =========================
# CONFIG
# =========================
DATASET_PATH = "/content/drive/MyDrive/Milestone2_Training_Data"
MODEL_PATH = "/content/drive/MyDrive/PCB_Project/Milestone2/output/pcb_defect_model.keras"
OUTPUT_DIR = "/content/drive/MyDrive/PCB_Project/Milestone2/output"

IMG_SIZE = (128, 128)
BATCH_SIZE = 32
SEED = 42

os.makedirs(OUTPUT_DIR, exist_ok=True)

# =========================
# LOAD VALIDATION DATA
# =========================
val_ds = tf.keras.utils.image_dataset_from_directory(
    DATASET_PATH,
    validation_split=0.2,
    subset="validation",
    seed=SEED,
    image_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    shuffle=False
)

class_names = val_ds.class_names
num_classes = len(class_names)
label_ids = list(range(num_classes))

print("Classes:", class_names)
print(f"Found {num_classes} classes.")

val_ds = val_ds.map(lambda x, y: (x / 255.0, y))

# =========================
# LOAD MODEL
# =========================
print("Loading trained model...")
model = tf.keras.models.load_model(MODEL_PATH)
print("Model loaded successfully.")

# =========================
# PREDICTIONS
# =========================
y_true = []
y_pred = []

for images, labels in val_ds:
    preds = model.predict(images, verbose=0)
    y_pred.extend(np.argmax(preds, axis=1))
    y_true.extend(labels.numpy())

y_true = np.array(y_true)
y_pred = np.array(y_pred)

# =========================
# CLASSIFICATION REPORT
# =========================
print("\n📊 CLASSIFICATION REPORT:\n")

report = classification_report(
    y_true,
    y_pred,
    labels=label_ids,          # 🔑 FIX
    target_names=class_names,
    zero_division=0
)

print(report)

# =========================
# CONFUSION MATRIX
# =========================
cm = confusion_matrix(y_true, y_pred, labels=label_ids)

plt.figure(figsize=(8, 6))
sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    cmap="Blues",
    xticklabels=class_names,
    yticklabels=class_names
)
plt.xlabel("Predicted")
plt.ylabel("True")
plt.title("Confusion Matrix")
plt.tight_layout()

cm_path = os.path.join(OUTPUT_DIR, "confusion_matrix.png")
plt.savefig(cm_path)
plt.close()

print(f"✅ Confusion matrix saved at: {cm_path}")
print("🎯 EVALUATION COMPLETED SUCCESSFULLY")

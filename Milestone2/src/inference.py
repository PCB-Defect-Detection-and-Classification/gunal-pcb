# ============================================================
# Milestone 2 – Module 4: Inference & Visual Proof
# ============================================================

import os
import random
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# CONFIG
# -----------------------------
DATASET_PATH = "/content/drive/MyDrive/Milestone2_Training_Data"
MODEL_PATH = "/content/drive/MyDrive/PCB_Project/Milestone2/output/pcb_defect_model.keras"
OUTPUT_DIR = "/content/drive/MyDrive/PCB_Project/Milestone2/output/Annotated_Test_Images"

IMG_SIZE = (128, 128)
NUM_IMAGES = 12
SEED = 42

os.makedirs(OUTPUT_DIR, exist_ok=True)
random.seed(SEED)

# -----------------------------
# LOAD MODEL
# -----------------------------
print("🔄 Loading model...")
model = tf.keras.models.load_model(MODEL_PATH)
print("✅ Model loaded")

# -----------------------------
# LOAD CLASS NAMES
# -----------------------------
class_names = sorted(os.listdir(DATASET_PATH))
print("📂 Classes:", class_names)

# -----------------------------
# COLLECT RANDOM IMAGES
# -----------------------------
samples = []

for cls in class_names:
    cls_path = os.path.join(DATASET_PATH, cls)
    images = os.listdir(cls_path)
    for img in images:
        samples.append((cls, os.path.join(cls_path, img)))

random.shuffle(samples)
samples = samples[:NUM_IMAGES]

# -----------------------------
# INFERENCE + SAVE IMAGES
# -----------------------------
plt.figure(figsize=(12, 8))

for i, (true_label, img_path) in enumerate(samples):
    img = tf.keras.utils.load_img(img_path, target_size=IMG_SIZE)
    img_array = tf.keras.utils.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    preds = model.predict(img_array, verbose=0)
    pred_label = class_names[np.argmax(preds)]

    plt.subplot(3, 4, i + 1)
    plt.imshow(img)
    plt.axis("off")
    plt.title(f"True: {true_label}\nPred: {pred_label}")

    save_name = f"Test_{i}_True_{true_label}_Pred_{pred_label}.jpg"
    plt.imsave(os.path.join(OUTPUT_DIR, save_name), img)

plt.tight_layout()
grid_path = os.path.join(OUTPUT_DIR, "Inference_Grid.png")
plt.savefig(grid_path)
plt.close()

print(f"\n🖼️ Inference images saved in: {OUTPUT_DIR}")
print(f"🧾 Grid image saved at: {grid_path}")
print("\n🎉 INFERENCE COMPLETED SUCCESSFULLY")

# ============================================================
# Milestone 2 – Module 3: Model Training
# PCB Defect Detection & Classification
# ============================================================

import os
import tensorflow as tf
import matplotlib.pyplot as plt

# -----------------------------
# CONFIG
# -----------------------------
DATASET_PATH = "/content/drive/MyDrive/Milestone2_Training_Data"
OUTPUT_DIR = "/content/drive/MyDrive/PCB_Project/Milestone2/output"

MODEL_PATH = os.path.join(OUTPUT_DIR, "pcb_defect_model.keras")
PLOT_PATH = os.path.join(OUTPUT_DIR, "train_val_acc_n_train_val_loss.png")

IMG_SIZE = (128, 128)
BATCH_SIZE = 32
EPOCHS = 30
SEED = 42

os.makedirs(OUTPUT_DIR, exist_ok=True)

# -----------------------------
# LOAD DATASET
# -----------------------------
train_ds = tf.keras.utils.image_dataset_from_directory(
    DATASET_PATH,
    validation_split=0.2,
    subset="training",
    seed=SEED,
    image_size=IMG_SIZE,
    batch_size=BATCH_SIZE
)

val_ds = tf.keras.utils.image_dataset_from_directory(
    DATASET_PATH,
    validation_split=0.2,
    subset="validation",
    seed=SEED,
    image_size=IMG_SIZE,
    batch_size=BATCH_SIZE
)

class_names = train_ds.class_names
NUM_CLASSES = len(class_names)

print("📂 Classes detected:", class_names)

AUTOTUNE = tf.data.AUTOTUNE
train_ds = train_ds.prefetch(AUTOTUNE)
val_ds = val_ds.prefetch(AUTOTUNE)

# -----------------------------
# DATA AUGMENTATION
# -----------------------------
data_augmentation = tf.keras.Sequential([
    tf.keras.layers.RandomFlip("horizontal"),
    tf.keras.layers.RandomRotation(0.15),
])

# -----------------------------
# MODEL ARCHITECTURE
# -----------------------------
base_model = tf.keras.applications.EfficientNetB0(
    include_top=False,
    input_shape=(128, 128, 3),
    weights="imagenet"
)

base_model.trainable = False  # Frozen backbone

inputs = tf.keras.Input(shape=(128, 128, 3))
x = data_augmentation(inputs)
x = tf.keras.applications.efficientnet.preprocess_input(x)
x = base_model(x, training=False)
x = tf.keras.layers.GlobalAveragePooling2D()(x)
x = tf.keras.layers.Dropout(0.3)(x)
x = tf.keras.layers.Dense(256, activation="relu")(x)
x = tf.keras.layers.Dropout(0.2)(x)
outputs = tf.keras.layers.Dense(NUM_CLASSES, activation="softmax")(x)

model = tf.keras.Model(inputs, outputs)

# -----------------------------
# COMPILE MODEL
# -----------------------------
model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=1e-3),
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)

model.summary()

# -----------------------------
# CALLBACKS
# -----------------------------
callbacks = [
    tf.keras.callbacks.ModelCheckpoint(
        MODEL_PATH,
        monitor="val_accuracy",
        save_best_only=True,
        verbose=1
    ),
    tf.keras.callbacks.ReduceLROnPlateau(
        monitor="val_loss",
        factor=0.3,
        patience=3,
        min_lr=1e-6,
        verbose=1
    ),
    tf.keras.callbacks.EarlyStopping(
        monitor="val_loss",
        patience=6,
        restore_best_weights=True,
        verbose=1
    )
]

# -----------------------------
# TRAIN MODEL (ALWAYS RUNS)
# -----------------------------
print("\n🚀 Starting model training...\n")

history = model.fit(
    train_ds,
    validation_data=val_ds,
    epochs=EPOCHS,
    callbacks=callbacks,
    verbose=1
)

# -----------------------------
# SAVE FINAL MODEL
# -----------------------------
model.save(MODEL_PATH)
print(f"\n✅ Model saved at: {MODEL_PATH}")

# -----------------------------
# PLOT TRAINING CURVES
# -----------------------------
acc = history.history["accuracy"]
val_acc = history.history["val_accuracy"]
loss = history.history["loss"]
val_loss = history.history["val_loss"]

plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.plot(acc, label="Train Accuracy")
plt.plot(val_acc, label="Val Accuracy")
plt.legend()
plt.title("Accuracy")

plt.subplot(1, 2, 2)
plt.plot(loss, label="Train Loss")
plt.plot(val_loss, label="Val Loss")
plt.legend()
plt.title("Loss")

plt.tight_layout()
plt.savefig(PLOT_PATH)
plt.close()

print(f"📊 Training curves saved at: {PLOT_PATH}")
print("\n🎉 TRAINING COMPLETED SUCCESSFULLY")


import cv2
import os

def extract_and_save_rois(image, boxes, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    roi_paths = []

    for i, (x, y, w, h) in enumerate(boxes, start=1):
        roi = image[y:y+h, x:x+w]
        path = os.path.join(output_dir, f"roi_{i}.png")
        cv2.imwrite(path, roi)
        roi_paths.append(path)

    return roi_paths


import cv2
import numpy as np
import pandas as pd
from datetime import datetime

from Milestone3.backend.image_processing import process_pcb_images
from Milestone3.backend.defect_localization import find_defect_bounding_boxes


def run_inspection(golden_path, test_path):
    _, test_img, binary_mask = process_pcb_images(
        golden_path,
        test_path
    )

    boxes = find_defect_bounding_boxes(binary_mask, min_area=100)

    annotated = test_img.copy()
    defect_data = []

    for i, (x, y, w, h) in enumerate(boxes, start=1):
        cv2.rectangle(
            annotated,
            (x, y),
            (x + w, y + h),
            (0, 0, 255),
            2
        )

        defect_data.append({
            "Defect_ID": i,
            "X": x,
            "Y": y,
            "Width": w,
            "Height": h
        })

    df = pd.DataFrame(defect_data)
    df["Timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return annotated, df

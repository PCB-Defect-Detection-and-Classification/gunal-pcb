
import cv2
from backend.image_processing import process_pcb_images
from backend.defect_localization import find_defect_bounding_boxes
from backend.roi_extraction import extract_and_save_rois

template_path = "data/uploads/golden/golden.jpg"
test_path = "data/uploads/test/test.jpg"

template, test, diff, binary_mask = process_pcb_images(
    template_path,
    test_path,
    save_outputs=True
)

boxes = find_defect_bounding_boxes(binary_mask, min_area=100)

roi_paths = extract_and_save_rois(
    test,
    boxes,
    output_dir="data/processed/rois"
)

print(f"Detected {len(boxes)} defect regions")
for p in roi_paths:
    print(p)

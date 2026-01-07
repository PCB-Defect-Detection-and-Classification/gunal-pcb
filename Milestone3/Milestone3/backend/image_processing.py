
import cv2
import os

def process_pcb_images(template_path, test_path, save_outputs=False):
    template = cv2.imread(template_path)
    test = cv2.imread(test_path)

    if template is None or test is None:
        raise ValueError("Could not read input images")

    template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    test_gray = cv2.cvtColor(test, cv2.COLOR_BGR2GRAY)
    test_gray = cv2.resize(test_gray, (template_gray.shape[1], template_gray.shape[0]))

    diff = cv2.absdiff(template_gray, test_gray)
    _, binary_mask = cv2.threshold(
        diff, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )

    if save_outputs:
        cv2.imwrite("data/processed/diff/diff_map.png", diff)
        cv2.imwrite("data/processed/masks/binary_mask.png", binary_mask)

    return template, test, diff, binary_mask

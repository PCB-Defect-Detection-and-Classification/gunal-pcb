
# PCB Defect Detection – Milestone 3

## Overview
This milestone implements classical image-processing-based PCB defect localization
and prepares cropped defect regions (ROIs) for future CNN training.

## Pipeline
1. Golden vs Test PCB comparison
2. Grayscale + alignment
3. Absolute difference
4. Otsu thresholding
5. Bounding box localization
6. ROI extraction

## How to Run
pip install -r requirements.txt
python run_pipeline.py

## Status
- Defect localization ✅
- Bounding boxes ✅
- ROI extraction ✅

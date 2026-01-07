# PCB Defect Detection & Classification — Milestone 3

## Overview
This milestone focuses on building a **production-style backend pipeline**
for PCB defect detection using **classical image processing**, and preparing
defect regions (ROIs) for CNN-based classification.

The system compares a **golden template PCB** with a **test PCB** to:
- Detect defect regions
- Localize defects using bounding boxes
- Extract cropped defect ROIs
- Prepare outputs for frontend visualization and reporting

---

## Folder Structure
```
Milestone3/
├── app/ # Streamlit frontend
│ └── main.py
├── backend/ # Core backend logic
│ ├── image_processing.py
│ ├── defect_localization.py
│ └── roi_extraction.py
├── data/
│ ├── uploads/
│ │ ├── golden/ # Uploaded golden PCB images
│ │ └── test/ # Uploaded test PCB images
│ └── processed/
│ ├── diff/ # Difference maps
│ ├── masks/ # Binary defect masks
│ └── rois/ # Cropped defect ROIs
├── reports/
│ └── inspection_reports/ # (Planned) PDF inspection reports
├── utils/
├── run_pipeline.py # End-to-end backend runner
├── requirements.txt
└── README.md

```

---

## Defect Detection Pipeline

1. Load golden template and test PCB images
2. Convert to grayscale and align dimensions
3. Compute absolute difference
4. Apply Otsu thresholding to obtain defect mask
5. Extract defect bounding boxes using contour analysis
6. Crop and save defect ROIs automatically

---

## How to Run (Google Colab)

1. Upload PCB images:
data/uploads/golden/golden.jpg
data/uploads/test/test.jpg


2. Run backend pipeline:
``bash
python run_pipeline.py
Outputs are saved automatically in:

powershell
Copy code
data/processed/
├── diff/
├── masks/
└── rois/
Frontend (Optional)
A Streamlit-based frontend (app/main.py) is provided for future integration.
It allows image uploads and visualization of results when run locally.

Status
 Backend pipeline implemented

 Defect localization with bounding boxes

 ROI extraction for CNN input

 Clean modular structure

 CNN inference integration (next milestone)

 PDF inspection report generation

Conclusion
Milestone 3 establishes a solid backend foundation that bridges classical
image processing (Milestone 1) and CNN-based defect classification
(Milestone 2), preparing the system for full-stack deployment.

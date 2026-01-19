AI-DRIVEN PCB DEFECT DETECTION AND CLASSIFICATION SYSTEM
=========================================================================

AN END-TO-END INDUSTRIAL AUTOMATED OPTICAL INSPECTION (AOI) PLATFORM


---------------------------------------------------------------------------
PROJECT OVERVIEW
---------------------------------------------------------------------------

This repository presents a complete, production-oriented Artificial Intelligence
system for Printed Circuit Board (PCB) defect inspection.

The system is designed as an Industrial Automated Optical Inspection (AOI)
platform capable of:

- Detecting manufacturing defects with high recall
- Localizing defect regions precisely
- Classifying defect types using deep learning
- Performing quality assessment and decision-making
- Generating inspection artifacts suitable for real QA workflows

Unlike academic prototypes that demonstrate isolated models, this project
delivers a fully integrated inspection pipeline aligned with real manufacturing
requirements.


---------------------------------------------------------------------------
SYSTEM PHILOSOPHY
---------------------------------------------------------------------------

The core philosophy of this system is:

"Do not rely on deep learning where classical vision is more reliable."

Accordingly:
- Classical Computer Vision is used for defect localization to ensure
  near-zero missed critical defects.
- Deep Learning is used only for classification, where it provides maximum value.
- Business logic and analytics convert predictions into actionable decisions.

This hybrid architecture mirrors real-world industrial AOI systems.


---------------------------------------------------------------------------
TECHNOLOGY STACK
---------------------------------------------------------------------------

Frontend Interface     : Streamlit  
Image Processing       : OpenCV, NumPy  
Deep Learning Framework: TensorFlow, Keras  
Model Architecture     : EfficientNetB0 (Custom Head)  
Database               : SQLite (Persistent Inspection Logs)  
Reporting              : Pandas, Matplotlib  
Deployment              : Local / Cloud-ready  

---------------------------------------------------------------------------
PROJECT STRUCTURE
---------------------------------------------------------------------------
```
gunal-pcb/
│
├── Milestone1/    Classical Image Processing and Defect Localization
├── Milestone2/    CNN Training and Evaluation
├── Milestone3/    Backend and Frontend Integration
├── Milestone4/    Final QA Platform and Deployment
│
└── README.md      Master Project Documentation
```

---------------------------------------------------------------------------
DEVELOPMENT MILESTONES
---------------------------------------------------------------------------

MILESTONE 1: DEFECT LOCALIZATION (COMPUTER VISION)
-------------------------------------------------
Objective:
Identify potential defect regions with maximum recall.

Key Techniques:
- Image alignment and normalization
- Absolute image differencing
- Otsu thresholding
- Morphological noise removal
- Bounding box extraction

Outcome:
Reliable localization of candidate defect regions without deep learning.


MILESTONE 2: DEFECT CLASSIFICATION (DEEP LEARNING)
-------------------------------------------------
Objective:
Accurately classify localized defect regions.

Key Techniques:
- EfficientNetB0 backbone
- Custom dense classification head
- Data augmentation and regularization
- Confusion-matrix-based evaluation

Performance:
- Validation Accuracy: 97.80%
- Robust generalization across all defect classes


MILESTONE 3: SYSTEM INTEGRATION
------------------------------
Objective:
Bridge classical detection and CNN classification into a unified system.

Key Contributions:
- ROI extraction pipeline
- Scale-consistent inference strategy
- Streamlit-based inspection interface
- Visualization of detected defects

Outcome:
End-to-end inspection pipeline usable by non-technical users.


MILESTONE 4: FINAL QA PLATFORM
-----------------------------
Objective:
Deliver a production-ready inspection system.

Advanced Features:
- Smart PCB alignment
- Automated batch processing
- Cost estimation and scrap logic
- Persistent inspection database
- Analytics dashboard
- Exportable inspection artifacts

This milestone converts the system into an industrial QA product.


---------------------------------------------------------------------------
SUPPORTED DEFECT TYPES
---------------------------------------------------------------------------

Defect Type         | Criticality | Recall
--------------------|-------------|--------
Open Circuit        | Critical    | 100%
Short Circuit       | Critical    | 100%
Missing Hole        | Critical    | 100%
Mouse Bite          | Moderate    | 96.5%
Spur                | Minor       | 98.2%
Spurious Copper     | Minor       | 95.8%


---------------------------------------------------------------------------
RUNNING THE FINAL APPLICATION
---------------------------------------------------------------------------

1. Clone the repository:

   git clone https://github.com/PCB-Defect-Detection-and-Classification/gunal-pcb.git
   cd gunal-pcb

2. Install dependencies:

   pip install -r Milestone4/requirements.txt

3. Launch the application:

   streamlit run Milestone4/app/main.py


---------------------------------------------------------------------------
ENGINEERING HIGHLIGHTS
---------------------------------------------------------------------------

- High-recall detection prioritizes safety-critical defects
- Deep learning used only where statistically justified
- Modular and maintainable architecture
- Designed for inspection engineers, not demos
- Fully reproducible and documented pipeline


---------------------------------------------------------------------------
AUTHOR
---------------------------------------------------------------------------

Gunal  
Internship Capstone Project  
AI-Based PCB Defect Detection and Classification System


---------------------------------------------------------------------------
FINAL NOTE
---------------------------------------------------------------------------

This repository represents a complete industrial inspection system,
not a proof-of-concept.

Every component was designed with reliability, interpretability,
and real manufacturing constraints in mind.

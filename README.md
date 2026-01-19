🔬 AI-Driven PCB Defect Detection & Classification System

Industrial-Grade Automated Optical Inspection (AOI) Platform

Internship Capstone Project
📊 Final Classification Accuracy: 97.80%
🚨 Recall on Critical Defects: 100%

📖 Executive Summary

This project presents a production-ready Automated Optical Inspection (AOI) system for detecting, localizing, classifying, and analyzing manufacturing defects in Printed Circuit Boards (PCBs).

Unlike traditional academic prototypes, this system is designed as a complete Quality Assurance (QA) platform, integrating:

* Classical Computer Vision for precise defect localization

* Deep Learning (CNNs) for accurate defect classification

* Business Intelligence logic for repair costing and scrap decisions

* Persistent analytics using a database-backed inspection history

The final system enables factory-ready inspection workflows, batch processing, audit tracking, and professional reporting.

| Layer     | Technology        | Purpose                                |
| --------- | ----------------- | -------------------------------------- |
| Frontend  | Streamlit         | Interactive inspection dashboard       |
| Backend   | Python, OpenCV    | Image alignment, defect extraction     |
| AI Model  | TensorFlow, Keras | Defect classification (EfficientNet)   |
| Database  | SQLite            | Persistent inspection logs & analytics |
| Reporting | Pandas, PDF tools | CSV logs & inspection reports          |

📂 Project Roadmap (Milestones)

The repository is structured into four progressive milestones, each building toward an industrial-grade solution.

🟢 Milestone 1 — Defect Detection Logic

Focus: Classical Computer Vision

Key Contributions

ORB feature matching for automatic template–test alignment

Image differencing and morphological processing

Binary defect mask generation

Outcome:
Accurate extraction of defect regions (ROIs) from raw PCB images.

📁 Milestone1/

🟡 Milestone 2 — Deep Learning Model Training

Focus: Defect Classification

Key Contributions

Trained an EfficientNet-based CNN

Multi-class classification of PCB defects

Confusion matrix, accuracy & loss analysis

Performance

97.8% validation accuracy

Robust performance on unseen test data

📁 Milestone2/

🟠 Milestone 3 — System Integration

Focus: Backend + Frontend Integration

Key Contributions

Unified detection + classification pipeline

ROI-based inference to reduce false positives

Bounding-box visualization & Streamlit UI

Outcome:
End-to-end PCB inspection with localized defect visualization.

📁 Milestone3/

🔴 Milestone 4 — Final Product & Deployment

Focus: Industrial Features & User Experience

Key Contributions

Optimized backend inference pipeline

Exportable results (images, logs)

Complete documentation and demo assets

Outcome:
A fully deployable AOI application suitable for real manufacturing environments.

📁 Milestone4/

✨ Advanced Capabilities (Beyond Requirements)
🧠 Smart Alignment & Preprocessing

* Automatic rotation, scaling, and warping using ORB + homography

* Noise suppression via morphological filtering

💰 Business Intelligence Logic

* Repair cost estimation per defect type

* Automatic SCRAP / PASS decision logic

* Critical-defect prioritization

🏭 Batch Inspection

* ZIP-based bulk PCB processing

* Scalable inspection without repeated uploads

🗄️ Persistent Analytics

* SQLite-backed inspection history

* Yield tracking and defect trends

* Audit-ready logs for QA teams

| Defect Type     | Recall | Severity    |
| --------------- | ------ | ----------- |
| Open Circuit    | 100%   | 🔴 Critical |
| Short Circuit   | 100%   | 🔴 Critical |
| Missing Hole    | 100%   | 🔴 Critical |
| Mouse Bite      | 96.5%  | 🟡 Moderate |
| Spur            | 98.2%  | 🟢 Minor    |
| Spurious Copper | 95.8%  | 🟢 Minor    |

🚀 Running the Final Application (Milestone 4)
1️⃣ Clone the Repository
git clone https://github.com/PCB-Defect-Detection-and-Classification/gunal-pcb.git
cd gunal-pcb

2️⃣ Install Dependencies
pip install -r Milestone4/requirements.txt

3️⃣ Launch the Dashboard
cd Milestone4
streamlit run app/main.py

📚 Documentation

Detailed documentation is available inside Milestone 4:

📖 User Guide — Instructions for operators and inspectors

🛠️ Technical Report — Algorithms, architecture, and design decisions

📁 Milestone4/Documentation/

🏆 Project Highlights

✔ Industrial AOI workflow
✔ High-recall defect detection
✔ Deep learning classification
✔ Persistent analytics & reporting
✔ Deployment-ready architecture

👤 Author

Gunal
Internship Capstone Project
2025–2026
  



# 👤 User Guide – PCB Defect Inspection System

## 1. Introduction
This guide explains how to use the PCB Defect Inspection System for quality inspection tasks.

---

## 2. System Requirements
- Python 3.8+
- Streamlit
- OpenCV
- NumPy
- Pandas

---

## 3. Running the Application
From the Milestone4 directory:
streamlit run app/main.py

yaml
Copy code

---

## 4. Using the Interface
1. Upload **Golden PCB Image**
2. Upload **Test PCB Image**
3. Click **Run Inspection**
4. View detected defects
5. Download:
   - Annotated Image
   - CSV Defect Log

---

## 5. Output Files
- Annotated Image: Bounding boxes around defects
- CSV Log: Coordinates and dimensions of defects

---

## 6. Notes
- Ensure images are properly aligned
- Best results achieved with similar lighting conditions

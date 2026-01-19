
# 📘 Technical Report – PCB Defect Detection System

## 1. Introduction
This report documents the architecture and algorithms used in the final PCB defect inspection system.

---

## 2. System Architecture
The system is divided into:
- Frontend (Streamlit UI)
- Backend Processing Pipeline
- Export & Reporting Module

---

## 3. Defect Detection Pipeline
1. Image Loading
2. Grayscale Conversion
3. Image Alignment
4. Absolute Difference Computation
5. Otsu Thresholding
6. Morphological Cleanup
7. Bounding Box Extraction

---

## 4. Algorithms Used
- Absolute Image Differencing
- Otsu Thresholding
- Contour Detection
- Area-based filtering

---

## 5. Output Generation
- Annotated PCB images
- CSV inspection logs
- Timestamped inspection records

---

## 6. Performance
- Fast inference (<1s per image pair)
- Modular and extensible backend
- Suitable for batch and real-time inspection

---

## 7. Conclusion
This system demonstrates how classical image processing can be used effectively for PCB defect inspection and provides a strong foundation for future deep-learning extensions.

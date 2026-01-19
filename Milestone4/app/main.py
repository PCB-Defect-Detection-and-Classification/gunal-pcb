
import streamlit as st
import cv2
import os
from backend.pipeline import run_inspection

st.set_page_config(page_title="PCB Defect Inspection", layout="wide")

st.title("🔍 PCB Defect Inspection System")
st.markdown("### Milestone 4 – Final Application")

golden_file = st.file_uploader("Upload Golden PCB Image", type=["jpg", "png"])
test_file = st.file_uploader("Upload Test PCB Image", type=["jpg", "png"])

if golden_file and test_file:
    os.makedirs("exports/images", exist_ok=True)
    os.makedirs("exports/logs", exist_ok=True)

    golden_path = f"exports/{golden_file.name}"
    test_path = f"exports/{test_file.name}"

    with open(golden_path, "wb") as f:
        f.write(golden_file.read())

    with open(test_path, "wb") as f:
        f.write(test_file.read())

    if st.button("🚀 Run Inspection"):
        with st.spinner("Processing PCB images..."):
            annotated_img, defect_log = run_inspection(
                golden_path, test_path
            )

        st.success(f"Detected {len(defect_log)} defect regions")

        st.image(
            cv2.cvtColor(annotated_img, cv2.COLOR_BGR2RGB),
            caption="Detected Defects",
            use_column_width=True
        )

        img_out = "exports/images/annotated_output.png"
        csv_out = "exports/logs/defect_log.csv"

        cv2.imwrite(img_out, annotated_img)
        defect_log.to_csv(csv_out, index=False)

        st.subheader("⬇️ Download Results")

        with open(img_out, "rb") as f:
            st.download_button(
                "Download Annotated Image",
                f,
                file_name="annotated_output.png"
            )

        with open(csv_out, "rb") as f:
            st.download_button(
                "Download Defect Log (CSV)",
                f,
                file_name="defect_log.csv"
            )

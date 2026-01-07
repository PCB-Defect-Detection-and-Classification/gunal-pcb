
import streamlit as st
from PIL import Image

st.set_page_config(page_title="PCB Defect Detection", layout="wide")
st.title("🔍 PCB Defect Detection System")

col1, col2 = st.columns(2)

with col1:
    golden = st.file_uploader("Upload Golden PCB", type=["png","jpg","jpeg"])
    if golden:
        st.image(Image.open(golden), caption="Golden PCB", use_column_width=True)

with col2:
    test = st.file_uploader("Upload Test PCB", type=["png","jpg","jpeg"])
    if test:
        st.image(Image.open(test), caption="Test PCB", use_column_width=True)

st.info("Backend integration completed in Milestone 3")

import streamlit as st
import pandas as pd
import os
from PIL import Image

# Set wide layout
st.set_page_config(layout="wide")

# Path to the directory containing images
image_dir = "Calculus"  # Updated path

# Load images and create a DataFrame (replace this with actual labels if available)
image_files = os.listdir(image_dir)
data = {
    "filename": image_files,
    "label": [f"Label for {file}" for file in image_files],  # Replace with actual labels if available
}

df = pd.DataFrame(data)

# Custom CSS to increase font size
st.markdown(
    """
    <style>
    .big-font {
        font-size:24px !important;
    }
    .medium-font {
        font-size:20px !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Streamlit App
st.markdown("<h1 class='big-font' style='text-align: center; color: black;'>Oral Diseases Classification</h1>", unsafe_allow_html=True)

# Layout with two columns
col1, col2 = st.columns([1, 2])

with col1:
    st.markdown("<h3 class='medium-font' style='color: black;'>Choose an image:</h3>", unsafe_allow_html=True)
    selected_image = st.selectbox("Select an image", df["filename"], label_visibility='collapsed')

with col2:
    image_path = os.path.join(image_dir, selected_image)
    image = Image.open(image_path)
    st.image(image, caption=f"{selected_image} - {df[df['filename'] == selected_image]['label'].values[0]}", use_column_width=True)

# Optional: Add more functionalities (e.g., predictions, analysis, etc.)

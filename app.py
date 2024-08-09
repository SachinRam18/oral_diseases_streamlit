import streamlit as st
import pandas as pd
import os
from PIL import Image

# Path to the directory containing images
image_dir = "C:/Users/Sachin/Downloads/Calculus"

# Example of how to create a DataFrame if you have labels
# If you have a CSV file with image names and labels, load it with pd.read_csv
# For this example, we're creating it manually

# Assuming filenames have labels embedded or you have a CSV file
image_files = os.listdir(image_dir)
data = {
    "filename": image_files,
    "label": [f"Label for {file}" for file in image_files],  # Replace with actual labels if available
}

df = pd.DataFrame(data)

# Streamlit App
st.title("Oral Diseases Classification")

# Dropdown to select an image
selected_image = st.selectbox("Choose an image", df["filename"])

# Display the selected image
image_path = os.path.join(image_dir, selected_image)
image = Image.open(image_path)
st.image(image, caption=f"{selected_image} - {df[df['filename'] == selected_image]['label'].values[0]}")

# Optional: Add more functionalities (e.g., predictions, analysis, etc.)

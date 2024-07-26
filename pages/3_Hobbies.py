# 3_Hobbies.py
# Don't remove the comment above.

import streamlit as st  # type: ignore
from PIL import Image
import os
import sys
sys.path.append('..')
from constant import info
from main_app import DocumentQAApp  # Corrected the import path

def local_css(file_name):
    try:
        with open(file_name) as f:
            st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
    except FileNotFoundError:
        st.error(f"CSS file {file_name} not found.")

def load_images_from_directory(directory):
    image_files = []
    supported_formats = (".png", ".jpg", ".jpeg", ".gif", ".PNG", ".JPG", ".JPEG", ".GIF")
    for file in os.listdir(directory):
        if file.lower().endswith(supported_formats):
            image_files.append(os.path.join(directory, file))
    return image_files

app = DocumentQAApp()  # Initialize the main app class to access its methods and properties

local_css("styles/style.css")  # Updated path

st.sidebar.image(app.photo, caption="Profile Picture", use_column_width=True)

st.title("🎨 Hobbies")

image_files = load_images_from_directory("images")

if image_files:
    cols = st.columns(3)  # Create 3 columns for displaying images
    for i, image_path in enumerate(image_files):
        with cols[i % 3]:
            try:
                image = Image.open(image_path)
                st.image(image, caption=os.path.basename(image_path))
            except FileNotFoundError:
                st.error(f"Image {image_path} not found.")
else:
    st.write("No images found in the directory.")

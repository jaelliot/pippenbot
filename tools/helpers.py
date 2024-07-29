# utils/helpers.py

import os
import base64
import streamlit as st
from PIL import Image

sss = st.session_state

def once_load_images():
    image_names = ['me']

    sss['images'] = {
        name: Image.open(f"images/{name}.jpg")
        for name in image_names if os.path.exists(f"images/{name}.jpg")
    }

def get_base64_image(image_path):
    with open(image_path, 'rb') as img_file:
        img_bytes = img_file.read()
    img_base64 = base64.b64encode(img_bytes).decode('utf-8')
    return img_base64

def background():
    if 'bg_64' not in sss:
        image_path = 'images/IMG_2981.jpg'
        sss['bg_x'], sss['bg_y'] = Image.open(image_path).size
        sss['bg_64'] = get_base64_image(image_path)
        sss['bg_ext'] = image_path.rsplit('.', 1)[1]
    
   
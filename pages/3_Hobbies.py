import streamlit as st # type: ignore
from PIL import Image
from constant import info
from streamlit_app import DocumentQAApp

def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

app = DocumentQAApp()  # Initialize the main app class to access its methods and properties

local_css("styles/style.css")  # Updated path

st.sidebar.markdown(app.photo, unsafe_allow_html=True)

img_1 = Image.open("images/1.jpg")  # Updated path
img_2 = Image.open("images/2.png")  # Updated path
img_3 = Image.open("images/3.png")  # Updated path

st.title("🎨 Hobbies")

col1, col2, col3 = st.columns(3)

with col1:
    st.image(img_1)

with col2:
    st.image(img_2)

with col3:
    st.image(img_3)

import streamlit as st # type: ignore
import base64
from constant import info
from streamlit_app import DocumentQAApp

def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

app = DocumentQAApp()  # Initialize the main app class to access its methods and properties

local_css("styles/style.css")  # Updated path

st.sidebar.markdown(app.photo, unsafe_allow_html=True)

st.title("📄 Resume")

st.write("[Click here if it's blocked by your browser](https://jayalexanderelliot.com)")

with open("resume/resume.pdf", "rb") as f:  # Updated path
    base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="1000mm" height="1000mm" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)

import os
import base64
import streamlit as st
from tools.layout_utils import always
from tools.content_utils import footer
from tools.helpers import background
sss = st.session_state

def main():
    st.header("Curriculum Vitae", anchor='cv', divider="orange")
    
    # Path to the resume PDF
    resume_path = os.path.join("resume", "resume.pdf")
    
    # Check if the file exists
    if os.path.exists(resume_path):
        with open(resume_path, "rb") as pdf_file:
            base64_pdf = base64.b64encode(pdf_file.read()).decode("utf-8")
        pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="600px"></iframe>'
        st.markdown(pdf_display, unsafe_allow_html=True)
        st.markdown(f"Download the [CV](https://drive.proton.me/urls/QDXZ97SQ5R#PZSkIiQfsvAA)")
    else:
        st.error("The resume file was not found.")

if __name__ == "__main__":
    always()
    main()
    footer()
    background()

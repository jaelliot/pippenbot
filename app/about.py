# app/about.py

import streamlit as st # type: ignore
from utils.constant import info

def main():
    st.title(f"About Me - {info['Full_Name']}")
    
    st.markdown(f"## Introduction")
    st.markdown(info.get('Intro', 'Introduction not provided.'))
    
    st.markdown(f"## About")
    st.markdown(info.get('About', 'About information not provided.'))
    
    st.markdown(f"## Contact Information")
    contact_info = f"""
    - **Email:** [{info['Email']}](mailto:{info['Email']})
    - **LinkedIn:** [{info['Social_Media']['LinkedIn']}]({info['Social_Media']['LinkedIn']})
    - **Location:** [Utah Valley University](https://maps.app.goo.gl/bfAP9bXekxB31iXp7)
    """
    st.markdown(contact_info)

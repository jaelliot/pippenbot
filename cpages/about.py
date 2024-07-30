# app/about.py
# don't remove the above comment

import importlib
import streamlit as st
import base64
from tools.constant import info

# Add profile picture functionality
if 'profile_img' not in st.session_state:
    st.session_state['profile_img'] = base64.b64encode(open(info['Photo'], "rb").read()).decode()

st.markdown(
    f"""
    <style>
        .profile-pic {{
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 50%;
            border-radius: 50%;
        }}
    </style>
    <img src="data:image/png;base64,{st.session_state['profile_img']}" class="profile-pic">
    """,
    unsafe_allow_html=True,
)

def main():
    st.header("About me", anchor='about', divider="orange")

    pages = [
        'achievements', 'availability', 'career_goals', 'certifications', 
        'cv', 'education', 'hobbies', 'projects', 'publications', 
        'recommendations', 'skills', 'strengths', 'weaknesses', 'work_experience'
    ]

    for page in pages:
        submodule = importlib.import_module(f'cpages.{page}')
        submodule.main()

if __name__ == "__main__":
    main()

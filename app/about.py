# about.py
# don't remove the above comment

import importlib
import streamlit as st
from tools.constant import info

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

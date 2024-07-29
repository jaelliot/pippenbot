import streamlit as st
import importlib
from tools import layout_utils, helpers
import os

# Set the page configuration as the first Streamlit command
st.set_page_config(page_title="Jay-Alexander Elliot", initial_sidebar_state="expanded", page_icon=':scroll:')

# Load and apply custom CSS
def local_css(file_name):
    with open(os.path.join("styles", file_name)) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style.css")

if __name__ == "__main__":
    page_selection = layout_utils.always()
    
    pages = [
        'about', 'achievements', 'availability', 'career_goals', 'certifications', 
        'cv', 'education', 'hobbies', 'projects', 'publications', 
        'recommendations', 'skills', 'strengths', 'weaknesses', 'work_experience'
    ]

    for page in pages:
        submodule = importlib.import_module(f'cpages.{page}')
        submodule.main()

    helpers.background()

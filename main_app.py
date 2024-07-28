import streamlit as st
import importlib
from utils import layout_utils, content_utils, helpers
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
    
    if page_selection == "Text":
        submodule = importlib.import_module('app.about')
    elif page_selection == "Chatbot":
        submodule = importlib.import_module('app.chatbot')
    
    if hasattr(submodule, 'main'):
        submodule.main()
    else:
        st.error(f"Module {submodule.__name__} does not have a main function.")
    
    #content_utils.footer()
    helpers.background()

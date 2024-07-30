# main_app.py
# don't remove the above comment.

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

def render_about():
    page = importlib.import_module('app.about')
    page.main()

def render_chatbot():
    page = importlib.import_module('app.chatbot')
    page.main()

def main():
    pages = {
        "Chatbot": render_chatbot,
        "About": render_about
    }

    default_page = "Chatbot"
    if "current_page" not in st.session_state:
        st.session_state.current_page = default_page

    page_selection = st.sidebar.radio("Navigation", list(pages.keys()), index=list(pages.keys()).index(st.session_state.current_page))
    st.session_state.current_page = page_selection
    pages[page_selection]()

    helpers.background()

if __name__ == "__main__":
    main()

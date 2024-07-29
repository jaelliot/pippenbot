# tools/__init__.py

from .layout_utils import check_layout, once_set_layout, once_layout_toast, fix_layout, always as layout_always
from .sidebar_utils import add_logo_N_styles, sidebar, sidebar_pages, redirect_button
from .content_utils import footer
from .helpers import once_load_images, get_base64_image, background

import streamlit as st
from tools.constant import info

def always():
    layout_always()
    state = st.set_page_config(
        page_title=info["Full_Name"],
        initial_sidebar_state="auto",
        page_icon=':scroll:',
        layout=st.session_state['layout'],
        menu_items={
            'About': f"""
                ## Portfolio of {info["Full_Name"]}
                {info["Full_Name"]} is a Software Engineer with a background in DevOps and AI.
            """
        },
    )
    once_layout_toast()
    once_load_images()
    with st.sidebar:
        page_selection = sidebar()
    
    fix_layout()
    return page_selection

# utils/layout_utils.py
#please don't remove the above comment

import streamlit as st
from time import sleep
from streamlit_js_eval import streamlit_js_eval
from tools.sidebar_utils import sidebar
from tools.helpers import once_load_images

sss = st.session_state

def check_layout():
    width = streamlit_js_eval(js_expressions='screen.width')
    height = streamlit_js_eval(js_expressions='screen.height')
    inner_width = streamlit_js_eval(js_expressions="window.innerWidth")
    sleep(1)
        
    if width is not None and height is not None:
        if width < height:
            sss['layout'] = "wide"
            sss['a4_width'] = int(width * 0.92)
            sss['a4_height'] = 700
        else:
            sss['layout'] = "centered"
            sss['a4_width'] = inner_width
            sss['a4_height'] = 1020

def once_set_layout():
    if 'layout' not in sss:
        with st.spinner('Checking your device layout...'):
            check_layout()
            st.rerun()

def once_layout_toast():
    if 'layout_toasted' not in sss:
        st.toast(
            f"{'Narrow' if sss['layout'] == 'wide' else 'Wide'} layout detected. Refresh to reset.", 
            icon = '🛠️')
        sss['layout_toasted'] = True

def fix_layout():
    if sss['layout'] == 'wide':
        st.write('''
        <style>
            [data-testid="column"] {
                width: calc(16.6666% - 1rem) !important;
                flex: 1 1 calc(16.6666% - 1rem) !important;
                min-width: calc(16.6666% - 1rem) !important;
            }
            .st-emotion-cache-1tpzimh {
                max-width: 20% !important;
            }
            .main{
                position: absolute !important;
            }
        </style>
        ''', unsafe_allow_html=True)
    else:
        st.write('''
        <style>
            [data-testid="column"] {
            }
            .st-emotion-cache-1tpzimh {
                max-width: inherit;
            }
            div.block-container {
                padding-top: 1.5rem;
                max-width: 55rem;
            }
        </style>
        ''', unsafe_allow_html=True)

def always():
    once_set_layout()
    once_layout_toast()
    once_load_images()
    with st.sidebar:
        page_selection = sidebar()
    
    fix_layout()
    return page_selection

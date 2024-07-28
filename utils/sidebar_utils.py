# utils/sidebar_utils.py

import base64
import streamlit as st # type: ignore
from utils.constant import info

sss = st.session_state

contact = f"""
    <span style="color: #000000;">:globe_with_meridians: [LinkedIn]({info['Social_Media']['LinkedIn']})</span>  
    <span style="color: #000000;">:email: [{info['Email']}](mailto:{info['Email']})</span>   
    <span style="color: #000000;">:earth_africa: [Utah Valley University](https://maps.app.goo.gl/bfAP9bXekxB31iXp7)</span>  
"""

def add_logo_N_styles():
    if 'profile_img' not in sss:
        sss['profile_img'] = base64.b64encode(open(info['Photo'], "rb").read()).decode()
    
    st.markdown(
        f"""
        <style>
            [data-testid="stSidebarUserContent"] {{
                background-image: url(data:image/png;base64,{sss['profile_img']});
                background-repeat: no-repeat;
                padding-top: 80px;
                background-size: 150px;
                background-position: 20px 0px;
            }}
            [data-testid="stSidebarUserContent"]::before {{
                content: "";
                margin-left: 20px;
                font-size: 10px;
            }}
            [data-testid="stSidebarHeader"] {{
                padding: 0rem 0rem 0rem;
            }}
            [data-testid="stHeader"] {{
                height: 0;
            }}
            [class=".stPageLink"]::before {{
                margin-top: -0.5rem;
                margin-bottom: -0.5rem;
            }}
            a {{
                color: #000000 !important;
            }}
        </style>
        """,
        unsafe_allow_html=True,
    )

def sidebar():
    add_logo_N_styles()
    
    pages = ["Text", "Chatbot"]
    page_selection = st.sidebar.radio("Navigation", pages)
    
    st.sidebar.header(info["Full_Name"], divider="orange")
    sidebar_pages()
    st.sidebar.subheader("", divider="orange")
    st.sidebar.markdown(contact, unsafe_allow_html=True)  # Added unsafe_allow_html=True to allow HTML rendering
    
    return page_selection

def redirect_button(url: str, icon: str=None, text: str= None, color="transparent"):
    st.markdown(f'''
    <link rel="stylesheet" style="text-decoration: none;" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" />
    <a href="{url}" target="_self" style="color: inherit; text-decoration: none;">
        <div style="
                display: flex;
                flex-direction: row;
                -webkit-box-align: center;
                align-items: center;
                -webkit-box-pack: start;
                justify-content: flex-start;
                gap: 0.5rem;
                border-radius: 0.25rem;
                padding-left: 0.5rem;
                padding-right: 0.5rem;
                margin-top: 0.125rem;
                margin-bottom: 0.125rem;
                line-height: 2;
                background-color: {color};
            ">
            <span class="material-symbols-outlined" style="
                    fill: currentcolor;
                    display: inline-flex;
                    -webkit-box-align: center;
                    align-items: center;
                    font-size: 1.25rem;
                    width: 1.25rem;
                    height: 1.25rem;
                    flex-shrink: 0;
                ">
                {icon}
            </span>
            <span style="
                    color: #000000;  # Set to dark color
                    overflow: hidden;
                    white-space: nowrap;
                    text-overflow: ellipsis;
                    display: table-cell;
                ">
                {text}
            </span>
        </div>
    </a>
    ''',
    unsafe_allow_html=True)

def sidebar_pages():
    sss['pages'] = {
        "#about": ("About", 'person'),
        "#experiences": ("Experiences", 'history'),
        "#education": ("Education", 'import_contacts'),
        "#projects": ("Projects", 'content_paste'),
        "#skills": ("Skills", 'handyman'),
        "#publications": ("Publications", 'history_edu'),
        "#cv": ("Curriculum vitae", 'contact_page'),
        "#recommendations": ("Recommendations", 'mail'),
    }

    for anchor, (label, icon) in sss['pages'].items():
        redirect_button(anchor, icon=icon, text=label)

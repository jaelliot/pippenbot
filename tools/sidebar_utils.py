# sidebar_utils.py
# Please don't remove the comment above.

import base64
import streamlit as st
from tools.constant import info

sss = st.session_state

contact = f"""
    <span style="color: #000000;">:globe_with_meridians: [LinkedIn]({info['Social_Media']['LinkedIn']})</span><br>
    <span style="color: #000000;">:email: [{info['Email']}](mailto:{info['Email']})</span><br>
    <span style="color: #000000;">:earth_americas: [Utah Valley University](https://maps.app.goo.gl/bfAP9bXekxB31iXp7)</span><br>
    <span style="color: #000000;">:link: [GitHub](https://github.com/jaelliot)</span><br>
    <span style="color: #000000;">:link: [Website](https://www.jayalexanderelliot.com)</span><br>
    <span style="color: #000000;">:briefcase: [Side Gig Website](https://mobilelegalsolutions.com)</span><br>
    <span style="color: #000000;">:musical_note: [Spotify](https://open.spotify.com/user/31kck6h4276svjagei5pbexd2fym)</span><br>
"""

def add_logo_N_styles():
    if 'profile_img' not in sss:
        sss['profile_img'] = base64.b64encode(open(info['Photo'], "rb").read()).decode()
    
    st.markdown(
        f"""
        <style>
            [data-testid="stSidebarUserContent"] {{
                background-image: url(data:image/png;base64,{sss['profile_img']});
                padding-top: 120px;
                background-size: 100px;
                background-position: 20px 20px;
            }}
            [data-testid="stSidebarUserContent"]::before {{
                content: "{info['Full_Name']}";
                margin-left: 20px;
                margin-bottom: 20px;
                font-size: 18px;
                position: relative;
                top: -10px;
                font-weight: bold;
            }}
            [data-testid="stSidebarHeader"] {{
                padding-top: 0;
                padding-bottom: 0;
            }}
            [data-testid="stHeader"] {{
                height: 0;
            }}
            .sidebar-content {{
                padding-top: 20px;
            }}
            .sidebar-link {{
                text-decoration: none;
                color: #000000 !important;
                padding: 8px 0;
                display: flex;
                align-items: center;
            }}
            .sidebar-link:hover {{
                background-color: #f0f0f0;
            }}
            .sidebar-link .icon {{
                margin-right: 10px;
                width: 24px;
                text-align: center;
            }}
            .divider {{
                border-top: 1px solid #e0e0e0;
                margin: 10px 0;
            }}
        </style>
        """,
        unsafe_allow_html=True,
    )

def sidebar():
    add_logo_N_styles()
    
    st.sidebar.markdown('<div class="sidebar-content">', unsafe_allow_html=True)
    pages = ["Chatbot", "Text"]
    st.sidebar.radio("Navigation", pages)
    st.sidebar.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    sidebar_pages()
    st.sidebar.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    st.sidebar.markdown(contact, unsafe_allow_html=True)
    st.sidebar.markdown('</div>', unsafe_allow_html=True)
    
    return pages

def redirect_button(url: str, icon: str=None, text: str= None):
    st.markdown(f'''
    <a href="{url}" class="sidebar-link">
        <span class="icon">{icon}</span>
        <span>{text}</span>
    </a>
    ''',
    unsafe_allow_html=True)

def sidebar_pages():
    sss['pages'] = {
        "#about": ("About", '👤'),
        "#career_goals": ("Career Goals", '🚀'),
        "#work_experience": ("Work Experience", '💼'),
        "#education": ("Education", '🎓'),
        "#skills": ("Skills", '🛠️'),
        "#certifications": ("Certifications", '📜'),
        "#achievements": ("Achievements", '🏆'),
        "#projects": ("Projects", '📁'),
        "#publications": ("Publications", '📚'),
        "#recommendations": ("Recommendations", '📬'),
        "#strengths": ("Strengths", '💪'),
        "#weaknesses": ("Weaknesses", '🔧'),
        "#hobbies": ("Hobbies", '🎨'),
        "#availability": ("Availability", '📅'),
        "#cv": ("Curriculum Vitae", '📄'),
    }

    for anchor, (label, icon) in sss['pages'].items():
        redirect_button(anchor, icon=icon, text=label)
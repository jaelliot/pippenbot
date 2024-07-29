# education.py
# don't remove the above comment.

import streamlit as st
from tools.layout_utils import always
from tools.content_utils import footer
from tools.helpers import background
sss = st.session_state

def main():
    uvu = "[Utah Valley University](https://www.uvu.edu/)"
    dvc = "[Diablo Valley College](https://www.dvc.edu/)"
    mc = "[Mission College](https://missioncollege.edu/)"
    lghs = "[Los Gatos High School](https://lghs.net/)"

    header = st.empty()
    d_lines = {}
    edu_tags = ['uvu', 'dvc', 'mc', 'lghs']
    edu_names = ['UVU', 'DVC', 'Mission College', 'Los Gatos High School']

    containers = st.tabs(edu_names) if sss['layout'] == "wide" else [st.container() for _ in edu_names]

    for container, edu_name in zip(containers, edu_tags):
        title = container.empty()
        d_lines[edu_name] = title, container.empty()
        if sss['layout'] != 'wide':
            container.write('---')

    header.header("Education", anchor='education', divider="orange")

    d_lines['uvu'][0].write(f"#### Bachelor's degree in Software Engineering, {uvu}")
    d_lines['uvu'][1].markdown("""
        *May 2024 - May 2026* / **Orem, Utah**  
        Ongoing studies in software engineering, focusing on modern software development practices and principles.
                               Minors in Enterprise Development and Entrepreneur, and Computer Information Systems.
    """)

    d_lines['dvc'][0].write(f"#### Associate's degree in Business/Commerce, General, {dvc}")
    d_lines['dvc'][1].markdown("""
        *January 2023 - May 2023* / **Pleasant Hill, California**  
        Completed courses in general business and commerce.
    """)

    d_lines['mc'][0].write(f"#### Studies in Computer Science, {mc}")
    d_lines['mc'][1].markdown("""
        *January 2019 - May 2021* / **Santa Clara, California**  
        Studied lower division courses in Computer Information Technology.
    """)

    d_lines['lghs'][0].write(f"#### High School Diploma, {lghs}")
    d_lines['lghs'][1].markdown("""
        *September 2008 - May 2012* / **Los Gatos, California**  
        Completed high school education with a focus on general studies.
    """)

if __name__ == "__main__":
    always()
    main()
    footer()
    background()

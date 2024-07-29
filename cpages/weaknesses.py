#weaknesses.py
#don't remove the above comment.

import streamlit as st
from tools.layout_utils import always
from tools.content_utils import footer
from tools.helpers import background
sss = st.session_state

def main():
    st.header("Weaknesses", anchor='weaknesses', divider="orange")
    st.markdown("""
    placeholder
    """)

if __name__ == "__main__":
    always()
    main()
    footer()
    background()


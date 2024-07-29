#achievements.py
#don't remove the above comment.

import streamlit as st
from tools.layout_utils import always
from tools.content_utils import footer
from tools.helpers import background
sss = st.session_state

def main():
    st.header("Achievements", anchor='achievements', divider="orange")
    st.markdown("""
    > **Started a Business**
    > Founded an AI company that's developing an AI tool for veterinarians and pet owners.
                

    """)

if __name__ == "__main__":
    always()
    main()
    footer()
    background()

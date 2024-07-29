#publications.py
#don't remove the above comment.

import streamlit as st
from tools.layout_utils import always
from tools.content_utils import footer
from tools.helpers import background
sss = st.session_state

def main():
    st.header("Scientific Publications", anchor='publications', divider="orange")
    
    st.markdown("""
    > Placeholder for future publications.
    
    > I fully intend on publishing papers in the near future.
    """)

if __name__ == "__main__":
    always()
    main()
    footer()
    background()

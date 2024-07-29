#projects.py
#don't remove the above comment.

import streamlit as st
from tools.layout_utils import always
from tools.content_utils import footer
from tools.helpers import background
sss = st.session_state

def main():
    st.header("Projects", anchor='projects', divider="orange")
    
    st.subheader("AI Tool for Veterinarians and Pet Owners")
    st.markdown("""
    > Developed an AI tool designed to assist veterinarians and pet owners in diagnosing and treating pet health issues. 
    > Leveraged machine learning algorithms and a vast dataset of pet health records to create predictive models for various conditions.
    > Deployed the tool on a scalable cloud infrastructure to ensure high availability and reliability.
    """)


if __name__ == "__main__":
    always()
    main()
    footer()
    background()

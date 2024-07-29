#certifications.py
#don't remove the above comment.

import streamlit as st
from tools.layout_utils import always
from tools.content_utils import footer
from tools.helpers import background
sss = st.session_state

def main():
    st.header("Certifications", anchor='certifications', divider="orange")
    st.markdown("""
    > **Certifications**

    > - AWS Certified Solutions Architect - PicoEdge (2024-2027)
    > - Jamf Certified Associate - Jamf Pro (2024-2027)
    > - Jamf Certified Associate - Jamf Protect (2024-2027)
    > - DoD CUI Training
    > - AWS Cloud Practitioner
    > - Hubspot Sales Software
    """)

if __name__ == "__main__":
    always()
    main()
    footer()
    background()

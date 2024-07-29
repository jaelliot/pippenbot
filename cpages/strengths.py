#strengths.py
#don't remove the above comment.

import streamlit as st
from tools.layout_utils import always
from tools.content_utils import footer
from tools.helpers import background
sss = st.session_state

def main():
    st.header("Strengths", anchor='strengths', divider="green")
    st.markdown("""
    > **Quick Learner:** My ADHD mind allows me to quickly absorb and master new skillsets.
    
    > **Cloud Expertise:** Extensive experience with AWS, Azure, GCP, and other cloud platforms.
    
    > **Automation Guru:** Skilled in automating infrastructure and deployment tasks using tools like Terraform, Ansible, and GitHub Actions.
    
    > **Technical Proficiency:** Proficient in Docker, Kubernetes, Shell/Powershell, Python, and various operating systems including Linux and FreeBSD.
    
    > **Leadership:** Proven leadership and team management skills, fostering collaboration and technical growth in cross-functional teams.
    
    > **Customer Focus:** Strong background in customer service and technical support, excelling at diagnosing and resolving issues to improve customer satisfaction.
    """)

if __name__ == "__main__":
    always()
    main()
    footer()
    background()

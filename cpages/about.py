# about.py
# don't remove the above comment.

import streamlit as st
from tools.layout_utils import always
from tools.content_utils import footer
from tools.helpers import background
sss = st.session_state

def main():
    st.header("About me", anchor='about', divider="orange")
    st.markdown("""
    > Hello, my name is Jay-Alexander Elliot.

    > An accomplished IT professional with a focus on Data Center and DevOps roles, I am a resourceful bilingual engineer with extensive skills in cloud monitoring, automation, deployment, and troubleshooting. 
    > I bring robust experience in data management, including data extraction and pipeline creation for AI training. I excel in building cloud environments using infrastructure-as-code (IaC) tools, and have significant experience with Linux, Unix, and Windows server operating systems.

    > I always had a keen interest in infrastructure maintenance and operations optimization, as evidenced by my zero-downtime management of private cloud infrastructure at picoEdge. 
    > With an extensive background in customer service and technical support, I excel at diagnosing and resolving issues, as demonstrated during my time as an In-store Technician. 

    > After my tenure as a Datacenter Technician at Redapt Inc., where I performed server setup and troubleshooting, I have honed my skills in virtual and physical infrastructure management and task automation, gained at RosaLind.
    > I am skilled in tools like Docker, Shell/Powershell, Git, Microsoft Azure, Python, Red Hat Linux, and AWS. I am well-positioned to alleviate a company's IT challenges in a Data Center environment.

    > I am currently actively seeking new opportunities and ready to start immediately. I aim to leverage my expertise in cloud technologies, automation, and infrastructure management to drive innovation and create solutions that positively impact businesses and society.
    """)

if __name__ == "__main__":
    always()
    main()
    footer()
    background()

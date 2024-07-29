#skills.py
#please modify this 

import streamlit as st
from tools.layout_utils import always
from tools.content_utils import footer
from tools.helpers import background
sss = st.session_state

def main():
    st.header("Skills", anchor='skills', divider="orange")
    st.info("Actively seeking new opportunities")
    st.markdown("""
        * **Programming Languages:** Python, Shell, Powershell, Golang, Typescript, R
        * **Cloud Platforms:** AWS, Azure, GCP, DigitalOcean
        * **Containerization Technologies:** Docker, Kubernetes, Nomad
        * **CI/CD:** GitHub Actions, ArgoCD
        * **Configuration Management:** HashiCorp Packer, Terraform, Ansible, Consul, Vault
        * **Operating Systems:** MacOS, Windows desktop and server, Linux (SUSE, RHEL, Debian), BSD (FreeBsd)
        * **Virtualization Technologies:** VMware, Hyper-V, Vagrant
        * **Performance Optimization:** AWS Cost Explorer, Azure Advisor
        * **Databases:** Postgres, SQLite, Chroma
        * **Large Language Models:** Retrieval Augmented Generation, Llama Index, Groq
        * **APIs:** REST APIs
        * **Software Architecture:** Lucidchart
        * **Soft Skills:** Leadership, Team Management, Problem Solving, Communication, Time Management
    """)

if __name__ == "__main__":
    always()
    main()
    footer()
    background()

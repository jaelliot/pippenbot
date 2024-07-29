# work_experiences.py
# don't remove the above comment

import streamlit as st
from tools.layout_utils import always
from tools.content_utils import footer
from tools.helpers import background
sss = st.session_state

def main():
    picoedge = "[PicoEdge](https://www.picoedge.com/)"
    parrot_health = "[Parrot Health](https://www.parrothealth.com/)"
    redapt = "[Redapt Inc.](https://www.redapt.com/)"
    kingstar = "[King Star Computers](https://www.kingstarcomputers.com/)"
    staples = "[Staples](https://www.staples.com/)"
    rosalind = "[ROSALIND](https://www.rosalind.com/)"

    header = st.empty()
    d_lines = {}
    job_tags = ['picoedge', 'parrot_health', 'redapt', 'kingstar', 'staples', 'rosalind']
    job_names = ['PicoEdge', 'Parrot Health', 'Redapt Inc.', 'King Star Computers', 'Staples', 'ROSALIND']
    
    containers = st.tabs(job_names) if sss['layout'] == "wide" else [st.container() for _ in job_names]
    
    for container, job_name in zip(containers, job_tags):
        title = container.empty()
        d_lines[job_name] = title, container.empty(), container.empty()
        if sss['layout'] != 'wide':
            container.write('---')
        
    header.header("Work Experience", anchor='work_experience', divider="orange")

    d_lines['picoedge'][0].write(f"#### DevOps Engineer, {picoedge}")
    d_lines['picoedge'][1].markdown("""
        **March 2020 - April 2024** / **Remote**
        * Ongoing maintenance of private cloud infrastructure
        * Ensuring zero downtime for mission-critical Linux and FreeBSD servers
        * Automating manual tasks with scripting languages (Python, Shell, Powershell, Ansible)
        * Providing 24/7 on-call support for critical systems
        * Effective implementation of FreeBSD for firewalls and server OS, Ubuntu Linux for machine learning, and wiki.js for documentation
    """)
    d_lines['picoedge'][2].expander('Technologies and Skills').write("""
        Linux · FreeBSD · Python · Shell · Powershell · Ansible · Automation · Cloud Infrastructure
    """)
    
    d_lines['parrot_health'][0].write(f"#### DevOps Engineer, {parrot_health}")
    d_lines['parrot_health'][1].markdown("""
        **April 2020 - October 2023** / **San Francisco Bay Area**
        * Managed and optimized Parrot Health's AWS infrastructure, focusing on server-less architecture through tools like AWS Lambda, DynamoDB, and API Gateway
        * Facilitated seamless integration of healthcare services on iOS and Android, employing agile methodologies
        * Implemented a containerization strategy with Docker, enhancing deployment efficiency and system reliability
        * Led cross-functional teams, guiding projects from initiation to deployment
    """)
    d_lines['parrot_health'][2].expander('Technologies and Skills').write("""
        AWS · Server-less Architecture · Docker · Agile Methodologies · Cross-functional Team Leadership
    """)
    
    d_lines['redapt'][0].write(f"#### Data Center Technician (Contract), {redapt}")
    d_lines['redapt'][1].markdown("""
        **May 2021 - October 2021** / **Redwood City, CA**
        * Obtained expertise and experience in RedHat Linux environments
        * Administered and addressed incidents with ServiceNow
        * Executed physical server builds in line with SOPs and QA standards to improve system performance
    """)
    d_lines['redapt'][2].expander('Technologies and Skills').write("""
        RedHat Linux · ServiceNow · Server Builds · Incident Management
    """)
    
    d_lines['kingstar'][0].write(f"#### Server Engineer (Contract), {kingstar}")
    d_lines['kingstar'][1].markdown("""
        **April 2019 - June 2019** / **Sunnyvale, CA**
        * Enhanced server performance by implementing optimized configurations and routine maintenance
        * Reduced downtime through proactive monitoring and timely resolution of server issues
        * Improved security measures with regular patch updates and vulnerability assessments
    """)
    d_lines['kingstar'][2].expander('Technologies and Skills').write("""
        Server Performance · Monitoring · Security Measures · Patch Updates · Vulnerability Assessments
    """)
    
    d_lines['staples'][0].write(f"#### Computer Technician, {staples}")
    d_lines['staples'][1].markdown("""
        **August 2017 - February 2019** / **Greater San Diego Area**
        * Responsible for repairing various customer electronics, including laptops, tablets, and both Apple and Android smartphones
        * Enhanced customer satisfaction by providing timely and efficient computer repair services
        * Assisted customers who required technical advice and direction
    """)
    d_lines['staples'][2].expander('Technologies and Skills').write("""
        Electronics Repair · Customer Service · Troubleshooting
    """)
    
    d_lines['rosalind'][0].write(f"#### Information Technology Infrastructure Specialist (Contract), {rosalind}")
    d_lines['rosalind'][1].markdown("""
        **September 2016 - July 2017** / **San Diego Metropolitan Area**
        * Carried out the automation of tasks and parsing of logs with Python, Bash, Docker, and Ansible
        * Aided and supported developers in developing solutions for program errors
        * Performed regular backups to prevent data loss
        * Leveraged Ubuntu Linux and VMware vCenter to perform virtual and physical infrastructure management
        * Effectively utilized DataDog to execute monitoring activities and resolve a wide range of software and hardware issues
    """)
    d_lines['rosalind'][2].expander('Technologies and Skills').write("""
        Python · Bash · Docker · Ansible · Automation · Backup Solutions · Ubuntu Linux · VMware vCenter · DataDog
    """)

if __name__ == "__main__":
    always()
    main()
    footer()
    background()

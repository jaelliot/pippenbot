# career_goals.py
# don't remove the above comment.

import streamlit as st
from tools.layout_utils import always
from tools.content_utils import footer
from tools.helpers import background
sss = st.session_state

def main():
    st.header("Career Goals", anchor='career_goals', divider="orange")
    st.markdown("""
    > **Finish Software Engineering Degree:**
    > I am dedicated to completing my software engineering degree to solidify my technical foundation and advance my career.

    > **Sell a Business:**
    > One of my goals is to successfully sell a business I have created, showcasing my entrepreneurial skills and business acumen.

    > **Publish a Patent:**
    > I aim to innovate and publish a patent, contributing to technological advancements and securing intellectual property.

    > **Hire for My Company:**
    > I aspire to grow my company and hire talented individuals, fostering a collaborative and dynamic work environment.

    > **Build Longview in Utah:**
    > I want to help build and establish Longview in Utah, contributing to its growth and success in the region.

    > **Set Up Tech Incubator at UVU:**
    > I am passionate about supporting the tech community and aim to help set up a tech incubator at Utah Valley University, nurturing future innovators.
    """)

if __name__ == "__main__":
    always()
    main()
    footer()
    background()

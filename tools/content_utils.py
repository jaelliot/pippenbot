# utils/content_utils.py

import streamlit as st
from tools.constant import info

contact = f"""
    :globe_with_meridians: [LinkedIn]({info['Social_Media']['LinkedIn']})  
    :email: [{info['Email']}](mailto:{info['Email']})   
    :earth_americas: [Utah Valley University](https://maps.app.goo.gl/bfAP9bXekxB31iXp7)  
"""

def footer():
    st.header("How to reach me?", anchor='contact', divider="orange")
    st.markdown("""
        The best way to contact me is by email.
    """)
    st.write(contact)

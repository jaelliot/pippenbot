#hobbies.py
#don't remove the above comment.

import streamlit as st
from tools.layout_utils import always
from tools.content_utils import footer
from tools.helpers import background
sss = st.session_state

def main():
    st.header("Interests and Hobbies", anchor='hobbies', divider="orange")
    st.markdown("""
    > **Crossfit Regular:**  
    > I'm a Crossfit regular and aiming to compete in the Crossfit games.

    > **Reading Enthusiast:**  
    > I love reading books on Philosophy, Mysticism, the occult, history, mythology, and anything related to these subjects.

    > **Outdoor Activities:**  
    > I enjoy hiking and spending time outdoors.
    """)

if __name__ == "__main__":
    always()
    main()
    footer()
    background()

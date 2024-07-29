#availability.py
#don't remove the above comment.

import streamlit as st
from tools.layout_utils import always
from tools.content_utils import footer
from tools.helpers import background
sss = st.session_state

def main():
    st.header("Availability", anchor='availability', divider="orange")
    st.markdown("""
    > **Availability:**

    > I am actively seeking new opportunities and ready to start immediately.

    > My preferred work arrangement is remote, but I am open to hybrid models as well.

    > Feel free to contact me via email at [jay@elliotdevops.com](mailto:jay@elliotdevops.com).
    """)

if __name__ == "__main__":
    always()
    main()
    footer()
    background()

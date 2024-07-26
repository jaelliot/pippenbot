import streamlit as st
import requests
from llama_index.core import VectorStoreIndex
from llama_index.readers.file import SimpleDirectoryReader
from PIL import Image
import json
from constant import info  # Assuming info is defined in constant.py
from models import MODELS

st.set_page_config(page_title='Template', layout="wide", page_icon='📄')

class DocumentQAApp:
    def __init__(self):
        self.groq_api_key = None
        self.headers = None
        self.documents = SimpleDirectoryReader(input_dir="resume").load_data()  # Changed to "resume" directory
        self.full_name = info['Full_Name']
        self.name = info["Name"]
        self.photo = info['Photo']
        self.intro = info["Intro"]
        self.about = info['About']
        self.email = info["Email"]

    @st.cache_data
    def read_document(self, uploaded_file):
        document = uploaded_file.read().decode()
        return document

    @st.cache_data
    def prepare_payload(self, document, question, model):
        messages = [
            {
                "role": "user",
                "content": f"Here's a document: {document} \n\n---\n\n {question}",
            }
        ]
        payload = {
            "model": model,
            "messages": messages
        }
        return payload

    @st.cache_data
    def send_request(self, url, headers, payload):
        response = requests.post(url, headers=headers, json=payload)
        return response

    def ask_bot(self, input_text):
        model = MODELS["LLaMA3 8b"]["model_id"]
        index = VectorStoreIndex.from_documents(self.documents)

        PROMPT_QUESTION = f"""You are an AI assistant dedicated to assisting {self.name} in job search by providing recruiters with relevant and concise information. 
        If you do not know the answer, politely admit it and let recruiters know how to contact {self.name} to get more information directly. 
        Human: {input_text}
        """
        
        output = index.as_query_engine().query(PROMPT_QUESTION)
        return output.response

    def get_text(self):
        input_text = st.text_input("Enter your questions and hit Enter to know more about me from my AI agent!", key="input")
        return input_text

    def load_css(self, file_name):
        with open(file_name) as f:
            st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

    def gradient(self, color1, color2, color3, content1, content2):
        st.markdown(f'<h1 style="text-align:center;background-image: linear-gradient(to right,{color1}, {color2});font-size:60px;border-radius:2%;">'
                    f'<span style="color:{color3};">{content1}</span><br>'
                    f'<span style="color:white;font-size:17px;">{content2}</span></h1>', 
                    unsafe_allow_html=True)

    def run(self):
        st.title("📄 Document question answering")
        st.write(
            "Upload a document below and ask a question about it and a LLamaBot will answer! "
            "To use this app, you need to provide a Groq API key, which you can get [here](https://groq.com/account/api-keys). "
        )

        self.groq_api_key = st.text_input("Groq API Key", type="password")
        if not self.groq_api_key:
            st.info("Please add your Groq API key to continue.", icon="🗝️")
        else:
            self.headers = {
                "Authorization": f"Bearer {self.groq_api_key}",
                "Content-Type": "application/json"
            }

            uploaded_file = st.file_uploader("Upload a document (.txt or .md)", type=("txt", "md"))

            question = st.text_area(
                "Now ask a question about the document!",
                placeholder="Can you give me a short summary?",
                disabled=not uploaded_file,
            )

            if uploaded_file and question:
                with st.spinner("Processing document..."):
                    document = self.read_document(uploaded_file)
                    payload = self.prepare_payload(document, question, MODELS["LLaMA3 8b"]["model_id"])
                    response = self.send_request("https://api.groq.com/openai/v1/chat/completions", self.headers, payload)

                    if response.status_code == 200:
                        answer = response.json()["choices"][0]["message"]["content"]
                        st.write(answer)
                    else:
                        st.error(f"Error: {response.status_code}, {response.text}")

                if st.button("Ask another question"):
                    st.experimental_rerun()

        st.sidebar.markdown(self.photo, unsafe_allow_html=True)
        self.load_css("styles/style.css")  # Changed to "styles/style.css"

        with st.container():
            col1, col2 = st.columns([8, 3])

        with col1:
            self.gradient('#FFD4DD', '#000395', 'e0fbfc', f"Hi, I'm {self.full_name}", self.intro)
            st.write("")
            st.write(self.about)
        
        st.subheader('Career Snapshot')
        with open('bio.txt', "r") as f:  # Changed to 'bio.txt'
            data = f.read()
        # Import timeline from streamlit_timeline
        from streamlit_timeline import timeline
        timeline(data, height=400)

        st.subheader("Contact Me")
        contact_form = f"""
        <form action="https://formsubmit.co/{self.email}" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="Your name" required>
            <input type="email" name="email" placeholder="Your email" required>
            <textarea name="message" placeholder="Your message here" required></textarea>
            <button type="submit">Send</button>
        </form>
        """
        st.markdown(contact_form, unsafe_allow_html=True)


if __name__ == "__main__":
    app = DocumentQAApp()
    app.run()

from langchain_google_genai import ChatGoogleGenerativeAI
from streamlit_lottie import st_lottie
import streamlit as st
import json

if "api_key" not in st.session_state:
    st.session_state.api_key = ''


# Function to load and display the lottie file
def display_lottiefile(filename):
    # Load the lottie file
    with open(filename, "r") as f:
        lottie_file = json.load(f)
    st_lottie(lottie_file, speed=1, reverse=False, loop=True, quality="high", height=150, width=300, key=None)


# Function to configure sidebar to verify and get the model  api key
def configure_apikey_sidebar():
    st.session_state.api_key = st.sidebar.text_input(f'Enter Google API Key', type='password',
                                                 help='Get Google API Key from: https://aistudio.google.com/app/apikey')
    if st.session_state.api_key == '':
        st.sidebar.warning('Enter the API key')
        app_unlock = False

    elif st.session_state.api_key.startswith('AI') and (len(st.session_state.api_key) == 39):
        st.sidebar.success(' Proceed!', icon='️👉')
        app_unlock = True
    else:
        st.sidebar.warning('Please enter the correct credentials!', icon='⚠️')
        app_unlock = False

    return app_unlock


def configure_about_sidebar():
    with st.sidebar.expander('Contact'):
        st.markdown(''' Any Queries: Contact [Zeeshan Altaf](mailto:zeeshan.altaf@gmail.com)''')
    with st.sidebar.expander('Source Code'):
        st.markdown(''' Source code: [GitHub](https://github.com/mzeeshanaltaf/crewai-agent-tech-chronicle-gemini)''')


def configure_llm():
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", verbose=True, temperature=0.5,
                                 google_api_key=st.session_state.api_key)

    return llm

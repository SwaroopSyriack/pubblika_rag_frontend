import streamlit as st
from chat import display_sidebar, display_chat_interface


st.title("Pubblika Chatbot")

# Initialize session state variables
if "messages" not in st.session_state:
    st.session_state.messages = []

if "session_id" not in st.session_state:
    st.session_state.session_id = None

# Display the chat interface
display_chat_interface()
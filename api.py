import requests
import streamlit as st

def get_api_response(question, session_id):
    headers = {'accept': 'application/json', 'Content-Type': 'application/json'}
    data = {"question": question}
    if session_id:
        data["session_id"] = session_id

    try:
        response = requests.post("https://pubblika-rag-backend.onrender.com", headers=headers, json=data)
        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"API request failed with status code {response.status_code}: {response.text}")
            return None
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        return None
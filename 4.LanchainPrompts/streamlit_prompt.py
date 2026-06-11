import streamlit as st
import requests

# Page setup
st.set_page_config(page_title="TinyLlama Chat", page_icon="🤖")
st.title("🤖 TinyLlama Local UI")

# FastAPI endpoint location (Change localhost to your VM's public/private IP if needed)
API_URL = "http://[IP_ADDRESS]:[PORT]/v1/chat"

# Initialize session state for message history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display persistent message history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input text box
if user_input := st.chat_input("Ask TinyLlama something..."):
    # Append and show user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Call FastAPI backend
    with st.chat_message("assistant"):
        status_placeholder = st.empty()
        status_placeholder.markdown("*Thinking...*")
        
        try:
            # Match the schema expected by the FastAPI backend
            payload = {"prompt": user_input}
            response = requests.post(API_URL, json=payload, timeout=30)
            
            if response.status_code == 200:
                reply = response.json().get("response", "No response text found.")
                status_placeholder.markdown(reply)
                st.session_state.messages.append({"role": "assistant", "content": reply})
            else:
                status_placeholder.markdown(f"⚠️ Error: API returned status {response.status_code}")
                
        except requests.exceptions.RequestException as e:
            status_placeholder.markdown(f"❌ Connection Error: Cannot reach backend at {API_URL}")

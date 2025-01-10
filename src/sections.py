import streamlit as st
import time
import os

from src.utils import load_json

env_variables = load_json("./env_variable.json")

@st.dialog(title="Welcome to Job tracker app")
def passcode_dialog():
    st.session_state.passcode = st.text_input("Enter passcode", type="password", max_chars=6)

    if st.button("Submit", type="primary", icon = "🎯"):
        if st.session_state.passcode == env_variables["app_passcode"]:
            #st.success("Correct passcode. Welcome to the app!")
            with st.spinner('Welcome! Loading job applications...'):
                time.sleep(1)
                st.session_state.correct_passcode = True
                st.rerun()
            
        else:
            st.error("Incorrect passcode. Please try again.")
    
    
    



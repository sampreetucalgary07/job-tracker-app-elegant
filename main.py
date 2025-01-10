import streamlit as st
# import os

from src.sections import passcode_dialog 
from src.job_tracker import job_tracker_page

if __name__ == "__main__":
    st.set_page_config(page_title="Job Appl. Tracker", layout="wide", menu_items={"Get help": "https://linkedin.com/in/sampreet-v-70b36b1a1" })
    if "correct_passcode" not in st.session_state:
        st.session_state.correct_passcode = False
       
    if st.session_state.correct_passcode == False:
        passcode_dialog()
    else:
        job_tracker_page()

    
    
        

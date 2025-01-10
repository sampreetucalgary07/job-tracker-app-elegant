import json
import streamlit as st

def load_json(file_path):
    with open(file_path, "r") as f:
        return json.load(f)

def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)



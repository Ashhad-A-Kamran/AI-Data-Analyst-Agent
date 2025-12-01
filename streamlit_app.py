import streamlit as st
import requests

uploaded_file = st.file_uploader("Upload your dataset")

if uploaded_file:
    files = {"file": (uploaded_file.name, uploaded_file, "application/octet-stream")}
    response = requests.post("http://127.0.0.1:8000/process-file", files=files)
    st.write(response.json())
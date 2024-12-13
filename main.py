import streamlit as st

def uploaderFile():
    uploadedFile = st.file_uploader("Escolha um arquivo", ['json'])

    if uploadedFile:
        
        stringJson = uploadedFile.getvalue().decode("utf-8")
        st.json(stringJson)


uploaderFile()
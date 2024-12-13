import streamlit as st
import json

def arquivoUploader():

    arquivo_uploaded = st.file_uploader("Escolha um arquivo", ['json'])

    if arquivo_uploaded:
        
        string_json = arquivo_uploaded.getvalue().decode("utf-8")
        dados_json = json.loads(string_json)
        return dados_json
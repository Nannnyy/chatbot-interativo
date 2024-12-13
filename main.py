import streamlit as st
import json
from models.pergunta import Pergunta

def arquivoUploader():
    arquivo_uploaded = st.file_uploader("Escolha um arquivo", ['json'])

    if arquivo_uploaded:
        
        string_json = arquivo_uploaded.getvalue().decode("utf-8")
        dados_json = json.loads(string_json)
        st.json(dados_json)
        return dados_json

def construirListaPerguntas(dicionario_json):
    perguntas = [Pergunta(
        pergunta['id'],
        pergunta['texto'],
        pergunta['tipo'],
        pergunta['resposta_correta']
    ) for pergunta in dicionario_json['perguntas']]

    for pergunta in perguntas:
        st.write(pergunta)

dicionario_json = arquivoUploader()
construirListaPerguntas(dicionario_json)
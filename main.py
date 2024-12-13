import streamlit as st
import json

from models.pergunta import Pergunta
from fila.fila import Fila
from fila.no import No

def arquivoUploader():
    arquivo_uploaded = st.file_uploader("Escolha um arquivo", ['json'])

    if arquivo_uploaded:
        
        string_json = arquivo_uploaded.getvalue().decode("utf-8")
        dados_json = json.loads(string_json)
        st.write(string_json)

        #imprimir o json
        st.json(dados_json)
        return dados_json

def construirListaPerguntas(dicionario_json):
    perguntas = [Pergunta(
        pergunta['id'],
        pergunta['texto'],
        pergunta['tipo'],
        pergunta['resposta_correta'],
        pergunta.get('opcoes', None)
    ) for pergunta in dicionario_json['perguntas']]

    return perguntas

def adicionarPerguntasNaFila(lista_perguntas):
    fila = Fila()

    for pergunta in lista_perguntas:
        fila.enfileirar(No(pergunta))
    fila.imprimirFila()


dicionario_json = arquivoUploader()
if dicionario_json:
    lista_perguntas = construirListaPerguntas(dicionario_json)
    adicionarPerguntasNaFila(lista_perguntas)
else:
    st.write("Arquivo ainda não carregado")
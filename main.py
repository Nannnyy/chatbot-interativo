import streamlit as st

from utils.arquivoUploader import arquivoUploader
from utils.construtorPergunta import construirListaPerguntas
from utils.gerenciadorDeFila import *


from fila.fila import Fila

def main():

    st.title("Bem-vindo ao Chatbot 🤖")
    st.markdown("Instruções")

    dicionario_json = arquivoUploader()

    if dicionario_json:

        lista_perguntas = construirListaPerguntas(dicionario_json)
        fila = adicionarPerguntasNaFila(Fila(), lista_perguntas)
        
        for i in range(fila.getTamanho()):

            pergunta = getPergunta(fila)
            gerarPergunta(pergunta)

if __name__ == '__main__':
    main()
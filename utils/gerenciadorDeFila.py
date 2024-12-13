import streamlit as st

from fila.no import No
from .verificar_resposta import verificarResposta

def adicionarPerguntasNaFila(fila, lista_perguntas):
    for pergunta in lista_perguntas:
        fila.enfileirar(No(pergunta))
    return fila

def getPergunta(fila):
    no = fila.desenfileirar()
    pergunta = no.getValor()
    return pergunta

def gerarPergunta(pergunta):

    with st.chat_message("assistant"):

        st.write(f"Questão {pergunta.getId()}")
        st.write(pergunta.getTexto())
        resposta = st.chat_input("Digite a sua resposta", key=str(pergunta.getId()))
        
        if resposta: 
            correta = verificarResposta(resposta, pergunta.getRespostaCorreta())

            if correta:
                st.success("Correto!")
            else:
                st.error("Incorreto!")
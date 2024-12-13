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
    pergunta_id = pergunta.getId()

    if f"status_question_{pergunta_id}" not in st.session_state:
        st.session_state[f"status_question_{pergunta_id}"] = None

    with st.chat_message("assistant"):

        st.write(f"Questão {pergunta_id}")
        st.write(pergunta.getTexto())
        resposta = st.chat_input("Digite a sua resposta", key=str(pergunta.getId()))
        
        if resposta: 
            correta = verificarResposta(resposta, pergunta.getRespostaCorreta())

            if correta:
                st.session_state[f"status_question_{pergunta_id}"] = "Correto"
            else:
                st.session_state[f"status_question_{pergunta_id}"] = "Errado"
            
        if st.session_state[f"status_question_{pergunta_id}"] == "Correto":
            st.success("Correto!")
        elif st.session_state[f"status_question_{pergunta_id}"] == "Errado":
            st.error("Errado!")
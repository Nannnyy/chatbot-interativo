import streamlit as st

from .removerAcento import removerAcentos

def verificarResposta(resposta, pergunta):

    if removerAcentos(resposta.lower()) == removerAcentos(pergunta.lower()):
        return True
    return False

import streamlit as st

from utils.arquivoUploader import arquivoUploader
from utils.construtorPergunta import construirListaPerguntas
from utils.gerenciadorDeFila import adicionarPerguntasNaFila
from fila.fila import Fila

def main():
    dicionario_json = arquivoUploader()

    if dicionario_json:

        lista_perguntas = construirListaPerguntas(dicionario_json)

        fila = adicionarPerguntasNaFila(Fila(), lista_perguntas)
        
        fila.imprimirFila()

    else:
        st.write("Arquivo ainda não carregado")


if __name__ == '__main__':
    main()
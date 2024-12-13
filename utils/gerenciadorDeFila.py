from fila.no import No

def adicionarPerguntasNaFila(fila, lista_perguntas):
    for pergunta in lista_perguntas:
        fila.enfileirar(No(pergunta))
    return fila 
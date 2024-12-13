from .no import No

class Fila:

    def __init__(self):
        self.tamanho = 0
        self.inicio = None
        self.fim = None

    def adicionarPerguntasNaFila(self, lista_perguntas):
        for pergunta in lista_perguntas:
            self.enfileirar(No(pergunta))

    def getTamanho(self):
        return self.tamanho

    def verificarVazia(self):
        return (self.tamanho == 0)
    
    def enfileirar(self, no):
        if self.verificarVazia():
            self.inicio = no
            self.fim = no
        else:
            self.fim.setProximo(no)
            self.fim = no
        self.tamanho += 1
    
    def desenfileirar(self):
        if self.verificarVazia():
            return None

        antigoInicio = self.inicio
        self.inicio = antigoInicio.getProximo()
        self.tamanho -= 1
        return antigoInicio

    def getCabeca(self):
        return self.inicio

    # def imprimirFila(self):
    #     no = self.inicio
    #     print("Início -> ", end='')
    #     while(no is not None):
    #         print(f"{no.getValor()}")
    #         no = no.getProximo()
    #     print("Fim")
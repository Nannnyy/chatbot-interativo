class Pergunta:
     
    def __init__(self, id, texto, tipo, resposta_correta):
        self.id = id
        self.texto = texto
        self.tipo = tipo
        self.resposta_correta = resposta_correta
    
    def __repr__(self):
        return f"(id: {self.id}, texto: {self.texto}, tipo: {self.tipo}, resposta correta: {self.resposta_correta})"

    def getId(self):
        return self.id

    def getTexto(self):
        return self.texto

    def getTipo(self):
        return self.tipo
    
    def getRespostaCorreta(self):
        return self.resposta_correta
    

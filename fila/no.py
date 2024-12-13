class No:

    def __init__(self, valor, proximo=None):
        self.valor = valor
        self.proximo = proximo
    
    def __str__(self):
        return self.valor

    def getValor(self):
        return self.valor
    
    def setValor(self, valor):
        self.valor = valor
    
    def getProximo(self):
        return self.proximo
    
    def setProximo(self, proximo):
        self.proximo = proximo

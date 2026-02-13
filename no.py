class No:
    def __init__(self, palavra, linha):
        self.palavra = palavra
        self.linhas = [linha]
        self.esquerda = None
        self.direita = None
        self.altura = 1
class Memoria:

    def __init__(self,tamanho,ocupado):
        self.tamanho = tamanho
        self.ocupado = ocupado

    def updateOcupado(self,up):
        self.ocupado = self.ocupado + up
        return self.ocupado

    def getOcupado(self):
        return self.ocupado



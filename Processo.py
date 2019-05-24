class Processo:


    def setCod(self,cod):
        self.cod = cod

    def getCod(self):
        return self.cod

    def setTamanho(self,tamanho):
        self.tamanho = tamanho

    def getTamanho(self):
        return self.tamanho

    def setPrioridade(self,prioridade):
        self.prioridade = prioridade

    def getPrioridade(self):
        return self.prioridade

    def setTempoDeChegada(self,t):
        self.t = t

    def getTempoDeChegada(self):
        return self.t

    def bubblesort(self,lista):
        elementos = len(lista) - 1
        ordenado = False
        while not ordenado:
            ordenado = True
            for i in range(elementos):
                if lista[i][3] > lista[i + 1][3]:
                    lista[i], lista[i + 1] = lista[i + 1], lista[i]
                    ordenado = False
        return lista
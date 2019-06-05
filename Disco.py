class Disco:

    def swap(self,lista,cod,tamanho,prioridade,tempo,p):
        p.setCod(cod)
        p.setTamanho(tamanho)
        p.setPrioridade(prioridade)
        p.setTempoDeChegada(tempo)
        lista.append(p)
        return lista

    def setDisco(self,lista):
        self.lista = lista

    def getDisco(self):
        return self.lista

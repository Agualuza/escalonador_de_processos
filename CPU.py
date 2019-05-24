class CPU:

    def __init__(self,ocupado,freq):
        self.ocupado = ocupado
        self.tempoProcesso = 0
        self.freq = freq

    def getFreq(self):
        return self.freq

    def setOcupado(self,ocupado):
        self.ocupado = ocupado

    def getOcupado(self):
        return self.ocupado

    def setProcesso(self,processo):
        self.processo = processo

    def getProcesso(self):
        return self.processo

    def setTempoProcesso(self, tempoProcesso):
        self.tempoProcesso = tempoProcesso

    def getTempoProcesso(self):
        return self.tempoProcesso
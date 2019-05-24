from CPU import *
from Disco import *
from Memoria import *
from Processo import *
from TimerContinuo import *


p = []
processo = []
fila_geral = []
fila_ftr = []
fila1 = []
fila2 = []
fila3 = []
tempo = 0
contador = -1
c1 = -1
c2 = -1
c3 = -1
prioridadeMaiorQueZero = False

cpu1 = CPU(False,2)
cpu2 = CPU(False,4)
cpu3 = CPU(False,8)
cpu4 = CPU(False,16)
mem = Memoria(16000,0)
fim = False

def clock():
    global tempo
    global contador
    global c1
    global c2
    global c3
    global prioridadeMaiorQueZero
    print("len: ",len(fila_ftr))
    if contador+1 <= len(fila_ftr)-1:
        if fila_ftr[contador+1][3]-1 <= tempo:
            contador = contador + 1
        prioridadeMaiorQueZero = False
    else:
        prioridadeMaiorQueZero = True

    if not prioridadeMaiorQueZero:
        if contador > -1:
            if len(fila_ftr) > 0:
                if not cpu1.getOcupado():
                    if tempo < fila_ftr[contador][3] + (fila_ftr[contador][1]/cpu1.getFreq()):
                        cpu1.setOcupado(True)
                        cpu1.setTempoProcesso(fila_ftr[contador][3]+(fila_ftr[contador][1]/cpu1.getFreq()))
                        fila_ftr.pop(contador)
                elif not cpu2.getOcupado():
                    if tempo < fila_ftr[contador][3] + (fila_ftr[contador][1]/cpu2.getFreq()):
                        cpu2.setOcupado(True)
                        cpu2.setTempoProcesso(fila_ftr[contador][3] + (fila_ftr[contador][1]/cpu2.getFreq()))
                        fila_ftr.pop(contador)
                elif not cpu3.getOcupado():
                    if tempo < fila_ftr[contador][3] + (fila_ftr[contador][1]/cpu3.getFreq()):
                        fila_ftr.pop(contador)
                        cpu3.setOcupado(True)
                        cpu3.setTempoProcesso(fila_ftr[contador][3] + (fila_ftr[contador][1]/cpu3.getFreq()))
                        fila_ftr.pop(contador)
                elif not cpu4.getOcupado():
                    if tempo < fila_ftr[contador][3] + (fila_ftr[contador][1]/cpu4.getFreq()):
                        fila_ftr.pop(contador)
                        cpu4.setOcupado(True)
                        cpu4.setTempoProcesso(fila_ftr[contador][3] + (fila_ftr[contador][1]/cpu4.getFreq()))
                        fila_ftr.pop(contador)
        if cpu1.getTempoProcesso() <= tempo:
            cpu1.setOcupado(False)
            cpu1.setTempoProcesso(0)
        if cpu2.getTempoProcesso() <= tempo:
            cpu2.setOcupado(False)
            cpu2.setTempoProcesso(0)
        if cpu3.getTempoProcesso() <= tempo:
            cpu3.setOcupado(False)
            cpu3.setTempoProcesso(0)
        if cpu4.getTempoProcesso() <= tempo:
            cpu4.setOcupado(False)
            cpu4.setTempoProcesso(0)
    else:
        if c1+1 <= len(fila1)-1:
            if fila1[c1 + 1][3] - 1 <= tempo:
                c1 = c1 + 1
        else:
            if prioridadeMaiorQueZero:
                t.cancel()
        if c1 > -1:
            if not cpu1.getOcupado():
                if tempo < fila1[c1][3] + (fila1[c1][1]/cpu1.getFreq()):
                    cpu1.setOcupado(True)
                    cpu1.setTempoProcesso(fila1[c1][3]+(fila1[c1][1]/cpu1.getFreq()))
                    fila1.pop(c1)
            elif not cpu2.getOcupado():
                if tempo < fila1[c1][3] + (fila1[c1][1]/cpu2.getFreq()):
                    cpu2.setOcupado(True)
                    cpu2.setTempoProcesso(fila1[c1][3] + (fila1[c1][1]/cpu2.getFreq()))
                    fila1.pop(c1)
            elif not cpu3.getOcupado():
                if tempo < fila1[c1][3] + (fila1[c1][1]/cpu3.getFreq()):
                    cpu3.setOcupado(True)
                    cpu3.setTempoProcesso(fila1[c1][3] + (fila1[c1][1]/cpu3.getFreq()))
                    fila1.pop(c1)
            elif not cpu4.getOcupado():
                if tempo < fila1[c1][3] + (fila1[c1][1]/cpu4.getFreq()):
                    cpu4.setOcupado(True)
                    cpu4.setTempoProcesso(fila1[c1][3] + (fila1[c1][1]/cpu4.getFreq()))
                    fila1.pop(c1)
            if cpu1.getTempoProcesso() <= tempo:
                cpu1.setOcupado(False)
                cpu1.setTempoProcesso(0)
                fila2.append(fila1[c1])
            if cpu2.getTempoProcesso() <= tempo:
                cpu2.setOcupado(False)
                cpu2.setTempoProcesso(0)
                fila2.append(fila1[c1])
            if cpu3.getTempoProcesso() <= tempo:
                cpu3.setOcupado(False)
                cpu3.setTempoProcesso(0)
                fila2.append(fila1[c1])
            if cpu4.getTempoProcesso() <= tempo:
                cpu4.setOcupado(False)
                cpu4.setTempoProcesso(0)
                fila2.append(fila1[c1])

    tempo = tempo + 1
    for i in fila_ftr:
        print("ftr ", i)
    for i in fila1:
        print("fila 1", i)
    for i in fila2:
        print("fila 2", i)
    print(tempo,": ",cpu1.getOcupado(),cpu2.getOcupado(),cpu3.getOcupado(),cpu4.getOcupado())

n_processo = int(input("Entre com o número de processos a serem submetidos: "))

for i in range (n_processo):
    linha = []
    for j in range (1):
        linha.append(i)
        linha.append(int(input("entre com o tamanho do processo " + str(i) + ": ")))
        linha.append(int(input("entre com a prioridade do processo " + str(i) + ": ")))
        linha.append(int(input("entre com o tempo de chegada do processo " + str(i) + ": ")))
    p.append(linha)

for i in range (n_processo):
    np = Processo()
    processo.append(np)
    processo[i].setCod(p[i][0])
    processo[i].setTamanho(p[i][1])
    processo[i].setPrioridade(p[i][2])
    processo[i].setTempoDeChegada(p[i][3])


pord = processo[0].bubblesort(p)

for i in pord:
    fila_geral.append(i)

for i in fila_geral:
    if i[2] == 0:
        fila_ftr.append(i)
    else:
        fila1.append(i)

t = TimerContinuo(1.0,clock)
t.start()



t = TimerContinuo(1.0,clock)
t.start()







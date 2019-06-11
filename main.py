from CPU import *
from Disco import *
from Memoria import *
from Processo import *
from Impressora import *
from TimerContinuo import *
from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *


#declaracao de variaveis globais
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
pop1, pop2, pop3, pop4 = [], [], [], []
po1, po2, po3, po4 = [], [], [], []
p1, p2, p3, p4 = [], [], [], []
listaDisco = []
pp1, pp2, pp3, pp4 = [], [], [], []

q1, q2, q3, q4 = 0, 0, 0, 0
min1, min2, min3 = 99999, 99999, 99999

prioridadeMaiorQueZero = False

temp1 = 0
temp2 = 0
temp3 = 0
temp4 = 0

janela = Window(950, 600)
janela.set_background_color((255, 255, 255))
barra = []

listaDisco = []
disco = Disco(False, listaDisco)

ocpu1 = Sprite("img/cpu_ocupado.png")
ocpu2 = Sprite("img/cpu_ocupado.png")
ocpu3 = Sprite("img/cpu_ocupado.png")
ocpu4 = Sprite("img/cpu_ocupado.png")
fcpu1 = Sprite("img/cpu_livre.png")
fcpu2 = Sprite("img/cpu_livre.png")
fcpu3 = Sprite("img/cpu_livre.png")
fcpu4 = Sprite("img/cpu_livre.png")

oimpressora1 = Sprite("img/impressora_ocupada.png")
oimpressora2 = Sprite("img/impressora_ocupada.png")
fimpressora1 = Sprite("img/impressora_livre.png")
fimpressora2 = Sprite("img/impressora_livre.png")
odisco1 = Sprite("img/disco_ocupado.png")
odisco2 = Sprite("img/disco_ocupado.png")
fdisco1 = Sprite("img/disco_livre.png")
fdisco2 = Sprite("img/disco_livre.png")

fundo = Sprite("img/fundo.jpg")

ocpu1.set_position(330, 60)
ocpu2.set_position(400, 60)
ocpu3.set_position(470, 60)
ocpu4.set_position(540, 60)
fcpu1.set_position(330, 60)
fcpu2.set_position(400, 60)
fcpu3.set_position(470, 60)
fcpu4.set_position(540, 60)
oimpressora1.set_position(330, 140)
oimpressora2.set_position(400, 140)
fimpressora1.set_position(330, 140)
fimpressora2.set_position(400, 140)
odisco1.set_position(470, 140)
odisco2.set_position(540, 140)
fdisco1.set_position(470, 140)
fdisco2.set_position(540, 140)

ocpu1.hide()
ocpu2.hide()
ocpu3.hide()
ocpu4.hide()
oimpressora1.hide()
oimpressora2.hide()
odisco1.hide()
odisco2.hide()

cpu1 = CPU(False, 2)
cpu2 = CPU(False, 2)
cpu3 = CPU(False, 2)
cpu4 = CPU(False, 2)
mem = Memoria(16000, 0)
recursoImpressora1 = Impressora(False)
recursoImpressora2 = Impressora(False)
recursoDisco1 = Disco(False, listaDisco)
recursoDisco2 = Disco(False, listaDisco)
fim = False

#funcao principal
def clock():
    global tempo
    global contador #posicao na fila ftr
    global c1 #posicao na fila1
    global c2 #posicao na fila2
    global c3 #posicao na fila3
    global prioridadeMaiorQueZero
    global po1, po2, po3, po4, p1, p2, p3, p4, pop1, pop2, pop3, pop4 #processo retirado da fila (pop - fila1,po - fila2,p - fila 3, numero é o numero da cpu)

    global min1, min2, min3
    global q1, q2, q3, q4
    global pp1, pp2, pp3, pp4

    #verifica se tem processos na fila ftr
    if contador + 1 <= len(fila_ftr) - 1:
        if fila_ftr[contador + 1][3] - 1 <= tempo:
            contador = contador + 1
        prioridadeMaiorQueZero = False
    else:
        prioridadeMaiorQueZero = True

    print("Prioridade ", prioridadeMaiorQueZero)
    #se tiver elemento na fila ftr
    if not prioridadeMaiorQueZero:
        if contador > -1:
            if len(fila_ftr) > 0:
                #verifica cpu por cpu até encontrar uma livre
                #se a cpu nao tiver ocupada
                #verifica se o processo precisa da impressora e/ou disco
                #se tiver os rescursos disponiveis seta cpu e recursos utilizados como ocupados
                #salva o processo em uma variavel e o retira da lista
                #decrementa o contador
                if not cpu1.getOcupado():
                    if fila_ftr[contador][5] == 1 and fila_ftr[contador][6] == 1:
                        if not recursoImpressora1.getStatus() and not recursoDisco1.getStatus():
                            recursoDisco1.setStatus(True)
                            recursoImpressora1.setStatus(True)
                            cpu1.setOcupado(True)
                            cpu1.setTempoProcesso(tempo + (fila_ftr[contador][4]))
                            mem.updateOcupado(-fila_ftr[contador][1])
                            pp1 = fila_ftr.pop(contador)
                            contador = contador - 1
                        elif not recursoImpressora2.getStatus() and not recursoDisco1.getStatus():
                            recursoDisco1.setStatus(True)
                            recursoImpressora2.setStatus(True)
                            cpu1.setOcupado(True)
                            cpu1.setTempoProcesso(tempo + (fila_ftr[contador][4]))
                            mem.updateOcupado(-fila_ftr[contador][1])
                            pp1 = fila_ftr.pop(contador)
                            contador = contador - 1
                        elif not recursoImpressora1.getStatus() and not recursoDisco2.getStatus():
                            recursoDisco2.setStatus(True)
                            recursoImpressora1.setStatus(True)
                            cpu1.setOcupado(True)
                            cpu1.setTempoProcesso(tempo + (fila_ftr[contador][4]))
                            mem.updateOcupado(-fila_ftr[contador][1])
                            pp1 = fila_ftr.pop(contador)
                            contador = contador - 1
                        elif not recursoImpressora2.getStatus() and not recursoDisco2.getStatus():
                            recursoDisco1.setStatus(True)
                            recursoImpressora2.setStatus(True)
                            cpu1.setOcupado(True)
                            cpu1.setTempoProcesso(tempo + (fila_ftr[contador][4]))
                            mem.updateOcupado(-fila_ftr[contador][1])
                            pp1 = fila_ftr.pop(contador)
                            contador = contador - 1
                    elif fila_ftr[contador][5] == 1:
                        if not recursoImpressora1.getStatus():
                            recursoImpressora1.setStatus(True)
                            cpu1.setOcupado(True)
                            cpu1.setTempoProcesso(tempo + (fila_ftr[contador][4]))
                            mem.updateOcupado(-fila_ftr[contador][1])
                            pp1 = fila_ftr.pop(contador)
                            contador = contador - 1
                        elif not recursoImpressora2.getStatus():
                            recursoImpressora2.setStatus(True)
                            cpu1.setOcupado(True)
                            cpu1.setTempoProcesso(tempo + (fila_ftr[contador][4]))
                            mem.updateOcupado(-fila_ftr[contador][1])
                            pp1 = fila_ftr.pop(contador)
                            contador = contador - 1
                    elif fila_ftr[contador][6] == 1:
                        if not recursoDisco1.getStatus():
                            recursoDisco1.setStatus(True)
                            cpu1.setOcupado(True)
                            cpu1.setTempoProcesso(tempo + (fila_ftr[contador][4]))
                            mem.updateOcupado(-fila_ftr[contador][1])
                            pp1 = fila_ftr.pop(contador)
                            contador = contador - 1
                        elif not recursoDisco2.getStatus():
                            recursoDisco2.setStatus(True)
                            cpu1.setOcupado(True)
                            cpu1.setTempoProcesso(tempo + (fila_ftr[contador][4]))
                            mem.updateOcupado(-fila_ftr[contador][1])
                            pp1 = fila_ftr.pop(contador)
                            contador = contador - 1

                    else:
                        cpu1.setOcupado(True)
                        cpu1.setTempoProcesso(tempo + (fila_ftr[contador][4]))
                        mem.updateOcupado(-fila_ftr[contador][1])
                        pp1 = fila_ftr.pop(contador)
                        contador = contador - 1
                elif not cpu2.getOcupado():
                    if fila_ftr[contador][5] == 1 and fila_ftr[contador][6] == 1:
                        if not recursoImpressora1.getStatus() and not recursoDisco1.getStatus():
                            recursoDisco1.setStatus(True)
                            recursoImpressora1.setStatus(True)
                            cpu2.setOcupado(True)
                            cpu2.setTempoProcesso(tempo + (fila_ftr[contador][4]))
                            mem.updateOcupado(-fila_ftr[contador][1])
                            pp2 = fila_ftr.pop(contador)
                            contador = contador - 1
                        elif not recursoImpressora2.getStatus() and not recursoDisco1.getStatus():
                            recursoDisco1.setStatus(True)
                            recursoImpressora2.setStatus(True)
                            cpu2.setOcupado(True)
                            cpu2.setTempoProcesso(tempo + (fila_ftr[contador][4]))
                            mem.updateOcupado(-fila_ftr[contador][1])
                            pp2 = fila_ftr.pop(contador)
                            contador = contador - 1
                        elif not recursoImpressora1.getStatus() and not recursoDisco2.getStatus():
                            recursoDisco2.setStatus(True)
                            recursoImpressora1.setStatus(True)
                            cpu2.setOcupado(True)
                            cpu2.setTempoProcesso(tempo + (fila_ftr[contador][4]))
                            mem.updateOcupado(-fila_ftr[contador][1])
                            pp2 = fila_ftr.pop(contador)
                            contador = contador - 1
                        elif not recursoImpressora2.getStatus() and not recursoDisco2.getStatus():
                            recursoDisco1.setStatus(True)
                            recursoImpressora2.setStatus(True)
                            cpu2.setOcupado(True)
                            cpu2.setTempoProcesso(tempo + (fila_ftr[contador][4]))
                            mem.updateOcupado(-fila_ftr[contador][1])
                            pp2 = fila_ftr.pop(contador)
                            contador = contador - 1
                    elif fila_ftr[contador][5] == 1:
                        if not recursoImpressora1.getStatus():
                            recursoImpressora1.setStatus(True)
                            cpu2.setOcupado(True)
                            cpu2.setTempoProcesso(tempo + (fila_ftr[contador][4]))
                            mem.updateOcupado(-fila_ftr[contador][1])
                            pp2 = fila_ftr.pop(contador)
                            contador = contador - 1
                        elif not recursoImpressora2.getStatus():
                            recursoImpressora2.setStatus(True)
                            cpu2.setOcupado(True)
                            cpu2.setTempoProcesso(tempo + (fila_ftr[contador][4]))
                            mem.updateOcupado(-fila_ftr[contador][1])
                            pp2 = fila_ftr.pop(contador)
                            contador = contador - 1
                    elif fila_ftr[contador][6] == 1:
                        if not recursoDisco1.getStatus():
                            recursoDisco1.setStatus(True)
                            cpu2.setOcupado(True)
                            cpu2.setTempoProcesso(tempo + (fila_ftr[contador][4]))
                            mem.updateOcupado(-fila_ftr[contador][1])
                            pp2 = fila_ftr.pop(contador)
                            contador = contador - 1
                        elif not recursoDisco2.getStatus():
                            recursoDisco2.setStatus(True)
                            cpu2.setOcupado(True)
                            cpu2.setTempoProcesso(tempo + (fila_ftr[contador][4]))
                            mem.updateOcupado(-fila_ftr[contador][1])
                            pp2 = fila_ftr.pop(contador)
                            contador = contador - 1

                    else:
                        cpu2.setOcupado(True)
                        cpu2.setTempoProcesso(tempo + (fila_ftr[contador][4]))
                        mem.updateOcupado(-fila_ftr[contador][1])
                        pp2 = fila_ftr.pop(contador)
                        contador = contador - 1
                elif not cpu3.getOcupado():

                    if fila_ftr[contador][5] == 1 and fila_ftr[contador][6] == 1:
                        if not recursoImpressora1.getStatus() and not recursoDisco1.getStatus():
                            recursoDisco1.setStatus(True)
                            recursoImpressora1.setStatus(True)
                            cpu3.setOcupado(True)
                            cpu3.setTempoProcesso(tempo + (fila_ftr[contador][4]))
                            mem.updateOcupado(-fila_ftr[contador][1])
                            pp3 = fila_ftr.pop(contador)
                            contador = contador - 1
                        elif not recursoImpressora2.getStatus() and not recursoDisco1.getStatus():
                            recursoDisco1.setStatus(True)
                            recursoImpressora2.setStatus(True)
                            cpu3.setOcupado(True)
                            cpu3.setTempoProcesso(tempo + (fila_ftr[contador][4]))
                            mem.updateOcupado(-fila_ftr[contador][1])
                            pp3 = fila_ftr.pop(contador)
                            contador = contador - 1
                        elif not recursoImpressora1.getStatus() and not recursoDisco2.getStatus():
                            recursoDisco2.setStatus(True)
                            recursoImpressora1.setStatus(True)
                            cpu3.setOcupado(True)
                            cpu3.setTempoProcesso(tempo + (fila_ftr[contador][4]))
                            mem.updateOcupado(-fila_ftr[contador][1])
                            pp3 = fila_ftr.pop(contador)
                            contador = contador - 1
                        elif not recursoImpressora2.getStatus() and not recursoDisco2.getStatus():
                            recursoDisco1.setStatus(True)
                            recursoImpressora2.setStatus(True)
                            cpu3.setOcupado(True)
                            cpu3.setTempoProcesso(tempo + (fila_ftr[contador][4]))
                            mem.updateOcupado(-fila_ftr[contador][1])
                            pp3 = fila_ftr.pop(contador)
                            contador = contador - 1
                    elif fila_ftr[contador][5] == 1:
                        if not recursoImpressora1.getStatus():
                            recursoImpressora1.setStatus(True)
                            cpu3.setOcupado(True)
                            cpu3.setTempoProcesso(tempo + (fila_ftr[contador][4]))
                            mem.updateOcupado(-fila_ftr[contador][1])
                            pp3 = fila_ftr.pop(contador)
                            contador = contador - 1
                        elif not recursoImpressora2.getStatus():
                            recursoImpressora2.setStatus(True)
                            cpu3.setOcupado(True)
                            cpu3.setTempoProcesso(tempo + (fila_ftr[contador][4]))
                            mem.updateOcupado(-fila_ftr[contador][1])
                            pp3 = fila_ftr.pop(contador)
                            contador = contador - 1
                    elif fila_ftr[contador][6] == 1:
                        if not recursoDisco1.getStatus():
                            recursoDisco1.setStatus(True)
                            cpu3.setOcupado(True)
                            cpu3.setTempoProcesso(tempo + (fila_ftr[contador][4]))
                            mem.updateOcupado(-fila_ftr[contador][1])
                            pp3 = fila_ftr.pop(contador)
                            contador = contador - 1
                        elif not recursoDisco2.getStatus():
                            recursoDisco2.setStatus(True)
                            cpu3.setOcupado(True)
                            cpu3.setTempoProcesso(tempo + (fila_ftr[contador][4]))
                            mem.updateOcupado(-fila_ftr[contador][1])
                            pp3 = fila_ftr.pop(contador)
                            contador = contador - 1

                    else:
                        cpu3.setOcupado(True)
                        cpu3.setTempoProcesso(tempo + (fila_ftr[contador][4]))
                        mem.updateOcupado(-fila_ftr[contador][1])
                        pp3 = fila_ftr.pop(contador)
                        contador = contador - 1
                elif not cpu4.getOcupado():
                    if fila_ftr[contador][5] == 1 and fila_ftr[contador][6] == 1:
                        if not recursoImpressora1.getStatus() and not recursoDisco1.getStatus():
                            recursoDisco1.setStatus(True)
                            recursoImpressora1.setStatus(True)
                            cpu4.setOcupado(True)
                            cpu4.setTempoProcesso(tempo + (fila_ftr[contador][4]))
                            mem.updateOcupado(-fila_ftr[contador][1])
                            pp4 = fila_ftr.pop(contador)
                            contador = contador - 1
                        elif not recursoImpressora2.getStatus() and not recursoDisco1.getStatus():
                            recursoDisco1.setStatus(True)
                            recursoImpressora2.setStatus(True)
                            cpu4.setOcupado(True)
                            cpu4.setTempoProcesso(tempo + (fila_ftr[contador][4]))
                            mem.updateOcupado(-fila_ftr[contador][1])
                            pp4 = fila_ftr.pop(contador)
                            contador = contador - 1
                        elif not recursoImpressora1.getStatus() and not recursoDisco2.getStatus():
                            recursoDisco2.setStatus(True)
                            recursoImpressora1.setStatus(True)
                            cpu4.setOcupado(True)
                            cpu4.setTempoProcesso(tempo + (fila_ftr[contador][4]))
                            mem.updateOcupado(-fila_ftr[contador][1])
                            pp4 = fila_ftr.pop(contador)
                            contador = contador - 1
                        elif not recursoImpressora2.getStatus() and not recursoDisco2.getStatus():
                            recursoDisco1.setStatus(True)
                            recursoImpressora2.setStatus(True)
                            cpu4.setOcupado(True)
                            cpu4.setTempoProcesso(tempo + (fila_ftr[contador][4]))
                            mem.updateOcupado(-fila_ftr[contador][1])
                            pp4 = fila_ftr.pop(contador)
                            contador = contador - 1
                    elif fila_ftr[contador][5] == 1:
                        if not recursoImpressora1.getStatus():
                            recursoImpressora1.setStatus(True)
                            cpu4.setOcupado(True)
                            cpu4.setTempoProcesso(tempo + (fila_ftr[contador][4]))
                            mem.updateOcupado(-fila_ftr[contador][1])
                            pp4 = fila_ftr.pop(contador)
                            contador = contador - 1
                        elif not recursoImpressora2.getStatus():
                            recursoImpressora2.setStatus(True)
                            cpu4.setOcupado(True)
                            cpu4.setTempoProcesso(tempo + (fila_ftr[contador][4]))
                            mem.updateOcupado(-fila_ftr[contador][1])
                            pp4 = fila_ftr.pop(contador)
                            contador = contador - 1
                    elif fila_ftr[contador][6] == 1:
                        if not recursoDisco1.getStatus():
                            recursoDisco1.setStatus(True)
                            cpu4.setOcupado(True)
                            cpu4.setTempoProcesso(tempo + (fila_ftr[contador][4]))
                            mem.updateOcupado(-fila_ftr[contador][1])
                            pp4 = fila_ftr.pop(contador)
                            contador = contador - 1
                        elif not recursoDisco2.getStatus():
                            recursoDisco2.setStatus(True)
                            cpu4.setOcupado(True)
                            cpu4.setTempoProcesso(tempo + (fila_ftr[contador][4]))
                            mem.updateOcupado(-fila_ftr[contador][1])
                            pp4 = fila_ftr.pop(contador)
                            contador = contador - 1

                    else:
                        cpu4.setOcupado(True)
                        cpu4.setTempoProcesso(tempo + (fila_ftr[contador][4]))
                        mem.updateOcupado(-fila_ftr[contador][1])
                        fila_ftr.pop(contador)
                        contador = contador - 1

    else:
        #coloca o contador da lista no elemento que é menor ou igual o tempo +1
        #faz isso para as 3 filas

        if c1 + 1 <= len(fila1) - 1:
            if fila1[c1 + 1][3] - 1 <= tempo + 1:
                c1 = c1 + 1

        if c2 + 1 <= len(fila2) - 1:
            if fila2[c2 + 1][3] - 1 <= tempo + 1:
                c2 = c2 + 1

        if c3 + 1 <= len(fila3) - 1:
            if fila3[c3 + 1][3] - 1 <= tempo + 1:
                c3 = c3 + 1

        prioridadeMax = 1 #fila com a maior prioridade

        #procura a maior prioridade de cada fila ( no caso a que tem o menor numero )

        if len(fila1) > 0:
            min1 = 99999
            for i in fila1:
                if min1 >= i[2]:
                    min1 = i[2]
        else:
            min1 = 99999

        if len(fila2) > 0:
            min2 = 99999
            for i in fila2:
                if min2 >= i[2]:
                    min2 = i[2]
        else:
            min2 = 99999

        if len(fila3) > 0:
            min3 = 99999
            for i in fila3:
                if min3 >= i[2]:
                    min3 = i[2]
        else:
            min3 = 99999

        #seta a variavel de prioridade de acordo com a a fila que tem a maior prioridade
        if min1 <= min2 and min1 <= min3:
            prioridadeMax = 1
        elif min2 < min1 and min2 < min3:
            prioridadeMax = 2
        elif min3 < min1 and min3 < min2:
            prioridadeMax = 3

        if prioridadeMax == 1:
            if c1 > -1:
                # verifica cpu por cpu até encontrar uma livre
                # se a cpu nao tiver ocupada
                # verifica se o processo precisa da impressora e/ou disco
                # se tiver os rescursos disponiveis seta cpu e recursos utilizados como ocupados
                # salva o processo em uma variavel e o retira da lista
                # decrementa o contador
                if not cpu1.getOcupado():
                    if fila1[c1][5] == 1 and fila1[c1][6] == 1:
                        if not recursoImpressora1.getStatus() and not recursoDisco1.getStatus():
                            recursoDisco1.setStatus(True)
                            recursoImpressora1.setStatus(True)
                            cpu1.setOcupado(True)
                            cpu1.setTempoProcesso(tempo + 2)
                            temp = fila1[c1][4] / 2
                            if temp > 0:
                                mem.updateOcupado(-(fila1[c1][1] / temp))
                            pop1 = fila1.pop(c1)
                            c1 = c1 - 1
                            pop1[4] = pop1[4] - 2
                            q1 = q1 + 1
                        elif not recursoImpressora2.getStatus() and not recursoDisco1.getStatus():
                            recursoDisco1.setStatus(True)
                            recursoImpressora2.setStatus(True)
                            cpu1.setOcupado(True)
                            cpu1.setTempoProcesso(tempo + 2)
                            temp = fila1[c1][4] / 2
                            if temp > 0:
                                mem.updateOcupado(-(fila1[c1][1] / temp))
                            pop1 = fila1.pop(c1)
                            c1 = c1 - 1
                            pop1[4] = pop1[4] - 2
                            q1 = q1 + 1
                        elif not recursoImpressora1.getStatus() and not recursoDisco2.getStatus():
                            recursoDisco2.setStatus(True)
                            recursoImpressora1.setStatus(True)
                            cpu1.setOcupado(True)
                            cpu1.setTempoProcesso(tempo + 2)
                            temp = fila1[c1][4] / 2
                            if temp > 0:
                                mem.updateOcupado(-(fila1[c1][1] / temp))
                            pop1 = fila1.pop(c1)
                            c1 = c1 - 1
                            pop1[4] = pop1[4] - 2
                            q1 = q1 + 1
                        elif not recursoImpressora2.getStatus() and not recursoDisco2.getStatus():
                            recursoDisco2.setStatus(True)
                            recursoImpressora2.setStatus(True)
                            cpu1.setOcupado(True)
                            cpu1.setTempoProcesso(tempo + 2)
                            temp = fila1[c1][4] / 2
                            if temp > 0:
                                mem.updateOcupado(-(fila1[c1][1] / temp))
                            pop1 = fila1.pop(c1)
                            c1 = c1 - 1
                            pop1[4] = pop1[4] - 2
                            q1 = q1 + 1
                    elif fila1[c1][5] == 1:
                        if not recursoImpressora1.getStatus():
                            recursoImpressora1.setStatus(True)
                            cpu1.setOcupado(True)
                            cpu1.setTempoProcesso(tempo + 2)
                            temp = fila1[c1][4] / 2
                            if temp > 0:
                                mem.updateOcupado(-(fila1[c1][1] / temp))
                            pop1 = fila1.pop(c1)
                            c1 = c1 - 1
                            pop1[4] = pop1[4] - 2
                            q1 = q1 + 1
                        elif not recursoImpressora2.getStatus():
                            recursoImpressora1.setStatus(True)
                            cpu1.setOcupado(True)
                            cpu1.setTempoProcesso(tempo + 2)
                            temp = fila1[c1][4] / 2
                            if temp > 0:
                                mem.updateOcupado(-(fila1[c1][1] / temp))
                            pop1 = fila1.pop(c1)
                            c1 = c1 - 1
                            pop1[4] = pop1[4] - 2
                            q1 = q1 + 1

                    elif fila1[c1][6] == 1:
                        if not recursoDisco1.getStatus():
                            recursoDisco1.setStatus(True)
                            cpu1.setOcupado(True)
                            cpu1.setTempoProcesso(tempo + 2)
                            temp = fila1[c1][4] / 2
                            if temp > 0:
                                mem.updateOcupado(-(fila1[c1][1] / temp))
                            pop1 = fila1.pop(c1)
                            c1 = c1 - 1
                            pop1[4] = pop1[4] - 2
                            q1 = q1 + 1
                        elif not recursoDisco2.getStatus():
                            recursoDisco2.setStatus(True)
                            cpu1.setOcupado(True)
                            cpu1.setTempoProcesso(tempo + 2)
                            temp = fila1[c1][4] / 2
                            if temp > 0:
                                mem.updateOcupado(-(fila1[c1][1] / temp))
                            pop1 = fila1.pop(c1)
                            c1 = c1 - 1
                            pop1[4] = pop1[4] - 2
                            q1 = q1 + 1


                    else:
                        cpu1.setOcupado(True)
                        cpu1.setTempoProcesso(tempo + 2)
                        temp = fila1[c1][4] / 2
                        if temp > 0:
                            mem.updateOcupado(-(fila1[c1][1] / temp))
                        pop1 = fila1.pop(c1)
                        c1 = c1 - 1
                        pop1[4] = pop1[4] - 2
                        q1 = q1 + 1
                elif not cpu2.getOcupado():
                    if fila1[c1][5] == 1 and fila1[c1][6] == 1:
                        if not recursoImpressora1.getStatus() and not recursoDisco1.getStatus():
                            recursoDisco1.setStatus(True)
                            recursoImpressora1.setStatus(True)
                            cpu2.setOcupado(True)
                            cpu2.setTempoProcesso(tempo + 2)
                            temp = fila1[c1][4] / 2
                            if temp > 0:
                                mem.updateOcupado(-(fila1[c1][1] / temp))
                            pop2 = fila1.pop(c1)
                            pop2[4] = pop2[4] - 2
                            c1 = c1 - 1
                            q2 = q2 + 1
                        elif not recursoImpressora2.getStatus() and not recursoDisco1.getStatus():
                            recursoDisco1.setStatus(True)
                            recursoImpressora2.setStatus(True)
                            cpu2.setOcupado(True)
                            cpu2.setTempoProcesso(tempo + 2)
                            temp = fila1[c1][4] / 2
                            if temp > 0:
                                mem.updateOcupado(-(fila1[c1][1] / temp))
                            pop2 = fila1.pop(c1)
                            pop2[4] = pop2[4] - 2
                            c1 = c1 - 1
                            q2 = q2 + 1
                        elif not recursoImpressora1.getStatus() and not recursoDisco2.getStatus():
                            recursoDisco2.setStatus(True)
                            recursoImpressora1.setStatus(True)
                            cpu2.setOcupado(True)
                            cpu2.setTempoProcesso(tempo + 2)
                            temp = fila1[c1][4] / 2
                            if temp > 0:
                                mem.updateOcupado(-(fila1[c1][1] / temp))
                            pop2 = fila1.pop(c1)
                            pop2[4] = pop2[4] - 2
                            c1 = c1 - 1
                            q2 = q2 + 1
                        elif not recursoImpressora2.getStatus() and not recursoDisco2.getStatus():
                            recursoDisco2.setStatus(True)
                            recursoImpressora2.setStatus(True)
                            cpu2.setOcupado(True)
                            cpu2.setTempoProcesso(tempo + 2)
                            temp = fila1[c1][4] / 2
                            if temp > 0:
                                mem.updateOcupado(-(fila1[c1][1] / temp))
                            pop2 = fila1.pop(c1)
                            pop2[4] = pop2[4] - 2
                            c1 = c1 - 1
                            q2 = q2 + 1
                    elif fila1[c1][5] == 1:
                        if not recursoImpressora1.getStatus():
                            recursoImpressora1.setStatus(True)
                            cpu2.setOcupado(True)
                            cpu2.setTempoProcesso(tempo + 2)
                            temp = fila1[c1][4] / 2
                            if temp > 0:
                                mem.updateOcupado(-(fila1[c1][1] / temp))
                            pop2 = fila1.pop(c1)
                            pop2[4] = pop2[4] - 2
                            c1 = c1 - 1
                            q2 = q2 + 1
                        elif not recursoImpressora2.getStatus():
                            recursoImpressora1.setStatus(True)
                            cpu2.setOcupado(True)
                            cpu2.setTempoProcesso(tempo + 2)
                            temp = fila1[c1][4] / 2
                            if temp > 0:
                                mem.updateOcupado(-(fila1[c1][1] / temp))
                            pop2 = fila1.pop(c1)
                            pop2[4] = pop2[4] - 2
                            c1 = c1 - 1
                            q2 = q2 + 1

                    elif fila1[c1][6] == 1:
                        if not recursoDisco1.getStatus():
                            recursoDisco1.setStatus(True)
                            cpu2.setOcupado(True)
                            cpu2.setTempoProcesso(tempo + 2)
                            temp = fila1[c1][4] / 2
                            if temp > 0:
                                mem.updateOcupado(-(fila1[c1][1] / temp))
                            pop2 = fila1.pop(c1)
                            pop2[4] = pop2[4] - 2
                            c1 = c1 - 1
                            q2 = q2 + 1
                        elif not recursoDisco2.getStatus():
                            recursoDisco2.setStatus(True)
                            cpu2.setOcupado(True)
                            cpu2.setTempoProcesso(tempo + 2)
                            temp = fila1[c1][4] / 2
                            if temp > 0:
                                mem.updateOcupado(-(fila1[c1][1] / temp))
                            pop2 = fila1.pop(c1)
                            pop2[4] = pop2[4] - 2
                            c1 = c1 - 1
                            q2 = q2 + 1


                    else:
                        cpu2.setOcupado(True)
                        cpu2.setTempoProcesso(tempo + 2)
                        temp = fila1[c1][4] / 2
                        if temp > 0:
                            mem.updateOcupado(-(fila1[c1][1] / temp))
                        pop2 = fila1.pop(c1)
                        pop2[4] = pop2[4] - 2
                        c1 = c1 - 1
                        q2 = q2 + 1
                elif not cpu3.getOcupado():
                    if fila1[c1][5] == 1 and fila1[c1][6] == 1:
                        if not recursoImpressora1.getStatus() and not recursoDisco1.getStatus():
                            recursoDisco1.setStatus(True)
                            recursoImpressora1.setStatus(True)
                            cpu3.setOcupado(True)
                            cpu3.setTempoProcesso(tempo + 2)
                            temp = fila1[c1][4] / 2
                            if temp > 0:
                                mem.updateOcupado(-(fila1[c1][1] / temp))
                            pop3 = fila1.pop(c1)
                            c1 = c1 - 1
                            pop3[4] = pop3[4] - 2
                            q3 = q3 + 1
                        elif not recursoImpressora2.getStatus() and not recursoDisco1.getStatus():
                            recursoDisco1.setStatus(True)
                            recursoImpressora2.setStatus(True)
                            cpu3.setOcupado(True)
                            cpu3.setTempoProcesso(tempo + 2)
                            temp = fila1[c1][4] / 2
                            if temp > 0:
                                mem.updateOcupado(-(fila1[c1][1] / temp))
                            pop3 = fila1.pop(c1)
                            c1 = c1 - 1
                            pop3[4] = pop3[4] - 2
                            q3 = q3 + 1
                        elif not recursoImpressora1.getStatus() and not recursoDisco2.getStatus():
                            recursoDisco2.setStatus(True)
                            recursoImpressora1.setStatus(True)
                            cpu3.setOcupado(True)
                            cpu3.setTempoProcesso(tempo + 2)
                            temp = fila1[c1][4] / 2
                            if temp > 0:
                                mem.updateOcupado(-(fila1[c1][1] / temp))
                            pop3 = fila1.pop(c1)
                            c1 = c1 - 1
                            pop3[4] = pop3[4] - 2
                            q3 = q3 + 1
                        elif not recursoImpressora2.getStatus() and not recursoDisco2.getStatus():
                            recursoDisco2.setStatus(True)
                            recursoImpressora2.setStatus(True)
                            cpu3.setOcupado(True)
                            cpu3.setTempoProcesso(tempo + 2)
                            temp = fila1[c1][4] / 2
                            if temp > 0:
                                mem.updateOcupado(-(fila1[c1][1] / temp))
                            pop3 = fila1.pop(c1)
                            c1 = c1 - 1
                            pop3[4] = pop3[4] - 2
                            q3 = q3 + 1
                    elif fila1[c1][5] == 1:
                        if not recursoImpressora1.getStatus():
                            recursoImpressora1.setStatus(True)
                            cpu3.setOcupado(True)
                            cpu3.setTempoProcesso(tempo + 2)
                            temp = fila1[c1][4] / 2
                            if temp > 0:
                                mem.updateOcupado(-(fila1[c1][1] / temp))
                            pop3 = fila1.pop(c1)
                            c1 = c1 - 1
                            pop3[4] = pop3[4] - 2
                            q3 = q3 + 1
                        elif not recursoImpressora2.getStatus():
                            recursoImpressora1.setStatus(True)
                            cpu3.setOcupado(True)
                            cpu3.setTempoProcesso(tempo + 2)
                            temp = fila1[c1][4] / 2
                            if temp > 0:
                                mem.updateOcupado(-(fila1[c1][1] / temp))
                            pop3 = fila1.pop(c1)
                            c1 = c1 - 1
                            pop3[4] = pop3[4] - 2
                            q3 = q3 + 1

                    elif fila1[c1][6] == 1:
                        if not recursoDisco1.getStatus():
                            recursoDisco1.setStatus(True)
                            cpu3.setOcupado(True)
                            cpu3.setTempoProcesso(tempo + 2)
                            temp = fila1[c1][4] / 2
                            if temp > 0:
                                mem.updateOcupado(-(fila1[c1][1] / temp))
                            pop3 = fila1.pop(c1)
                            c1 = c1 - 1
                            pop3[4] = pop3[4] - 2
                            q3 = q3 + 1
                        elif not recursoDisco2.getStatus():
                            recursoDisco2.setStatus(True)
                            cpu3.setOcupado(True)
                            cpu3.setTempoProcesso(tempo + 2)
                            temp = fila1[c1][4] / 2
                            if temp > 0:
                                mem.updateOcupado(-(fila1[c1][1] / temp))
                            pop3 = fila1.pop(c1)
                            c1 = c1 - 1
                            pop3[4] = pop3[4] - 2
                            q3 = q3 + 1


                    else:
                        cpu3.setOcupado(True)
                        cpu3.setTempoProcesso(tempo + 2)
                        temp = fila1[c1][4] / 2
                        if temp > 0:
                            mem.updateOcupado(-(fila1[c1][1] / temp))
                        pop3 = fila1.pop(c1)
                        c1 = c1 - 1
                        pop3[4] = pop3[4] - 2
                        q3 = q3 + 1
                elif not cpu4.getOcupado():
                    if fila1[c1][5] == 1 and fila1[c1][6] == 1:
                        if not recursoImpressora1.getStatus() and not recursoDisco1.getStatus():
                            recursoDisco1.setStatus(True)
                            recursoImpressora1.setStatus(True)
                            cpu4.setOcupado(True)
                            cpu4.setTempoProcesso(tempo + 2)
                            temp = fila1[c1][4] / 2
                            if temp > 0:
                                mem.updateOcupado(-(fila1[c1][1] / temp))
                            pop4 = fila1.pop(c1)
                            c1 = c1 - 1
                            pop4[4] = pop4[4] - 2
                            q4 = q4 + 1
                        elif not recursoImpressora2.getStatus() and not recursoDisco1.getStatus():
                            recursoDisco1.setStatus(True)
                            recursoImpressora2.setStatus(True)
                            cpu4.setOcupado(True)
                            cpu4.setTempoProcesso(tempo + 2)
                            temp = fila1[c1][4] / 2
                            if temp > 0:
                                mem.updateOcupado(-(fila1[c1][1] / temp))
                            pop4 = fila1.pop(c1)
                            c1 = c1 - 1
                            pop4[4] = pop4[4] - 2
                            q4 = q4 + 1
                        elif not recursoImpressora1.getStatus() and not recursoDisco2.getStatus():
                            recursoDisco2.setStatus(True)
                            recursoImpressora1.setStatus(True)
                            cpu4.setOcupado(True)
                            cpu4.setTempoProcesso(tempo + 2)
                            temp = fila1[c1][4] / 2
                            if temp > 0:
                                mem.updateOcupado(-(fila1[c1][1] / temp))
                            pop4 = fila1.pop(c1)
                            c1 = c1 - 1
                            pop4[4] = pop4[4] - 2
                            q4 = q4 + 1
                        elif not recursoImpressora2.getStatus() and not recursoDisco2.getStatus():
                            recursoDisco2.setStatus(True)
                            recursoImpressora2.setStatus(True)
                            cpu4.setOcupado(True)
                            cpu4.setTempoProcesso(tempo + 2)
                            temp = fila1[c1][4] / 2
                            if temp > 0:
                                mem.updateOcupado(-(fila1[c1][1] / temp))
                            pop4 = fila1.pop(c1)
                            c1 = c1 - 1
                            pop4[4] = pop4[4] - 2
                            q4 = q4 + 1
                    elif fila1[c1][5] == 1:
                        if not recursoImpressora1.getStatus():
                            recursoImpressora1.setStatus(True)
                            cpu4.setOcupado(True)
                            cpu4.setTempoProcesso(tempo + 2)
                            temp = fila1[c1][4] / 2
                            if temp > 0:
                                mem.updateOcupado(-(fila1[c1][1] / temp))
                            pop4 = fila1.pop(c1)
                            c1 = c1 - 1
                            pop4[4] = pop4[4] - 2
                            q4 = q4 + 1
                        elif not recursoImpressora2.getStatus():
                            recursoImpressora1.setStatus(True)
                            cpu4.setOcupado(True)
                            cpu4.setTempoProcesso(tempo + 2)
                            temp = fila1[c1][4] / 2
                            if temp > 0:
                                mem.updateOcupado(-(fila1[c1][1] / temp))
                            pop4 = fila1.pop(c1)
                            c1 = c1 - 1
                            pop4[4] = pop4[4] - 2
                            q4 = q4 + 1

                    elif fila1[c1][6] == 1:
                        if not recursoDisco1.getStatus():
                            recursoDisco1.setStatus(True)
                            cpu4.setOcupado(True)
                            cpu4.setTempoProcesso(tempo + 2)
                            temp = fila1[c1][4] / 2
                            if temp > 0:
                                mem.updateOcupado(-(fila1[c1][1] / temp))
                            pop4 = fila1.pop(c1)
                            c1 = c1 - 1
                            pop4[4] = pop4[4] - 2
                            q4 = q4 + 1
                        elif not recursoDisco2.getStatus():
                            recursoDisco2.setStatus(True)
                            cpu4.setOcupado(True)
                            cpu4.setTempoProcesso(tempo + 2)
                            temp = fila1[c1][4] / 2
                            if temp > 0:
                                mem.updateOcupado(-(fila1[c1][1] / temp))
                            pop4 = fila1.pop(c1)
                            c1 = c1 - 1
                            pop4[4] = pop4[4] - 2
                            q4 = q4 + 1


                    else:
                        cpu4.setOcupado(True)
                        cpu4.setTempoProcesso(tempo + 2)
                        temp = fila1[c1][4] / 2
                        if temp > 0:
                            mem.updateOcupado(-(fila1[c1][1] / temp))
                        pop4 = fila1.pop(c1)
                        c1 = c1 - 1
                        pop4[4] = pop4[4] - 2
                        q4 = q4 + 1

        elif prioridadeMax == 2:
            if c2 > -1:
                # verifica cpu por cpu até encontrar uma livre
                # se a cpu nao tiver ocupada
                # verifica se o processo precisa da impressora e/ou disco
                # se tiver os rescursos disponiveis seta cpu e recursos utilizados como ocupados
                # salva o processo em uma variavel e o retira da lista
                # decrementa o contador
                if not cpu1.getOcupado():
                    if fila2[c2][5] == 1 and fila2[c2][6] == 1:
                        if not recursoImpressora1.getStatus() and not recursoDisco1.getStatus():
                            recursoDisco1.setStatus(True)
                            recursoImpressora1.setStatus(True)
                            cpu1.setOcupado(True)
                            cpu1.setTempoProcesso(tempo + 2)
                            temp = fila2[c2][4] / 2
                            if temp > 0:
                                mem.updateOcupado(-(fila2[c2][1] / temp))
                            po1 = fila2.pop(c2)
                            c2 = c2 - 1
                            po1[4] = po1[4] - 2
                            q1 = q1 + 1
                        elif not recursoImpressora2.getStatus() and not recursoDisco1.getStatus():
                            recursoDisco1.setStatus(True)
                            recursoImpressora2.setStatus(True)
                            cpu1.setOcupado(True)
                            cpu1.setTempoProcesso(tempo + 2)
                            temp = fila2[c2][4] / 2
                            if temp > 0:
                                mem.updateOcupado(-(fila2[c2][1] / temp))
                            po1 = fila2.pop(c2)
                            c2 = c2 - 1
                            po1[4] = po1[4] - 2
                            q1 = q1 + 1
                        elif not recursoImpressora1.getStatus() and not recursoDisco2.getStatus():
                            recursoDisco2.setStatus(True)
                            recursoImpressora1.setStatus(True)
                            cpu1.setOcupado(True)
                            cpu1.setTempoProcesso(tempo + 2)
                            temp = fila2[c2][4] / 2
                            if temp > 0:
                                mem.updateOcupado(-(fila2[c2][1] / temp))
                            po1 = fila2.pop(c2)
                            c2 = c2 - 1
                            po1[4] = po1[4] - 2
                            q1 = q1 + 1
                        elif not recursoImpressora2.getStatus() and not recursoDisco2.getStatus():
                            recursoDisco2.setStatus(True)
                            recursoImpressora2.setStatus(True)
                            cpu1.setOcupado(True)
                            cpu1.setTempoProcesso(tempo + 2)
                            temp = fila2[c2][4] / 2
                            if temp > 0:
                                mem.updateOcupado(-(fila2[c2][1] / temp))
                            po1 = fila2.pop(c2)
                            c2 = c2 - 1
                            po1[4] = po1[4] - 2
                            q1 = q1 + 1
                    elif fila2[c2][5] == 1:
                        if not recursoImpressora1.getStatus():
                            recursoImpressora1.setStatus(True)
                            cpu1.setOcupado(True)
                            cpu1.setTempoProcesso(tempo + 2)
                            temp = fila2[c2][4] / 2
                            if temp > 0:
                                mem.updateOcupado(-(fila2[c2][1] / temp))
                            po1 = fila2.pop(c2)
                            c2 = c2 - 1
                            po1[4] = po1[4] - 2
                            q1 = q1 + 1
                        elif not recursoImpressora2.getStatus():
                            recursoImpressora1.setStatus(True)
                            cpu1.setOcupado(True)
                            cpu1.setTempoProcesso(tempo + 2)
                            temp = fila2[c2][4] / 2
                            if temp > 0:
                                mem.updateOcupado(-(fila2[c2][1] / temp))
                            po1 = fila2.pop(c2)
                            c2 = c2 - 1
                            po1[4] = po1[4] - 2
                            q1 = q1 + 1

                    elif fila2[c2][6] == 1:
                        if not recursoDisco1.getStatus():
                            recursoDisco1.setStatus(True)
                            cpu1.setOcupado(True)
                            cpu1.setTempoProcesso(tempo + 2)
                            temp = fila2[c2][4] / 2
                            if temp > 0:
                                mem.updateOcupado(-(fila2[c2][1] / temp))
                            po1 = fila2.pop(c2)
                            c2 = c2 - 1
                            po1[4] = po1[4] - 2
                            q1 = q1 + 1
                        elif not recursoDisco2.getStatus():
                            recursoDisco2.setStatus(True)
                            cpu1.setOcupado(True)
                            cpu1.setTempoProcesso(tempo + 2)
                            temp = fila2[c2][4] / 2
                            if temp > 0:
                                mem.updateOcupado(-(fila2[c2][1] / temp))
                            po1 = fila2.pop(c2)
                            c2 = c2 - 1
                            po1[4] = po1[4] - 2
                            q1 = q1 + 1


                    else:
                        cpu1.setOcupado(True)
                        cpu1.setTempoProcesso(tempo + 2)
                        temp = fila2[c2][4] / 2
                        if temp > 0:
                            mem.updateOcupado(-(fila2[c2][1] / temp))
                        po1 = fila2.pop(c2)
                        c2 = c2 - 1
                        po1[4] = po1[4] - 2
                        q1 = q1 + 1
                elif not cpu2.getOcupado():
                    if fila2[c2][5] == 1 and fila2[c2][6] == 1:
                        if not recursoImpressora1.getStatus() and not recursoDisco1.getStatus():
                            recursoDisco1.setStatus(True)
                            recursoImpressora1.setStatus(True)
                            cpu2.setOcupado(True)
                            cpu2.setTempoProcesso(tempo + 2)
                            temp = fila2[c2][4] / 2
                            if temp > 0:
                                mem.updateOcupado(-(fila2[c2][1] / temp))
                            po2 = fila2.pop(c2)
                            c2 = c2 - 1
                            po2[4] = po2[4] - 2
                            q2 = q2 + 1
                        elif not recursoImpressora2.getStatus() and not recursoDisco1.getStatus():
                            recursoDisco1.setStatus(True)
                            recursoImpressora2.setStatus(True)
                            cpu2.setOcupado(True)
                            cpu2.setTempoProcesso(tempo + 2)
                            temp = fila2[c2][4] / 2
                            if temp > 0:
                                mem.updateOcupado(-(fila2[c2][1] / temp))
                            po2 = fila2.pop(c2)
                            c2 = c2 - 1
                            po2[4] = po2[4] - 2
                            q2 = q2 + 1
                        elif not recursoImpressora1.getStatus() and not recursoDisco2.getStatus():
                            recursoDisco2.setStatus(True)
                            recursoImpressora1.setStatus(True)
                            cpu2.setOcupado(True)
                            cpu2.setTempoProcesso(tempo + 2)
                            temp = fila2[c2][4] / 2
                            if temp > 0:
                                mem.updateOcupado(-(fila2[c2][1] / temp))
                            po2 = fila2.pop(c2)
                            c2 = c2 - 1
                            po2[4] = po2[4] - 2
                            q2 = q2 + 1
                        elif not recursoImpressora2.getStatus() and not recursoDisco2.getStatus():
                            recursoDisco2.setStatus(True)
                            recursoImpressora2.setStatus(True)
                            cpu2.setOcupado(True)
                            cpu2.setTempoProcesso(tempo + 2)
                            temp = fila2[c2][4] / 2
                            if temp > 0:
                                mem.updateOcupado(-(fila2[c2][1] / temp))
                            po2 = fila2.pop(c2)
                            c2 = c2 - 1
                            po2[4] = po2[4] - 2
                            q2 = q2 + 1
                    elif fila2[c2][5] == 1:
                        if not recursoImpressora1.getStatus():
                            recursoImpressora1.setStatus(True)
                            cpu2.setOcupado(True)
                            cpu2.setTempoProcesso(tempo + 2)
                            temp = fila2[c2][4] / 2
                            if temp > 0:
                                mem.updateOcupado(-(fila2[c2][1] / temp))
                            po2 = fila2.pop(c2)
                            c2 = c2 - 1
                            po2[4] = po2[4] - 2
                            q2 = q2 + 1
                        elif not recursoImpressora2.getStatus():
                            recursoImpressora1.setStatus(True)
                            cpu2.setOcupado(True)
                            cpu2.setTempoProcesso(tempo + 2)
                            temp = fila2[c2][4] / 2
                            if temp > 0:
                                mem.updateOcupado(-(fila2[c2][1] / temp))
                            po2 = fila2.pop(c2)
                            c2 = c2 - 1
                            po2[4] = po2[4] - 2
                            q2 = q2 + 1

                    elif fila2[c2][6] == 1:
                        if not recursoDisco1.getStatus():
                            recursoDisco1.setStatus(True)
                            cpu2.setOcupado(True)
                            cpu2.setTempoProcesso(tempo + 2)
                            temp = fila2[c2][4] / 2
                            if temp > 0:
                                mem.updateOcupado(-(fila2[c2][1] / temp))
                            po2 = fila2.pop(c2)
                            c2 = c2 - 1
                            po2[4] = po2[4] - 2
                            q2 = q2 + 1
                        elif not recursoDisco2.getStatus():
                            recursoDisco2.setStatus(True)
                            cpu2.setOcupado(True)
                            cpu2.setTempoProcesso(tempo + 2)
                            temp = fila2[c2][4] / 2
                            if temp > 0:
                                mem.updateOcupado(-(fila2[c2][1] / temp))
                            po2 = fila2.pop(c2)
                            c2 = c2 - 1
                            po2[4] = po2[4] - 2
                            q2 = q2 + 1


                    else:
                        cpu2.setOcupado(True)
                        cpu2.setTempoProcesso(tempo + 2)
                        temp = fila2[c2][4] / 2
                        if temp > 0:
                            mem.updateOcupado(-(fila2[c2][1] / temp))
                        po2 = fila2.pop(c2)
                        c2 = c2 - 1
                        po2[4] = po2[4] - 2
                        q2 = q2 + 1
                elif not cpu3.getOcupado():
                    if fila2[c2][5] == 1 and fila2[c2][6] == 1:
                        if not recursoImpressora1.getStatus() and not recursoDisco1.getStatus():
                            recursoDisco1.setStatus(True)
                            recursoImpressora1.setStatus(True)
                            cpu3.setOcupado(True)
                            cpu3.setTempoProcesso(tempo + 2)
                            temp = fila2[c2][4] / 2
                            if temp > 0:
                                mem.updateOcupado(-(fila2[c2][1] / temp))
                            po3 = fila2.pop(c2)
                            c2 = c2 - 1
                            po3[4] = po3[4] - 2
                            q3 = q3 + 1
                        elif not recursoImpressora2.getStatus() and not recursoDisco1.getStatus():
                            recursoDisco1.setStatus(True)
                            recursoImpressora2.setStatus(True)
                            cpu3.setOcupado(True)
                            cpu3.setTempoProcesso(tempo + 2)
                            temp = fila2[c2][4] / 2
                            if temp > 0:
                                mem.updateOcupado(-(fila2[c2][1] / temp))
                            po3 = fila2.pop(c2)
                            c2 = c2 - 1
                            po3[4] = po3[4] - 2
                            q3 = q3 + 1
                        elif not recursoImpressora1.getStatus() and not recursoDisco2.getStatus():
                            recursoDisco2.setStatus(True)
                            recursoImpressora1.setStatus(True)
                            cpu3.setOcupado(True)
                            cpu3.setTempoProcesso(tempo + 2)
                            temp = fila2[c2][4] / 2
                            if temp > 0:
                                mem.updateOcupado(-(fila2[c2][1] / temp))
                            po3 = fila2.pop(c2)
                            c2 = c2 - 1
                            po3[4] = po3[4] - 2
                            q3 = q3 + 1
                        elif not recursoImpressora2.getStatus() and not recursoDisco2.getStatus():
                            recursoDisco2.setStatus(True)
                            recursoImpressora2.setStatus(True)
                            cpu3.setOcupado(True)
                            cpu3.setTempoProcesso(tempo + 2)
                            temp = fila2[c2][4] / 2
                            if temp > 0:
                                mem.updateOcupado(-(fila2[c2][1] / temp))
                            po3 = fila2.pop(c2)
                            c2 = c2 - 1
                            po3[4] = po3[4] - 2
                            q3 = q3 + 1
                    elif fila2[c2][5] == 1:
                        if not recursoImpressora1.getStatus():
                            recursoImpressora1.setStatus(True)
                            cpu3.setOcupado(True)
                            cpu3.setTempoProcesso(tempo + 2)
                            temp = fila2[c2][4] / 2
                            if temp > 0:
                                mem.updateOcupado(-(fila2[c2][1] / temp))
                            po3 = fila2.pop(c2)
                            c2 = c2 - 1
                            po3[4] = po3[4] - 2
                            q3 = q3 + 1
                        elif not recursoImpressora2.getStatus():
                            recursoImpressora1.setStatus(True)
                            cpu3.setOcupado(True)
                            cpu3.setTempoProcesso(tempo + 2)
                            temp = fila2[c2][4] / 2
                            if temp > 0:
                                mem.updateOcupado(-(fila2[c2][1] / temp))
                            po3 = fila2.pop(c2)
                            c2 = c2 - 1
                            po3[4] = po3[4] - 2
                            q3 = q3 + 1

                    elif fila2[c2][6] == 1:
                        if not recursoDisco1.getStatus():
                            recursoDisco1.setStatus(True)
                            cpu3.setOcupado(True)
                            cpu3.setTempoProcesso(tempo + 2)
                            temp = fila2[c2][4] / 2
                            if temp > 0:
                                mem.updateOcupado(-(fila2[c2][1] / temp))
                            po3 = fila2.pop(c2)
                            c2 = c2 - 1
                            po3[4] = po3[4] - 2
                            q3 = q3 + 1
                        elif not recursoDisco2.getStatus():
                            recursoDisco2.setStatus(True)
                            cpu3.setOcupado(True)
                            cpu3.setTempoProcesso(tempo + 2)
                            temp = fila2[c2][4] / 2
                            if temp > 0:
                                mem.updateOcupado(-(fila2[c2][1] / temp))
                            po3 = fila2.pop(c2)
                            c2 = c2 - 1
                            po3[4] = po3[4] - 2
                            q3 = q3 + 1


                    else:
                        cpu3.setOcupado(True)
                        cpu3.setTempoProcesso(tempo + 2)
                        temp = fila2[c2][4] / 2
                        if temp > 0:
                            mem.updateOcupado(-(fila2[c2][1] / temp))
                        po3 = fila2.pop(c2)
                        c2 = c2 - 1
                        po3[4] = po3[4] - 2
                        q3 = q3 + 1
                elif not cpu4.getOcupado():
                    if fila2[c2][5] == 1 and fila2[c2][6] == 1:
                        if not recursoImpressora1.getStatus() and not recursoDisco1.getStatus():
                            recursoDisco1.setStatus(True)
                            recursoImpressora1.setStatus(True)
                            cpu4.setOcupado(True)
                            cpu4.setTempoProcesso(tempo + 2)
                            temp = fila2[c2][4] / 2
                            if temp > 0:
                                mem.updateOcupado(-(fila2[c2][1] / temp))
                            po4 = fila2.pop(c2)
                            c2 = c2 - 1
                            po4[4] = po4[4] - 2
                            q4 = q4 + 1
                        elif not recursoImpressora2.getStatus() and not recursoDisco1.getStatus():
                            recursoDisco1.setStatus(True)
                            recursoImpressora2.setStatus(True)
                            cpu4.setOcupado(True)
                            cpu4.setTempoProcesso(tempo + 2)
                            temp = fila2[c2][4] / 2
                            if temp > 0:
                                mem.updateOcupado(-(fila2[c2][1] / temp))
                            po4 = fila2.pop(c2)
                            c2 = c2 - 1
                            po4[4] = po4[4] - 2
                            q4 = q4 + 1
                        elif not recursoImpressora1.getStatus() and not recursoDisco2.getStatus():
                            recursoDisco2.setStatus(True)
                            recursoImpressora1.setStatus(True)
                            cpu4.setOcupado(True)
                            cpu4.setTempoProcesso(tempo + 2)
                            temp = fila2[c2][4] / 2
                            if temp > 0:
                                mem.updateOcupado(-(fila2[c2][1] / temp))
                            po4 = fila2.pop(c2)
                            c2 = c2 - 1
                            po4[4] = po4[4] - 2
                            q4 = q4 + 1
                        elif not recursoImpressora2.getStatus() and not recursoDisco2.getStatus():
                            recursoDisco2.setStatus(True)
                            recursoImpressora2.setStatus(True)
                            cpu4.setOcupado(True)
                            cpu4.setTempoProcesso(tempo + 2)
                            temp = fila2[c2][4] / 2
                            if temp > 0:
                                mem.updateOcupado(-(fila2[c2][1] / temp))
                            po4 = fila2.pop(c2)
                            c2 = c2 - 1
                            po4[4] = po4[4] - 2
                            q4 = q4 + 1
                    elif fila2[c2][5] == 1:
                        if not recursoImpressora1.getStatus():
                            recursoImpressora1.setStatus(True)
                            cpu4.setOcupado(True)
                            cpu4.setTempoProcesso(tempo + 2)
                            temp = fila2[c2][4] / 2
                            if temp > 0:
                                mem.updateOcupado(-(fila2[c2][1] / temp))
                            po4 = fila2.pop(c2)
                            c2 = c2 - 1
                            po4[4] = po4[4] - 2
                            q4 = q4 + 1
                        elif not recursoImpressora2.getStatus():
                            recursoImpressora1.setStatus(True)
                            cpu4.setOcupado(True)
                            cpu4.setTempoProcesso(tempo + 2)
                            temp = fila2[c2][4] / 2
                            if temp > 0:
                                mem.updateOcupado(-(fila2[c2][1] / temp))
                            po4 = fila2.pop(c2)
                            c2 = c2 - 1
                            po4[4] = po4[4] - 2
                            q4 = q4 + 1

                    elif fila2[c2][6] == 1:
                        if not recursoDisco1.getStatus():
                            recursoDisco1.setStatus(True)
                            cpu4.setOcupado(True)
                            cpu4.setTempoProcesso(tempo + 2)
                            temp = fila2[c2][4] / 2
                            if temp > 0:
                                mem.updateOcupado(-(fila2[c2][1] / temp))
                            po4 = fila2.pop(c2)
                            c2 = c2 - 1
                            po4[4] = po4[4] - 2
                            q4 = q4 + 1
                        elif not recursoDisco2.getStatus():
                            recursoDisco2.setStatus(True)
                            cpu4.setOcupado(True)
                            cpu4.setTempoProcesso(tempo + 2)
                            temp = fila2[c2][4] / 2
                            if temp > 0:
                                mem.updateOcupado(-(fila2[c2][1] / temp))
                            po4 = fila2.pop(c2)
                            c2 = c2 - 1
                            po4[4] = po4[4] - 2
                            q4 = q4 + 1


                    else:
                        cpu4.setOcupado(True)
                        cpu4.setTempoProcesso(tempo + 2)
                        temp = fila2[c2][4] / 2
                        if temp > 0:
                            mem.updateOcupado(-(fila2[c2][1] / temp))
                        po4 = fila2.pop(c2)
                        c2 = c2 - 1
                        po4[4] = po4[4] - 2
                        q4 = q4 + 1


        else:
            if c3 > -1:
                # verifica cpu por cpu até encontrar uma livre
                # se a cpu nao tiver ocupada
                # verifica se o processo precisa da impressora e/ou disco
                # se tiver os rescursos disponiveis seta cpu e recursos utilizados como ocupados
                # salva o processo em uma variavel e o retira da lista
                # decrementa o contador
                if not cpu1.getOcupado():
                    if fila3[c3][5] == 1 and fila3[c3][6] == 1:
                        if not recursoImpressora1.getStatus() and not recursoDisco1.getStatus():
                            recursoDisco1.setStatus(True)
                            recursoImpressora1.setStatus(True)
                            cpu1.setOcupado(True)
                            cpu1.setTempoProcesso(tempo + 2)
                            temp = fila3[c3][4] / 2
                            if temp > 0:
                                mem.updateOcupado(-(fila3[c3][1] / temp))
                            p1 = fila3.pop(c3)
                            c3 = c3 - 1
                            p1[4] = p1[4] - 2
                            q1 = q1 + 1
                        elif not recursoImpressora2.getStatus() and not recursoDisco1.getStatus():
                            recursoDisco1.setStatus(True)
                            recursoImpressora2.setStatus(True)
                            cpu1.setOcupado(True)
                            cpu1.setTempoProcesso(tempo + 2)
                            temp = fila3[c3][4] / 2
                            if temp > 0:
                                mem.updateOcupado(-(fila3[c3][1] / temp))
                            p1 = fila3.pop(c3)
                            c3 = c3 - 1
                            p1[4] = p1[4] - 2
                            q1 = q1 + 1
                        elif not recursoImpressora1.getStatus() and not recursoDisco2.getStatus():
                            recursoDisco2.setStatus(True)
                            recursoImpressora1.setStatus(True)
                            cpu1.setOcupado(True)
                            cpu1.setTempoProcesso(tempo + 2)
                            temp = fila3[c3][4] / 2
                            if temp > 0:
                                mem.updateOcupado(-(fila3[c3][1] / temp))
                            p1 = fila3.pop(c3)
                            c3 = c3 - 1
                            p1[4] = p1[4] - 2
                            q1 = q1 + 1
                        elif not recursoImpressora2.getStatus() and not recursoDisco2.getStatus():
                            recursoDisco2.setStatus(True)
                            recursoImpressora2.setStatus(True)
                            cpu1.setOcupado(True)
                            cpu1.setTempoProcesso(tempo + 2)
                            temp = fila3[c3][4] / 2
                            if temp > 0:
                                mem.updateOcupado(-(fila3[c3][1] / temp))
                            p1 = fila3.pop(c3)
                            c3 = c3 - 1
                            p1[4] = p1[4] - 2
                            q1 = q1 + 1
                    elif fila3[c3][5] == 1:
                        if not recursoImpressora1.getStatus():
                            recursoImpressora1.setStatus(True)
                            cpu1.setOcupado(True)
                            cpu1.setTempoProcesso(tempo + 2)
                            temp = fila3[c3][4] / 2
                            if temp > 0:
                                mem.updateOcupado(-(fila3[c3][1] / temp))
                            p1 = fila3.pop(c3)
                            c3 = c3 - 1
                            p1[4] = p1[4] - 2
                            q1 = q1 + 1
                        elif not recursoImpressora2.getStatus():
                            recursoImpressora1.setStatus(True)
                            cpu1.setOcupado(True)
                            cpu1.setTempoProcesso(tempo + 2)
                            temp = fila3[c3][4] / 2
                            if temp > 0:
                                mem.updateOcupado(-(fila3[c3][1] / temp))
                            p1 = fila3.pop(c3)
                            c3 = c3 - 1
                            p1[4] = p1[4] - 2
                            q1 = q1 + 1

                    elif fila3[c3][6] == 1:
                        if not recursoDisco1.getStatus():
                            recursoDisco1.setStatus(True)
                            cpu1.setOcupado(True)
                            cpu1.setTempoProcesso(tempo + 2)
                            temp = fila3[c3][4] / 2
                            if temp > 0:
                                mem.updateOcupado(-(fila3[c3][1] / temp))
                            p1 = fila3.pop(c3)
                            c3 = c3 - 1
                            p1[4] = p1[4] - 2
                            q1 = q1 + 1
                        elif not recursoDisco2.getStatus():
                            recursoDisco2.setStatus(True)
                            cpu1.setOcupado(True)
                            cpu1.setTempoProcesso(tempo + 2)
                            temp = fila3[c3][4] / 2
                            if temp > 0:
                                mem.updateOcupado(-(fila3[c3][1] / temp))
                            p1 = fila3.pop(c3)
                            c3 = c3 - 1
                            p1[4] = p1[4] - 2
                            q1 = q1 + 1


                    else:
                        cpu1.setOcupado(True)
                        cpu1.setTempoProcesso(tempo + 2)
                        temp = fila3[c3][4] / 2
                        if temp > 0:
                            mem.updateOcupado(-(fila3[c3][1] / temp))
                        p1 = fila3.pop(c3)
                        c3 = c3 - 1
                        p1[4] = p1[4] - 2
                        q1 = q1 + 1
                elif not cpu2.getOcupado():
                    if fila3[c3][5] == 1 and fila3[c3][6] == 1:
                        if not recursoImpressora1.getStatus() and not recursoDisco1.getStatus():
                            recursoDisco1.setStatus(True)
                            recursoImpressora1.setStatus(True)
                            cpu2.setOcupado(True)
                            cpu2.setTempoProcesso(tempo + 2)
                            temp = fila3[c3][4] / 2
                            if temp > 0:
                                mem.updateOcupado(-(fila3[c3][1] / temp))
                            p2 = fila3.pop(c3)
                            c3 = c3 - 1
                            p2[4] = p2[4] - 2
                            q2 = q2 + 1
                        elif not recursoImpressora2.getStatus() and not recursoDisco1.getStatus():
                            recursoDisco1.setStatus(True)
                            recursoImpressora2.setStatus(True)
                            cpu2.setOcupado(True)
                            cpu2.setTempoProcesso(tempo + 2)
                            temp = fila3[c3][4] / 2
                            if temp > 0:
                                mem.updateOcupado(-(fila3[c3][1] / temp))
                            p2 = fila3.pop(c3)
                            c3 = c3 - 1
                            p2[4] = p2[4] - 2
                            q2 = q2 + 1
                        elif not recursoImpressora1.getStatus() and not recursoDisco2.getStatus():
                            recursoDisco2.setStatus(True)
                            recursoImpressora1.setStatus(True)
                            cpu2.setOcupado(True)
                            cpu2.setTempoProcesso(tempo + 2)
                            temp = fila3[c3][4] / 2
                            if temp > 0:
                                mem.updateOcupado(-(fila3[c3][1] / temp))
                            p2 = fila3.pop(c3)
                            c3 = c3 - 1
                            p2[4] = p2[4] - 2
                            q2 = q2 + 1
                        elif not recursoImpressora2.getStatus() and not recursoDisco2.getStatus():
                            recursoDisco2.setStatus(True)
                            recursoImpressora2.setStatus(True)
                            cpu2.setOcupado(True)
                            cpu2.setTempoProcesso(tempo + 2)
                            temp = fila3[c3][4] / 2
                            if temp > 0:
                                mem.updateOcupado(-(fila3[c3][1] / temp))
                            p2 = fila3.pop(c3)
                            c3 = c3 - 1
                            p2[4] = p2[4] - 2
                            q2 = q2 + 1
                    elif fila3[c3][5] == 1:
                        if not recursoImpressora1.getStatus():
                            recursoImpressora1.setStatus(True)
                            cpu2.setOcupado(True)
                            cpu2.setTempoProcesso(tempo + 2)
                            temp = fila3[c3][4] / 2
                            if temp > 0:
                                mem.updateOcupado(-(fila3[c3][1] / temp))
                            p2 = fila3.pop(c3)
                            c3 = c3 - 1
                            p2[4] = p2[4] - 2
                            q2 = q2 + 1
                        elif not recursoImpressora2.getStatus():
                            recursoImpressora1.setStatus(True)
                            cpu2.setOcupado(True)
                            cpu2.setTempoProcesso(tempo + 2)
                            temp = fila3[c3][4] / 2
                            if temp > 0:
                                mem.updateOcupado(-(fila3[c3][1] / temp))
                            p2 = fila3.pop(c3)
                            c3 = c3 - 1
                            p2[4] = p2[4] - 2
                            q2 = q2 + 1

                    elif fila3[c3][6] == 1:
                        if not recursoDisco1.getStatus():
                            recursoDisco1.setStatus(True)
                            cpu2.setOcupado(True)
                            cpu2.setTempoProcesso(tempo + 2)
                            temp = fila3[c3][4] / 2
                            if temp > 0:
                                mem.updateOcupado(-(fila3[c3][1] / temp))
                            p2 = fila3.pop(c3)
                            c3 = c3 - 1
                            p2[4] = p2[4] - 2
                            q2 = q2 + 1
                        elif not recursoDisco2.getStatus():
                            recursoDisco2.setStatus(True)
                            cpu2.setOcupado(True)
                            cpu2.setTempoProcesso(tempo + 2)
                            temp = fila3[c3][4] / 2
                            if temp > 0:
                                mem.updateOcupado(-(fila3[c3][1] / temp))
                            p2 = fila3.pop(c3)
                            c3 = c3 - 1
                            p2[4] = p2[4] - 2
                            q2 = q2 + 1


                    else:
                        cpu2.setOcupado(True)
                        cpu2.setTempoProcesso(tempo + 2)
                        temp = fila3[c3][4] / 2
                        if temp > 0:
                            mem.updateOcupado(-(fila3[c3][1] / temp))
                        p2 = fila3.pop(c3)
                        c3 = c3 - 1
                        p2[4] = p2[4] - 2
                        q2 = q2 + 1
                elif not cpu3.getOcupado():
                    if fila3[c3][5] == 1 and fila3[c3][6] == 1:
                        if not recursoImpressora1.getStatus() and not recursoDisco1.getStatus():
                            recursoDisco1.setStatus(True)
                            recursoImpressora1.setStatus(True)
                            cpu3.setOcupado(True)
                            cpu3.setTempoProcesso(tempo + 2)
                            temp = fila3[c3][4] / 2
                            if temp > 0:
                                mem.updateOcupado(-(fila3[c3][1] / temp))
                            p3 = fila3.pop(c3)
                            c3 = c3 - 1
                            p3[4] = p3[4] - 2
                            q3 = q3 + 1
                        elif not recursoImpressora2.getStatus() and not recursoDisco1.getStatus():
                            recursoDisco1.setStatus(True)
                            recursoImpressora2.setStatus(True)
                            cpu3.setOcupado(True)
                            cpu3.setTempoProcesso(tempo + 2)
                            temp = fila3[c3][4] / 2
                            if temp > 0:
                                mem.updateOcupado(-(fila3[c3][1] / temp))
                            p3 = fila3.pop(c3)
                            c3 = c3 - 1
                            p3[4] = p3[4] - 2
                            q3 = q3 + 1
                        elif not recursoImpressora1.getStatus() and not recursoDisco2.getStatus():
                            recursoDisco2.setStatus(True)
                            recursoImpressora1.setStatus(True)
                            cpu3.setOcupado(True)
                            cpu3.setTempoProcesso(tempo + 2)
                            temp = fila3[c3][4] / 2
                            if temp > 0:
                                mem.updateOcupado(-(fila3[c3][1] / temp))
                            p3 = fila3.pop(c3)
                            c3 = c3 - 1
                            p3[4] = p3[4] - 2
                            q3 = q3 + 1
                        elif not recursoImpressora2.getStatus() and not recursoDisco2.getStatus():
                            recursoDisco2.setStatus(True)
                            recursoImpressora2.setStatus(True)
                            cpu3.setOcupado(True)
                            cpu3.setTempoProcesso(tempo + 2)
                            temp = fila3[c3][4] / 2
                            if temp > 0:
                                mem.updateOcupado(-(fila3[c3][1] / temp))
                            p3 = fila3.pop(c3)
                            c3 = c3 - 1
                            p3[4] = p3[4] - 2
                            q3 = q3 + 1
                    elif fila3[c3][5] == 1:
                        if not recursoImpressora1.getStatus():
                            recursoImpressora1.setStatus(True)
                            cpu3.setOcupado(True)
                            cpu3.setTempoProcesso(tempo + 2)
                            temp = fila3[c3][4] / 2
                            if temp > 0:
                                mem.updateOcupado(-(fila3[c3][1] / temp))
                            p3 = fila3.pop(c3)
                            c3 = c3 - 1
                            p3[4] = p3[4] - 2
                            q3 = q3 + 1
                        elif not recursoImpressora2.getStatus():
                            recursoImpressora1.setStatus(True)
                            cpu3.setOcupado(True)
                            cpu3.setTempoProcesso(tempo + 2)
                            temp = fila3[c3][4] / 2
                            if temp > 0:
                                mem.updateOcupado(-(fila3[c3][1] / temp))
                            p3 = fila3.pop(c3)
                            c3 = c3 - 1
                            p3[4] = p3[4] - 2
                            q3 = q3 + 1

                    elif fila3[c3][6] == 1:
                        if not recursoDisco1.getStatus():
                            recursoDisco1.setStatus(True)
                            cpu3.setOcupado(True)
                            cpu3.setTempoProcesso(tempo + 2)
                            temp = fila3[c3][4] / 2
                            if temp > 0:
                                mem.updateOcupado(-(fila3[c3][1] / temp))
                            p3 = fila3.pop(c3)
                            c3 = c3 - 1
                            p3[4] = p3[4] - 2
                            q3 = q3 + 1
                        elif not recursoDisco2.getStatus():
                            recursoDisco2.setStatus(True)
                            cpu3.setOcupado(True)
                            cpu3.setTempoProcesso(tempo + 2)
                            temp = fila3[c3][4] / 2
                            if temp > 0:
                                mem.updateOcupado(-(fila3[c3][1] / temp))
                            p3 = fila3.pop(c3)
                            c3 = c3 - 1
                            p3[4] = p3[4] - 2
                            q3 = q3 + 1


                    else:
                        cpu3.setOcupado(True)
                        cpu3.setTempoProcesso(tempo + 2)
                        temp = fila3[c3][4] / 2
                        if temp > 0:
                            mem.updateOcupado(-(fila3[c3][1] / temp))
                        p3 = fila3.pop(c3)
                        c3 = c3 - 1
                        p3[4] = p3[4] - 2
                        q3 = q3 + 1
                elif not cpu4.getOcupado():
                    if fila3[c3][5] == 1 and fila3[c3][6] == 1:
                        if not recursoImpressora1.getStatus() and not recursoDisco1.getStatus():
                            recursoDisco1.setStatus(True)
                            recursoImpressora1.setStatus(True)
                            cpu4.setOcupado(True)
                            cpu4.setTempoProcesso(tempo + 2)
                            temp = fila3[c3][4] / 2
                            if temp > 0:
                                mem.updateOcupado(-(fila3[c3][1] / temp))
                            p4 = fila3.pop(c3)
                            c3 = c3 - 1
                            p4[4] = p4[4] - 2
                            q4 = q4 + 1
                        elif not recursoImpressora2.getStatus() and not recursoDisco1.getStatus():
                            recursoDisco1.setStatus(True)
                            recursoImpressora2.setStatus(True)
                            cpu4.setOcupado(True)
                            cpu4.setTempoProcesso(tempo + 2)
                            temp = fila3[c3][4] / 2
                            if temp > 0:
                                mem.updateOcupado(-(fila3[c3][1] / temp))
                            p4 = fila3.pop(c3)
                            c3 = c3 - 1
                            p4[4] = p4[4] - 2
                            q4 = q4 + 1
                        elif not recursoImpressora1.getStatus() and not recursoDisco2.getStatus():
                            recursoDisco2.setStatus(True)
                            recursoImpressora1.setStatus(True)
                            cpu4.setOcupado(True)
                            cpu4.setTempoProcesso(tempo + 2)
                            temp = fila3[c3][4] / 2
                            if temp > 0:
                                mem.updateOcupado(-(fila3[c3][1] / temp))
                            p4 = fila3.pop(c3)
                            c3 = c3 - 1
                            p4[4] = p4[4] - 2
                            q4 = q4 + 1
                        elif not recursoImpressora2.getStatus() and not recursoDisco2.getStatus():
                            recursoDisco2.setStatus(True)
                            recursoImpressora2.setStatus(True)
                            cpu4.setOcupado(True)
                            cpu4.setTempoProcesso(tempo + 2)
                            temp = fila3[c3][4] / 2
                            if temp > 0:
                                mem.updateOcupado(-(fila3[c3][1] / temp))
                            p4 = fila3.pop(c3)
                            c3 = c3 - 1
                            p4[4] = p4[4] - 2
                            q4 = q4 + 1
                    elif fila3[c3][5] == 1:
                        if not recursoImpressora1.getStatus():
                            recursoImpressora1.setStatus(True)
                            cpu4.setOcupado(True)
                            cpu4.setTempoProcesso(tempo + 2)
                            temp = fila3[c3][4] / 2
                            if temp > 0:
                                mem.updateOcupado(-(fila3[c3][1] / temp))
                            p4 = fila3.pop(c3)
                            c3 = c3 - 1
                            p4[4] = p4[4] - 2
                            q4 = q4 + 1
                        elif not recursoImpressora2.getStatus():
                            recursoImpressora1.setStatus(True)
                            cpu4.setOcupado(True)
                            cpu4.setTempoProcesso(tempo + 2)
                            temp = fila3[c3][4] / 2
                            if temp > 0:
                                mem.updateOcupado(-(fila3[c3][1] / temp))
                            p4 = fila3.pop(c3)
                            c3 = c3 - 1
                            p4[4] = p4[4] - 2
                            q4 = q4 + 1

                    elif fila3[c3][6] == 1:
                        if not recursoDisco1.getStatus():
                            recursoDisco1.setStatus(True)
                            cpu4.setOcupado(True)
                            cpu4.setTempoProcesso(tempo + 2)
                            temp = fila3[c3][4] / 2
                            if temp > 0:
                                mem.updateOcupado(-(fila3[c3][1] / temp))
                            p4 = fila3.pop(c3)
                            c3 = c3 - 1
                            p4[4] = p4[4] - 2
                            q4 = q4 + 1
                        elif not recursoDisco2.getStatus():
                            recursoDisco2.setStatus(True)
                            cpu4.setOcupado(True)
                            cpu4.setTempoProcesso(tempo + 2)
                            temp = fila3[c3][4] / 2
                            if temp > 0:
                                mem.updateOcupado(-(fila3[c3][1] / temp))
                            p4 = fila3.pop(c3)
                            c3 = c3 - 1
                            p4[4] = p4[4] - 2
                            q4 = q4 + 1


                    else:
                        cpu4.setOcupado(True)
                        cpu4.setTempoProcesso(tempo + 2)
                        temp = fila3[c3][4] / 2
                        if temp > 0:
                            mem.updateOcupado(-(fila3[c3][1] / temp))
                        p4 = fila3.pop(c3)
                        c3 = c3 - 1
                        p4[4] = p4[4] - 2
                        q4 = q4 + 1
    aux1, aux2, aux3 = 0, 0, 0
    print("pop ", pop1)

    #verifica todas as filas se o processo que foi retirado esta em alguma fila
    if len(fila1) > 0:
        for i in fila1:
            if len(pop1) > 0:
                if i[0] == pop1[0]:
                    aux1 = 1
            if len(po1) > 0:
                if i[0] == po1[0]:
                    aux1 = 1
            if len(p1) > 0:
                if i[0] == p1[0]:
                    aux1 = 1
            if len(pop2) > 0:
                if i[0] == pop2[0]:
                    aux1 = 1
            if len(po2) > 0:
                if i[0] == po2[0]:
                    aux1 = 1
            if len(p2) > 0:
                if i[0] == p2[0]:
                    aux1 = 1
            if len(pop3) > 0:
                if i[0] == pop3[0]:
                    aux1 = 1
            if len(po3) > 0:
                if i[0] == po3[0]:
                    aux1 = 1
            if len(p3) > 0:
                if i[0] == p3[0]:
                    aux1 = 1
            if len(pop4) > 0:
                if i[0] == pop4[0]:
                    aux1 = 1
            if len(po4) > 0:
                if i[0] == po4[0]:
                    aux1 = 1
            if len(p4) > 0:
                if i[0] == p4[0]:
                    aux1 = 1
    if len(fila2) > 0:
        for i in fila2:
            if len(pop1) > 0:
                if i[0] == pop1[0]:
                    aux2 = 1
            if len(po1) > 0:
                if i[0] == po1[0]:
                    aux2 = 1
            if len(p1) > 0:
                if i[0] == p1[0]:
                    aux2 = 1
            if len(pop2) > 0:
                if i[0] == pop2[0]:
                    aux2 = 1
            if len(po2) > 0:
                if i[0] == po2[0]:
                    aux2 = 1
            if len(p2) > 0:
                if i[0] == p2[0]:
                    aux2 = 1
            if len(pop3) > 0:
                if i[0] == pop3[0]:
                    aux2 = 1
            if len(po3) > 0:
                if i[0] == po3[0]:
                    aux2 = 1
            if len(p3) > 0:
                if i[0] == p3[0]:
                    aux2 = 1
            if len(pop4) > 0:
                if i[0] == pop4[0]:
                    aux2 = 1
            if len(po4) > 0:
                if i[0] == po4[0]:
                    aux2 = 1
            if len(p4) > 0:
                if i[0] == p4[0]:
                    aux2 = 1
    if len(fila3) > 0:
        for i in fila3:
            if len(pop1) > 0:
                if i[0] == pop1[0]:
                    aux2 = 1
            if len(po1) > 0:
                if i[0] == po1[0]:
                    aux2 = 1
            if len(p1) > 0:
                if i[0] == p1[0]:
                    aux2 = 1
            if len(pop2) > 0:
                if i[0] == pop2[0]:
                    aux2 = 1
            if len(po2) > 0:
                if i[0] == po2[0]:
                    aux2 = 1
            if len(p2) > 0:
                if i[0] == p2[0]:
                    aux2 = 1
            if len(pop3) > 0:
                if i[0] == pop3[0]:
                    aux2 = 1
            if len(po3) > 0:
                if i[0] == po3[0]:
                    aux2 = 1
            if len(p3) > 0:
                if i[0] == p3[0]:
                    aux2 = 1
            if len(pop4) > 0:
                if i[0] == pop4[0]:
                    aux2 = 1
            if len(po4) > 0:
                if i[0] == po4[0]:
                    aux2 = 1
            if len(p4) > 0:
                if i[0] == p4[0]:
                    aux2 = 1

    #verifica se o tempo de finalizar o procesos que ta executando
    #é igual ao tempo do sistema
    # se for libera a cpu e os recursos
    # faz isso para todas as cpus
    # adiciona o processo na proxima fila

    if cpu1.getTempoProcesso() == tempo:
        if len(pp1) > 0:
            if pp1[5] == 1:
                if recursoImpressora1.getStatus():
                    recursoImpressora1.setStatus(False)
                elif recursoImpressora2.getStatus():
                    recursoImpressora2.setStatus(False)
            if pp1[6] == 1:
                if recursoDisco1.getStatus():
                    recursoDisco1.setStatus(False)
                elif recursoDisco2.getStatus():
                    recursoDisco2.setStatus(False)

        cpu1.setOcupado(False)
        cpu1.setTempoProcesso(0)
        if len(pop1) > 0:
            if pop1[5] == 1:
                if recursoImpressora1.getStatus():
                    recursoImpressora1.setStatus(False)
                elif recursoImpressora2.getStatus():
                    recursoImpressora2.setStatus(False)
            if pop1[6] == 1:
                if recursoDisco1.getStatus():
                    recursoDisco1.setStatus(False)
                elif recursoDisco2.getStatus():
                    recursoDisco2.setStatus(False)
            if aux2 == 0 and aux3 == 0 and aux1 == 0:
                if pop1[4] <= 0:
                    pass
                else:
                    fila2.append(pop1)
            q1 = 0
        if len(po1) > 0:
            if po1[5] == 1:
                if recursoImpressora1.getStatus():
                    recursoImpressora1.setStatus(False)
                elif recursoImpressora2.getStatus():
                    recursoImpressora2.setStatus(False)
            if po1[6] == 1:
                if recursoDisco1.getStatus():
                    recursoDisco1.setStatus(False)
                elif recursoDisco2.getStatus():
                    recursoDisco2.setStatus(False)
            if aux2 == 0 and aux3 == 0 and aux1 == 0:
                if po1[4] <= 0:
                    pass
                else:
                    fila3.append(po1)
            q1 = 0
        if len(p1) > 0:
            if p1[5] == 1:
                if recursoImpressora1.getStatus():
                    recursoImpressora1.setStatus(False)
                elif recursoImpressora2.getStatus():
                    recursoImpressora2.setStatus(False)
            if p1[6] == 1:
                if recursoDisco1.getStatus():
                    recursoDisco1.setStatus(False)
                elif recursoDisco2.getStatus():
                    recursoDisco2.setStatus(False)
            if aux2 == 0 and aux3 == 0 and aux1 == 0:
                if p1[4] <= 0:
                    pass
                else:
                    fila1.append(p1)
            q1 = 0
    if cpu2.getTempoProcesso() == tempo:
        if len(pp2) > 0:
            if pp2[5] == 1:
                if recursoImpressora1.getStatus():
                    recursoImpressora1.setStatus(False)
                elif recursoImpressora2.getStatus():
                    recursoImpressora2.setStatus(False)
            if pp2[6] == 1:
                if recursoDisco1.getStatus():
                    recursoDisco1.setStatus(False)
                elif recursoDisco2.getStatus():
                    recursoDisco2.setStatus(False)

        cpu2.setOcupado(False)
        cpu2.setTempoProcesso(0)
        if len(pop2) > 0:
            if pop2[5] == 1:
                if recursoImpressora1.getStatus():
                    recursoImpressora1.setStatus(False)
                elif recursoImpressora2.getStatus():
                    recursoImpressora2.setStatus(False)
            if pop2[6] == 1:
                if recursoDisco1.getStatus():
                    recursoDisco1.setStatus(False)
                elif recursoDisco2.getStatus():
                    recursoDisco2.setStatus(False)
            if aux2 == 0 and aux3 == 0 and aux1 == 0:
                if pop2[4] <= 0:
                    pass
                else:
                    fila2.append(pop2)
            q2 = 0
        if len(po2) > 0:
            if po2[5] == 1:
                if recursoImpressora1.getStatus():
                    recursoImpressora1.setStatus(False)
                elif recursoImpressora2.getStatus():
                    recursoImpressora2.setStatus(False)
            if po2[6] == 1:
                if recursoDisco1.getStatus():
                    recursoDisco1.setStatus(False)
                elif recursoDisco2.getStatus():
                    recursoDisco2.setStatus(False)
            if aux2 == 0 and aux3 == 0 and aux1 == 0:
                if po2[4] <= 0:
                    pass
                else:
                    fila3.append(po2)
            q2 = 0
        if len(p2) > 0:
            if p2[5] == 1:
                if recursoImpressora1.getStatus():
                    recursoImpressora1.setStatus(False)
                elif recursoImpressora2.getStatus():
                    recursoImpressora2.setStatus(False)
            if p2[6] == 1:
                if recursoDisco1.getStatus():
                    recursoDisco1.setStatus(False)
                elif recursoDisco2.getStatus():
                    recursoDisco2.setStatus(False)
            if aux2 == 0 and aux3 == 0 and aux1 == 0:
                if p2[4] <= 0:
                    pass
                else:
                    fila1.append(p2)
            q2 = 0
    if cpu3.getTempoProcesso() == tempo:
        if len(pp3) > 0:
            if pp3[5] == 1:
                if recursoImpressora1.getStatus():
                    recursoImpressora1.setStatus(False)
                elif recursoImpressora2.getStatus():
                    recursoImpressora2.setStatus(False)
            if pp3[6] == 1:
                if recursoDisco1.getStatus():
                    recursoDisco1.setStatus(False)
                elif recursoDisco2.getStatus():
                    recursoDisco2.setStatus(False)

        cpu3.setOcupado(False)
        cpu3.setTempoProcesso(0)
        if len(pop3) > 0:
            if pop3[5] == 1:
                if recursoImpressora1.getStatus():
                    recursoImpressora1.setStatus(False)
                elif recursoImpressora2.getStatus():
                    recursoImpressora2.setStatus(False)
            if pop3[6] == 1:
                if recursoDisco1.getStatus():
                    recursoDisco1.setStatus(False)
                elif recursoDisco2.getStatus():
                    recursoDisco2.setStatus(False)
            if aux2 == 0 and aux3 == 0 and aux1 == 0:
                if pop3[4] <= 0:
                    pass
                else:
                    fila2.append(pop3)
            q3 = 0
        if len(po3) > 0:
            if po3[5] == 1:
                if recursoImpressora1.getStatus():
                    recursoImpressora1.setStatus(False)
                elif recursoImpressora2.getStatus():
                    recursoImpressora2.setStatus(False)
            if po3[6] == 1:
                if recursoDisco1.getStatus():
                    recursoDisco1.setStatus(False)
                elif recursoDisco2.getStatus():
                    recursoDisco2.setStatus(False)
            if aux2 == 0 and aux3 == 0 and aux1 == 0:
                if po3[4] <= 0:
                    pass
                else:
                    fila3.append(po3)
            q3 = 0
        if len(p3) > 0:
            if p3[5] == 1:
                if recursoImpressora1.getStatus():
                    recursoImpressora1.setStatus(False)
                elif recursoImpressora2.getStatus():
                    recursoImpressora2.setStatus(False)
            if p3[6] == 1:
                if recursoDisco1.getStatus():
                    recursoDisco1.setStatus(False)
                elif recursoDisco2.getStatus():
                    recursoDisco2.setStatus(False)
            if aux2 == 0 and aux3 == 0 and aux1 == 0:
                if p3[4] <= 0:
                    pass
                else:
                    fila1.append(p3)
            q3 = 0
    if cpu4.getTempoProcesso() == tempo:
        if len(pp4) > 0:
            if pp4[5] == 1:
                if recursoImpressora1.getStatus():
                    recursoImpressora1.setStatus(False)
                elif recursoImpressora2.getStatus():
                    recursoImpressora2.setStatus(False)
            if pp4[6] == 1:
                if recursoDisco1.getStatus():
                    recursoDisco1.setStatus(False)
                elif recursoDisco2.getStatus():
                    recursoDisco2.setStatus(False)

        cpu4.setOcupado(False)
        cpu4.setTempoProcesso(0)
        if len(pop4) > 0:
            if pop4[5] == 1:
                if recursoImpressora1.getStatus():
                    recursoImpressora1.setStatus(False)
                elif recursoImpressora2.getStatus():
                    recursoImpressora2.setStatus(False)
            if pop4[6] == 1:
                if recursoDisco1.getStatus():
                    recursoDisco1.setStatus(False)
                elif recursoDisco2.getStatus():
                    recursoDisco2.setStatus(False)
            if aux2 == 0 and aux3 == 0 and aux1 == 0:
                if pop4[4] <= 0:
                    pass
                else:
                    fila2.append(pop4)
            q4 = 0
        if len(po4) > 0:
            if po4[5] == 1:
                if recursoImpressora1.getStatus():
                    recursoImpressora1.setStatus(False)
                elif recursoImpressora2.getStatus():
                    recursoImpressora2.setStatus(False)
            if po4[6] == 1:
                if recursoDisco1.getStatus():
                    recursoDisco1.setStatus(False)
                elif recursoDisco2.getStatus():
                    recursoDisco2.setStatus(False)
            if aux2 == 0 and aux3 == 0 and aux1 == 0:
                if po4[4] <= 0:
                    pass
                else:
                    fila3.append(po4)
            q4 = 0
        if len(p4) > 0:
            if p4[5] == 1:
                if recursoImpressora1.getStatus():
                    recursoImpressora1.setStatus(False)
                elif recursoImpressora2.getStatus():
                    recursoImpressora2.setStatus(False)
            if p4[6] == 1:
                if recursoDisco1.getStatus():
                    recursoDisco1.setStatus(False)
                elif recursoDisco2.getStatus():
                    recursoDisco2.setStatus(False)
            if aux2 == 0 and aux3 == 0 and aux1 == 0:
                if p4[4] <= 0:
                    pass
                else:
                    fila1.append(p4)
            q4 = 0
    # se a memoria tiver espaco traz oque estiver no disco
    if mem.getOcupado() < mem.getTamanho():
        if len(listaDisco) > 0:
            for i in range(len(listaDisco)):
                espaco = mem.getTamanho() - mem.getOcupado()
                if espaco >= listaDisco[i][1]:
                    temp = listaDisco.pop(i)
                    if temp[2] == 0:
                        fila_ftr.append(temp)
                    else:
                        fila1.append(temp)

    prioridadeMaiorQueZero = False

    for i in fila_ftr:
        if i[3] <= tempo:
            print("ftr ", i)
    for i in fila1:
        if i[3] <= tempo:
            print("fila 1", i)
    for i in fila2:
        if i[3] <= tempo:
            print("fila 2", i)
    for i in fila3:
        if i[3] <= tempo:
            print("fila 3", i)

    print("MEM: ", mem.getOcupado())
    print("c1 :", c1)
    print("c2 :", c2)
    print("c3 :", c3)

    tempo = tempo + 1
    print(tempo, ": ", cpu1.getOcupado(), cpu2.getOcupado(), cpu3.getOcupado(), cpu4.getOcupado())
    print("---------------------------------------------------------------")


proce = Processo()

valores = proce.leProcesso("entrada.txt")
k = 0

for i in valores:
    linha = []
    for j in range(1):
        linha.append(k)
        linha.append(int(i[3]))
        linha.append(int(i[1]))
        linha.append(int(i[0]))
        linha.append(int(i[2]))
        linha.append(int(i[4]))
        linha.append(int(i[5]))
        k = k + 1
    p.append(linha)

# instancia os processos
for i in range(len(valores)):
    if p[i][1] <= 512:
        if mem.getOcupado() <= mem.getTamanho():
            np = Processo()
            processo.append(np)
            processo[i].setCod(p[i][0])
            processo[i].setTamanho(p[i][1])
            processo[i].setPrioridade(p[i][2])
            processo[i].setTempoDeChegada(p[i][3])
            processo[i].setTempoDeProcesso(p[i][4])
            processo[i].setImpressora(p[i][5])
            processo[i].setDisco(p[i][6])
            mem.updateOcupado(p[i][1])
        else:
            np = Processo()
            listaDisco = disco.swap(listaDisco, p[i][0], p[i][1], p[i][2], p[i][3], np)
            d = Disco()
            d.setDisco(listaDisco)
            listaDisco.append(d)

pord = processo[0].bubblesort(p)

#coloca os processos numa fila geral
for i in pord:
    fila_geral.append(i)

# distribui os processos nas filas ftr e 1 de acordo com a prioridade
for i in fila_geral:
    if i[2] == 0:
        fila_ftr.append(i)
    else:
        fila1.append(i)

#instancia o timercontinuo
#que executa a funcao clock de 1 em 1 segundo
t = TimerContinuo(1.0, clock)
t.start()
k = 0

#parte grafica
while True:
    x = 10
    y1 = 10
    y2 = 10
    y3 = 10
    y4 = 10
    s = ""
    for i in range(tempo):
        s += " |"
    #mostra os processos nas filas
    if k == tempo:
        fundo.draw()
        for j in fila_ftr:
            if j[3] <= tempo:
                barra.append(Sprite("img/barra.png"))
                for i in barra:
                    i.set_position(x, y1)
                    janela.draw_text(str(j[0]), 250 + i.x, 275 + i.y, size=15, color=(0, 0, 0), font_name="Arial",
                                     bold=True,
                                     italic=False)
                    i.draw()

                y1 += 20

        for j in fila1:
            if j[3] <= tempo:
                barra.append(Sprite("img/barra.png"))
                for i in barra:
                    i.set_position(x + 150, y2)
                    janela.draw_text(str(j[0]), 250 + i.x, 275 + i.y, size=15, color=(0, 0, 0), font_name="Arial",
                                     bold=True,
                                     italic=False)
                    i.draw()
                y2 += 20
        for j in fila2:
            if j[3] <= tempo:
                barra.append(Sprite("img/barra.png"))
                for i in barra:
                    i.set_position(x + 300, y3)
                    janela.draw_text(str(j[0]), 250 + i.x, 275 + i.y, size=15, color=(0, 0, 0), font_name="Arial",
                                     bold=True,
                                     italic=False)
                    i.draw()
                y3 += 20
        for j in fila3:
            if j[3] <= tempo:
                barra.append(Sprite("img/barra.png"))
                for i in barra:
                    i.set_position(x + 450, y4)
                    janela.draw_text(str(j[0]), 250 + i.x, 275 + i.y, size=15, color=(0, 0, 0), font_name="Arial",
                                     bold=True,
                                     italic=False)
                    i.draw()
                y4 += 20
        y1, y2, y3, y4 = 10, 10, 10, 10
    else:
        k += 1
    #mostra cada cpu se esta ocupado ou livre
    if cpu1.getOcupado():
        fcpu1.hide()
        ocpu1.unhide()
    else:
        fcpu1.unhide()
        ocpu1.hide()

    if cpu2.getOcupado():
        fcpu2.hide()
        ocpu2.unhide()
    else:
        fcpu2.unhide()
        ocpu2.hide()

    if cpu3.getOcupado():
        fcpu3.hide()
        ocpu3.unhide()
    else:
        fcpu3.unhide()
        ocpu3.hide()

    if cpu4.getOcupado():
        fcpu4.hide()
        ocpu4.unhide()
    else:
        fcpu4.unhide()
        ocpu4.hide()
    #mostra cada recurso se esta ocupado ou livre
    if recursoImpressora1.getStatus():
        fimpressora1.hide()
        oimpressora1.unhide()
    else:
        fimpressora1.unhide()
        oimpressora1.hide()

    if recursoImpressora2.getStatus():
        fimpressora2.hide()
        oimpressora2.unhide()
    else:
        fimpressora2.unhide()
        oimpressora2.hide()

    if recursoDisco1.getStatus():
        fdisco1.hide()
        odisco1.unhide()
    else:
        fdisco1.unhide()
        odisco1.hide()

    if recursoDisco2.getStatus():
        fdisco2.hide()
        odisco2.unhide()
    else:
        fdisco2.unhide()
        odisco2.hide()

    fcpu1.draw()
    fcpu2.draw()
    fcpu3.draw()
    fcpu4.draw()
    ocpu1.draw()
    ocpu2.draw()
    ocpu3.draw()
    ocpu4.draw()
    oimpressora1.draw()
    oimpressora2.draw()
    fimpressora1.draw()
    fimpressora2.draw()
    odisco1.draw()
    odisco2.draw()
    fdisco1.draw()
    fdisco2.draw()

    janela.draw_text("Tempo: " + s, 10, 10, size=15, color=(0, 0, 0), font_name="Arial", bold=True,
                     italic=False)
    janela.draw_text("Fila FTR", 210, 250, size=25, color=(0, 0, 0), font_name="Arial", bold=True, italic=False)
    janela.draw_text("Fila 1", 370, 250, size=25, color=(0, 0, 0), font_name="Arial", bold=True, italic=False)
    janela.draw_text("Fila 2", 520, 250, size=25, color=(0, 0, 0), font_name="Arial", bold=True, italic=False)
    janela.draw_text("Fila 3", 670, 250, size=25, color=(0, 0, 0), font_name="Arial", bold=True, italic=False)

    janela.update()
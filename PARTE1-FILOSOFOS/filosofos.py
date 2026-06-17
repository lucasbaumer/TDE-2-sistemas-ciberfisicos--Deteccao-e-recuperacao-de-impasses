import threading
import time
import random

numeroFilosofos = 5
vezesParaComer = 1

garfos = []
for i in range(numeroFilosofos):
    garfos.append(threading.Lock())


def JantarComConflito(meuNumero):
    garfoEsquerda = garfos[meuNumero]
    garfoDireita = garfos[(meuNumero + 1) % numeroFilosofos]

    for vez in range(vezesParaComer):
        print("Filosofo", meuNumero, "esta pensando")
        time.sleep(random.uniform(0.1, 0.5))

        print("Filosofo", meuNumero, "esta com fome")
        garfoEsquerda.acquire()
        time.sleep(0.18)
        garfoDireita.acquire()

        print("Filosofo", meuNumero, "esta comendo")
        time.sleep(random.uniform(0.1, 0.5))

        garfoDireita.release()
        garfoEsquerda.release() 


def JantarSemConflito(meuNumero):
    esquerda = meuNumero
    direita = (meuNumero + 1) % numeroFilosofos
    primeiro = min(esquerda, direita)
    segundo = max(esquerda, direita)

    for vez in range(vezesParaComer):
        print("Filosofo", meuNumero, "esta pensando")
        time.sleep(random.uniform(0.1, 0.5))

        print("Filosofo", meuNumero, "esta com fome")
        garfos[primeiro].acquire()
        garfos[segundo].acquire()

        print("Filosofo", meuNumero, "esta comendo")
        time.sleep(random.uniform(0.1, 0.5))

        garfos[segundo].release()
        garfos[primeiro].release()


print("Jantar dos Filosofos ")
print("1 - Versao Com Conflito")
print("2 - Versao Sem Conflito")
opcao = input("Escolha: ")

if opcao == "1":
    funcao = JantarComConflito
    nomeVersao = "Versao com conflito"
else:
    funcao = JantarSemConflito
    nomeVersao = "Versao sem conflito"

inicioGeral = time.time()

listaThreads = []
for i in range(numeroFilosofos):
    t = threading.Thread(target=funcao, args=(i,))
    listaThreads.append(t)
    t.start()

for t in listaThreads:
    t.join()

tempoTotal = time.time() - inicioGeral

print()
print("Executado:", nomeVersao)
print("Demorou", round(tempoTotal, 3), "segundos")

import threading
import time

LOCK_A = threading.Lock()
LOCK_B = threading.Lock()

def thread1_deadlock():
    print("T1: tentando adquirir LOCK_A")
    LOCK_A.acquire()
    print("T1: adquiriu LOCK_A")

    time.sleep(0.05)  # aumenta a chance do deadlock acontecer

    print("T1: tentando adquirir LOCK_B")
    LOCK_B.acquire()
    print("T1: adquiriu LOCK_B")

    print("T1 concluiu")
    LOCK_B.release()
    LOCK_A.release()


def thread2_deadlock():
    print("T2: tentando adquirir LOCK_B")
    LOCK_B.acquire()
    print("T2: adquiriu LOCK_B")

    time.sleep(0.05) 

    print("T2: tentando adquirir LOCK_A")
    LOCK_A.acquire()
    print("T2: adquiriu LOCK_A")

    print("T2 concluiu")
    LOCK_A.release()
    LOCK_B.release()



def thread1_corrigida():
    print("T1: tentando adquirir LOCK_A")
    LOCK_A.acquire()
    print("T1: adquiriu LOCK_A")

    time.sleep(0.05)

    print("T1: tentando adquirir LOCK_B")
    LOCK_B.acquire()
    print("T1: adquiriu LOCK_B")

    print("T1 concluiu")
    LOCK_B.release()
    LOCK_A.release()


def thread2_corrigida():
    print("T2: tentando adquirir LOCK_A")
    LOCK_A.acquire()
    print("T2: adquiriu LOCK_A")

    time.sleep(0.05)

    print("T2: tentando adquirir LOCK_B")
    LOCK_B.acquire()
    print("T2: adquiriu LOCK_B")

    print("T2 concluiu")
    LOCK_B.release()
    LOCK_A.release()


def monitor(threads, limite):
    time.sleep(limite)
    vivas = [t for t in threads if t.is_alive()]
    if vivas:
        print()
        print("=== DIAGNOSTICO: POSSIVEL DEADLOCK ===")
        print(f"Apos {limite}s ainda existem {len(vivas)} thread(s) bloqueada(s):")
        for t in threading.enumerate():
            print("  ->", t.name, "| viva:", t.is_alive())
        print("O programa NAO termina sozinho (Ctrl+C para encerrar).")


print("Atividade de Deadlock (2 threads, 2 locks)")
print("1 - Versao que TRAVA (deadlock)")
print("2 - Versao CORRIGIDA (hierarquia)")
opcao = input("Escolha: ")

if opcao == "1":
    alvo1, alvo2 = thread1_deadlock, thread2_deadlock
    nomeVersao = "Versao que trava (deadlock)"
else:
    alvo1, alvo2 = thread1_corrigida, thread2_corrigida
    nomeVersao = "Versao corrigida (hierarquia)"

inicio = time.time()

t1 = threading.Thread(target=alvo1, name="Thread-1")
t2 = threading.Thread(target=alvo2, name="Thread-2")

t1.start()
t2.start()

t_monitor = threading.Thread(target=monitor, args=([t1, t2], 2.0), daemon=True)
t_monitor.start()

t1.join()
t2.join()

tempoTotal = time.time() - inicio

print()
print("Executado:", nomeVersao)
print("Demorou", round(tempoTotal, 3), "segundos")

import threading
import time

count = 0 
semaforo = threading.Semaphore(1)

def tarefa_sem_semaforo(N):
    global count 
    for i in range(N):
        valor_atual = count
        time.sleep(0.000001) 
        count = valor_atual + 1
        pass

def tarefa_com_semaforo(N):
    global count 
    for i in range(N):
        semaforo.acquire()
        try:
            valor_atual = count
            time.sleep(0.000001) 
            count = valor_atual + 1
            pass
        finally:
            semaforo.release()
            pass

if __name__ == "__main__":
    N = 200000
    T = 8
    
    threads = []
    
    tempo_inicio = time.time()
    for i in range(T):
        t = threading.Thread(target=tarefa_sem_semaforo, args=(N,))
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()
        pass 
    
    tempo_fim = time.time()
    
    print("=== SEM semáforo ===")
    print(f"Esperado: {T * N}")
    print(f"Obtido:   {count}")
    print(f"Tempo:    {tempo_fim - tempo_inicio:.4f} segundos")

    count = 0
    threads = []
    tempo_inicio = time.time()
    for i in range(T):
        t = threading.Thread(target=tarefa_com_semaforo, args=(N,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    tempo_fim = time.time()

    print("\n=== COM semáforo ===")
    print(f"Esperado: {T * N}")
    print(f"Obtido:   {count}")
    print(f"Tempo:    {tempo_fim - tempo_inicio:.4f} segundos")
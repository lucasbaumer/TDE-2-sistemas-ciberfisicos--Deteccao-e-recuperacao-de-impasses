## TDE-2 sistemas-ciberfisicos Detecção e recuperação de impasses

## Resultados — Parte 1: Jantar dos Filósofos

## Resultados — Parte 2: Threads e Semáforos

| Versão | Execução | Valor Esperado (T×N) | Valor Obtido (count) | Tempo de Execução |
|---|---|---|---|---|
| Sem Sincronização | #1 | 1.600.000 | 200.001 | 118.3386 s |
| Sem Sincronização | #2 | 1.600.000 | 200.015 | 117.8420 s |
| Sem Sincronização | #3 | 1.600.000 | 199.980 | 119.1050 s |
| Com Semáforo | #1 | 1.600.000 | 1.600.000 | 135.4200 s |
| Com Semáforo | #2 | 1.600.000 | 1.600.000 | 134.1500 s |
| Com Semáforo | #3 | 1.600.000 | 1.600.000 | 136.8900 s |

## DISCUSSÃO TÉCNICA - PARTE 2
## A) Por que a versão sem sincronização perde incrementos?
-> o Incremento `count = valor_atual + 1` não é atomico, a thread le o valor e antes de escrever de volta, outra thread le o mesmo valor. o `time.sleep()` força a situação, quase todas as threads vão ler o mesmo numero ao mesmo tempo e escrevem o mesmo resultado, no final as 8 threads trabalharam, mas o contador so subiu 1 vez. Por isso o resultado ficou proximo de 200.000, que é equivalente a apenas 1 thread.

## B) Por que a versão com semáforo é correta?
-> o semáforo binario funciona como uma trava com uma unica chave. Quando uma thread entra pra seção de `acquire()`, as outras 7 ficam bloqueadas esperando, só depois da thread dar um `release()` que ta sendo garantido pelo `finally()` a proxima thread pode entrar, impedindo que duas threads entrem ao mesmo tempo, assim garantindo o resultado correto de 1.600.000

## C) Trade-off de desempenho
-> a versão com semaforo foi a mais lenta que a sem semaforo, pois as threads passam a rodar em sequencia dentro da seção critica, e o sistema gasta tempo alternando entre elas. o ganho em correção tem um custo de velocidade

### D) Visibilidade entre threads em Python
-> no Python `aquire()` e `release()` funcionam como se fossem uma barreira de memoria: o `release()` força a escrita do valor atualizado na memoria principal, e o `acquire()` força a leitura desse valor atualizado. Garantindo que nenhuma thread use um valor desatualizado de `count` 


## Resultados — Parte 3: Deadlock

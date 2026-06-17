## TDE-2 sistemas-ciberfisicos Detecção e recuperação de impasses
## Equipe 9 
## Integrantes: Lucas Baumer, Matheus Kormann, Vinicius Yudi
## Linguagem escolhida: Python

## Resultados — Parte 1: Jantar dos Filósofos
### Variaveis utilizadas
```
Numero de filosofos = 5
Vezes que cada um comeu = 1
```

| Versão | Execução | Resultado | Tempo de Execução |
|---|---|---|---|
| Com Conflito | #1 | Terminouv| 2.184 s |
| Com Conflito | #2 | deadlock | -.---- |
| com Conflito | #3 | deadlock | -.---- |
| Corrigida | #1 | Terminou | 1.136 s |
| Corrigida | #2 | Terminou | 1.43 s |
| Corrigida | #3 | Terminou | 0.904 s |

### Resultodo com Conflito
 ```
 PS C:\Users\mathe\OneDrive\Documentos\PUCPR\7_Período\PSCF\TDE-2-sistemas-ciberfisicos--Deteccao-e-recuperacao-de-impasses> & C:\Users\mathe\AppData\Local\Programs\Python\Python313\python.exe c:/Users/mathe/OneDrive/Documentos/PUCPR/7_Período/PSCF/TDE-2-sistemas-ciberfisicos--Deteccao-e-recuperacao-de-impasses/PARTE1-FILOSOFOS/filosofos.py
Jantar dos Filosofos 
1 - Versao Com Conflito
2 - Versao Sem Conflito
Escolha: 1
Filosofo 0 esta pensando
Filosofo 1 esta pensando
Filosofo 2 esta pensando
Filosofo 3 esta pensando
Filosofo 4 esta pensando
Filosofo 3 esta com fome
Filosofo 2 esta com fome
Filosofo 0 esta com fome
Filosofo 1 esta com fome
Filosofo 4 esta com fome
```
### Resultodo corigido
```
PS C:\Users\mathe\OneDrive\Documentos\PUCPR\7_Período\PSCF\TDE-2-sistemas-ciberfisicos--Deteccao-e-recuperacao-de-impasses> & C:\Users\mathe\AppData\Local\Programs\Python\Python313\python.exe c:/Users/mathe/OneDrive/Documentos/PUCPR/7_Período/PSCF/TDE-2-sistemas-ciberfisicos--Deteccao-e-recuperacao-de-impasses/PARTE1-FILOSOFOS/filosofos.py
Jantar dos Filosofos 
1 - Versao Com Conflito
2 - Versao Sem Conflito
Escolha: 2
Filosofo 0 esta pensando
Filosofo 1 esta pensando
Filosofo 2 esta pensando
Filosofo 3 esta pensando
Filosofo 4 esta pensando
Filosofo 0 esta com fome
Filosofo 0 esta comendo
Filosofo 1 esta com fome
Filosofo 4 esta com fome
Filosofo 2 esta com fome
Filosofo 2 esta comendo
Filosofo 4 esta comendo
Filosofo 3 esta com fome
Filosofo 1 esta comendo
Filosofo 3 esta comendo

Executado: Versao sem conflito
Demorou 0.904 segundos
```

## DISCUSSÃO TÉCNICA - PARTE 1

## A) Como funciona a dinâmica do problema?
-> o Problema consiste em 5 filosofos em uma messa redonda com 5 garfos. para poder comer o filosofo presis de 2garfos um na esquerda e outro na direta. antes de comer ele tenque pensar depois ficar com fome e entao comer. nesesitando dos 2 garfos.


## B) Por que o impasse () surge na versão com Conflito?
-> Na versão com Conflito cada filósofo pega primeiro o garfo da esquerda e depois o da direita. Se os 5 ficarem com fome ao mesmo tempo e cada um pegar o garfo da esquerda, todos os 5 garfos ficam ocupados e cada filósofo fica esperando o garfo da direita, que ta na mão do vizinho. Ninguem solta o garfo, ninguem come, e todos esperam pra sempre. Isso forma um ciclo de espera unfinito

## C) Qual condição de Coffman é negada na solução?
-> pra resolver eu usei a hierarquia de recursos. basicamente cada garfo tem um numero de 0 a 4 e eu obrigo todo filosofo a pegar primeiro o garfo de numero menor e so depois o de numero maior, usando o min e o max. isso quebra a espera circular porque o ultimo filosofo acaba pegando os garfos na ordem invertida dos outros, então não tem como fechar aquele ciclo de todo mundo esperando todo mundo. acabando como os problemas de deadlocks

## D) Como justiça e progresso são garantidos?
-> Como nunca trava, sempre tem pelo menos um filósofo que consegue os 2 garfos, come e depois libera, então o sistema sempre progride. Os tempos de pensar e comer são aleatorios, então nenhum filósofo fica sempre na frente dos outros, evitando que um mesmo coma sempre antes e os outros passem fome.

---

## Resultados — Parte 2: Threads e Semáforos

| Versão | Execução | Valor Esperado (T×N) | Valor Obtido (count) | Tempo de Execução |
|---|---|---|---|---|
| Sem Sincronização | #1 | 1.600.000 | 200.001 | 118.3386 s |
| Sem Sincronização | #2 | 1.600.000 | 200.015 | 122.8420 s |
| Sem Sincronização | #3 | 1.600.000 | 199.980 | 119.1050 s |
| Com Semáforo | #1 | 1.600.000 | 1.600.000 | 991.4221 s |
| Com Semáforo | #2 | 1.600.000 | 1.600.000 | 992.4221 s |
| Com Semáforo | #3 | 1.600.000 | 1.600.000 | 991.8921 s |

## DISCUSSÃO TÉCNICA - PARTE 2
## A) Por que a versão sem sincronização perde incrementos?
-> o Incremento `count = valor_atual + 1` não é atomico, a thread le o valor e antes de escrever de volta, outra thread le o mesmo valor. o `time.sleep()` força a situação, quase todas as threads vão ler o mesmo numero ao mesmo tempo e escrevem o mesmo resultado, no final as 8 threads trabalharam, mas o contador so subiu 1 vez. Por isso o resultado ficou proximo de 200.000, que é equivalente a apenas 1 thread.

## B) Por que a versão com semáforo é correta?
-> o semáforo binario funciona como uma trava com uma unica chave. Quando uma thread entra pra seção de `acquire()`, as outras 7 ficam bloqueadas esperando, só depois da thread dar um `release()` que ta sendo garantido pelo `finally()` a proxima thread pode entrar, impedindo que duas threads entrem ao mesmo tempo, assim garantindo o resultado correto de 1.600.000

## C) Trade-off de desempenho
-> a versão com semaforo foi a mais lenta que a sem semaforo, pois as threads passam a rodar em sequencia dentro da seção critica, e o sistema gasta tempo alternando entre elas. o ganho em correção tem um custo de velocidade

### D) Visibilidade entre threads em Python
-> no Python `aquire()` e `release()` funcionam como se fossem uma barreira de memoria: o `release()` força a escrita do valor atualizado na memoria principal, e o `acquire()` força a leitura desse valor atualizado. Garantindo que nenhuma thread use um valor desatualizado de `count` 

<<<<<<< HEAD
---
=======
## Para executar o Codigo entre na pasta `PARTE2-SEMAFORO`, e digite o comando `python semaforo.py` no terminal, dê pressione a tecla `Enter` e espere ele executar: o programa vai rodar os dois testes em sequência, e após cada execução retornará os logs de: valor esperado, valor obtido e tempo de execução, caso queira testar com outros valores ou reduzir o tempo de teste, mude as variáveis de dentro do bloco "if __name__ == "__main__":
"T = 8 (Número de threads/operários)"
"N = 200000 (Número de incrementos por thread)"
>>>>>>> 59c30ff406f685745b7815f83f150b85ba331338

## Resultados — Parte 3: Deadlock

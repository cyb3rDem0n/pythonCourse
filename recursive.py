"""
 ad ogni passaggio il risultato viene riassegnato, e questo processo parte dall'ultimo passo (caso base) 
 e risale fino al primo. Ogni passaggio della ricorsione si risolve utilizzando il 
 risultato della chiamata successiva, ricalcolando il valore finale.

"""

def walk(top):
    if top == 0:
        return 0
    return top + walk(top -1)
        

print(walk(2))

"""
1a ricorsione - top = 2 + walk(2-1) => 3  | attendo risultato di walk
2a ricorsione - top = 1 "dovuto all'invocazione precedente walk(1)" + walk(0) => 1  | attendo risultato di walk
3a chiamata senza ricorsione - torna 0 | ricorsione terminata

La funziona termina quando walk(n) da il suo risultato finale

top verrà ricalcolato ad ogni giro e il suo valore sarà 3 perchè Python calcola ripercorrendo gli step intermedi,
quindi top vale 3 nell'ultima risalita

In altre parole:
Il risultato non viene sommato ad ogni step ontermedio ma ricalcolato o
costruito risalendo la catena delle chiamate ricorsive, passo dopo passo, fino alla somma finale. 
Ogni chiamata restituisce il suo valore, che viene utilizzato dalla chiamata precedente per completare la sua esecuzione.


"""

# FATTORIALE
def factorial_function_recursive(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    return n * factorial_function_recursive(n - 1)



# FIBONACCI
print(30 * "#")

def fib_recursive(n):
    if n < 1:
        return 0
    if n < 3:
        return 1
    # fib(7) viene divisa in due ad ogni step xke nn sappiamo quanto vale, arrivati al caso base si risale xke conosciamo il valore
    return fib_recursive(n - 1) + fib_recursive(n - 2)

print(fib_recursive(8))

"""
Passi dettagliati:

1 Chiamata iniziale: fibonacci(5)
La funzione non può ancora restituire un valore, quindi chiama fibonacci(4) e fibonacci(3).

2 Chiamata per fibonacci(4):

3 Chiama fibonacci(3) e fibonacci(2).
Chiamata per fibonacci(3):

4 Chiama fibonacci(2) e fibonacci(1).
Chiamata per fibonacci(2):

5 Chiama fibonacci(1) e fibonacci(0).

Casi base:

fibonacci(1) restituisce 1.
fibonacci(0) restituisce 0.

- A questo punto, la ricorsione ha raggiunto i casi base. Ora la funzione risale sommandoli:

Ritorno di fibonacci(2):

Somma fibonacci(1) + fibonacci(0) = 1 + 0 = 1.
Quindi fibonacci(2) ritorna 1.
Ritorno di fibonacci(3):

Somma fibonacci(2) + fibonacci(1) = 1 + 1 = 2.
Quindi fibonacci(3) ritorna 2.
Ritorno di fibonacci(4):

Somma fibonacci(3) + fibonacci(2) = 2 + 1 = 3.
Quindi fibonacci(4) ritorna 3.
Ritorno finale di fibonacci(5):

Somma fibonacci(4) + fibonacci(3) = 3 + 2 = 5.
Quindi fibonacci(5) ritorna 5.

"""

ar = [1,2,3,4]
print(ar[3:5], sep=" -- ")
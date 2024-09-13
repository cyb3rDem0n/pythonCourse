# Posso inizializzare una lista anche direttamente come segue

row = ["WHITE_PAWN" for i in range(8)]
squares = [x ** 2 for x in range(10)]
odds = [x for x in squares if x % 2 != 0 ]

# Array n-dimensionale

board = []
for i in range(2):
    row = ["EMPTY" for i in range(2)]
    board.append(row)

# metodo ridotto array 3 dimensioni
board2 = [["POPO" for i in range(3)] for j in range(3)]

print(f"Board: {board}\nBoard2: {board2}", sep="\n")

import random
array = [[random.randint(0, 100) for h in range(5)] for d in range(5)]

numero_da_cercare = 5
# Ciclo per scorrere tutti gli elementi dell'array bidimensionale
for i in range(len(array)):           # Ciclo sulle righe (i)
    for j in range(len(array[i])):    # Ciclo sugli elementi della riga (j)
        if array[i][j] == numero_da_cercare:
            print(f"Numero {numero_da_cercare} trovato in posizione ({i}, {j})")
            break  # interrompere la ricerca quando trovi il numero

array3D = [[random.randint(0, 100) for a in range(2)] for b in range(2) for c in range(2)]
print(array3D)

# Write a program which reads the number of blocks the builders have, 
# and outputs the height of the pyramid that can be built using these blocks.
# Each lower layer contains one block more than the layer above.

blocks = int(input("Enter the number of blocks: "))

height = 0
used_blocks = 0

while used_blocks <= blocks:
    print("used_blocks", used_blocks)
    height += 1  # Incrementa l'altezza
    used_blocks += height  # Aggiungi i blocchi necessari per questo livello

# Poiché l'ultimo ciclo incrementa height e used_blocks troppo, sottrai 1 all'altezza finale
print("The height of the pyramid is:", height - 1) 

# il ciclo parte da 0, quindi entriamo nel loop e incremento di 1 l'altezza e il num di blocchi usati
# sommo sempre l'altezza al numero di blochi
# secondo ciclo parto da 1, incremento e ho altezza 2 e usati 3 
# terzo ciclo parto da 3, incremento e ho altezza 3 e usati 6 
# quarto ciclo parto da 6, incremento e ho altezza 4 e usati 10
# partendo da 0 devo ridurre di uno il totale altrimenti avrei 11 blocchi
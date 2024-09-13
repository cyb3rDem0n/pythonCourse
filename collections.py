""" 
LISTE

"""

numbers = [1,2,3,4,5]
del numbers[4]

print(numbers, len(numbers), sep="\n")
print(numbers[-1]) # elemento all'ultima posizione
print(numbers[-2]) # elemento alla penultima posizione
print(30*"#")

#list.append(value)
#list.insert(location, value)

# popolare dinamicamente una lista
my_list = []  # Creating an empty list.

for i in range(5):
    my_list.append(i + 1)
    print(my_list[i])

# COme mostra il CASO2, posso usare anche semplicemente l'inidce i per sommare i valori, e non serve nemmeno la len()
total = 0
totalNew = 0
for i in range(len(my_list)):
    total += my_list[i]

# CASO 2
for i in my_list:
    totalNew += i

print(total, totalNew, sep=" -- ")


# se voglio invertire l'ordine di una lista posso usare una logica del tipo_
my_list = [10, 1, 8, 3, 5]
length = len(my_list)
print("ORIGINAL: ",my_list)

for i in range(length // 2):
    my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]

print("INVERTED: ",my_list)


# In Python questo è legale

lst = [1, [2, 3], 4] # lst[1] printa [2,3]
my_list = [1, None, True, 'I am a string', 256, 0]

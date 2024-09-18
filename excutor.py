"""Create a program with a for loop and a continue statement. The program should
iterate over a string of digits, replace each 0 with x, and print the modified 
string to the screen. 

for digit in "0165031806510":
    if digit == "0":
        print("x", end="")
        continue
    print(digit, end="")




for ch in "john.smith@pythoninstitute.org":
    if ch == "@":
        break
    print(ch, end="") 

t = [[3-i for i in range(3)] for j in range(3)] # non lho capito
print(t)
s = 0
for i in range(3):
    s+= t[i][i]
print(s)

# fa 4 perchè esegue piu cicli finchè non è >= 10 
# e perchè anche quando vale 2^4 entra lo stesso e stampa prima di fermarsi
# occhio dove sta il controllo
var = 1
while var < 10:
    print("#")
    var = var << 1



# occhio perchè INSERT aggiunge un elemento alla lista che diventa di indica 4
vals = [0,1,2]
vals.insert(0,1)
print(vals)
del vals[1]
print(vals)




a = 1   # 0001
b = 0   # 0000
c = a & b   # 0
d = a | b   # 1
e = a ^ b   # 1
print(c,d,e)
print(c+d+e)



# crea la lista al contrario perchè l'indice di inserimento
# è sempre 0 quindi l elemento successivo lo mette a destra del nuovo
list1 = [1,2,3]
list2 = []
for v in list1:
    print(v)
    list2.insert(0,v)
print(list2)



# lo SLICING [-i+1:-j+1] non seleziona ma taglia la lista
# Python usa sempre un intervallo inclusivo per il primo indice (i), ma esclusivo per il secondo indice (j).
listx = [1,2,3,4]
#        -n,...,-1
#        -4,-3,-2,-1
for i in range(len(listx)):
    print("INDEX: ",i)
print(listx[-1]) # ultimo elem della lista
print(listx[-len(listx)]) # primo elemento della lista
print(listx[-3:-2]) # ottengo il 2

print(listx[-2])


# range(start INCLUSIVO, stop ESCLUSIVO, step)
listy = [i for i in range(-1,2)] # -1 0 1 2 sono 4 ma lo STOP è esclusivo quindi 3 valori
print(listy)

listk = [3,1,-2]
print(listk[listk[-1]]) 
# prende come indice il valore dell arrey in ultima posizione quindi -2,
# corrisponderà all elelemento in penultima posizione 1

for i in range(1):
    print("#")
else:
    print("#")


# stampa solo quando dispari quindi 1,3,5 - 3 volte #
var = 0
while var < 6:
    var += 1
    if var % 2 == 0:
        continue
    print("#")


month = 1
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day_of_year = 0
for i in range(month - 1):
    day_of_year += days_in_month[i]

print(day_of_year)

"""
def fun(a):
    if a > 30:
        return 3
    else:
        print(a)
        return a + fun(a + 3)
    
print(fun(25))
    

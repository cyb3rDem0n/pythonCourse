## 1
# 0,1,4,9,16 - sarebbe 0,1,2,3,4 ma avendo x*x moltiplico per se stesso x
# inoltre l'indice da eliminare è lst[2] che vale 4, quindi elimino 16 in i = 4
my_list = [x * x for x in range(5)]

def f1(lst):
    del lst[lst[2]]
    return lst

#print(f1(my_list))

## 2
# numero elementi della lista? 0
#il range tenta di generare numeri partendo da -1 fino a un valore minore di -2. 
# Tuttavia, -1 è già maggiore di -2, quindi non esistono numeri che soddisfano la condizione.
lst1 = [i for i in range(-1,-2)]
#print(len(lst1))

## 3
# IMPORTANT: -1 indica IL POSTO PRIMA DELL'ULTIMO ELEMENTO
# la lista risultante satà [1,1,1,2]
# v=0 metto lst[0] in ultima posizione - ovvero 1 => 1,1,2
# v=1 metto lst[1] in ultima posizione - ovvero 2 => 1,1,1,2
lst2 = [1,2]

for v in range(2):
    lst2.insert(-1, lst2[v])

#print(lst2)

## 3
## 0,1
## XOR => 0 1 1 0
a = 1
b = 0
a = a ^ b 
b = a ^ b
a = a ^ b
#print(a,b)

## 4
# stampa 21
"""
Per la tupla associata alla chiave '1', cioè (1, 2), gli indici sono:
dct['1'][0] = 1
dct['1'][1] = 2

Per la tupla associata alla chiave '2', cioè (2, 1), gli indici sono:
dct['2'][0] = 2
dct['2'][1] = 1
"""
dct = {}
dct['1'] = (1,2)
dct['2'] = (2,1)
for x in dct.keys():
    #print(dct[x][1], end="")
    print("")

## 5
# x=3, y=2
# se hai resto da 1 altrimento 0 se divisibile 10%5 da 0, 10%3 da 1

## 6 
# PEMDAS
x = 1 // 5 + 1 / 5 # 0 + 0.2
#print(x)

## 7
# type error
value = 0
#print(0/len(value))

## 8
# Positional argument cannot appear after keyword argumentsPylance
def f2(a,b):
    return a*b

#print(f2(b=2,2))

## 9
# solo quand intervengo sui valori le liste di sdoppiano
# puntano allo stessa locazione di mem
nums = [1,2,3]
vals = nums
del vals[:]
print(id(vals))
print(id(nums))

## 10
# [0, 1, 2] 
# [0, 1, 2] 
# [0, 1, 2]
# 0 0 - 0 1 - 0 2
# 1 0 - 1 1 - 1 2
# 2 0 - 2 1 - 2 2
# printa quando il valore trovato da resto quindi quando ho 1%2
lst3 = [[x for x in range(3)] for y in range(3)]

for r in range(3):
    for c in range(3):
        if lst3[r][c] % 2 != 0:
            print("#")

## 11
"""
Qui stai accedendo all'ultimo elemento della nuova tupla (4,) 
utilizzando l'indice -1. Poiché la tupla ha un solo elemento, 
tup[-1] restituisce semplicemente il valore 4 (non una tupla, ma l'elemento stesso).
"""
tup = (1,2,3,4,8)
tup = tup[-2:-1]
tup = tup[-1]
print(tup)

## 12

dct1 = {'one':'two','three':'one','two':'three'}
v = dct1 ['three']

for k in range(len(dct1)):
    print(dct1[v])
    v = dct1[v]

print(v)

## 13
# Non va in exception, la divisione fa 0.0
try:
    value1 = 0 #input("... ")
    #print(len(value1))
    print (int(value1)/len(value1))
except ValueError:
    print("CASE 1")
except (ZeroDivisionError):
    print("CASE 2")
except TypeError:
    print("CASE 3")
except:
    print("CASE GENERIC")

## 14
# Value Error
foo = (1,2,3)
#foo.index(0) # indichi il VALORE e ti da l'INDICE, il val zero da errore xke non c'è
#print(foo.index(1)) 

## 15
## Il brack non centra un caz, non ci sta loop quindi Syntax Error
"""
try:
    print(5/0)
    break
except:
    print("CASE 1")
except (ValueError, ZeroDivisionError):
    print("CASE 2")



angle = 0
for i in range (5):
    if i % 2 == 1:
        angle +=1
else:
    angle -=1
print(angle)

others = 0

for i in range(2):
    for j in range(2):
        if i != j:
            others +=1
else:
    others +=1
print(others)

##

list1 = [1,2]
list2 = list1[:] # copia glie elementi della lista
#list2 = list1 fa un acopia della lista
list2.append(3)
print(list1[-1])

##


trains_speed = {"t1": 300, "t2": 400, "t3": 500}

for t in trains_speed:
    print(t[0], end="")

for k in trains_speed.values():
    print(str(k)[0], end="")

"""    
answ = (True, True, False)
select = answ[3:] # taglio dall elemento 3 in poi - quindi 0 elementi - l indice non parte da 0
print(select)
points = 0
for answ in select[-2:]:
    if answ:
        points +=1
print(points)


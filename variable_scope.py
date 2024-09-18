# VARIABLE SCOPE

"""
What's happened?

the var variable created inside the function is not the same as when defined outside it - 
it seems that there two different variables of the same name;
moreover, the function's variable shadows the variable coming from the outside world.

A variable existing outside a function has a scope inside the functions' bodies, 
excluding those of them which define a variable of the same name.

It also means that the scope of a variable existing outside a function is supported 
only when getting its value (reading). Assigning a value forces the creation of the function's own variable.

** Pensala a livello di memoria.

"""

def my_function():
    print("Do I know that variable?", var)


var = 1 # in questo caso la l indirizzo di memoria è lo stesso
my_function()
print(var)

# l'output sarà
# Do I know that variable? 2
# 1

def my_function():
    var = 2
    print("Do I know that variable?", var)


var = 1 # in questo caso sono due indirizzi di memoria diversi
my_function()
print(var)

# Do I know that variable? 2
# 1

# GLOBAL SCOPE

global varName # se non indichiamo global allora verrà creata una nuova variabile con lo stesso nome
                # ma con indirizzo di mem diverso


z = 5  # Variabile globale

def modifica_variabile_globale():
    global z  # Dichiarazione della variabile globale
    z = 50    # Modifica della variabile globale

print(f"Prima della modifica: z = {z}")  # Output: z = 5
modifica_variabile_globale()
print(f"Dopo la modifica: z = {z}")      # Output: z = 50


"""
- Le variabili globali possono essere lette ovunque nel codice, ma per modificarle all'interno 
di una funzione bisogna usare la parola chiave global.
- Le variabili locali esistono solo all'interno della funzione 
o del blocco dove sono definite e mascherano le variabili globali con lo stesso nome.
- Funzioni annidate possono accedere alle variabili degli scope 
superiori (enclosing scope), e per modificare una variabile nell'enclosing scope si usa la parola chiave nonlocal.
"""

# IMPORTANTE
# - Per gli scalari, ogni variabile punta direttamente al valore memorizzato in memoria. 
#   Se una variabile scalare viene modificata, viene creato un nuovo oggetto.
# - Per le liste, ogni elemento della lista è un riferimento a un oggetto separato in memoria.
#   La lista stessa contiene solo i riferimenti agli oggetti, quindi modificare un elemento della lista non implica la creazione di una nuova lista.


def my_function(my_list_1):
    print("Print #1:", my_list_1)
    print("Print #2:", my_list_2)
    my_list_1 = [0, 1]
    print("Print #3:", my_list_1)
    print("Print #4:", my_list_2)


my_list_2 = [2, 3]
print(id(my_list_2))
my_function(my_list_2)
print(id(my_list_2))

print("Print #5:", my_list_2)

var = 1
print(id(var))
var = 2
print(id(var))

# OUTPUT
#140280933061168
#Print #1: [2, 3]
#Print #2: [2, 3]
#Print #3: [0, 1]
#Print #4: [2, 3]
#140280933061168
#Print #5: [2, 3]
#140280936082912
#140280936082944

# - if the argument is a list, then changing the value of the corresponding parameter doesn't affect the list 
# (remember: variables containing lists are stored in a different way than scalars),
# - but if you change a list identified by the parameter (note: the list, not the parameter!), the list will reflect the change.

# var INSIDE
def message():
    alt = 1
    print("Hello, World!")


#print(alt)  #darà errore perchè la variabile alt è stata dichiarata dentro la funzione e non la vediamo fuori

# QUESTO E' UN CASO IMPORTANTE E CHE FA CAPIRE COME FUNZIONA LO SCOPE DELLE VARIABILI

a = 1 # address00
print("a = 1 = ", id(a))

def fun():
    global a
    print("a = global  = ", id(a)) 
    a = 2
    print("a = 2 = ", id(a))
    print(a)


a = 3 # address01
print("a = 3 = ", id(a)) 

fun() 
# address01 di GLOBA A
# address02 di A = 2

print("a post fun  = ", id(a)) # address02

print(a) # = 2
print("a ultima  = ", id(a)) # address02

# Introduzione e concetti

"""
-   Sequence type is a type of data in Python which is able to store 
    more than one value (or less than one, as a sequence may be empty), 
    and these values can be sequentially (hence the name) browsed, element by element.

-   Mutability is a property of any of Python's data that describes its readiness 
    to be freely changed during program execution.

-   A tuple is an immutable sequence type. It can behave like a list, but it mustn't be modified in situ.
"""


# # # # # # # # # # # 
# T U P L E         #
# # # # # # # # # # # 
tuple_1 = (1, 2, 4, 8)
tuple_2 = 1., .5, .25, .125

print(tuple_1)
print(tuple_2)

empty_tuple = () # vuota

# tuple con un elemento richiedono che termini con una virgola
one_element_tuple_1 = (1, )
one_element_tuple_2 = 1.,
# Se rimuovo la virgola allora non sto piu  
# dischiarando una tupla ma una variabile
one_element_tuple_2 = 4 # questa è ovviamente una variabile
print(one_element_tuple_2)


# uso tuple
my_tuple = (1, 10, 100, 1000)

print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[1:])
print(my_tuple[:-2])

for elem in my_tuple:
    print("ciclo for:", elem)

# NON POSSO ESEGUIRE LE SEGUENTI OP SULLE TUPLE
# my_tuple.append(10000)
# del my_tuple[0]

# Posso eliminare completamente la tupla però
# del my_tuple

# my_tuple[1] = -10
# ottengo l'errore: AttributeError: 'tuple' object has no attribute 'append'

# OPERAZIONI SU TUPLE

# da tupla a lista
tup = 1, 2, 3, 
my_list = list(tup)

my_tuple = (1, 10, 100)

t1 = my_tuple + (1000, 10000)
t2 = my_tuple * 3

print(len(t2))
print(t1)
print(t2)
print(10 in my_tuple)
print(-10 not in my_tuple)

# UNPACKING
tup = 1, 2, 3
a, b, c = tup
print(a * b * c)

# # # # # # # # # # # 
# D I Z I O N A R I #
# # # # # # # # # # # 
# DICTIONARY || ORDERED COLLECTION - Key/Value pair

dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

phone_numbers = {'boss': 5551234567, 'Suzy': 22657854310}

empty_dictionary = {}

# DA TUPLA A DIZIONARIO
colors = (("green", "#008000"), ("blue", "#0000FF"))
colors_dictionary = dict(colors)
# DA DICT A TUPLA
my_list = ["car", "Ford", "flower", "Tulip"]
t = tuple(my_list)

# unire 2 dizionari
d1 = {'Adam Smith': 'A', 'Judy Paxton': 'B+'}
d2 = {'Mary Louis': 'A', 'Patrick White': 'C'}
d3 = {}
for item in (d1, d2):
    d3 = d1 , d2 # OPPURE d3.update(item)


# quanti 2 ci sono nella tupla?
tup = 1, 2, 3, 2, 4, 5, 6, 2, 7, 2, 8, 9
duplicates = tup.count(2)

print(dictionary)
print(phone_numbers)
print(empty_dictionary)
#The order in which a dictionary stores its data is completely out of your control, and your expectations.

# per prendere il valore partendo dalla chiave
print(dictionary['cat'])
print(phone_numbers['Suzy'])

# get_item = pol_eng_dictionary.get("cat") # uso get nei casi dimanici ovviamente


# Se una chiave indicata non è prensente andiamo in errore, 
# quindi meglio usare il seguente controllo
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
words = ['cat', 'lion', 'horse'] # word da cercare dentro dictionary

for word in words:
    if word in dictionary:
        print(word, "->", dictionary[word])
    else:
        print(word, "is not in dictionary")


# Per chiarezza è utile scrivere cosi 
# Example 1:
dictionary = {
              "cat": "chat",
              "dog": "chien",
              "horse": "cheval"
              }

# Example 2:
phone_numbers = {'boss': 5551234567,
                 'Suzy': 22657854310
                 }


# RICERCA e ORDINAMENTO DIZIONARIO !! a dictionary is not a sequence type - the for loop is useless with it but we have....
# .keys() method returns an iterable object consisting of all the keys gathered within the dictionary.
# sorted nel for ordina l'output

# posso usare il for sui diz
pol_eng_dictionary = {
    "zamek": "castle",
    "woda": "water",
    "gleba": "soil"
    }
for item in pol_eng_dictionary:
    print(item)

for key, value in pol_eng_dictionary.items():
    print("Pol/Eng ->", key, ":", value)

if "zamek" in pol_eng_dictionary:
    print("Yes")
else:
    print("No")

pol_eng_dictionary.clear()   # removes all the items
copy_dictionary = pol_eng_dictionary.copy()


# abbiamo un diz. con i nomi in inglese KEY e francese VALUES
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

for key in dictionary.keys():
    print(key, "->", dictionary[key])

for key in sorted(dictionary.keys()):
    print(dictionary[key])

# ITEMS restituisce il pair
for e, f in dictionary.items():
    print(e, "->", f)
# values solo il valore
for french in dictionary.values():
    print(french)


# INSERIMENTO ( se chiave esiste, sovrascrive valore), AGGIORNAMENO ( se chiave esiste, sovrascrive valore), ELIMINAZIONE e MODIFICA
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

dictionary['cat'] = 'minou' # EDIT VALUE

dictionary['swan'] = 'cygne' # ADD NEW VALUE ||  aggiungere o aggiornare una singola coppia chiave-valore.

dictionary.update({"duck": "canard"}) # UPDATE ADDING NEW VALUE ||  inserire o aggiornare più coppie in un'unica operazione
dictionary.update({'swan': 'cygne', 'fish': 'poisson'})

del dictionary['dog'] # removing a non-existing key causes an error.

dictionary.popitem() # remove the last item in a dictionary,


print(dictionary)


# MIX TUPLE E DIZIONARI

school_class = {} # mi dichiaro il mio dizionario

while True:
    name = input("Enter the student's name: ")
    if name == '':
        break
    
    score = int(input("Enter the student's score (0-10): "))
    if score not in range(0, 11):
	    break
    if name in school_class:
        school_class[name] += (score,) # se trovo il nome sommo l'iesimo score inserito nel loop
    else:
        school_class[name] = (score,) # se non lo trovo aggiungo uno nuovo
        
for name in sorted(school_class.keys()):
    adding = 0
    counter = 0
    for score in school_class[name]: # uso il for per sommare e calcolare la media
        adding += score
        counter += 1
    print(name, ":", adding / counter)
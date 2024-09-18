# Introduzione e concetti

"""
-   Sequence type is a type of data in Python which is able to store 
    more than one value (or less than one, as a sequence may be empty), 
    and these values can be sequentially (hence the name) browsed, element by element.

-   Mutability is a property of any of Python's data that describes its readiness 
    to be freely changed during program execution.

-   A tuple is an immutable sequence type. It can behave like a list, but it mustn't be modified in situ.


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
# my_tuple[1] = -10
# ottengo l'errore: AttributeError: 'tuple' object has no attribute 'append'

# OPERAZIONI SU TUPLE
my_tuple = (1, 10, 100)

t1 = my_tuple + (1000, 10000)
t2 = my_tuple * 3

print(len(t2))
print(t1)
print(t2)
print(10 in my_tuple)
print(-10 not in my_tuple)


# DICTIONARY || ORDERED COLLECTION - Key/Value pair
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
phone_numbers = {'boss': 5551234567, 'Suzy': 22657854310}
empty_dictionary = {}

print(dictionary)
print(phone_numbers)
print(empty_dictionary)
#The order in which a dictionary stores its data is completely out of your control, and your expectations.

# per prendere il valore partendo dalla chiave
print(dictionary['cat'])
print(phone_numbers['Suzy'])


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

"""
# RICERCA e ORDINAMENTO DIZIONARIO !! a dictionary is not a sequence type - the for loop is useless with it but we have....
# .keys() method returns an iterable object consisting of all the keys gathered within the dictionary.
# sorted nel for ordina l'output
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

for key in dictionary.keys():
    print(key, "->", dictionary[key])

for key in sorted(dictionary.keys()):
    print(dictionary[key])



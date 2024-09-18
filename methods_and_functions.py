"""

METHOD & FUNCTION

A function doesn't belong to any data - it gets data, it may create new data and it (generally) produces a result.

Method does all these things, but is also able to change the state of a selected entity.
A method is owned by the data it works for, while a function is owned by the whole code.

A typical function invocation looks as follows: result = function(arg),
while a typical method invocation looks like this:result = data.method(arg).

 
SHADOWING: una variabile dichiarata e definita dentro una funziona è nascosta, quindi un altra 
con lo stesso nome fuori dalla funzione non subirà alcuna "interferenza"

def message(number):
    # ho il parametro number
    print("Enter a number:", number)

number = 1234 # stesso nome del parametro
message(1)
print(number)

# nessun side effect


Parametri Posizionali e keyword argument passing. I parametri delle funzioni soo posizionali, quindi all'iesima
posizione ci sarà quel parametro. Ma posso essere piu preciso e assegnare a quel parametro un preciso valore passato


def introduction(first_name, last_name):
    print("Hello, my name is", first_name, last_name)

introduction(last_name="Skywalker", first_name="Luke") # assegno io il val al param

# potrei anche mizare come segue, anche se non ha tanto senso, l'importante è in questo
# caso mantenere l'ordine
def adding(a, b, c):
    print(a, "+", b, "+", c, "=", a + b + c)

adding(3, b=1, c = 2)
# adding(3, a = 1, b = 2) # questo da errore

def introduction(first_name, last_name="Smith"):
    print("Hello, my name is", first_name, last_name)

introduction(first_name="William")
introduction("Henry")
introduction("James", "Doe")

# funzioano tutte le invocazioni, ovviamente il valore gia presente di first_name viene sovrascritto da quello che passiamo


# il return 123 is irretrievably lost
def boring_function():
    print("'Boredom Mode' ON.")
    return 123 # lost

# None: oltre ad essere usato per controllo e per return di una f()
def strange_function(n):
    if(n % 2 == 0):
        return True
# l'else non definito ritorna None se printiamo la f()
print(strange_function(1))

"""

# RETURN - DIFFERENZE NELL OUTPUT
# CASE 1
def wishes():
    print("My Wishes")
    return "Happy Birthday"

wishes()    # outputs: My Wishes


# CASE 2
def wishes():
    print("My Wishes")
    return "Happy Birthday"

print(wishes())

# outputs: My Wishes
#          Happy Birthday

#######################################################################################

# anno bisestile o no:
# Se l'anno è divisibile per 4 → è bisestile, a meno che non sia divisibile per 100.
# Se l'anno è divisibile per 100 e non è divisibile per 400 → non è bisestile.
# Se l'anno è divisibile per 400 → è sempre bisestile.

def is_year_leap(year):
    if(year % 4 == 0 and year % 100 != 0):
        return True
    elif(year % 400 == 0):
        return True
    else:
        return False
# test
test_data = [1987,1900, 2000, 2016, 1987]
test_results = [False, False, True, True, False]
for i in range(len(test_data)):
	yr = test_data[i]
	print(yr,"->",end="")
	result = is_year_leap(yr)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")
          
# calcola il numero di giorni in 1 mese a seconda dell'anno passato - quindi se bisestile
def days_in_month(year, month):
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days_num = 0
    
    if(year < 0 or month < 0 or month > 12):
        days_num = None
    else:
        if(is_year_leap(year) == True):
            days[1] = 29
            days_num = days[month-1]
        else:
            days_num = days[month-1]
    return days_num

# test
test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]

for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr, mo, "->", end="")
	result = days_in_month(yr, mo)
	
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")




# Restituisce il giorno dell'anno dato l'anno, il mese e il giorno.
# Restituisce None se l'input non è valido.

def day_of_year(year, month, day):

    
    # Giorni in ciascun mese per un anno non bisestile
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # Regola febbraio se è un anno bisestile
    if is_year_leap(year):
        days_in_month[1] = 29
    
    # Verifica la validità del mese
    if not (1 <= month <= 12):
        return None
    
    # giorno compreso tra 1 e quello corrispondente in day_in_month
    if not (1 <= day <= days_in_month[month - 1]):
        return None
    
    # Calcola il giorno dell'anno manualmente, sommando i giorni dei mesi precedenti
    # 
    day_of_year = 0
    for i in range(month - 1):
        day_of_year += days_in_month[i]
    
    # Aggiungi il giorno corrente
    day_of_year += day
    
    return day_of_year


#######################################################################################

# trova il numero primo

"""
- Numeri minori o uguali a 1 non sono primi.
- 2 e 3 sono primi.
- Numeri pari diversi da 2 non sono primi.
- Verifica divisibilità solo fino alla radice quadrata del numero per evitare calcoli inutili.
- Controlliamo solo i numeri dispari, perché i numeri pari (escluso il 2) non possono essere primi.
"""
import math

def is_prime(num):
    if num <= 1:
        return False
    if num == 2 or num == 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    # Controlla j divisori da 5 fino a sqrt(n)
    for j in range(5, int(math.sqrt(num)) + 1, 2):
        if num % j == 0:
            return False
    return True

for i in range(1, 20):
	if is_prime(i + 1):
			print(i + 1, end=" ")
print()

# conversione da litri x 100km a miglia per galloni e viceversa
#1 American mile = 1609.344 metres
#1 American gallon = 3.785411784 litres

def liters_100km_to_miles_gallon(liters):
    if liters >= 1:
        mpg = 100/liters * 0.621371/0.264172 # km/L * 1km in miglia/1litro in galloni   
        return mpg
    else:
        return None
    
#######################################################################################


def miles_gallon_to_liters_100km(miles):
    if miles >= 1:
        lkm = miles * 1.60934/3.78541
        l100km = 100/lkm
        return l100km
    else:
        return None
# test
print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))


# posso indicare un valore di default in un paramentro di una funziona

def ft_and_inch_to_m(ft, inch = 0.0):
    return ft * 0.3048 + inch * 0.0254


print(ft_and_inch_to_m(6))




## FACTORIAL - FIBONACCI - RECURSIVE FUNCTION
##
## nel fattoriale come in fibonacci è importante una STOP CONDITION
## quindi la funzione richiama se stessa finchè il valore
## non raggiunge per decremento il valore della stop condition
## va sempre specificata nei ricorsivi
## RecursionError: maximum recursion depth exceeded
##


# fattoriale 
# n!=n×(n−1)×(n−2)×⋯×1  5!=5×4×3×2×1=120

def factorial_function(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    
    product = 1
    for i in range(2, n + 1):
        product *= i
    return product


for n in range(1, 6):  # testing
    print(n, factorial_function(n))


# FIBONACCI e tuple unpacking

def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1

    elem_1 = elem_2 = 1
    the_sum = 0
    for i in range(3, n + 1):
        the_sum = elem_1 + elem_2
        elem_1, elem_2 = elem_2, the_sum # tuple unpacking, valoridelle var di destra vanno a sinistra
    return the_sum

for n in range(1, 10):  # testing
    print(n, "->", fib(n))

# FATTORIALE RICORDIVO
def factorial_function_recursive(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    return n * factorial_function_recursive(n - 1)



# FIBONACCI RICORSIVO

def fib_recursive(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    return fib_recursive(n - 1) + fib_recursive(n - 2)

# ex0 passo IF, a = 25 + fun (28)
# ex1 passo IF, a = 28 + fun (31)
# ex2 non passo IF, a = 3
# quindi 25 + 28 + 3 = 56
# cosnsidera A su cui si sommano i valori

def fun(a):
    if a > 30:
        return 3
    else:
        return a + fun(a + 3)


print(fun(25))
############################################
# Function and Method ##############################
##############################################

"""
- A scope is the part of the code where a certain name is properly recognizable.

- A variable existing outside a function has a scope which includes the function's bodies.

- A variable defined inside the function has a scope inside the function's body only.

- If a certain variable is used inside a function and the variables name is listed as an 
argument of the global keyword, it has global scope, and it is also recognizable outside the function.
"""

# output is 2
def function():
    global variable
    variable += 1


variable = 1
function()
print(variable)
# removing the line containing the global keyword will spoil the code 
# and the UnboundLocalError exception will be raised.
# la var non è dichiarata prima dell uso


# Correto 
def function(a, b, c):
    print(a, b, c)


function(1, c=3, b=2)

# Type Error - the a parameter is set twice (once with the positional passing and once with 
# the keyword passing) while the c parameter is not set at all.
# function(1, a=1, b=2)

# Changing the parameter's value doesn't propagate it outside the function
# output 1
def function_case0(parameter):
    parameter = [2]

the_list = [1]
function_case0(the_list)
print(the_list)

# Parameter list or dictionary, changing its contents propagates them outside the function
# output 2
def function_case1(parameter):
    parameter[0] = 2

the_list = [1]
function_case1(the_list)
print(the_list)


"""
ZeroDivisionError   => raised by a division in which the divider is zero or is indistinguishable from zero (/, //, and %)
ValueError          => raised by the use of values that are inappropriate in the current context, for example, when a function receives an argument of a proper type, but its value is unacceptable, for example, int('')
TypeError           => raised by attempts to apply data of a type which cannot be accepted in the current context, for example, int(None)
AttributeError      => raised - among other occasions - when the code tries to activate a method that doesn't exist in a certain item, for example, the_list.apend() (note the typo!)
SyntaxError         => raised when the control reaches a line of code that violates Python's grammar, and which has remained undetected until now;
NameError           => raised when the code attempts to make use of a non-existent (not previously defined) item, for example, a variable or a function.
"""

# comb torna un array ordinato come descritto dal return
# quindi il valore dell'elemento 3 - d della rislta risultante vale 0
def comb(w, h=10, d=0, i=False):
    return [i,w,h,d]

print(comb(h=1, w=2)[3])

#
def proc(data):
    data = [1,2,3] # sto definendo una nuova lista, non uso quella definita globalmente
    return data[-2]

    # IMPORTANTE
    # data[1] = 2
    # return data[-2]
    # in questo caso la fun modifica ha effetto sul parametro

# la fun non modifica la lista dichiarata fuori
# do not affect global data
measure = [0 for i in range(3)] # Output: [0, 0, 0]
proc(measure)
# sto stampando semplicemente l elemento della lista
print(measure[-2]) # Output: 0
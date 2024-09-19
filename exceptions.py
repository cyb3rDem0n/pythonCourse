# USEFUL EXCEPTIONS:
# - ZeroDivisionError
# - ValueError: receives an argument of a proper type, but its value is unacceptable.
# - TypeError: try to apply a data whose type cannot be accepted in the current context
"""short_list = [1] one_value = short_list[0.5] """
# - AttributeError: attempts to make use of a method which isn’t contained in the lists
# - SyntaxError

# CASO BASE GENERICO
try:
    value = int(input('Enter a natural number: '))
    print('The reciprocal of', value, 'is', 1/value)        
except:
    print('I do not know what to do.')

# GESTIONE DI PIU TIPOLOGIE DI EXCEPTIONS
try:
    value = int(input('Enter a natural number: '))
    print('The reciprocal of', value, 'is', 1/value)        
except ValueError:
    print('I do not know what to do.')    
except ZeroDivisionError:
    print('Division by zero is not allowed in our Universe.') 

# ECCEZZIONI SPECIFICHE PIU DEFAULT
# QUELLA DI DEF: VA MESSA SEMPRE ALLA FINE
try:
    value = int(input('Enter a natural number: '))
    print('The reciprocal of', value, 'is', 1/value)        
except ValueError:
    print('I do not know what to do.')    
except ZeroDivisionError:
    print('Division by zero is not allowed in our Universe.')    
except:
    print('Something strange has happened here... Sorry!')
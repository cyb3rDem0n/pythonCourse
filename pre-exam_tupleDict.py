##########################################
## Tuples #################################
############################################
"""
- A tuple, like a list, is a data aggregate that contains a certain number (including zero) of elements of any type. Tuples, like lists, are sequences, but they are immutable. 
- You're not allowed to change any of the tuple elements, or add a new element, or remove an existing element. 
- Attempting to break this rule will raise the TypeError exception.
- Tuples can be initialized with tuple literals. 

For example, these assignments instantiate three tuples: one empty, one one-element, and one two-element:
"""
empty_tuple = () # tuple() has the same meaning
one_element_tuple = tuple(1) # must not be replaced with (1)!
one_element_tuple = 1, # the same effect as above
two_element_tuple = (1, 2.5)
two_element_tuple = 1, 2.5 # the same effect as above


# The number of elements contained in the tuple can be determined by the len() function. For example, the following snippet prints 4 to the screen:

print(len((1, 2.2, '3', True)))


"""
- Note the inner pair of parentheses – they cannot be omitted, as it will cause the tuple to be replaced with four independent values and will cause an error.
- Any of the tuple's elements can be accessed using indexing, which works in the same manner as in lists, including slicing.
- An attempt to access a non-existent tuple element raises the IndexError exception.
- If any of the slice's indices exceeds the permissible range, no exception is raised, and the non-existent elements are not taken into consideration. Therefore, the resulting slice may be an empty tuple. For example, the following snippet outputs () to the screen:
"""
print((1,2,3)[4:5])


# The in and not in operators can check whether or not any value is contained inside the tuple.

#Tuples can be iterated through (traversed) by the for loop, like lists.
#The + operator joins tuples together.
#The * operator multiplies tuples, just like lists.



############################################
# Dictionaries ##############################
##############################################

"""
- A dictionary is a data aggregate that gathers pairs of values. The first element in each pair is called the key, and the second one is called the value. 
- Both keys and values can be of any type.
- Dictionaries are mutable but are not sequences - the order of pairs is imposed by the order in which the keys are entered into the dictionary.
- Dictionaries can be initialized with dictionary literals. For example, these assignments instantiate two dictionaries - one empty and one containing two key:value pairs:
"""
empty_dictionary = {}
phone_directory = {'Emergency': 911, 'Speaking Clock': 767}

# Accessing a dictionary's value requires the use of its key. For example, the following line outputs 911 to the screen:

print(phone_directory['Emergency'])


"""
- An attempt to access an element whose key is absent in the dictionary raises the KeyError exception.
- The in and not in operators can be used to check whether a certain key exists in the dictionary. 

For example, the following line prints True False to the screen:
"""
print('Emergency' in phone_directory, 'White House' in phone_directory)


# The len() function returns the number of pairs contained in the directory. For example, the following line outputs 0 to the screen:
empty_directory = {}
print(len(empty_directory))


# Changing a value of the existing key is done by an assignment. For example, the following snippet outputs False to the screen:

attendance = {'Bob': True}
attendance['Bob'] = False
print(attendance['Bob'])


# Adding a new pair to the dictionary resembles a regular assignment. For example, the following snippet outputs 2 to the screen:

domains = {'au': 'Australia'}
domains['at'] = 'Austria'
print(len(domains))


# Removing a pair from a dictionary is done with the del instruction. For example, the following snippet outputs 0 to the screen:

currencies = {'USD': 'United States dollar'}
del currencies['USD']
print(len(currencies))


# When iterated through by the for loop, the dictionary displays only its keys. For example, the following snippet outputs A B to the screen:

phonetic = {'A': 'Alpha', 'B': 'Bravo'}
for key in phonetic:
    print(key, end=' ')


# The .keys() method returns a list of keys contained in the dictionary. For example, the following snippet outputs A B to the screen:

phonetic = {'A': 'Alpha', 'B': 'Bravo'}
for key in phonetic.keys():
    print(key, end=' ')


# The .values() method returns a list of values contained in the dictionary. For example, the following snippet outputs Alpha Bravo to the screen:

phonetic = {'A': 'Alpha', 'B': 'Bravo'}
for value in phonetic.values():
    print(value, end=' ')


# The .items() method returns a list of two-element tuples, each filled with key:value pairs. For example, the following snippet outputs ('A', 'Alpha') ('B', 'Bravo') to the screen:

phonetic = {'A': 'Alpha', 'B': 'Bravo'}
for item in phonetic.items():
    print(item, end=' ')

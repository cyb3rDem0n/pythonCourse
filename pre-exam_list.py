############################################
# List ##############################
##############################################

""" 
- A list is a data aggregate that contains a certain number (including zero) of elements of any type.
- Lists are sequences: they can be iterated, and the order of the elements is established.
- Lists are mutable: their contents may be changed.
- Lists can be initialized with list literals. For example, these two assignments instantiate two lists: the former is empty, while the latter contains three elements:
"""

empty_list = []
three_elements = [1, 'two', False]

#The number of elements contained in the list can be determined by the len() function. For example, the following snippet prints 3 to the screen:
print(len(['a', 'b', 'c']))


# Any of the list's elements can be accessed using indexing. List elements are indexed by integer numbers starting from zero. Therefore, the first list element's index is 0 while the last element's index is equal to the list length minus 1. Using indices that are not integers raises the TypeError exception. For example, the following snippet prints a b c 0 1 2 to the screen:

the_list = ['a', 'b', 'c']
counter = 0
for ix in range(len(the_list)):
    print(the_list[ix], end=' ')
    the_list[ix] = counter
    counter += 1
for ix in range(len(the_list)):
    print(the_list[ix], end=' ')



"""
- The list elements can be indexed with negative numbers, too. In this case, -1 accesses the last element of the list, and -2 accesses the one before the last, and so on. 
- The alternative first list element's index is -len(list).

- An attempt to access a non-existent list element (when the index goes out of the permissible range) raises the IndexError exception.

- A slice is a means by which the programmer can create a new list using a part of the already existing list.
"""
#The most general slice looks as follows:
# the_list[from:to:step]
# and selects those elements whose indices start at from, don't exceed to, and change with step. For example, the following snippet prints ['b', 'd'] to the screen:

print((1,2,3)[4:5])


# The following assumptions are made regarding the slices:
"""
the_list[from:to] is equivalent to the_list[from:to:1]
the_list[:to] is equivalent to the_list[0:to]
the_list[from:] is equivalent to the_list[from:len(the_list)-1]
the_list[:] is equivalent to the_list[0:len(the_list)-1]
"""

# Slices – like indices – can take negative values. For example, the following snippet prints [1,2] to the screen:

the_list = [0, 1, 2, 3]
print(the_list[-3:-1])

""" 
- If any of the slice's indices exceeds the allowable range, no exception is raised, and the non-existent elements are not taken into consideration. Therefore, it is possible that the resulting slice is an empty list.
- Assigning a list to a list does not copy elements. Such an assignment results in a situation when more than one name identifies the same data aggregate.
"""
# For example, the following snippet prints True to the screen:

list_a = [1]
list_b = list_a
list_b[0] = 0
print(list_a[0] == list_b[0])

# As the slice is a copy of the source list, the following snippet prints False to the screen:

list_a = [1]
list_b = list_a[:]
list_b[0] = 0
print(list_a[0] == list_b[0])


# The .append(element) method can be used to append an element to the end of an existing list. For example, the following snippet outputs [1] to the screen:

the_list = []
the_list.append(1)
print(the_list)


# The .insert(at_index, element) method can be used to insert the element at the at_index of the existing list. For example, the following snippet outputs [2, 1] to the screen:

the_list = [1]
the_list.insert(0, 2)
print(the_list)


# The del the_list[index] instruction can be used to remove any of the existing list elements. For example, the following snippet prints [] to the screen:

the_list = [1]
del the_list[0]
print(the_list)


# The in and not in operators can check whether any value is contained inside the list or not. For example, the following snippet prints True False to the screen:

the_list = [1, 'a']
print('a' in the_list, 1 not in the_list)


# Lists can be iterated through (traversed) by the for loop, which allows the programmer to scan all their elements without the use of explicit indexing. For example, the following snippet prints 1 2 3 to the screen:

the_list = [1,2,3]
for element in the_list:
    print(element, end=' ')


# List comprehension allows the programmer to construct lists in a compact way. For example, the following snippet prints [1,2,3] to the screen:

the_list = [x for x in range(1,4)]
print(the_list)

"""
- Strings, like lists, are sequences, and in many contexts they behave like lists, especially when they are indexed and sliced or are arguments of the len() function.
- The in and not in operators can be applied to strings to check if any string is a part of another string. An empty string is considered a part of any string, including an empty one.
- Strings are immutable and their contents cannot be changed.
"""
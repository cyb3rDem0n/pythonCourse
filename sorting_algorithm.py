def classic_bubblesort (my_list):
    if len(my_list) == 0:
        print("Empty List")
        return
    else:
        #my_list = [8, 10, 6, 2, 4]  # list to sort
        swapCount = 0
        swapped = True  # It's a little fake, we need it to enter the while loop.

        while swapped:
            swapped = False  # no swaps so far
            for i in range(len(my_list) - 1):
                if my_list[i] > my_list[i + 1]:
                    swapped = True  # a swap occurred!
                    swapCount = swapCount + 1
                    my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

        print(f"Sorted List: {my_list} \nNumber of Swap: {swapCount}")
        return my_list
    


my_list = [99, 11, 1]
my_list.reverse()
emptyList = []
classic_bubblesort(my_list)


def interactive_bubblesort ():
    my_list = []
    swapped = True
    num = int(input("How many elements do you want to sort: "))

    for i in range(num):
        val = float(input("Enter a list element: "))
        my_list.append(val)

    while swapped:
        swapped = False
        for i in range(len(my_list) - 1):
            if my_list[i] > my_list[i + 1]:
                swapped = True
                my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
    return my_list

# ATTENZIONE
# questa operazione copia/associa l'indirizzo di memoria di list_1 su list_2
# quindi l'output sarà 2 e non 1 perchè entrambi le liste fanno riferimento 
# alla stessa locazione di memoria
list_1 = [1]
list_2 = list_1
list_1[0] = 2
print(list_2)

# possiam usare
# my_list[start:end] oppure my_list[:]
test_list_new = []
test_list = [6,9,2,33,6,78,9467,74]
test_list = test_list_new[1:-1] # -1 indica fino al pen'ultimo elemento
test_list[0:]
test_list[:-1]
del test_list_new # elimina la lista non il suo contenuto
del test_list[1:3]

sample_list = ["A", "B", "C", "D", "E"]
new_list = sample_list[2:-1]
print(new_list)  # outputs: ['C', 'D']


## presenza o meno di elemento in una lisa
my_list2 = [0, 3, 12, 8, 2]
print(5 in my_list2)
print(5 not in my_list2)
print(12 in my_list2)


## MAIN EXE
my_list = [99, 11, 1]
emptyList = []
classic_bubblesort(my_list)
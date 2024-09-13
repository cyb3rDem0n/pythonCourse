def greater_number(my_list):
    
    if len(my_list) == 0:
        return
    else:
    
        largest = my_list[0]

        for i in my_list[1:]:
            if i > largest:
                largest = i

        print(largest)


def greater_number_verbosed(my_list):
    largest = my_list[0]

    for i in range(1, len(my_list)):
        if my_list[i] > largest:
            largest = my_list[i]

    print(largest)



example_list = [1,5,7,89,5,3,34,8,3,523,7485,34,2,5,3658,69,9022]
greater_number(example_list)
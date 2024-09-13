def search_item(my_list):
    to_find = 5
    found = False

    for i in range(len(my_list)):
        found = my_list[i] == to_find
        if found:
            break

    if found:
        print("Element found at index", i)
    else:
        print("absent")


def remove_duplicate (my_list):
    
    new_list = [my_list[0]]

    for number in my_list:  
        if number not in new_list:
            new_list.append(number)
    
    print("The list with unique elements only:")
    print(new_list)


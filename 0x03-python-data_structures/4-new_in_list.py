#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    my_list_cop = []
    if (idx < 0 or idx > len(my_list) - 1):
        return my_list
    for i in range(len(my_list)):
        if (i == idx):
            my_list_cop.insert(idx, element)
        else:
            my_list_cop.append(my_list[i])
    return my_list_cop

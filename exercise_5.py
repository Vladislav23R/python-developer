from functools import reduce

def generatiom(elem_1, elem_2):
    return elem_1 * elem_2


my_list = [el for el in range(100, 1001, 2)]
print(my_list)
print(reduce(generatiom, my_list))
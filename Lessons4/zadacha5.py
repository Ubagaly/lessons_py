from functools import reduce

my_list = [el for el in range(100, 1001) if el % 2 == 0]
def proizved (el, next_el):
    return el*next_el

num = reduce(proizved, my_list)

print(my_list,num)
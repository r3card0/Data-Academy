# returns the standard deviation of a list
from functools import reduce

def std_dev(source_list:list):
    mean = (reduce(lambda r,e : r + e, source_list )) / len(source_list) 
    # list comprehension = [element for element in iterable if condicion]
    sigma_list = [((i - mean) ** 2) for i in source_list]
    # high order function: reduce
    sigma = reduce(lambda r,e: r + e, sigma_list)
    dev_std = (sigma / (len(source_list) - 1)) ** 0.5
    return print(round(dev_std,2))

std_dev([8,2,12,10])

# [65,100,54,112,351,4,56]
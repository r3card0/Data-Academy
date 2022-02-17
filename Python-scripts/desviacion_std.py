# returns the standard deviation of a list
from functools import reduce

def std_dev(source_list:list):
    mean = len(source_list) // 2
    # list comprehension = [element for element in iterable if condicion]
    sigma_list = [((i - mean) ** 2) for i in source_list]
    # high order function: reduce
    sigma = reduce(lambda r,e: r + e, sigma_list)
    dev_std = (sigma / (len(source_list) - 1)) ** 0.05
    return print(round(dev_std,2))

std_dev([65,100,54,112,351,4,56])
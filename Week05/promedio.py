# returns the mean from a list
from functools import reduce

def promedio(lista:list):
    promedio = (reduce(lambda r,e : r + e, lista))/len(lista)
    return print(promedio)

promedio([75,75,75,65,54,23,1,100,96,78])
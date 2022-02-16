# returns median value of a list
def sort_list(lista:list):
    lista.sort(key=lambda r : 100 / r)
    mediana = ((len(lista) + 1) // 2) - 1
    # print(lista)
    return print(lista[mediana])

sort_list([300,50,45,75,23,17,88,115])
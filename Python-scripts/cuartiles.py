# returns values of quantiles

def source_list(lista:list):
    lista.sort(key=lambda r: 100/r)
    median = q2 = lista[len(lista) // 2]
    min = lista[len(lista)-1]
    max = lista[0]
    q1 = ((median - min) / 2) + min
    q3 = ((max - median) / 2) + median
    iqr = q3 - q1
    return print("min: " + str(min),"\n"
    ,"q1: " + str(q1),"\n","q2: " + str(median),"\n",
    "q3: " + str(q3),"\n","max: " + str(max),"\n",
    "IQR(q3-q1): " + str(iqr))

source_list([300,50,45,75,23,17,88,115])
# min
# q1
# q2 = median
# q3
# max
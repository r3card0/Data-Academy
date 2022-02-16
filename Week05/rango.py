# returns the range of a list

def rango(lista:list):
    lista.sort(key=lambda r : 100/r)
    maximo = lista[0]
    minimo = lista[(len(lista)-1)]
    print("The greater value: " + str(maximo))
    print("The lowest value: " + str(minimo))
    rango_lista = maximo - minimo
    print("The range value is: " + str(rango_lista))

rango([65,100,54,112,351,4,56,85,40,32,2,400])
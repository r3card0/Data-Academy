# ¿Qué es Numpy?

NumPy o Numerical Python es una librería para manejo de números de Python.

Su principal uso es el manejar estructuras de datos matriciales y funciones matemáticas de alto nivel.

Es muy utilizada en data science y en el mundo científico y matemático.

## ¿Por qué usar NumPy?

Una de sus ventajas es que tiene una estructura de datos que permite representar información compleja como archivos de imágenes, videos, sonidos, etc. NumPy permite trabajar con estos datos de forma númerica para que puedan ser analizados y usados en algoritmos de machine learning.

NumPy también utiliza estructuras de datos como sus arrays que ocupan menor espacio que una lista común en Python. Esto ayuda a que sean más rápidas de procesar y que podamos utilizar cantidades de datos más grandes.


## Comenzar a usar NumPy
Para empezar a utilizar NumPy dentro de Jupyter Notebooks en la nube, como Google Colab o Deepnote, no necesitas hace ninguna instalación. Simplemente escribe la siguiente línea en una celda de código y ejecútala.

````
import numpy as np
````

## Arrays de Numpy
Como vimos arriba, en NumPy usamos una estructura de datos llamada array. Estos son arreglos numéricos parecidos a listas en Python. De hecho tienen propiedas muy parecidas como ser mutables y poder hacer slicing.

Los arrays son n-dimensionales. Esto quiere decir que pueden ser de muchas dimensiones dependiendo si tienen varias filas y columnas.

* Un array unidimensional es una sola columna o fila de alguna tablar, justo como una lista de Python
* Un array bidimensional es lo que conocemos como matriz y es la forma en la que podemos representar tablas de datos en NumPy.
* Un array de tres dimensiones o más es una matriz de matrices, mejor conocida como tensor.

Una característica muy importante de cualquier array es que solo puede tener datos de un mismo tipo.

Es decir que si tiene números enteros, todos sus elementos deben ser enteros. Si son números flotantes todos deberán ser flotantes.

Para crear un array con NumPy utilizamos el método np.array(tu_lista).

Nota: dentro de los paréntesis puede ir más de una lista para así crear arrays de dos o más dimensiones.

````
vector = np.array([1, 2, 4, 8, 16])
print(vector)
>>> [ 1  2  4  8 16]

matrix = np.array([[5, 10], [15, 30]])
print(matrix)
>>> [[ 5 10]
 [15 30]]
````
Dentro del método np.array() también pueden ir variables que contengan las listas con las que crearemos los arrays.

````
lista_1 = (100, 200, 300, 400)
lista_2 = (3, 4, 5, 6)

vector_2 = np.array(lista_1)
print(vector_2)
>>> [100 200 300 400]

matrix_2 = np.array([lista_1, lista_2])
print(matrix_2)
>>> [[100 200 300 400]
 [  3   4   5   6]]
````
Por último, utilicemos el método type() de Python sobre nuestros arrays para ver que efectivamente son ndarray de NumPy.

````
type(vector)
>>> numpy.ndarray
````

Reto: practica crear nuevos arrays
Dentro de la notebook en la que estás trabajando crea dos nuevos vectores y dos nuevas matrices.

Puedes utilizar variables o listas directamente en ellas.

## Tamaño de los arrays
Dentro de NumPy también existen funciones que nos sirven para conocer las dimensiones de un array y su tipo de datos.

## .shape
.shape nos da las dimensiones del array.

````
vector.shape
>>> (5,)

matrix.shape
>>> (2, 2)

matrix_2.shape
>>> (2, 4)
````
Para vectores el único valor es la cantidad de elementos en él.
Para matrices el primer valor son las filas y el segundo las columnas.
Para un tensor el primer valor es la “profundidad”, el segundo las filas y el tercero las columnas.

## .dtype
.dtype devuelve el tipo de datos que hay en un array.

````
vector.dtype
>>> dtype('int64')

matrix.dtype
>>> dtype('int64')

vector_4 = np.array([1.4, 5.6, 6.8])
vector_4.dtype
>>> dtype('float64')
````
Reto: conoce la forma de tus arrays
Nuevamente crea nuevos vectores y matrices dentro de tu notebook.

Utiliza los métodos .shape para conocer su forma y .dtype conocer su tipo de dato.

Comparte tus resultados en los comentarios de la clase.
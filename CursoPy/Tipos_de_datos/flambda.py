
from random import randint


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# de esta forma podemos crear una función anónima (lambda) que recibe un parámetro y devuelve el cuadrado de ese parámetro.
square = lambda num: num**2
# imprimimos la variable donde creamos nuestra función anónima y le pasamos el parámetro.
print(square(numeros[randint(0,9)]))
# otra forma de usar la función anónima es pasándola como parámetro a otra función.
# en este caso le pasamos la función anónima a la función map, que recibe una función y una lista.
# para que no salte el error de que map no es una lista, lo convertimos a una lista con list().
print(list(map(lambda num: num**1.5, numeros)))

print(filter(lambda num: num%2== 0, numeros))
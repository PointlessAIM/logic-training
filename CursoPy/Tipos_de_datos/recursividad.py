#algoritmo recursivo para saber si un numero es primo
import sys
def primo (numero, x):

    if x == 1:
        return True
    elif numero % x == 0:
        return False
    else:
        return primo(numero, x-1)

numero = int(input("Ingrese un numero: "))
sys.setrecursionlimit(numero+1)
retorno = primo(numero, numero-1)
if retorno == True:
    print("El numero es primo")
else:
    print("El numero no es primo")

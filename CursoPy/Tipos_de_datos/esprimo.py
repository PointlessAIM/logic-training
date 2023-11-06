def es_primo(numero):
    for n in range(2, numero):
        if numero % n == 0:
            print("No es primo", n, "es divisor")
            return False
    print("Es primo")
    return True

es_primo(77232917)


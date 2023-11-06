def es_palindromo(cadena):
    invertir = cadena[::-1]
    if cadena == invertir:
        return True
    else:
        return False

print(es_palindromo("anitalavalatina"))

def es_anagrama(cadena1:str,cadena2:str):
    return set(cadena1) == set(cadena2), cadena1

print(es_anagrama("elvis","lives")) #case sensitive

import random

def adivina(x):
    """
    The function adivina() takes a number x as an argument and generates a random number between 1 and
    x. It then prompts the user to guess the number and gives feedback on whether the guess is too high
    or too low
    
    :param x: The maximum number that the user can guess
    """
    numero_aleatorio = random.randint(1, x)
    adivina = 0
    while adivina != numero_aleatorio:
        advina = int(input(f"Adivina el número entre 1 y {x}: "))
        if advina < numero_aleatorio:
            print("Nope, intenta de nuevo. un poco más alto esta vez.")
        elif advina > numero_aleatorio:
            print("Nope, intenta de nuevo. un poco más bajo esta vez.")
        else:
            print(f"¡Bien hecho! ¡Has acertado! el número {numero_aleatorio} es correcto.") 
            break
        
def adivina_maquina(x):
    bajo = 1
    alto = x
    feedback = ''
    while feedback != 'c':
        if bajo != alto:
            adivina = random.randint(bajo, alto)
        else:
            adivina = bajo
        feedback = input(f"acaso {adivina} es: bajo (b), correcto (c), alto (a)? ")
        if feedback == 'a':
            alto = adivina - 1
        elif feedback == 'b':
            bajo = adivina + 1
    
    print(f"¡Bien hecho! ¡Has acertado! el número {adivina} es correcto.")

adivina(100)
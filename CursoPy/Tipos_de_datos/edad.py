edad= int(input("¿Cuántos años tienes? "))
nacionalidad= input("¿Cuál es tu país de origen? ")
confirma='S'
count=0
while (confirma=='S' and count <10):
    if edad < 18:
        print(f"Nacionalidad: {nacionalidad} \nNo puedes votar porque tienes {edad} años")
    else:
        print(f"Nacionalidad: {nacionalidad} \nPuedes votar porque tienes {edad} años")
    confirma= input("¿Quieres continuar? (S/N): ").upper()
    count += 1